import unittest
from arithmetic_expressions.functionality_database import FunctionalityDatabase, Function, PrefixUnaryOperation, BinaryOperation
from arithmetic_expressions.parsing import ExpressionParser
from arithmetic_expressions.evaluation import ExpressionEvaluator
from functionality.std import Rational, Decimal, ComplexRational
import functionality.std
import math

class FullEvaluationTest(unittest.TestCase):
    def test_addition(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('3+5')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(8, 1))
    def test_subtraction(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('3-5')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(-2, 1))
    def test_addition_multiplication1(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('3+5*2')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(13, 1))
    def test_addition_multiplication2(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('3*5+2')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(17, 1))
    def test_addition_multiplication_brackets1(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('(3+5)*2')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(16, 1))
    def test_addition_multiplication_brackets2(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('3*(5+2)')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(21, 1))
    def test_unary_operator(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('-10')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(-10, 1))
    def test_unary_operator_addition(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('+10+-5')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(5, 1))
    def test_unary_operator_multiplication(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('-10*-2')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(20, 1))
    def test_unary_operator_complicated(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('-(+(-5-2)*3)+5')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(26, 1))
    def test_constant(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('pi')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(22, 7))
    def test_implicit_multiplication(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('2pi')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Rational(44, 7))
    def test_function(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('exp(0)')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, Decimal(1))
    def test_function2(self):
        fd = create_fd()
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('sin(pi)')
        res = evaluator.evaluate(tokens)
        self.assertAlmostEqual(float(res), math.sin(22/7))
    def test_complex(self):
        fd = create_fd()
        fd.constants['i'] = ComplexRational(0, 1, 1, 1)
        parser = ExpressionParser(fd)
        evaluator = ExpressionEvaluator(fd)
        tokens = parser.parse_expression('1/(1-i)')
        res = evaluator.evaluate(tokens)
        self.assertEqual(res, ComplexRational(1, 2, 1, 2))

LETTERS = set([chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)])
DIGITS = set([str(i) for i in range(10)])
PUNCTUATION = set(['+', '-', '*', '/', '%', ','])

def create_fd() -> FunctionalityDatabase:
    fd = FunctionalityDatabase(' ', '()', '(', '.', LETTERS, DIGITS, PUNCTUATION, functionality.std.parse_int, functionality.std.parse_decimal)

    fd.register_operation(BinaryOperation(1, '+', '+', functionality.std.add))
    fd.register_operation(BinaryOperation(1, '-', '-', functionality.std.subtract))
    fd.register_operation(BinaryOperation(2, '*', '*', functionality.std.multiply))
    fd.register_operation(BinaryOperation(2, '/', '/', functionality.std.divide))
    fd.register_operation(BinaryOperation(2, '//', '//', functionality.std.floordivide))
    fd.register_operation(BinaryOperation(2, '%', '%', functionality.std.modulo))
    fd.register_operation(PrefixUnaryOperation(1, '+', '+u', functionality.std.pos))
    fd.register_operation(PrefixUnaryOperation(1, '-', '-u', functionality.std.neg))
    fd.register_operation(BinaryOperation(2, None, ' ', functionality.std.multiply))
    fd.register_operation(BinaryOperation(0, ',', ',', functionality.std.add_parameter))
    fd.register_operation(BinaryOperation(3, None, '()', functionality.std.evaluate_function))

    fd.register_bracket('(', ')')
    fd.register_bracket('[', ']')

    fd.register_constant('pi', Rational(22, 7))
    for i in range(ord('a'), ord('z') + 1):
        fd.register_variable(chr(i))
    for i in range(ord('A'), ord('Z') + 1):
        fd.register_variable(chr(i))
    
    fd.register_function(Function('sin', functionality.std.sin))
    fd.register_function(Function('cos', functionality.std.cos))
    fd.register_function(Function('exp', functionality.std.exp))
    fd.register_function(Function('log', functionality.std.ln))

    return fd


if __name__ == '__main__':
    unittest.main()