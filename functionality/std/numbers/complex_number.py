from abc import abstractmethod
from math import sqrt
from typing import Union
from arithmetic_expressions.functionality_database import Value

class ComplexNumber(Value):
    """An abstract base class for numbers"""
    @abstractmethod
    def is_real(self) -> bool:
        """Returns True if a number is real"""

    @abstractmethod
    def is_rational(self) -> bool:
        """Returns True if a number is rational (and real)"""
    
    @abstractmethod
    def is_complex_rational(self) -> bool:
        """Returns True if a number is rational, i.e. if both its real and imaginary part are rational"""

    @abstractmethod
    def is_int(self) -> bool:
        """Returns True if a number is an integer"""
    
    @abstractmethod
    def is_gaussian_int(self) -> bool:
        """Returns True if a number is a Gaussian integer"""
    
    @abstractmethod
    def is_positive(self) -> bool:
        """Returns True if a number is positive real"""
    
    @abstractmethod
    def is_negative(self) -> bool:
        """Returns True if a number is negative real"""
    
    @abstractmethod
    def is_zero(self) -> bool:
        """Returns True if a number is zero"""
    
    @abstractmethod
    def re(self) -> 'ComplexNumber':
        """Returns the real part"""
    
    @abstractmethod
    def im(self) -> 'ComplexNumber':
        """Returns the imaginary part"""
    
    @abstractmethod
    def to_decimal(self) -> Union['Decimal', 'ComplexDecimal']:
        """Converts a complex number to a (complex) decimal number"""
    
    @abstractmethod
    def conj(self) -> 'ComplexNumber':
        """Returns the complex conjugate"""
    
    @abstractmethod
    def abs_squared(self) -> 'ComplexNumber':
        """Returns the absoulute value squared"""
    
    @abstractmethod
    def inv(self) -> 'ComplexNumber':
        """Returns the multiplicative inverse"""
    
    def __abs__(self) -> 'ComplexNumber':
        return Decimal(sqrt(self.abs_squared().to_decimal().val))
    
    def __truediv__(self, value : object) -> 'ComplexNumber':
        if isinstance(value, ComplexNumber):
            if value.is_zero():
                raise ZeroDivisionError()
            else:
                return self * value.inv()
        
        return NotImplemented
    
from .decimal import Decimal
from .complex_decimal import ComplexDecimal