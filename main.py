from arithmetic_expressions.parsing import ExpressionParser
from arithmetic_expressions.evaluation import ExpressionEvaluator
from data_loading import load_functionality

with open("data/functionality/default.json") as file:
    fd = load_functionality(file)

parser = ExpressionParser(fd)
evaluator = ExpressionEvaluator(fd)

while True:
    expression = input('>> ')
    tokens = parser.parse_expression(expression)
    res = evaluator.evaluate(tokens)
    print(f'Result: {res}', end='\n\n')