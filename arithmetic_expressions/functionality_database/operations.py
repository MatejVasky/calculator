from abc import ABC, abstractmethod
from .value import Value

class Operation():
    """A base class for operations"""
    def __init__(self, priority : int, symbol : str, token : str):
        """A constructor for the Operation class"""
        self.priority = priority
        self.symbol = symbol
        self.token = token

class BinaryOperation(Operation):
    """A base class for binary operators"""
    def __init__(self, priority : int, symbol : str, token : str):
        """A constructor for the BinaryOperation class"""
        super().__init__(priority, symbol, token)

    @abstractmethod
    def evaluate(self, a : Value, b : Value):
        """Evaluates a given binary operation. a and b are operands"""
        pass

class PrefixUnaryOperation(Operation):
    """A base class for prefix unary operators"""
    def __init__(self, priority : int, symbol : str, token : str):
        """A constructor for the PrefixUnaryOperation class"""
        super().__init__(priority, symbol, token)
    
    @abstractmethod
    def evaluate(self, a : Value):
        """Evaluates a given prefix unary operation. a is the operand"""
        pass
