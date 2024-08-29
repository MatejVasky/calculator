from typing import Callable
from .value import Value
from .parameters import Parameters
from .exceptions import EvaluationError, FunctionOrOperationEvaluationError

class Function(Value):
    """A class representing a function in an arithmetic expression. Can be treated as a value by the ExpressionEvaluator"""
    def __init__(self, name : str, evaluate : Callable[..., Value]):
        """A constructor for Function"""
        # Check name type
        if not isinstance(name, str):
            raise TypeError("name must be of type str")
        if len(name) == 0:
            raise ValueError("name must be of length at least 1")
        # Assign to class members
        self.name = name
        self.__evaluate = evaluate
    
    def evaluate(self, arg : Value) -> Value:
        """Evaluates a function with given argument. Multiple parameters must be wrapped into a Parameters object; a single parameter can be passed on its own
        or as a single element of a Parameters object"""
        # Check arg type
        if not isinstance(arg, Value):
            raise TypeError("arg must be of type Value")
        
        try:
            # If arg is of type Parameters, unpack it and evaluate
            if isinstance(arg, Parameters):
                res = self.__evaluate(*arg)
            # Otherwise, pass arg directly to evaluation function
            else:
                res = self.__evaluate(arg)
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
                raise FunctionOrOperationEvaluationError(TypeError("evaluate must return object of type Value or None"))