from abc import abstractmethod
from math import sqrt, atan2, log, exp, cos, sin
from typing import Union
from arithmetic_expressions.functionality_database import Value
from datastructures import gcd, pow_by_squaring, get_int_nth_root

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

    @abstractmethod
    def numerator(self) -> int:
        """Returns the numerator of a (real) rational number"""
    
    @abstractmethod
    def denominator(self) -> int:
        """Returns the denominator of a (real) rational number"""
    
    def arg(self) -> 'Decimal':
        """Returns the argument"""
        if self.is_zero():
            raise ValueError("argument of 0 is undefined")
        return Decimal(atan2(float(self.im()), float(self.re())))
    
    def log(self) -> Union['Decimal', 'ComplexDecimal']:
        """Returns the logarithm (with the imaginary part from (-pi, pi])"""
        if self.is_zero():
            raise ValueError("log(0) is undefined")
        if self.is_positive():
            return Decimal(log(self))
        else:
            return ComplexDecimal(log(abs(self)), float(self.arg()))
    
    def exp(self) -> Union['Decimal', 'ComplexDecimal']:
        """Applies the complex exponential to this number"""
        if self.is_real():
            return Decimal(exp(self))
        else:
            r = exp(self.re())
            theta = self.im()
            return ComplexDecimal(r * cos(theta), r * sin(theta))
    
    def __abs__(self) -> 'ComplexNumber':
        return Decimal(sqrt(self.abs_squared().to_decimal().val))
    
    def __truediv__(self, value : object) -> 'ComplexNumber':
        if isinstance(value, ComplexNumber):
            if value.is_zero():
                raise ZeroDivisionError()
            else:
                return self * value.inv()
        return NotImplemented
    
    def __pow__(self, value : object) -> 'ComplexNumber':
        if isinstance(value, ComplexNumber):
            if self.is_zero():
                if value.is_positive():
                    return self
                else:
                    raise ValueError("zero can only be raised to a positive power")
                
            elif self.is_complex_rational() and value.is_int():
                if value.is_positive():
                    return pow_by_squaring(self, int(value))
                elif value.is_zero():
                    return Rational(1, 1)
                else:
                    return pow_by_squaring(self.inv(), -int(value))
                
            elif self.is_rational() and value.is_rational():
                if self.numerator() < 0 and value.denominator() % 2 == 0:
                    return self.__default_pow(value)

                num_root = get_int_nth_root(value.denominator(), abs(self.numerator()))
                den_root = get_int_nth_root(value.denominator(), self.denominator())

                if num_root == None or den_root == None:
                    return self.__default_pow(value)
                
                if self.numerator() < 0:
                    num_root = -num_root

                if value.is_positive():
                    return Rational(num_root ** value.numerator(), den_root ** value.numerator())
                else:
                    return Rational(den_root ** -value.numerator(), num_root ** -value.numerator())
                    
            else:
                return self.__default_pow(value)
        return NotImplemented
    
    def __default_pow(self, value : 'ComplexNumber') -> 'ComplexNumber':
        """Returns e^(value * log(self)). If self is negative real, it tries to find a real result. If such a result does not exist, it returns a complex result"""
        if self.is_negative() and value.is_rational() and value.denominator() % 2 == 1:
            return -(abs(self).log() * value).exp()
        else:
            return (self.log() * value).exp()

from .rational import Rational
from .decimal import Decimal
from .complex_decimal import ComplexDecimal