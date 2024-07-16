from typing import Callable
from .value import Value
from .parameters import Parameters
from .exceptions import EvaluationError, FunctionOrOperationEvaluationException

class Function(Value):
    """An abstract base class for functions"""
    def __init__(self, name : str, evaluate : Callable[..., Value]):
        """A constructor for Function"""
        if not isinstance(name, str):
            raise TypeError("name must be of type str")
        self.name = name
        self.__evaluate = evaluate
    
    def evaluate(self, arg : Value) -> Value:
        """Evaluates a function with given arguments"""
        if not isinstance(arg, Value):
            raise TypeError("arg must be of type Value")
        
        try:
            if isinstance(arg, Parameters):
                res = self.__evaluate(*arg)
            else:
                res = self.__evaluate(arg)
        except Exception as e:
            if isinstance(e, EvaluationError):
                raise e
            else:
                raise FunctionOrOperationEvaluationException(e)
        else:
            return res