from arithmetic_expressions.functionality_database import Value, unpack_variables
from arithmetic_expressions.functionality_database.exceptions import WrongNumberOfArgumentsError, UndefinedError
from ..numbers import ComplexNumber, Decimal
import math

@unpack_variables
def sin(*args : Value) -> Decimal:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("sin takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Decimal(math.sin(float(x)))
    raise UndefinedError("sin expects a complex number as an argument")

@unpack_variables
def cos(*args : Value) -> Decimal:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("cos takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Decimal(math.cos(float(x)))
    raise UndefinedError("cos expects a complex number as an argument")

@unpack_variables
def exp(*args : Value) -> Decimal:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("exp takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Decimal(math.exp(float(x)))
    raise UndefinedError("exp expects a complex number as an argument")

@unpack_variables
def log(*args : Value) -> Decimal:
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("log takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_positive():
        return Decimal(math.log(float(x)))
    raise UndefinedError("log expects a complex number as an argument")