from functionality.std import Rational, ComplexRational, Decimal, ComplexDecimal, add, subtract, multiply, divide, floordivide, modulo, add_parameter, evaluate_function, pos, neg
from arithmetic_expressions.functionality_database.exceptions import UndefinedError, FunctionOrOperationEvaluationException
from arithmetic_expressions.functionality_database import Variable, Parameters, Function
import unittest
from math import sqrt

class STDOperationsTest(unittest.TestCase):
    def test_add1(self):
        q1 = Rational(4, 5)
        q2 = ComplexRational(3, 5, 8, 5)
        self.assertEqual(add(q1, q2), ComplexRational(7, 5, 8, 5))
    def test_add2(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.25, 1)
        self.assertEqual(add(q1, q2), ComplexDecimal(0.75, 1))
    def test_add_error1(self):
        q1 = Decimal(0.5)
        q2 = Function('f', test_function)
        with self.assertRaises(UndefinedError):
            add(q1, q2)
    def test_add_error2(self):
        q1 = Function('f', test_function)
        q2 = Rational(5, 6)
        with self.assertRaises(UndefinedError):
            add(q1, q2)
    def test_add_variable1(self):
        q1 = Variable('x', Rational(2, 3))
        q2 = Rational(5, 6)
        self.assertEqual(add(q1, q2), Rational(3, 2))
    def test_add_variable2(self):
        q1 = Rational(2, 3)
        q2 = Variable('x', Rational(5, 6))
        self.assertEqual(add(q1, q2), Rational(3, 2))
    
    def test_subtract1(self):
        q1 = Rational(4, 5)
        q2 = ComplexRational(3, 5, 8, 5)
        self.assertEqual(subtract(q1, q2), ComplexRational(1, 5, -8, 5))
    def test_subtract2(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.25, 1)
        self.assertEqual(subtract(q1, q2), ComplexDecimal(0.25, -1))
    def test_subtract_error1(self):
        q1 = Decimal(0.5)
        q2 = Function('f', test_function)
        with self.assertRaises(UndefinedError):
            subtract(q1, q2)
    def test_subtract_error2(self):
        q1 = Function('f', test_function)
        q2 = Rational(5, 6)
        with self.assertRaises(UndefinedError):
            subtract(q1, q2)
    def test_subtract_variable1(self):
        q1 = Variable('x', Rational(2, 3))
        q2 = Rational(5, 6)
        self.assertEqual(subtract(q1, q2), Rational(-1, 6))
    def test_subtract_variable2(self):
        q1 = Rational(2, 3)
        q2 = Variable('x', Rational(5, 6))
        self.assertEqual(subtract(q1, q2), Rational(-1, 6))
    
    def test_multiply1(self):
        q1 = Rational(4, 5)
        q2 = ComplexRational(3, 5, 8, 5)
        self.assertEqual(multiply(q1, q2), ComplexRational(12, 25, 32, 25))
    def test_multiply2(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.25, 1)
        self.assertEqual(multiply(q1, q2), ComplexDecimal(0.125, 0.5))
    def test_multiply_error1(self):
        q1 = Decimal(0.5)
        q2 = Function('f', test_function)
        with self.assertRaises(UndefinedError):
            multiply(q1, q2)
    def test_multiply_error2(self):
        q1 = Function('f', test_function)
        q2 = Rational(5, 6)
        with self.assertRaises(UndefinedError):
            multiply(q1, q2)
    def test_multiply_variable1(self):
        q1 = Variable('x', Rational(2, 3))
        q2 = Rational(5, 6)
        self.assertEqual(multiply(q1, q2), Rational(5, 9))
    def test_multiply_variable2(self):
        q1 = Rational(2, 3)
        q2 = Variable('x', Rational(5, 6))
        self.assertEqual(multiply(q1, q2), Rational(5, 9))
    
    def test_divide1(self):
        q1 = ComplexRational(3, 5, 8, 5)
        q2 = Rational(4, 5)
        self.assertEqual(divide(q1, q2), ComplexRational(3, 4, 2, 1))
    def test_divide2(self):
        q1 = ComplexDecimal(0.25, 1)
        q2 = Decimal(0.5)
        self.assertEqual(divide(q1, q2), ComplexDecimal(0.5, 2))
    def test_divide_wrong_type1(self):
        q1 = Decimal(0.5)
        q2 = Function('f', test_function)
        with self.assertRaises(UndefinedError):
            divide(q1, q2)
    def test_divide_wrong_type2(self):
        q1 = Function('f', test_function)
        q2 = Rational(5, 6)
        with self.assertRaises(UndefinedError):
            divide(q1, q2)
    def test_divide_zero_division(self):
        q1 = Function('f', test_function)
        q2 = Rational(0, 1)
        with self.assertRaises(UndefinedError):
            divide(q1, q2)
    def test_divide_variable1(self):
        q1 = Variable('x', Rational(2, 3))
        q2 = Rational(5, 6)
        self.assertEqual(divide(q1, q2), Rational(4, 5))
    def test_divide_variable2(self):
        q1 = Rational(2, 3)
        q2 = Variable('x', Rational(5, 6))
        self.assertEqual(divide(q1, q2), Rational(4, 5))
    
    def test_floordivide1(self):
        q1 = ComplexRational(5, 1, 0, 1)
        q2 = Rational(4, 1)
        self.assertEqual(floordivide(q1, q2), Rational(1, 1))
    def test_floordivide2(self):
        q1 = Rational(-7, 1)
        q2 = Rational(3, 1)
        self.assertEqual(floordivide(q1, q2), Rational(-3, 1))
    def test_floordivide_wrong_type1(self):
        q1 = Rational(5, 1)
        q2 = Function('f', test_function)
        with self.assertRaises(UndefinedError):
            floordivide(q1, q2)
    def test_floordivide_wrong_type2(self):
        q1 = Function('f', test_function)
        q2 = Rational(5, 1)
        with self.assertRaises(UndefinedError):
            floordivide(q1, q2)
    def test_floordivide_not_int1(self):
        q1 = Rational(5, 3)
        q2 = Rational(3, 1)
        with self.assertRaises(UndefinedError):
            floordivide(q1, q2)
    def test_floordivide_not_int2(self):
        q1 = Rational(5, 1)
        q2 = Rational(5, 3)
        with self.assertRaises(UndefinedError):
            floordivide(q1, q2)
    def test_floordivide_zero_division(self):
        q1 = Function('f', test_function)
        q2 = Rational(0, 1)
        with self.assertRaises(UndefinedError):
            floordivide(q1, q2)
    def test_floordivide_variable1(self):
        q1 = Variable('x', Rational(6, 1))
        q2 = Rational(4, 1)
        self.assertEqual(floordivide(q1, q2), Rational(1, 1))
    def test_floordivide_variable2(self):
        q1 = Rational(6, 1)
        q2 = Variable('x', Rational(4, 1))
        self.assertEqual(floordivide(q1, q2), Rational(1, 1))
    
    def test_modulo1(self):
        q1 = ComplexRational(5, 1, 0, 1)
        q2 = Rational(4, 1)
        self.assertEqual(modulo(q1, q2), Rational(1, 1))
    def test_modulo2(self):
        q1 = Rational(-7, 1)
        q2 = Rational(3, 1)
        self.assertEqual(modulo(q1, q2), Rational(2, 1))
    def test_modulo_wrong_type1(self):
        q1 = Rational(5, 1)
        q2 = Function('f', test_function)
        with self.assertRaises(UndefinedError):
            modulo(q1, q2)
    def test_modulo_wrong_type2(self):
        q1 = Function('f', test_function)
        q2 = Rational(5, 1)
        with self.assertRaises(UndefinedError):
            modulo(q1, q2)
    def test_modulo_not_int1(self):
        q1 = Rational(5, 3)
        q2 = Rational(3, 1)
        with self.assertRaises(UndefinedError):
            modulo(q1, q2)
    def test_modulo_not_int2(self):
        q1 = Rational(5, 1)
        q2 = Rational(5, 3)
        with self.assertRaises(UndefinedError):
            modulo(q1, q2)
    def test_modulo_zero_division(self):
        q1 = Function('f', test_function)
        q2 = Rational(0, 1)
        with self.assertRaises(UndefinedError):
            modulo(q1, q2)
    def test_modulo_variable1(self):
        q1 = Variable('x', Rational(6, 1))
        q2 = Rational(4, 1)
        self.assertEqual(modulo(q1, q2), Rational(2, 1))
    def test_modulo_variable2(self):
        q1 = Rational(6, 1)
        q2 = Variable('x', Rational(4, 1))
        self.assertEqual(modulo(q1, q2), Rational(2, 1))

    def test_add_parameter1(self):
        params = Parameters()
        q = Rational(4, 1)
        self.assertListEqual(list(add_parameter(params, q)), [Rational(4, 1)])
    def test_add_parameter2(self):
        params = Parameters(Rational(1, 3), Rational(-3, 4))
        q = Rational(4, 1)
        self.assertListEqual(list(add_parameter(params, q)), [Rational(1, 3), Rational(-3, 4), Rational(4, 1)])
    def test_add_parameter3(self):
        q1 = Rational(1, 3)
        q2 = Rational(4, 1)
        self.assertListEqual(list(add_parameter(q1, q2)), [Rational(1, 3), Rational(4, 1)])
    def test_add_parameter_wrong_type(self):
        q = Rational(4, 1)
        params = Parameters(Rational(1, 3), Rational(-3, 4))
        with self.assertRaises(UndefinedError):
            add_parameter(q, params)
    def test_add_parameter_variable1(self):
        x = Variable('x', Rational(6, 1))
        q1 = x
        q2 = Rational(4, 1)
        self.assertListEqual(list(add_parameter(q1, q2)), [x, Rational(4, 1)])
    def test_add_parameter_variable2(self):
        x = Variable('x', Rational(4, 1))
        q1 = Rational(6, 1)
        q2 = x
        self.assertListEqual(list(add_parameter(q1, q2)), [Rational(6, 1), x])
    
    def test_evaluate_function1(self):
        f = Function('f', test_function)
        q = Rational(4, 1)
        self.assertEqual(evaluate_function(f, q), Rational(4, 1))
    def test_evaluate_function2(self):
        f = Function('f', test_function)
        params = Parameters(Rational(1, 3), Rational(-3, 4))
        self.assertEqual(evaluate_function(f, params), Rational(1, 3))
    def test_evaluate_function_wrong_type(self):
        q = Rational(4, 1)
        params = Parameters(Rational(1, 3), Rational(-3, 4))
        with self.assertRaises(UndefinedError):
            evaluate_function(q, params)
    def test_evaluate_function_variable1(self):
        f = Variable('f', Function('f', test_function))
        q = Rational(4, 1)
        self.assertEqual(evaluate_function(f, q), Rational(4, 1))
    def test_evaluate_function_variable2(self):
        f = Variable('f', Function('f', test_function))
        x = Variable('x', Rational(4, 1))
        self.assertEqual(evaluate_function(f, x), x)
    def test_evaluate_function_error1(self):
        f = Function('f', test_function)
        params = Parameters()
        with self.assertRaises(UndefinedError):
            evaluate_function(f, params)
    def test_evaluate_function_error2(self):
        f = Function('f', test_function)
        g = Function('g', test_function)
        with self.assertRaises(FunctionOrOperationEvaluationException):
            evaluate_function(f, g)
    
    def test_pos1(self):
        q = Rational(4, 5)
        self.assertEqual(pos(q), Rational(4, 5))
    def test_pos2(self):
        q = ComplexDecimal(0.5, 1)
        self.assertEqual(pos(q), ComplexDecimal(0.5, 1))
    def test_pos_error(self):
        q = Function('f', test_function)
        with self.assertRaises(UndefinedError):
            pos(q)
    def test_pos_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(pos(q), Rational(2, 3))
    
    def test_neg1(self):
        q = Rational(4, 5)
        self.assertEqual(neg(q), Rational(-4, 5))
    def test_neg2(self):
        q = ComplexDecimal(0.5, 1)
        self.assertEqual(neg(q), ComplexDecimal(-0.5, -1))
    def test_neg_error(self):
        q = Function('f', test_function)
        with self.assertRaises(UndefinedError):
            neg(q)
    def test_neg_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(neg(q), Rational(-2, 3))
    
def test_function(*args):
    if len(args) == 0:
        raise UndefinedError()
    if isinstance(args[0], Function):
        raise TypeError()
    return args[0]

if __name__ == '__main__':
    unittest.main()