from typing import Optional
from .value import Value
from .exceptions import VariableUndefinedError

class Variable(Value):
    """A class for representing variables used for saving results of computations"""
    def __init__(self, name : str, value : Optional[Value]):
        """Creates a new variable. value allows specification of a starting value. If left as None, the variable will not contain a value until one is assigned using the set_value method"""
        # Type checks
        if not isinstance(name, str):
            raise TypeError("name must be of type str")
        if not isinstance(value, Value) and value != None:
            raise TypeError("value must be of type Value or None")
        # Assignments
        self.name = name
        self.__value = value
    
    def get_value(self) -> Value:
        """Returns variable's value"""
        # Check if it has been assigned a value
        if self.__value == None:
            raise VariableUndefinedError()
        # Return
        return self.__value
    
    def set_value(self, value : Value) -> None:
        """Sets variable's value"""
        # Check type
        if not isinstance(value, Value):
            raise TypeError("value must be of type Value")
        # Save value
        self.__value = value

def unpack_variables(f):
    """Unpacks all variables"""
    def wrapper(*args):
        newargs = []
        for i in range(len(args)):
            if isinstance(args[i], Variable):
                newargs.append(args[i].get_value())
            else:
                newargs.append(args[i])
        return f(*newargs)
    return wrapper