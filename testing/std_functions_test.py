from functionality.std import Rational, ComplexRational, Decimal, ComplexDecimal, add, subtract, multiply, divide, floordivide, modulo, pos, neg, sin, cos, exp, log
from arithmetic_expressions.functionality_database.exceptions import WrongNumberOfArgumentsError, UndefinedError
from arithmetic_expressions.functionality_database import Variable
import unittest
import math

class STDOperationsTest(unittest.TestCase):
    def test_sin1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(sin(q)), math.sin(4/5))
    def test_sin2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(sin(q)), math.sin(0.5))
    def test_sin_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            sin()
    def test_sin_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            sin(q1, q2)
    def test_sin_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            sin(q)
    def test_sin_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            sin(q)
    def test_sin_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(float(sin(q)), math.sin(2/3))
    
    def test_cos1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(cos(q)), math.cos(4/5))
    def test_cos2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(cos(q)), math.cos(0.5))
    def test_cos_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            cos()
    def test_cos_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            cos(q1, q2)
    def test_cos_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            cos(q)
    def test_cos_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            cos(q)
    def test_cos_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(float(cos(q)), math.cos(2/3))
    
    def test_exp1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(exp(q)), math.exp(4/5))
    def test_exp2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(exp(q)), math.exp(0.5))
    def test_exp_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            exp()
    def test_exp_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            exp(q1, q2)
    def test_exp_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            exp(q)
    def test_exp_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            exp(q)
    def test_exp_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(float(exp(q)), math.exp(2/3))
    
    def test_log1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(log(q)), math.log(4/5))
    def test_log2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(log(q)), math.log(0.5))
    def test_log_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            log()
    def test_log_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            log(q1, q2)
    def test_log_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            log(q)
    def test_log_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            log(q)
    def test_log_negative(self):
        q = Decimal(-1)
        with self.assertRaises(UndefinedError):
            log(q)
    def test_log_zero(self):
        q = Decimal(0)
        with self.assertRaises(UndefinedError):
            log(q)
    def test_log_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(float(log(q)), math.log(2/3))

if __name__ == '__main__':
    unittest.main()