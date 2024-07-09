from typing import Union
from .complex_number import ComplexNumber

class Decimal(ComplexNumber):
    """A class for real decimal numbers"""
    def __init__(self, a : Union[float, int]):
        """Creates a real decimal number"""
        # Check arguments
        if isinstance(a, int):
            a = float(a)
        elif not isinstance(a, float):
            raise TypeError("a must be of type float or int")
        
        self.val = a
    
    def __repr__(self) -> str:
        return f"Decimal({self.val})"
    
    def is_real(self) -> bool:
        return True
    
    def is_rational(self) -> bool:
        return False
    
    def is_complex_rational(self) -> bool:
        return False
    
    def is_int(self) -> bool:
        return False

    def is_gaussian_int(self) -> bool:
        return False
    
    def is_positive(self) -> bool:
        return self.val > 0
    
    def is_negative(self) -> bool:
        return self.val < 0

    def is_zero(self) -> bool:
        return self.val == 0
    
    def re(self) -> 'Decimal':
        return self
    
    def im(self) -> 'Decimal':
        return Decimal(0)
    
    def to_decimal(self) -> 'Decimal':
        return self
    
    def conj(self) -> 'Decimal':
        return self
    
    def abs_squared(self) -> 'Decimal':
        return Decimal(self.val * self.val)
    
    def inv(self) -> 'Decimal':
        if self.is_zero():
            raise ZeroDivisionError("Division by zero")
        return Decimal(1 / self.val)
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Rational):
            return self == value.to_decimal()
        elif isinstance(value, ComplexRational):
            return value.is_real() and self == value.re()
        elif isinstance(value, Decimal):
            return self.val == value.val
        elif isinstance(value, ComplexDecimal):
            return value.is_real() and self == value.re()
        return NotImplemented
    
    def __gt__(self, value : object) -> bool:
        if isinstance(value, Rational):
            return self > value.to_decimal()
        elif isinstance(value, ComplexRational) and value.is_real():
            return self > value.re()
        elif isinstance(value, Decimal):
            return self.val > value.val
        elif isinstance(value, ComplexDecimal) and value.is_real():
            return self > value.re()
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash(self.val)
    
    def __pos__(self) -> 'Decimal':
        return self
    
    def __neg__(self) -> 'Decimal':
        return Decimal(-self.val)
    
    def __abs__(self) -> 'Decimal':
        return Decimal(abs(self.val))

    def __add__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return self + value.to_decimal()
        elif isinstance(value, ComplexRational):
            return self + value.to_decimal()
        elif isinstance(value, Decimal):
            return Decimal(self.val + value.val)
        elif isinstance(value, ComplexDecimal):
            return ComplexDecimal(self.val + value.a, value.b)
        return NotImplemented
    
    def __sub__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return self - value.to_decimal()
        elif isinstance(value, ComplexRational):
            return self - value.to_decimal()
        elif isinstance(value, Decimal):
            return Decimal(self.val - value.val)
        elif isinstance(value, ComplexDecimal):
            return ComplexDecimal(self.val - value.a, -value.b)
        return NotImplemented
    
    def __mul__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return self * value.to_decimal()
        elif isinstance(value, ComplexRational):
            return self * value.to_decimal()
        elif isinstance(value, Decimal):
            return Decimal(self.val * value.val)
        elif isinstance(value, ComplexDecimal):
            return ComplexDecimal(self.val * value.a, self.val * value.b)
        return NotImplemented
    
    def __str__(self) -> str:
        return str(self.val)
    
    def __float__(self) -> float:
        return self.val

from .rational import Rational
from .complex_rational import ComplexRational
from .complex_decimal import ComplexDecimal