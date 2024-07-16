from arithmetic_expressions.functionality_database import Function, Parameters, Variable, unpack_variables
from arithmetic_expressions.functionality_database.exceptions import EvaluationError, FunctionOrOperationEvaluationException
from functionality.std import Rational
import unittest

class FunctionTest(unittest.TestCase):
    def test_function_init(self):
        f = Function('f', test_function)
        self.assertEqual(f.name, 'f')
        self.assertEqual(f._Function__evaluate, test_function)
    def test_function_init_wrong_type(self):
        with self.assertRaises(TypeError):
            Function(1, test_function)
    
    def test_function_evaluate_no_params(self):
        f = Function('f', test_function)
        self.assertEqual(f.evaluate(Parameters()), Rational(0, 1))
    def test_function_evaluate_multiple_params(self):
        f = Function('f', test_function)
        self.assertEqual(f.evaluate(Parameters(Rational(1, 1), Rational(1, 2), Rational(3, 4))), Rational(1, 1))
    def test_function_evaluate_one_packed_param(self):
        f = Function('f', test_function)
        self.assertEqual(f.evaluate(Parameters(Rational(1, 1))), Rational(1, 1))
    def test_function_evaluate_one_unpacked_param(self):
        f = Function('f', test_function)
        self.assertEqual(f.evaluate(Rational(1, 1)), Rational(1, 1))
    def test_function_evaluate_unpacking_variable(self):
        f = Function('f', test_function)
        self.assertEqual(f.evaluate(Variable('x', Rational(1, 1))), Rational(1, 1))
    def test_function_evaluate_wrong_type(self):
        f = Function('f', test_function)
        with self.assertRaises(TypeError):
            f.evaluate(1)
    def test_function_evaluate_not_unpacking_variable(self):
        f = Function('f', test_function2)
        x = Variable('x', Rational(1, 1))
        self.assertEqual(f.evaluate(x), x)
    def test_function_evaluate_evaluation_error_handling(self):
        f = Function('f', test_function3)
        with self.assertRaises(EvaluationError):
            f.evaluate(Parameters())
    def test_function_evaluate_other_error_handling(self):
        f = Function('f', test_function4)
        with self.assertRaises(FunctionOrOperationEvaluationException):
            f.evaluate(Parameters())
    

@unpack_variables
def test_function(*args):
    if len(args) == 0:
        return Rational(0, 1)
    return args[0]

def test_function2(*args):
    if len(args) == 0:
        return Rational(0, 1)
    return args[0]

def test_function3(*args):
    if len(args) == 0:
        raise EvaluationError('hello')
    return args[0]

def test_function4(*args):
    return args[0]


if __name__ == "__main__":
    unittest.main()