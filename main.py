from arithmetic_expressions.parsing import ExpressionParser
from arithmetic_expressions.evaluation import ExpressionEvaluator
from arithmetic_expressions.functionality_database.exceptions import ParsingError, EvaluationError
from data_loading import load_functionality

# Welcome message
print("Welcome to calculator", end="\n\n")

# Functionality loading
print("Loading functionality...")
try:
    with open("data/functionality/default.json") as file:
        fd = load_functionality(file)
except:
    print("Failed to load functionality")
    input("Press enter to close the program")
    quit()
print("Functionality loaded")

# Initializing the parser and the evaluator
parser = ExpressionParser(fd)
evaluator = ExpressionEvaluator(fd)

while True:
    print()

    # Get input
    expression = input('>> ')

    # Try parsing
    try:
        tokens = parser.parse_expression(expression)
    except ParsingError as e:
        print("An error occurred:", e)
        continue

    # If the expression is empty, continue
    if len(tokens) == 0:
        continue

    # Try evaluating
    try:
        res = evaluator.evaluate(tokens)
    except EvaluationError as e:
        print("An error occurred:", e)
        continue
    
    # Print result
    print(f'Result: {res}')
    
    # Try getting an approximate value
    try:
        approx = res.get_approximate_value()
    except Exception:
        print("Failed to compute an approximate value")
    else:
        if approx != None:
            print(f'Approximate result: {approx}')