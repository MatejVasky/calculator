from arithmetic_expressions.functionality_database import Value, Variable, Function, unpack_variables, BinaryOperation, PrefixUnaryOperation
from arithmetic_expressions.evaluation import EvaluationError, FunctionOrOperationEvaluationException
from functionality.std import Rational
import unittest

class OperationTest(unittest.TestCase):
    def test_binary_operation_init(self):
        addition = BinaryOperation(1, '+', '+b', test_addition)
        self.assertEqual(addition.priority, 1)
        self.assertEqual(addition.symbol, '+')
        self.assertEqual(addition.token, '+b')
        self.assertEqual(addition._BinaryOperation__evaluate, test_addition)
    
    def test_binary_operation_evaluate(self):
        addition = BinaryOperation(1, '+', '+b', test_addition)
        self.assertEqual(addition.evaluate(Rational(1, 2), Rational(1, 3)), Rational(5, 6))
    def test_binary_operation_evaluate_unpacking_variable(self):
        addition = BinaryOperation(1, '+', '+b', test_addition)
        self.assertEqual(addition.evaluate(Variable('x', Rational(1, 2)), Variable('y', Rational(1, 3))), Rational(5, 6))
    def test_binary_operation_evaluate_wrong_type1(self):
        addition = BinaryOperation(1, '+', '+b', test_addition)
        with self.assertRaises(TypeError):
            addition.evaluate(1, Rational(1, 4))
    def test_binary_operation_evaluate_wrong_type2(self):
        addition = BinaryOperation(1, '+', '+b', test_addition)
        with self.assertRaises(TypeError):
            addition.evaluate(Rational(1, 4), 1)
    def test_binary_operation_evaluate_not_unpacking_variable(self):
        assignment = BinaryOperation(0, ':=', ':=', test_assignment)
        x = Variable('x', Rational(1, 1))
        assignment.evaluate(x, Rational(3, 5))
        self.assertEqual(x.get_value(), Rational(3, 5))
    def test_binary_operation_evaluate_evaluation_error_handling(self):
        assignment = BinaryOperation(0, ':=', ':=', test_assignment)
        with self.assertRaises(EvaluationError):
            assignment.evaluate(Rational(1, 3), Rational(2, 5))
    def test_binary_operation_evaluate_other_error_handling(self):
        addition = BinaryOperation(1, '+', '+b', test_addition)
        with self.assertRaises(FunctionOrOperationEvaluationException):
            addition.evaluate(Function('f', test_function), Rational(1, 5))
    
    def test_prefix_unary_operation_init(self):
        neg = PrefixUnaryOperation(1, '-', '-u', test_neg)
        self.assertEqual(neg.priority, 1)
        self.assertEqual(neg.symbol, '-')
        self.assertEqual(neg.token, '-u')
        self.assertEqual(neg._PrefixUnaryOperation__evaluate, test_neg)
    
    def test_prefix_unary_operation_evaluate(self):
        neg = PrefixUnaryOperation(1, '-', '-u', test_neg)
        self.assertEqual(neg.evaluate(Rational(1, 2)), Rational(-1, 2))
    def test_prefix_unary_operation_evaluate_unpacking_variable(self):
        neg = PrefixUnaryOperation(1, '-', '-u', test_neg)
        self.assertEqual(neg.evaluate(Variable('x', Rational(1, 2))), Rational(-1, 2))
    def test_prefix_unary_operation_evaluate_wrong_type(self):
        neg = PrefixUnaryOperation(1, '-', '-u', test_neg)
        with self.assertRaises(TypeError):
            neg.evaluate(1)
    def test_prefix_unary_operation_evaluate_not_unpacking_variable(self):
        increment = PrefixUnaryOperation(1, '++', '++', test_increment)
        x = Variable('x', Rational(1, 1))
        increment.evaluate(x)
        self.assertEqual(x.get_value(), Rational(2, 1))
    def test_prefix_unary_operation_evaluate_evaluation_error_handling(self):
        increment = PrefixUnaryOperation(1, '++', '++', test_increment)
        with self.assertRaises(EvaluationError):
            increment.evaluate(Rational(1, 3))
    def test_prefix_unary_operation_evaluate_other_error_handling(self):
        neg = PrefixUnaryOperation(1, '-', '-u', test_neg)
        with self.assertRaises(FunctionOrOperationEvaluationException):
            neg.evaluate(Function('f', test_function))
    
@unpack_variables
def test_addition(a : Value, b : Value):
    return a + b

def test_assignment(a : Value, b : Value):
    if not isinstance(a, Variable):
        raise EvaluationError('not a variable')
    if isinstance(b, Variable):
        b = b.get_value()
    a.set_value(b)

@unpack_variables
def test_neg(a : Value):
    return -a

def test_increment(a : Value):
    if not isinstance(a, Variable):
        raise EvaluationError('not a variable')
    a.set_value(a.get_value() + Rational(1, 1))

def test_function(*args):
    if len(args) == 0:
        raise EvaluationError('hello')
    return args[0]

if __name__ == "__main__":
    unittest.main()