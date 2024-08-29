from typing import Any, Optional
from math import floor

def gcd(a : int, b : int):
    """Returns the greatest common divisor of a and b"""
    # Type check
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b have to be of type int")
    # Euclid's algorithm
    a, b = abs(a), abs(b)
    while a > 0:
        a, b = b % a, a
    # Return
    return b

def pow_by_squaring(value, n : int) -> Any:
    """Multiplies value n times"""
    # Type and value check
    if not isinstance(n, int):
        raise TypeError("n must be of type int")
    if n <= 0:
        raise ValueError("n must be positive")
    # Evaluate
    try:
        return pow_by_squaring_inner(value, n)
    except Exception:
        raise ValueError("value does not support multiplication")

def pow_by_squaring_inner(value, n : int) -> Any:
    """A recursive implementation of the exponentiation by squaring algorithm"""
    # x^1 = x
    if n == 1:
        return value
    # x^(2k) = (x^k) * (x^k)
    elif n % 2 == 0:
        smaller_pow = pow_by_squaring_inner(value, n // 2)
        return smaller_pow * smaller_pow
    # x^(2k + 1) = (x^k) * (x^k) * x
    else:
        smaller_pow = pow_by_squaring_inner(value, n // 2)
        return smaller_pow * smaller_pow * value

def get_int_nth_root(n : int, x : int) -> Optional[int]:
    """Computes the nth root of x. Returns None if it is not an integer"""
    # Type and value checks
    if not isinstance(n, int):
        raise TypeError("n must be of type int")
    if not isinstance(x, int):
        raise TypeError("x must be of type int")
    if n <= 0:
        raise ValueError("n must be positive")
    if x < 0:
        raise ValueError("x must be non-negative")
    
    # Get an approximate value (with an error of less than 1, hopefully)
    approx = x ** (1/n)
    # Round it down to the nearest integer
    fl = floor(approx)
    # Try exponentiating the rounded down version. If you get the original value, that is the exact result
    if fl ** n == x:
        return fl
    # Try the same with the next integer (i.e. f1 + 1)
    elif (fl + 1) ** n == x:
        return fl + 1
    # If that does not work, the root is not an integer
    else:
        return None