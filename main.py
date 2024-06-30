from functionality_database import FunctionalityDatabase
from arithmetic_expression_parser import ExpressionParser, ParsingError

parser = ExpressionParser(FunctionalityDatabase())

while True:
    try:
        print(parser.parse_expression(input()))
    except ParsingError as e:
        print(e)