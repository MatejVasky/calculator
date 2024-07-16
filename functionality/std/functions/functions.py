from arithmetic_expressions.functionality_database import Value, unpack_variables
from arithmetic_expressions.functionality_database.exceptions import UndefinedError
from ..numbers import ComplexNumber, Decimal
import math

@unpack_variables
def sin(*args : Value) -> Decimal:
    if len(args) != 1:
        raise UndefinedError()
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Decimal(math.sin(float(x)))
    raise UndefinedError()

@unpack_variables
def cos(*args : Value) -> Decimal:
    if len(args) != 1:
        raise UndefinedError()
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Decimal(math.cos(float(x)))
    raise UndefinedError()

@unpack_variables
def exp(*args : Value) -> Decimal:
    if len(args) != 1:
        raise UndefinedError()
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Decimal(math.exp(float(x)))
    raise UndefinedError()

@unpack_variables
def log(*args : Value) -> Decimal:
    if len(args) != 1:
        raise UndefinedError()
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_positive():
        return Decimal(math.log(float(x)))
    raise UndefinedError()