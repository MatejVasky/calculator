from typing import Callable, Optional, List
from .value import Value
from .exceptions import EvaluationError, FunctionOrOperationEvaluationError

class Operation():
    """A base class for operations"""
    def __init__(self, priority : int, symbol : Optional[str], token : str):
        """A constructor for the Operation class"""
        # Check types
        if not isinstance(priority, int):
            raise TypeError("priority must be of type int")
        if not isinstance(symbol, str) and symbol != None:
            raise TypeError("symbol must be of type str or None")
        if not isinstance(token, str):
            raise TypeError("token must be of type str")
        # Priority must be non-negative
        if priority < 0:
            raise ValueError("priority must be non-negative")
        # Symbol must not be an empty string
        if symbol == "":
            raise ValueError("symbol must be of length at least one")
        
        # Assignments
        self.priority = priority
        self.symbol = symbol
        self.token = token

class BinaryOperation(Operation):
    """A class for binary operations"""
    def __init__(self, priority : int, symbol : Optional[str], token : str, banned_after : List[str], evaluate : Callable[[Value, Value], Value]):
        """A constructor for the BinaryOperation class.\n
        banned_after specifies a list of tokens this operation should be banned after. If the last previous operation to this one of a smaller
        or equal priority is of equal priority and its token is in the banned_after list, the evaluator throws an error"""
        # Super-class constructor
        super().__init__(priority, symbol, token)

        # Check banned_after type
        if not isinstance(banned_after, list):
            raise TypeError("banned_after must be a list")
        for op in banned_after:
            if not isinstance(op, str):
                raise TypeError("banned_after elements must be of type str")

        # Assignments
        self.__banned_after = banned_after
        self.__evaluate = evaluate
    
    def evaluate(self, a : Value, b : Value):
        """Evaluates the operation"""
        # Type checks
        if not isinstance(a, Value) or not isinstance(b, Value):
            raise TypeError("a and b must be of type Value")
        try:
            # Try evaluating
            res = self.__evaluate(a, b)
        except Exception as e:
            # Evaluation errors are re-thrown
            if isinstance(e, EvaluationError):
                raise e
            # Other errors cause a FunctionOrOperationEvaluationError to be raised
            else:
                raise FunctionOrOperationEvaluationError(e)
        else:
            # Result object of type Value
            if isinstance(res, Value):
                return res
            # Result object of a wrong type
            else:
                raise FunctionOrOperationEvaluationError(TypeError("evaluate must return object of type Value"))
    
    def is_banned_after(self, operation : 'Operation'):
        """Returns True, if self is not allowed after operation"""
        return isinstance(operation, BinaryOperation) and \
            self.priority == operation.priority and \
            operation.token in self.__banned_after

class PrefixUnaryOperation(Operation):
    """A base class for unary operations, whose symbol comes before their operand"""
    def __init__(self, priority : int, symbol : Optional[str], token : str, evaluate : Callable[[Value], Value]):
        """A constructor for the PrefixUnaryOperation class"""
        super().__init__(priority, symbol, token)
        self.__evaluate = evaluate

    def evaluate(self, a : Value):
        """Evaluates the operation"""
        # Type checks
        if not isinstance(a, Value):
            raise TypeError("a and b must be of type Value")
        try:
            # Try evaluating
            res = self.__evaluate(a)
        except Exception as e:
            # Evaluation errors are re-thrown
            if isinstance(e, EvaluationError):
                raise e
            # Other errors cause a FunctionOrOperationEvaluationError to be raised
            else:
                raise FunctionOrOperationEvaluationError(e)
        else:
            # Result object of type Value
            if isinstance(res, Value):
                return res
            # Result object of a wrong type
            else:
                raise FunctionOrOperationEvaluationError(TypeError("evaluate must return object of type Value"))