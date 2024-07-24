from arithmetic_expressions.functionality_database.exceptions import ParserError
from .numbers import Rational, Decimal

def parse_int(token : str) -> Rational:
    try:
        value = int(token)
    except ValueError:
        raise ParserError("failed to parse integer token")
    return Rational(value, 1)

def parse_decimal(token : str) -> Decimal:
    try:
        value = float(token)
    except ValueError:
        raise ParserError("failed to parse decimal token")
    return Decimal(value)