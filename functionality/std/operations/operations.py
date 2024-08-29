from arithmetic_expressions.functionality_database import Value, Variable, Parameters, Function, unpack_variables
from arithmetic_expressions.functionality_database.exceptions import UndefinedError
from ..numbers import ComplexNumber, Rational

@unpack_variables
def add(a : Value, b : Value) -> Value:
    """Addition"""
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        return a + b
    raise UndefinedError("addition undefined")

@unpack_variables
def subtract(a : Value, b : Value) -> Value:
    """Subtraction"""
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        return a - b
    raise UndefinedError("subtraction undefined")

@unpack_variables
def multiply(a : Value, b : Value) -> Value:
    """Multiplication"""
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        return a * b
    raise UndefinedError("multiplication undefined")

@unpack_variables
def divide(a : Value, b : Value) -> Value:
    """Division"""
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        if b.is_zero():
            raise UndefinedError("cannot divide by zero")
        return a / b
    raise UndefinedError("division undefined")

@unpack_variables
def floordivide(a : Value, b : Value) -> Value:
    """Only works with integers. Returns floor(a/b)"""
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        if not a.is_int() or not b.is_int():
            raise UndefinedError("can only perform floor division on integers")
        if b.is_zero():
            raise UndefinedError("cannot divide by zero")
        return Rational(int(a) // int(b), 1)
    raise UndefinedError("floor division undefined")

@unpack_variables
def modulo(a : Value, b : Value) -> Value:
    """Only works with integers. Returns the remainder of a modulo b"""
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        if not a.is_int() or not b.is_int():
            raise UndefinedError("can only perform modulo on integers")
        if b.is_zero():
            raise UndefinedError("cannot divide by zero")
        return Rational(int(a) % int(b), 1)
    raise UndefinedError("modulo undefined")

@unpack_variables
def power(a : Value, b : Value) -> Value:
    """Returns a^b"""
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        if a.is_zero() and not b.is_positive():
            raise UndefinedError("zero can only be raised to a positive power")
        return a ** b
    raise UndefinedError("exponentiation undefined")

def add_parameter(a : Value, b : Value) -> Value:
    """If a is of type Parameters, returns a + b. Otherwise returns Parameters(a, b)"""
    if isinstance(b, Parameters):
        raise UndefinedError("cannot add parameters from the right")
    if isinstance(a, Parameters):
        return a + b
    else:
        return Parameters(a, b)

def evaluate_function(a : Value, b : Value) -> Value:
    """Evaluates function a with b as the argument"""
    if isinstance(a, Variable):
        a = a.get_value()
    if not isinstance(a, Function):
        raise UndefinedError("cannot evaluate value, that is not a function")
    return a.evaluate(b)

@unpack_variables
def pos(a : Value) -> Value:
    """Returns +a"""
    if isinstance(a, ComplexNumber):
        return +a
    raise UndefinedError("positive operation failed")

@unpack_variables
def neg(a : Value) -> Value:
    """Returns -a"""
    if isinstance(a, ComplexNumber):
        return -a
    raise UndefinedError("negative operation failed")

def assign_to_variable(a : Value, b : Value) -> Value:
    """Assigns a value to a variable"""
    if isinstance(b, Variable):
        b = b.get_value()
    if isinstance(a, Variable) and isinstance(b, ComplexNumber):
        a.set_value(b)
        return b
    raise UndefinedError("variable assignment failed")