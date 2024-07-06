def gcd(a : int, b : int):
    """Returns the greatest common divisor of a and b"""
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b have to be of type int")
    a, b = abs(a), abs(b)
    while a > 0:
        a, b = b % a, a
    return b