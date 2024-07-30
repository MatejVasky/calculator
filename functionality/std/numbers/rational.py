from datastructures import gcd, pow_by_squaring, get_int_nth_root
from .complex_number import ComplexNumber

class Rational(ComplexNumber):
    """A class for rational rationals, i.e. numbers a/b, where a and b are integers and b != 0"""
    def __init__(self, a : int, b : int):
        """Creates a rational of the form a/b. b must be non-zero"""
        # Check arguments
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("a and b must be of type int")
        if b == 0:
            raise ValueError("b must be non-zero")
        
        # Make denominaors positive
        if b < 0:
            a, b = -a, -b

        # Make respective numerators and denominators coprime
        d = gcd(a, b)
        a, b = a // d, b // d

        # Set attributes
        self.a, self.b = a, b
    
    def __repr__(self) -> str:
        return f"Rational({self.a}, {self.b})"
    
    def is_real(self) -> bool:
        return True
    
    def is_rational(self) -> bool:
        return True
    
    def is_complex_rational(self) -> bool:
        return True
    
    def is_int(self) -> bool:
        return self.b == 1

    def is_gaussian_int(self) -> bool:
        return self.b == 1
    
    def is_positive(self) -> bool:
        return self.a > 0
    
    def is_negative(self) -> bool:
        return self.a < 0

    def is_zero(self) -> bool:
        return self.a == 0
    
    def re(self) -> 'Rational':
        return self
    
    def im(self) -> 'Rational':
        return Rational(0, 1)
    
    def to_decimal(self) -> 'Decimal':
        return Decimal(self.a / self.b)
    
    def conj(self) -> 'Rational':
        return self
    
    def abs_squared(self) -> 'Rational':
        return Rational(self.a * self.a, self.b * self.b)
    
    def inv(self) -> 'Rational':
        if self.is_zero():
            raise ZeroDivisionError("Division by zero")
        return Rational(self.b, self.a)
    
    def numerator(self) -> int:
        return self.a
    
    def denominator(self) -> int:
        return self.b
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Rational):
            return self.a == value.a and self.b == value.b
        elif isinstance(value, ComplexRational):
            return value.is_real() and self == value.re()
        elif isinstance(value, Decimal):
            return self.to_decimal() == value
        elif isinstance(value, ComplexDecimal):
            return value.is_real() and self == value.re()
        return NotImplemented
    
    def __gt__(self, value : object) -> bool:
        if isinstance(value, Rational):
            return self.a * value.b > value.a * self.b
        elif isinstance(value, ComplexRational) and value.is_real():
            return self > value.re()
        elif isinstance(value, Decimal):
            return self.to_decimal() > value
        elif isinstance(value, ComplexDecimal) and value.is_real():
            return self.to_decimal() > value.re()
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash((self.a, self.b))
    
    def __pos__(self) -> 'Rational':
        return self
    
    def __neg__(self) -> 'Rational':
        return Rational(-self.a, self.b)
    
    def __abs__(self) -> 'Rational':
        return Rational(abs(self.a), self.b)

    def __add__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return Rational(self.a * value.b + self.b * value.a, self.b * value.b)
        elif isinstance(value, ComplexRational):
            return ComplexRational(self.a * value.b + self.b * value.a, self.b * value.b, value.c, value.d)
        elif isinstance(value, Decimal):
            return self.to_decimal() + value
        elif isinstance(value, ComplexDecimal):
            return self.to_decimal() + value
        return NotImplemented
    
    def __sub__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return Rational(self.a * value.b - self.b * value.a, self.b * value.b)
        elif isinstance(value, ComplexRational):
            return ComplexRational(self.a * value.b - self.b * value.a, self.b * value.b, -value.c, value.d)
        elif isinstance(value, Decimal):
            return self.to_decimal() - value
        elif isinstance(value, ComplexDecimal):
            return self.to_decimal() - value
        return NotImplemented
    
    def __mul__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return Rational(self.a * value.a, self.b * value.b)
        elif isinstance(value, ComplexRational):
            return ComplexRational(self.a * value.a, self.b * value.b, self.a * value.c, self.b * value.d)
        elif isinstance(value, Decimal):
            return self.to_decimal() * value
        elif isinstance(value, ComplexDecimal):
            return self.to_decimal() * value
        return NotImplemented
    
    # def __pow__(self, value : object) -> ComplexNumber:
    #     if isinstance(value, ComplexNumber):
    #         if value.is_int():
    #             if value.is_positive():
    #                 return pow_by_squaring(self, int(value))
    #             elif value.is_zero():
    #                 return Rational(1, 1)
    #             else:
    #                 return pow_by_squaring(self.inv(), -int(value))
    #         elif value.is_rational():
    #             num_root = get_int_nth_root(value.denominator(), self.numerator())
    #             den_root = get_int_nth_root(value.denominator(), self.denominator())
    #             if num_root == None or den_root == None:
    #                 return (self.log() * value).exp()
    #             else:
    #                 return Rational(num_root, den_root)
    #         else:
    #             return (self.log() * value).exp()
    #     return NotImplemented
    
    def __str__(self) -> str:
        if self.b == 1:
            return str(self.a)
        else:
            return f"{self.a}/{self.b}"

    def __int__(self) -> int:
        if not self.is_int():
            raise ValueError(f"{self} is not an int")
        return self.a
    
    def __float__(self) -> float:
        return self.a / self.b

from .complex_rational import ComplexRational
from .decimal import Decimal
from .complex_decimal import ComplexDecimal