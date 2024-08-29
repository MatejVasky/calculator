from .value import Value

class Parameters(Value):
    """A class representing a list of parameters of a function"""
    def __init__(self, *args : Value):
        """Creates a Parameters object. Arguments will be saved as elements"""
        # Check arguments
        for arg in args:
            if not isinstance(arg, Value):
                raise TypeError()
        # Assignments
        self.__args = args
    
    def __getitem__(self, index : int) -> Value:
        """Returns the parameter at the given index"""
        # Check type
        if not isinstance(index, int):
            raise TypeError("Index must be of type int")
        # Check if index is in range
        if index < -len(self.__args) or index >= len(self.__args):
            raise IndexError("Index out of range")
        # Return
        return self.__args[index]
    
    def __len__(self) -> int:
        """Returns the number of parameters"""
        return len(self.__args)
    
    def __iter__(self) -> 'ParametersIterator':
        return ParametersIterator(self)
    
    def __add__(self, value : object) -> 'Parameters':
        """Returns a Parameters object with a value added to the end"""
        if isinstance(value, Value):
            return Parameters(*(self.__args), value)
        return NotImplemented

class ParametersIterator():
    """An iterator for the Parameters class"""
    def __init__(self, parameters : Parameters):
        """Creates a new iterator"""
        self.__parameters = parameters
        self.__counter = -1
    
    def __next__(self) -> Value:
        """Returns the next value"""
        # Check for the end of iteration
        if self.__counter + 1 >= len(self.__parameters):
            raise StopIteration
        # Increment counter
        self.__counter += 1
        # Return
        return self.__parameters[self.__counter]