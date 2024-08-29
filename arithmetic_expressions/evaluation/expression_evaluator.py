from typing import List, Optional
from arithmetic_expressions.functionality_database import FunctionalityDatabase, Value, Variable, Operation, PrefixUnaryOperation, BinaryOperation
from arithmetic_expressions.functionality_database.exceptions import InvalidTokensError, BannedSequenceOfOperationsError

class ExpressionEvaluator():
    """A class for evaluating a parsed arithmetic expression (i.e. an expression represented as a list of tokens)"""
    def __init__(self, fd : 'FunctionalityDatabase'):
        """Creates an ExpressionEvaluator. fd specifies the functionality database which should be used during evaluation"""
        # Type check
        if not isinstance(fd, FunctionalityDatabase):
            raise TypeError("fd must be of type FunctionalityDatabase")
        # Assignment
        self.fd = fd

    def evaluate(self, tokens : List[str]) -> 'Value':
        """Evaluates an expression. Assumes the list of tokens is valid (i.e. something that could be produced by an ExpressionParser with the right input)"""
        # Check argument type
        if not isinstance(tokens, list):
            raise TypeError("tokens must be of type list")

        # Stacks initialization
        operations : List[OpEntry] = [] # A stack for holding yet unevaluated operations
        results : List[Value] = [] # A stack for holding intermediate results

        # Main loop
        for token in tokens:
            # Integer tokens are parsed and added to results
            if self.fd.is_int(token):
                results.append(self.fd.parse_int(token))
            # Decimal tokens are parsed and added to results
            elif self.fd.is_decimal(token):
                results.append(self.fd.parse_decimal(token))
            # Constant tokens are looked up and added to results
            elif self.fd.is_constant(token):
                results.append(self.fd.constants[token])
            # Operation tokens are looked up and processed according to their type
            elif self.fd.is_operator(token):
                op = self.fd.operations[token]
                if isinstance(op, PrefixUnaryOperation):
                    self.__process_prefix_unary_operator(op, operations)
                elif isinstance(op, BinaryOperation):
                    self.__process_binary_operator(op, results, operations)
            # Left brackets add an OpEntry(None, -1) onto the operations stack
            elif self.fd.is_left_bracket(token):
                operations.append(OpEntry(None, -1))
            # Right brackets
            elif self.fd.is_right_bracket(token):
                self.__process_right_bracket(results, operations)
            # Unknown tokens cause an exception
            else:
                raise InvalidTokensError()
        
        # Evaluate remaining operations
        while len(operations) != 0:
            self.__evaluate_top_operation(results, operations)
        
        # Check if results has length 1 (if not, then the input was invalid)
        if len(results) != 1:
            raise InvalidTokensError()
        
        # Get and return the result
        res = results.pop()
        # Unpack variable, if applicable
        if isinstance(res, Variable):
            res = res.get_value()
        # Return
        return res
    
    def __process_prefix_unary_operator(self, op : 'PrefixUnaryOperation', operations : List['OpEntry']) -> None:
        """Adds a prefix unary operation to the operations stack with the right priority"""
        # Compute operation priority
        priority = op.priority
        if len(operations) != 0 and operations[-1].priority > priority:
            priority = operations[-1].priority
        # Add operation to the operations stack
        operations.append(OpEntry(op, priority))
    
    def __process_binary_operator(self, op : 'BinaryOperation', results : List['Value'], operations : List['OpEntry']) -> None:
        """Evaluates previous operations (as necessary) and adds op to the operations stack"""
        # Evaluate previous operations
        while len(operations) != 0 and operations[-1].priority >= op.priority:
            # Check operation bans
            if op.is_banned_after(operations[-1].op):
                raise BannedSequenceOfOperationsError()
            # Evaluate
            self.__evaluate_top_operation(results, operations)
        # Add op to the operations stack
        operations.append(OpEntry(op, op.priority))
    
    def __process_right_bracket(self, results : List['Value'], operations : List['OpEntry']) -> None:
        """Evaluates previous operations from the top of the operations stack until the topmost bracket and then pops the bracket"""
        # Evaluate operations
        while len(operations) != 0 and operations[-1].op != None:
            self.__evaluate_top_operation(results, operations)
        # If there is no bracket on the operations stack, the input is invalid
        if len(operations) == 0:
            raise InvalidTokensError()
        # Pop the topmost bracket
        operations.pop()
    
    def __evaluate_top_operation(self, results : List['Value'], operations : List['OpEntry']) -> None:
        """Evaluates the operation at the top of the operations stack"""
        # Get operation
        operation = operations.pop().op
        # Prefix unary operations
        if isinstance(operation, PrefixUnaryOperation):
            # Check if there are enough intermediate results
            if len(results) < 1:
                raise InvalidTokensError()
            # Evaluate operation
            results[-1] = operation.evaluate(results[-1])
        elif isinstance(operation, BinaryOperation):
            # Check if there are enough intermediate results
            if len(results) < 2:
                raise InvalidTokensError()
            # Get operands
            operand2 = results.pop()
            operand1 = results.pop()
            # Evaluate operation
            results.append(operation.evaluate(operand1, operand2))
    
class OpEntry():
    """A container class for an operation and its priority. Used by the ExpressionEvaluator"""
    def __init__(self, op : Optional['Operation'], priority : int):
        """Creates an OpEntry container. op specifies the operation (or None, if it represents a bracket) and priority specifies the priority (should be -1 for brackets)"""
        self.op = op
        self.priority = priority