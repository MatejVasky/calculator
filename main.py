from arithmetic_expressions.parsing import ExpressionParser
from arithmetic_expressions.evaluation import ExpressionEvaluator
from arithmetic_expressions.functionality_database.exceptions import ParsingError, EvaluationError
from data_loading import load_functionality

print("Welcome to calculator", end="\n\n")

print("Loading functionality...")
try:
    with open("data/functionality/default.json") as file:
        fd = load_functionality(file)
except:
    print("Failed to load functionality")
    input("Press enter to close the program")
    quit()
print("Functionality loaded", end="\n\n")

parser = ExpressionParser(fd)
evaluator = ExpressionEvaluator(fd)

while True:
    expression = input('>> ')

    try:
        tokens = parser.parse_expression(expression)
    except ParsingError as e:
        print("An error occurred:", e)
    else:
        if len(tokens) != 0:
            try:
                res = evaluator.evaluate(tokens)
            except EvaluationError as e:
                print("An error occurred:", e)
            else:
                print(f'Result: {res}')
                
                approx = res.get_approximate_value()
                if approx != None:
                    print(f'Approximate result: {approx}')

    print()