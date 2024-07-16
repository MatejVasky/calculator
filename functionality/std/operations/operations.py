from arithmetic_expressions.functionality_database import Value, Variable, Parameters, Function, unpack_variables
from arithmetic_expressions.functionality_database.exceptions import UndefinedError
from ..numbers import ComplexNumber, Rational

@unpack_variables
def add(a : Value, b : Value) -> Value:
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        return a + b
    raise UndefinedError()

@unpack_variables
def subtract(a : Value, b : Value) -> Value:
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        return a - b
    raise UndefinedError()

@unpack_variables
def multiply(a : Value, b : Value) -> Value:
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        return a * b
    raise UndefinedError()

@unpack_variables
def divide(a : Value, b : Value) -> Value:
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        if b.is_zero():
            raise UndefinedError()
        return a / b
    raise UndefinedError()

@unpack_variables
def floordivide(a : Value, b : Value) -> Value:
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        if not a.is_int() or not b.is_int():
            raise UndefinedError()
        if b.is_zero():
            raise UndefinedError()
        return Rational(int(a) // int(b), 1)
    raise UndefinedError()

@unpack_variables
def modulo(a : Value, b : Value) -> Value:
    if isinstance(a, ComplexNumber) and isinstance(b, ComplexNumber):
        if not a.is_int() or not b.is_int():
            raise UndefinedError()
        if b.is_zero():
            raise UndefinedError()
        return Rational(int(a) % int(b), 1)
    raise UndefinedError()

def add_parameter(a : Value, b : Value) -> Value:
    if isinstance(b, Parameters):
        raise UndefinedError()
    if isinstance(a, Parameters):
        return a + b
    else:
        return Parameters(a, b)

def evaluate_function(a : Value, b : Value) -> Value:
    if isinstance(a, Variable):
        a = a.get_value()
    if not isinstance(a, Function):
        raise UndefinedError()
    return a.evaluate(b)

@unpack_variables
def pos(a : Value) -> Value:
    if isinstance(a, ComplexNumber):
        return +a
    raise UndefinedError()

@unpack_variables
def neg(a : Value) -> Value:
    if isinstance(a, ComplexNumber):
        return -a
    raise UndefinedError()