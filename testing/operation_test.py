from arithmetic_expressions.functionality_database import Value, Variable, Function, unpack_variables, BinaryOperation, PrefixUnaryOperation
from arithmetic_expressions.functionality_database.exceptions import EvaluationError, FunctionOrOperationEvaluationError
from functionality.std import Rational
import unittest

class OperationTest(unittest.TestCase):
    def test_binary_operation_init1(self):
        addition = BinaryOperation(1, '+', '+b', [], test_addition)
        self.assertEqual(addition.priority, 1)
        self.assertEqual(addition.symbol, '+')
        self.assertEqual(addition.token, '+b')
        self.assertListEqual(addition._BinaryOperation__banned_after, [])
        self.assertEqual(addition._BinaryOperation__evaluate, test_addition)
    def test_binary_operation_init2(self):
        op = BinaryOperation(1, None, '+b', ['-'], test_addition)
        self.assertEqual(op.priority, 1)
        self.assertEqual(op.symbol, None)
        self.assertEqual(op.token, '+b')
        self.assertListEqual(op._BinaryOperation__banned_after, ['-'])
        self.assertEqual(op._BinaryOperation__evaluate, test_addition)
    def test_binary_operation_init_wrong_type1(self):
        with self.assertRaises(TypeError):
            BinaryOperation('1', '+', '+b', [], test_addition)
    def test_binary_operation_init_wrong_type2(self):
        with self.assertRaises(TypeError):
            BinaryOperation(1, 2, '+b', [], test_addition)
    def test_binary_operation_init_wrong_type3(self):
        with self.assertRaises(TypeError):
            BinaryOperation(1, '+', 3, [], test_addition)
    def test_binary_operation_init_wrong_type4(self):
        with self.assertRaises(TypeError):
            BinaryOperation(1, '+', 3, 'a', test_addition)
    def test_binary_operation_init_wrong_type5(self):
        with self.assertRaises(TypeError):
            BinaryOperation(1, '+', 3, ['a', 1], test_addition)
    
    def test_binary_operation_evaluate(self):
        addition = BinaryOperation(1, '+', '+b', [], test_addition)
        self.assertEqual(addition.evaluate(Rational(1, 2), Rational(1, 3)), Rational(5, 6))
    def test_binary_operation_evaluate_unpacking_variable(self):
        addition = BinaryOperation(1, '+', '+b', [], test_addition)
        self.assertEqual(addition.evaluate(Variable('x', Rational(1, 2)), Variable('y', Rational(1, 3))), Rational(5, 6))
    def test_binary_operation_evaluate_wrong_type1(self):
        addition = BinaryOperation(1, '+', '+b', [], test_addition)
        with self.assertRaises(TypeError):
            addition.evaluate(1, Rational(1, 4))
    def test_binary_operation_evaluate_wrong_type2(self):
        addition = BinaryOperation(1, '+', '+b', [], test_addition)
        with self.assertRaises(TypeError):
            addition.evaluate(Rational(1, 4), 1)
    def test_binary_operation_evaluate_not_unpacking_variable(self):
        assignment = BinaryOperation(0, ':=', ':=', [], test_assignment)
        x = Variable('x', Rational(1, 1))
        assignment.evaluate(x, Rational(3, 5))
        self.assertEqual(x.get_value(), Rational(3, 5))
    def test_binary_operation_evaluate_evaluation_error_handling(self):
        assignment = BinaryOperation(0, ':=', ':=', [], test_assignment)
        with self.assertRaises(EvaluationError):
            assignment.evaluate(Rational(1, 3), Rational(2, 5))
    def test_binary_operation_evaluate_other_error_handling(self):
        addition = BinaryOperation(1, '+', '+b', [], test_addition)
        with self.assertRaises(FunctionOrOperationEvaluationError):
            addition.evaluate(Function('f', test_function), Rational(1, 5))
    def test_binary_operation_evaluate_returns_int(self):
        op = BinaryOperation(1, '+', '+b', [], test_binary_int)
        with self.assertRaises(FunctionOrOperationEvaluationError):
            op.evaluate(Function('f', test_function), Rational(1, 5))
    def test_binary_operation_evaluate_returns_none(self):
        op = BinaryOperation(1, '+', '+b', [], test_binary_none)
        with self.assertRaises(FunctionOrOperationEvaluationError):
            op.evaluate(Function('f', test_function), Rational(1, 5))
    
    def test_binary_operation_is_banned_after_true(self):
        op1 = BinaryOperation(1, '*', '*', [], None)
        op2 = BinaryOperation(1, None, ' ', ['*'], None)
        self.assertTrue(op2.is_banned_after(op1))
    def test_binary_operation_is_banned_after_wrong_token(self):
        op1 = BinaryOperation(1, '/', '/', [], None)
        op2 = BinaryOperation(1, None, ' ', ['*'], None)
        self.assertFalse(op2.is_banned_after(op1))
    def test_binary_operation_is_banned_after_different_priorities(self):
        op1 = BinaryOperation(1, '*', '*', [], None)
        op2 = BinaryOperation(2, None, ' ', ['*'], None)
        self.assertFalse(op2.is_banned_after(op1))
    def test_binary_operation_is_banned_after_prefix_unary_operation(self):
        op1 = PrefixUnaryOperation(1, '-', '-u', None)
        op2 = BinaryOperation(2, None, ' ', ['*'], None)
        self.assertFalse(op2.is_banned_after(op1))
    
    def test_prefix_unary_operation_init1(self):
        neg = PrefixUnaryOperation(1, '-', '-u', test_neg)
        self.assertEqual(neg.priority, 1)
        self.assertEqual(neg.symbol, '-')
        self.assertEqual(neg.token, '-u')
        self.assertEqual(neg._PrefixUnaryOperation__evaluate, test_neg)
    def test_prefix_unary_operation_init2(self):
        op = PrefixUnaryOperation(1, None, '-u', test_neg)
        self.assertEqual(op.priority, 1)
        self.assertEqual(op.symbol, None)
        self.assertEqual(op.token, '-u')
        self.assertEqual(op._PrefixUnaryOperation__evaluate, test_neg)
    def test_prefix_unary_operation_init_wrong_type1(self):
        with self.assertRaises(TypeError):
            PrefixUnaryOperation('1', '-', '-u', test_neg)
    def test_prefix_unary_operation_init_wrong_type2(self):
        with self.assertRaises(TypeError):
            PrefixUnaryOperation(1, 2, '-u', test_neg)
    def test_prefix_unary_operation_init_wrong_type3(self):
        with self.assertRaises(TypeError):
            PrefixUnaryOperation(1, '-', 3, test_neg)
    
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
        with self.assertRaises(FunctionOrOperationEvaluationError):
            neg.evaluate(Function('f', test_function))
    def test_prefix_unary_operation_evaluate_returns_int(self):
        op = PrefixUnaryOperation(1, '-', '-u', test_unary_int)
        with self.assertRaises(FunctionOrOperationEvaluationError):
            op.evaluate(Rational(1, 5))
    def test_prefix_unary_operation_evaluate_returns_none(self):
        op = PrefixUnaryOperation(1, '-', '-u', test_unary_none)
        with self.assertRaises(FunctionOrOperationEvaluationError):
            op.evaluate(Rational(1, 5))
    
@unpack_variables
def test_addition(a : Value, b : Value):
    return a + b

def test_assignment(a : Value, b : Value):
    if not isinstance(a, Variable):
        raise EvaluationError('not a variable')
    if isinstance(b, Variable):
        b = b.get_value()
    a.set_value(b)
    return b

@unpack_variables
def test_neg(a : Value):
    return -a

def test_increment(a : Value):
    if not isinstance(a, Variable):
        raise EvaluationError('not a variable')
    a.set_value(a.get_value() + Rational(1, 1))
    return a.get_value()

def test_function(*args):
    if len(args) == 0:
        raise EvaluationError('hello')
    return args[0]

def test_binary_int(a : Value, b : Value):
    return 1

def test_binary_none(a : Value, b : Value):
    return None

def test_unary_int(a : Value):
    return 1

def test_unary_none(a : Value):
    return None

if __name__ == "__main__":
    unittest.main()