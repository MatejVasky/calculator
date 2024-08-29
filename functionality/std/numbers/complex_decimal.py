from typing import Union
from .complex_number import ComplexNumber

class ComplexDecimal(ComplexNumber):
    """A class for complex decimal numbers"""
    def __init__(self, a : Union[float, int], b : Union[float, int]):
        """Creates a complex decimal number a + bi"""
        # Check arguments
        if isinstance(a, int):
            a = float(a)
        elif not isinstance(a, float):
            raise TypeError("a must be of type float or int")
        
        if isinstance(b, int):
            b = float(b)
        elif not isinstance(b, float):
            raise TypeError("b must be of type float or int")
        
        self.a = a
        self.b = b
    
    def __repr__(self) -> str:
        return f"ComplexDecimal({self.a}, {self.b})"
    
    def is_real(self) -> bool:
        return self.b == 0
    
    def is_rational(self) -> bool:
        return False
    
    def is_complex_rational(self) -> bool:
        return False
    
    def is_int(self) -> bool:
        return False

    def is_gaussian_int(self) -> bool:
        return False
    
    def is_positive(self) -> bool:
        return self.a > 0 and self.b == 0
    
    def is_negative(self) -> bool:
        return self.a < 0 and self.b == 0

    def is_zero(self) -> bool:
        return self.a == 0 and self.b == 0

    def re(self) -> 'Decimal':
        return Decimal(self.a)
    
    def im(self) -> 'Decimal':
        return Decimal(self.b)
    
    def to_decimal(self) -> 'ComplexDecimal':
        return self
    
    def conj(self) -> 'ComplexDecimal':
        return ComplexDecimal(self.a, -self.b)
    
    def abs_squared(self) -> 'Decimal':
        return Decimal(self.a * self.a + self.b * self.b)
    
    def inv(self) -> 'ComplexDecimal':
        if self.is_zero():
            raise ZeroDivisionError("Division by zero")
        con = self.conj()
        abss = self.abs_squared()
        return ComplexDecimal(con.a / abss.val, con.b / abss.val)
    
    def numerator(self) -> int:
        raise ValueError("not rational")
    
    def denominator(self) -> int:
        raise ValueError("not rational")
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Rational):
            return self.is_real() and self.re() == value.to_decimal()
        elif isinstance(value, ComplexRational):
            value_dec = value.to_decimal()
            return self.re() == value_dec.re() and self.im() == value_dec.im()
        elif isinstance(value, Decimal):
            return self.is_real() and self.re() == value
        elif isinstance(value, ComplexDecimal):
            return self.a == value.a and self.b == value.b
        return NotImplemented
    
    def __gt__(self, value : object) -> bool:
        if not self.is_real():
            return NotImplemented
        elif isinstance(value, Rational):
            return self.is_real() and self.re() > value.to_decimal()
        elif isinstance(value, ComplexRational) and value.is_real():
            return self.is_real() and value.is_real() and self.re() > value.re().to_decimal()
        elif isinstance(value, Decimal):
            return self.is_real() and self.re() > value
        elif isinstance(value, ComplexDecimal) and value.is_real():
            return self.is_real() and value.is_real() and self.a > value.a
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash((self.a, self.b))
    
    def __pos__(self) -> 'ComplexDecimal':
        return self
    
    def __neg__(self) -> 'ComplexDecimal':
        return ComplexDecimal(-self.a, -self.b)

    def __add__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return self + value.to_decimal()
        elif isinstance(value, ComplexRational):
            return self + value.to_decimal()
        elif isinstance(value, Decimal):
            return ComplexDecimal(self.a + value.val, self.b)
        elif isinstance(value, ComplexDecimal):
            return ComplexDecimal(self.a + value.a, self.b + value.b)
        return NotImplemented
    
    def __sub__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return self - value.to_decimal()
        elif isinstance(value, ComplexRational):
            return self - value.to_decimal()
        elif isinstance(value, Decimal):
            return ComplexDecimal(self.a - value.val, self.b)
        elif isinstance(value, ComplexDecimal):
            return ComplexDecimal(self.a - value.a, self.b - value.b)
        return NotImplemented
    
    def __mul__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return self * value.to_decimal()
        elif isinstance(value, ComplexRational):
            return self * value.to_decimal()
        elif isinstance(value, Decimal):
            return ComplexDecimal(self.a * value.val, self.b * value.val)
        elif isinstance(value, ComplexDecimal):
            return ComplexDecimal(self.a * value.a - self.b * value.b,
                                  self.a * value.b + self.b * value.a)
        return NotImplemented
    
    def __str__(self) -> str:
        if self.b == 0:
            return str(self.a)
        elif self.a == 0:
            if self.b == 1:
                return "i"
            elif self.b == -1:
                return "-i"
            else:
                return f"{self.b}i"
        else:
            if self.b == 1:
                return f"{self.a} + i"
            elif self.b == -1:
                return f"{self.a} - i"
            elif self.b > 0:
                return f"{self.a} + {self.b}i"
            else:
                return f"{self.a} - {-self.b}i"
    
    def __float__(self) -> float:
        if not self.is_real():
            raise ValueError(f"{self} is not real")
        return self.a
        
from .rational import Rational
from .complex_rational import ComplexRational
from .decimal import Decimal