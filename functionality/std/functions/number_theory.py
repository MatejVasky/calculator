from arithmetic_expressions.functionality_database import Value, unpack_variables
from arithmetic_expressions.functionality_database.exceptions import WrongNumberOfArgumentsError, UndefinedError
from ..numbers import ComplexNumber, Rational
import datastructures

@unpack_variables
def gcd(*args : Value) -> Rational:
    if len(args) != 2:
        raise WrongNumberOfArgumentsError("gcd takes 2 arguments")
    
    m = args[0]
    n = args[1]
    if isinstance(m, ComplexNumber) and m.is_int() and isinstance(n, ComplexNumber) and n.is_int():
        return Rational(datastructures.gcd(int(m), int(n)), 1)
    raise UndefinedError("gcd takes a pair of integers as arguments")

@unpack_variables
def lcm(*args : Value) -> Rational:
    if len(args) != 2:
        raise WrongNumberOfArgumentsError("lcm takes 2 arguments")
    
    m = args[0]
    n = args[1]
    if isinstance(m, ComplexNumber) and m.is_int() and m.is_positive() and isinstance(n, ComplexNumber) and n.is_int() and n.is_positive():
        d = Rational(datastructures.gcd(int(m), int(n)), 1)
        return m * n / d
    raise UndefinedError("lcm takes a pair of positive integers as arguments")