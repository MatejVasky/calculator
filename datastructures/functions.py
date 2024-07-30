from typing import Any, Optional
from math import floor

def gcd(a : int, b : int):
    """Returns the greatest common divisor of a and b"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b have to be of type int")
    a, b = abs(a), abs(b)
    while a > 0:
        a, b = b % a, a
    return b

def pow_by_squaring(value, n : int) -> Any:
    """Multiplies value n times"""
    if not isinstance(n, int):
        raise TypeError("n must be of type int")
    if n <= 0:
        raise ValueError("n must be positive")
    
    try:
        return pow_by_squaring_inner(value, n)
    except Exception:
        raise ValueError("value does not support multiplication")

def pow_by_squaring_inner(value, n : int) -> Any:
    """A recursive implementation of the exponentiation by squaring algorithm"""
    if n == 1:
        return value
    elif n % 2 == 0:
        smaller_pow = pow_by_squaring_inner(value, n // 2)
        return smaller_pow * smaller_pow
    else:
        smaller_pow = pow_by_squaring_inner(value, n // 2)
        return smaller_pow * smaller_pow * value

def get_int_nth_root(n : int, x : int) -> Optional[int]:
    """Computes the nth root of x. Returns None if it is not an integer"""
    if not isinstance(n, int):
        raise TypeError("n must be of type int")
    if not isinstance(x, int):
        raise TypeError("x must be of type int")
    if n <= 0:
        raise ValueError("n must be positive")
    if x < 0:
        raise ValueError("x must be non-negative")
    
    approx = x ** (1/n)
    fl = floor(approx)
    if fl ** n == x:
        return fl
    elif (fl + 1) ** n == x:
        return fl + 1
    else:
        return None