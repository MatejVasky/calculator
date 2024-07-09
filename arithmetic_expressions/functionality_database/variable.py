from .value import Value

class Variable(Value):
    """A class for variables"""
    def __init__(self, name : str, value : Value):
        """Creates a new variable"""
        if not isinstance(value, Value):
            raise TypeError("value must be of type Value")

        self.name = name
        self.__value = value
    
    def get_value(self) -> Value:
        """Returns variable's value"""
        return self.__value
    
    def set_value(self, value : Value) -> None:
        """Sets variable's value"""
        if not isinstance(value, Value):
            raise TypeError("value must be of type Value")
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