from typing import Callable, Optional
from .value import Value
from .exceptions import EvaluationError, FunctionOrOperationEvaluationException

class Operation():
    """A base class for operations"""
    def __init__(self, priority : int, symbol : Optional[str], token : str):
        """A constructor for the Operation class"""
        if not isinstance(priority, int):
            raise TypeError("priority must be of type int")
        if not isinstance(symbol, str) and symbol != None:
            raise TypeError("symbol must be of type str")
        if not isinstance(token, str):
            raise TypeError("token must be of type str")
        if priority < 0:
            raise ValueError("priority must be non-negative")
        self.priority = priority
        self.symbol = symbol
        self.token = token

class BinaryOperation(Operation):
    """A base class for binary operations"""
    def __init__(self, priority : int, symbol : Optional[str], token : str, evaluate : Callable[[Value, Value], Value]):
        """A constructor for the BinaryOperation class"""
        super().__init__(priority, symbol, token)
        self.__evaluate = evaluate
    
    def evaluate(self, a : Value, b : Value):
        """Evaluates the operation"""
        if not isinstance(a, Value) or not isinstance(b, Value):
            raise TypeError("a and b must be of type Value")
        try:
            res = self.__evaluate(a, b)
        except Exception as e:
            if isinstance(e, EvaluationError):
                raise e
            else:
                raise FunctionOrOperationEvaluationException(e)
        else:
            return res

class PrefixUnaryOperation(Operation):
    """A base class for prefix unary operations"""
    def __init__(self, priority : int, symbol : Optional[str], token : str, evaluate : Callable[[Value], Value]):
        """A constructor for the PrefixUnaryOperation class"""
        super().__init__(priority, symbol, token)
        self.__evaluate = evaluate

    def evaluate(self, a : Value):
        """Evaluates the operation"""
        if not isinstance(a, Value):
            raise TypeError("a and b must be of type Value")
        try:
            res = self.__evaluate(a)
        except Exception as e:
            if isinstance(e, EvaluationError):
                raise e
            else:
                raise FunctionOrOperationEvaluationException(e)
        else:
            return res