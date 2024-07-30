from datastructures import gcd, pow_by_squaring, get_int_nth_root
from .complex_number import ComplexNumber

class ComplexRational(ComplexNumber):
    """A class for complex rationals, i.e. numbers a + bi, where a and b are rational"""
    def __init__(self, a : int, b : int, c : int, d : int):
        """Creates a complex rational of the form (a/b) + (c/d)i. b and d must be non-zero"""
        # Check arguments
        if not isinstance(a, int) or not isinstance(b, int) \
            or not isinstance(c, int) or not isinstance(d, int):
            raise TypeError("a, b, c and d must be of type int")
        if b == 0 or d == 0:
            raise ValueError("b and d must be non-zero")
        
        # Make denominaors positive
        if b < 0:
            a, b = -a, -b
        if d < 0:
            c, d = -c, -d

        # Make respective numerators and denominators coprime
        re_gcd, im_gcd = gcd(a, b), gcd(c, d)
        a, b = a // re_gcd, b // re_gcd
        c, d = c // im_gcd, d // im_gcd

        # Set attributes
        self.a, self.b, self.c, self.d = a, b, c, d
    
    def __repr__(self) -> str:
        return f"ComplexRational({self.a}, {self.b}, {self.c}, {self.d})"
    
    def is_real(self) -> bool:
        return self.c == 0
    
    def is_rational(self) -> bool:
        return self.c == 0
    
    def is_complex_rational(self) -> bool:
        return True
    
    def is_int(self) -> bool:
        return self.c == 0 and self.b == 1

    def is_gaussian_int(self) -> bool:
        return self.b == 1 and self.d == 1
    
    def is_positive(self) -> bool:
        return self.a > 0 and self.c == 0
    
    def is_negative(self) -> bool:
        return self.a < 0 and self.c == 0

    def is_zero(self) -> bool:
        return self.a == 0 and self.c == 0
    
    def re(self) -> 'Rational':
        return Rational(self.a, self.b)
    
    def im(self) -> 'Rational':
        return Rational(self.c, self.d)
    
    def to_decimal(self) -> 'ComplexDecimal':
        return ComplexDecimal(self.a / self.b, self.c / self.d)
    
    def conj(self) -> 'ComplexRational':
        return ComplexRational(self.a, self.b, -self.c, self.d)
    
    def abs_squared(self) -> 'Rational':
        return Rational(self.a * self.a * self.d * self.d + self.c * self.c * self.b * self.b,
                        self.b * self.b * self.d * self.d)
    
    def inv(self) -> 'ComplexRational':
        if self.is_zero():
            raise ZeroDivisionError("Division by zero")
        con = self.conj()
        abss = self.abs_squared()
        return ComplexRational(abss.b * con.a, abss.a * con.b, abss.b * con.c, abss.a * con.d)
    
    def numerator(self) -> int:
        if self.is_rational():
            return self.a
        raise ValueError("not rational")
    
    def denominator(self) -> int:
        if self.is_rational():
            return self.b
        raise ValueError("not rational")

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Rational):
            return self.is_real() and self.a == value.a and self.b == value.b
        elif isinstance(value, ComplexRational):
            return self.a == value.a and self.b == value.b and self.c == value.c and self.d == value.d
        elif isinstance(value, Decimal):
            return self.to_decimal() == value
        elif isinstance(value, ComplexDecimal):
            return self.to_decimal() == value
        return NotImplemented
    
    def __gt__(self, value : object) -> bool:
        if not self.is_real():
            return NotImplemented
        elif isinstance(value, Rational):
            return self.is_real() and self.a * value.b > value.a * self.b
        elif isinstance(value, ComplexRational) and value.is_real():
            return self.is_real() and value.is_real() and self.a * value.b > value.a * self.b
        elif isinstance(value, Decimal):
            return self.is_real() and self.to_decimal() > value
        elif isinstance(value, ComplexDecimal) and value.is_real():
            return self.is_real() and value.is_real() and self.re().to_decimal() > value.re()
        return NotImplemented
    
    def __hash__(self) -> int:
        return hash((self.a, self.b, self.c, self.d))
    
    def __pos__(self) -> 'ComplexRational':
        return self
    
    def __neg__(self) -> 'ComplexRational':
        return ComplexRational(-self.a, self.b, -self.c, self.d)

    def __add__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return ComplexRational(self.a * value.b + self.b * value.a, self.b * value.b, self.c, self.d)
        elif isinstance(value, ComplexRational):
            return ComplexRational(self.a * value.b + self.b * value.a, self.b * value.b,
                                   self.c * value.d + self.d * value.c, self.d * value.d)
        elif isinstance(value, Decimal):
            return self.to_decimal() + value
        elif isinstance(value, ComplexDecimal):
            return self.to_decimal() + value
        return NotImplemented
    
    def __sub__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return ComplexRational(self.a * value.b - self.b * value.a, self.b * value.b, self.c, self.d)
        elif isinstance(value, ComplexRational):
            return ComplexRational(self.a * value.b - self.b * value.a, self.b * value.b,
                                   self.c * value.d - self.d * value.c, self.d * value.d)
        elif isinstance(value, Decimal):
            return self.to_decimal() - value
        elif isinstance(value, ComplexDecimal):
            return self.to_decimal() - value
        return NotImplemented
    
    def __mul__(self, value : object) -> ComplexNumber:
        if isinstance(value, Rational):
            return ComplexRational(self.a * value.a, self.b * value.b,
                                   self.c * value.a, self.d * value.b)
        elif isinstance(value, ComplexRational):
            return ComplexRational(self.a*value.a*self.d*value.d - self.c*value.c*self.b*value.b,
                                   self.b*value.b*self.d*value.d,
                                   self.c*value.a*self.b*value.d + self.a*value.c*self.d*value.b,
                                   self.b*value.b*self.d*value.d)
            # ((a1*a2*d1*d2 - c1*c2*b1*b2)/(b1*b2*d1*d2)) + ((c1*a2*b1*d2 + a1*c2*b2*d1)/(b1*d1*b2*d2))i
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
    #         elif self.is_rational() and value.is_rational():
    #             num_root = get_int_nth_root(value.denominator(), self.numerator())
    #             den_root = get_int_nth_root(value.denominator(), self.denominator())
    #             if num_root == None or den_root == None:
    #                 return (self.log() * value).exp()
    #             else:
    #                 return Rational(num_root ** value.numerator(), den_root ** value.numerator())
    #         else:
    #             return (self.log() * value).exp()
    #     return NotImplemented
    
    def __str__(self) -> str:
        r = str(self.a) if self.b == 1 else f"{self.a}/{self.b}"
        if self.c == 0:
            return r
        elif self.a == 0:
            if self.d == 1:
                if self.c == 1:
                    return "i"
                elif self.c == -1:
                    return "-i"
                else:
                    return f"{self.c}i"
            else:
                if self.c > 0:
                    return f"({self.c}/{self.d})i"
                else:
                    return f"-({-self.c}/{self.d})i"
        else:
            if self.d == 1:
                if self.c == 1:
                    s, i = '+', 'i'
                elif self.c == -1:
                    s, i = '-', 'i'
                elif self.c > 0:
                    s, i = '+', f'{self.c}i'
                else:
                    s, i = '-', f'{-self.c}i'
            else:
                if self.c > 0:
                    s, i = '+', f'({self.c}/{self.d})i'
                else:
                    s, i = '-', f'({-self.c}/{self.d})i'
            return f"{r} {s} {i}"
        
    def __int__(self) -> int:
        if not self.is_int():
            raise ValueError(f"{self} is not an int")
        return self.a

    def __float__(self) -> float:
        if not self.is_real():
            raise ValueError(f"{self} is not real")
        return self.a / self.b

from .rational import Rational
from .decimal import Decimal
from .complex_decimal import ComplexDecimal