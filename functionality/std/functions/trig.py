from arithmetic_expressions.functionality_database import Value, unpack_variables
from arithmetic_expressions.functionality_database.exceptions import WrongNumberOfArgumentsError, UndefinedError
from ..numbers import ComplexNumber, Decimal
import math

@unpack_variables
def sin(*args : Value) -> Decimal:
    """Computes the sine"""
    # Check the number of arguments
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("sin takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Decimal(math.sin(float(x)))
    raise UndefinedError("sin expects a real number as an argument")

@unpack_variables
def cos(*args : Value) -> Decimal:
    """Computes the cosine"""
    # Check the number of arguments
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("cos takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Decimal(math.cos(float(x)))
    raise UndefinedError("cos expects a real number as an argument")

@unpack_variables
def tan(*args : Value) -> Decimal:
    """Computes the tangent"""
    # Check the number of arguments
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("tan takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        if math.cos(float(x)) == 0:
            raise UndefinedError("cot is undefined")
        return Decimal(math.sin(float(x)) / math.cos(float(x)))
    raise UndefinedError("tan expects a real number as an argument")

@unpack_variables
def cot(*args : Value) -> Decimal:
    """Computes the cotangent"""
    # Check the number of arguments
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("cot takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        if math.sin(float(x)) == 0:
            raise UndefinedError("cot is undefined")
        return Decimal(math.cos(float(x)) / math.sin(float(x)))
    raise UndefinedError("cot expects a real number as an argument")

@unpack_variables
def sec(*args : Value) -> Decimal:
    """Computes the secant"""
    # Check the number of arguments
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("sec takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        if math.cos(float(x)) == 0:
            raise UndefinedError("sec is undefined")
        return Decimal(1 / math.cos(float(x)))
    raise UndefinedError("sec expects a real number as an argument")

@unpack_variables
def csc(*args : Value) -> Decimal:
    """Computes the cosecant"""
    # Check the number of arguments
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("csc takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        if math.sin(float(x)) == 0:
            raise UndefinedError("csc is undefined")
        return Decimal(1 / math.sin(float(x)))
    raise UndefinedError("csc expects a real number as an argument")

@unpack_variables
def arcsin(*args : Value) -> Decimal:
    """Computes the arcsine. Takes values from [-1, 1] and returns a value from [-pi/2, pi/2]"""
    # Check the number of arguments
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("arcsin takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real() and -1 <= float(x) and float(x) <= 1:
        return Decimal(math.asin(float(x)))
    raise UndefinedError("arcsin expects an argument from [-1, 1]")

@unpack_variables
def arccos(*args : Value) -> Decimal:
    """Computes the arccosine. Takes values from [-1, 1] and returns a value from [0, pi]"""
    # Check the number of arguments
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("arccos takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real() and -1 <= float(x) and float(x) <= 1:
        return Decimal(math.acos(float(x)))
    raise UndefinedError("arccos expects an argument from [-1, 1]")

@unpack_variables
def arctan(*args : Value) -> Decimal:
    """Computes the arctangent. Returns values from (-pi/2, pi/2)"""
    # Check the number of arguments
    if len(args) != 1:
        raise WrongNumberOfArgumentsError("arctan takes 1 argument")
    
    x = args[0]
    if isinstance(x, ComplexNumber) and x.is_real():
        return Decimal(math.atan(float(x)))
    raise UndefinedError("arctan expects a real number as argument")