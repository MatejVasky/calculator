from typing import List, Optional
from arithmetic_expressions.functionality_database import FunctionalityDatabase, Value, Variable, Operation, PrefixUnaryOperation, BinaryOperation
from arithmetic_expressions.functionality_database.exceptions import InvalidTokensError

class ExpressionEvaluator():
    def __init__(self, fd : 'FunctionalityDatabase'):
        self.fd = fd

    def evaluate(self, tokens : List[str]) -> 'Value':
        """Evaluates an expression. Assumes the list of tokens is valid"""
        if not isinstance(tokens, list):
            raise TypeError("tokens must be of type list")

        operations : List[OpEntry] = []
        results : List[Value] = []

        for token in tokens:
            if self.fd.is_int(token):
                results.append(self.fd.parse_int(token))
            elif self.fd.is_decimal(token):
                results.append(self.fd.parse_decimal(token))
            elif self.fd.is_constant(token):
                results.append(self.fd.constants[token])
            elif self.fd.is_operator(token):
                op = self.fd.operations[token]
                if isinstance(op, PrefixUnaryOperation):
                    self.__process_prefix_unary_operator(op, operations)
                elif isinstance(op, BinaryOperation):
                    self.__process_binary_operator(op, results, operations)
            elif self.fd.is_left_bracket(token):
                operations.append(OpEntry(None, -1))
            elif self.fd.is_right_bracket(token):
                self.__process_right_bracket(results, operations)
            else:
                raise InvalidTokensError()
            
        while len(operations) != 0:
            self.__evaluate_top_operation(results, operations)
        
        if len(results) == 0:
            raise InvalidTokensError()

        res = results.pop()
        if isinstance(res, Variable):
            res = res.get_value()
        return res
    
    def __process_prefix_unary_operator(self, op : 'PrefixUnaryOperation', operations : List['OpEntry']) -> None:
        priority = op.priority
        if len(operations) != 0 and operations[-1].priority > priority:
            priority = operations[-1].priority
        operations.append(OpEntry(op, priority))
    
    def __process_binary_operator(self, op : 'BinaryOperation', results : List['Value'], operations : List['OpEntry']) -> None:
        while len(operations) != 0 and operations[-1].priority >= op.priority:
            self.__evaluate_top_operation(results, operations)
        operations.append(OpEntry(op, op.priority))
    
    def __process_right_bracket(self, results : List['Value'], operations : List['OpEntry']) -> None:
        while len(operations) != 0 and operations[-1].op != None:
            self.__evaluate_top_operation(results, operations)
        if len(operations) == 0:
            raise InvalidTokensError()
        operations.pop()
    
    def __evaluate_top_operation(self, results : List['Value'], operations : List['OpEntry']) -> None:
        operation = operations.pop().op
        if isinstance(operation, PrefixUnaryOperation):
            if len(results) < 1:
                raise InvalidTokensError()
            results[-1] = operation.evaluate(results[-1])
        elif isinstance(operation, BinaryOperation):
            if len(results) < 2:
                raise InvalidTokensError()
            operand2 = results.pop()
            operand1 = results.pop()
            results.append(operation.evaluate(operand1, operand2))
    
class OpEntry():
    def __init__(self, op : Optional['Operation'], priority : int):
        self.op = op
        self.priority = priority