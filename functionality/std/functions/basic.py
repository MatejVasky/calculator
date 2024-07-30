from arithmetic_expressions.functionality_database import Value, unpack_variables
from arithmetic_expressions.functionality_database.exceptions import WrongNumberOfArgumentsError, UndefinedError
from ..numbers import ComplexNumber, Decimal, ComplexDecimal, Rational
from typing import Union
import math

@unpack_variables
def exp(*args : Value) -> Union['Decimal', 'ComplexDecimal']:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("exp takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber):
        return x.exp()
    raise UndefinedError("exp expects a complex number as an argument")

@unpack_variables
def ln(*args : Value) -> Union['Decimal', 'ComplexDecimal']:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("ln takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber):
        if x.is_zero():
            raise UndefinedError("log(0) is undefined")
        return x.log()
    raise UndefinedError("log expects a complex number as an argument")

@unpack_variables
def log(*args : Value) -> Union['Decimal', 'ComplexDecimal']:
    if len(args) == 1:
        return ln(args[0])
    elif len(args) == 2:
        b = args[0]
        x = args[1]
        if not isinstance(b, ComplexNumber) or not b.is_positive() or float(b) == 1:
            raise UndefinedError("log base must be from (0, 1) U (1, infinity)")
        if not isinstance(x, ComplexNumber) or not x.is_positive():
            raise UndefinedError("log argument must be from (0, infinity)")
        return x.log() / b.log()
    else:
        raise WrongNumberOfArgumentsError("log takes 1 or 2 arguments")

@unpack_variables
def sign(*args : Value) -> ComplexNumber:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("sign takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        if x.is_positive():
            return Rational(1, 1)
        elif x.is_zero():
            return Rational(0, 1)
        else:
            return Rational(-1, 1)
    raise UndefinedError("sign expects a real number as an argument")

@unpack_variables
def sqrt(*args : Value) -> Decimal:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("sqrt takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber):
        return x ** Rational(1, 2)
    raise UndefinedError("sin expects a complex number as an argument")

@unpack_variables
def root(*args : Value) -> Decimal:
    if len(args) != 2:
        raise WrongNumberOfArgumentsError("root takes 2 arguments")
    
    n = args[0]
    x = args[1]
    if not isinstance(n, ComplexNumber) or n.is_zero():
        raise UndefinedError("the first argument of root must be a non-zero complex number")
    if not isinstance(x, ComplexNumber):
        raise UndefinedError("the second argument of root must be a complex number")
    return x ** n.inv()

@unpack_variables
def floor(*args : Value) -> Decimal:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("floor takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Rational(math.floor(x), 1)
    raise UndefinedError("floor expects a real number as an argument")

@unpack_variables
def ceil(*args : Value) -> Decimal:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("ceil takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Rational(math.ceil(x), 1)
    raise UndefinedError("ceil expects a real number as an argument")