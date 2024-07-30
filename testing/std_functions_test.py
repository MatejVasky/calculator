from functionality.std import Rational, ComplexRational, Decimal, ComplexDecimal, exp, ln, log, sign, sqrt, root, floor, ceil, sin, cos, tan, cot, sec, csc, arcsin, arccos, arctan, gcd, lcm
from arithmetic_expressions.functionality_database.exceptions import WrongNumberOfArgumentsError, UndefinedError
from arithmetic_expressions.functionality_database import Variable
import unittest
import math

class STDOperationsTest(unittest.TestCase):
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
        q = ComplexDecimal(1, 2)
        self.assertAlmostEqual(float(exp(q).re()), math.exp(1) * math.cos(2))
        self.assertAlmostEqual(float(exp(q).im()), math.exp(1) * math.sin(2))
    def test_exp_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertAlmostEqual(float(exp(q)), math.exp(2/3))
    
    def test_ln1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(ln(q)), math.log(4/5))
    def test_ln2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(ln(q)), math.log(0.5))
    def test_ln_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            ln()
    def test_ln_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            ln(q1, q2)
    def test_ln_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            ln(q)
    def test_ln_not_real(self):
        q = ComplexDecimal(1, math.sqrt(3))
        self.assertAlmostEqual(float(ln(q).re()), math.log(2))
        self.assertAlmostEqual(float(ln(q).im()), math.pi / 3)
    def test_ln_negative(self):
        q = Decimal(-1)
        self.assertAlmostEqual(float(ln(q).re()), 0)
        self.assertAlmostEqual(float(ln(q).im()), math.pi)
    def test_ln_zero(self):
        q = Decimal(0)
        with self.assertRaises(UndefinedError):
            ln(q)
    def test_ln_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertAlmostEqual(float(ln(q)), math.log(2/3))
    
    def test_log_single_parameter1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(log(q)), math.log(4/5))
    def test_log_single_parameter2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(log(q)), math.log(0.5))
    def test_log_two_parameters1(self):
        q1 = Rational(2, 3)
        q2 = ComplexRational(8, 27, 0, 1)
        self.assertAlmostEqual(float(log(q1, q2)), 3)
    def test_log_two_parameters2(self):
        q1 = Decimal(1.5)
        q2 = ComplexDecimal(27/8, 0)
        self.assertAlmostEqual(float(log(q1, q2)), 3)
    def test_log_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            log()
    def test_log_wrong_number_of_arguments2(self):
        q1 = Rational(3, 1)
        q2 = Rational(2, 1)
        q3 = Rational(5, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            log(q1, q2, q3)
    def test_log_single_parameter_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            log(q)
    def test_log_single_parameter_not_real(self):
        q = ComplexDecimal(1, math.sqrt(3))
        self.assertAlmostEqual(float(log(q).re()), math.log(2))
        self.assertAlmostEqual(float(log(q).im()), math.pi / 3)
    def test_log_single_parameter_negative(self):
        q = Decimal(-1)
        self.assertAlmostEqual(float(log(q).re()), 0)
        self.assertAlmostEqual(float(log(q).im()), math.pi)
    def test_log_single_parameter_zero(self):
        q = Decimal(0)
        with self.assertRaises(UndefinedError):
            log(q)
    def test_log_single_parameter_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(float(log(q)), math.log(2/3))
    def test_log_two_parameters_wrong_type1(self):
        q1 = 2
        q2 = Decimal(8)
        with self.assertRaises(UndefinedError):
            log(q1, q2)
    def test_log_two_parameters_wrong_type2(self):
        q1 = Decimal(2)
        q2 = 8
        with self.assertRaises(UndefinedError):
            log(q1, q2)
    def test_log_two_parameters_not_real1(self):
        q1 = ComplexDecimal(2, 3)
        q2 = Decimal(8)
        with self.assertRaises(UndefinedError):
            log(q1, q2)
    def test_log_two_parameters_not_real2(self):
        q1 = Decimal(2)
        q2 = ComplexDecimal(8, 3)
        with self.assertRaises(UndefinedError):
            log(q1, q2)
    def test_log_two_parameters_negative1(self):
        q1 = Decimal(-2)
        q2 = Decimal(8)
        with self.assertRaises(UndefinedError):
            log(q1, q2)
    def test_log_two_parameters_negative2(self):
        q1 = Decimal(2)
        q2 = Decimal(-8)
        with self.assertRaises(UndefinedError):
            log(q1, q2)
    def test_log_two_parameters_zero1(self):
        q1 = Decimal(0)
        q2 = Decimal(8)
        with self.assertRaises(UndefinedError):
            log(q1, q2)
    def test_log_two_parameters_zero2(self):
        q1 = Decimal(2)
        q2 = Decimal(0)
        with self.assertRaises(UndefinedError):
            log(q1, q2)
    def test_log_two_parameters_one1(self):
        q1 = Decimal(1)
        q2 = Decimal(8)
        with self.assertRaises(UndefinedError):
            log(q1, q2)
    def test_log_two_parameters_one2(self):
        q1 = Decimal(2)
        q2 = Decimal(1)
        self.assertAlmostEqual(float(log(q1, q2)), 0)
    def test_log_two_parameters_variable1(self):
        q1 = Variable('q', Decimal(2))
        q2 = Decimal(8)
        self.assertAlmostEqual(float(log(q1, q2)), 3)
    def test_log_two_parameters_variable2(self):
        q1 = Decimal(2)
        q2 = Variable('q', Decimal(8))
        self.assertAlmostEqual(float(log(q1, q2)), 3)
    
    def test_sign1(self):
        q = Rational(4, 5)
        self.assertEqual(sign(q), Rational(1, 1))
    def test_sign2(self):
        q = ComplexDecimal(-0.5, 0)
        self.assertEqual(sign(q), Rational(-1, 1))
    def test_sign3(self):
        q = ComplexRational(0, 1, 0, 1)
        self.assertEqual(sign(q), Rational(0, 1))
    def test_sign_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            sign()
    def test_sign_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            sign(q1, q2)
    def test_sign_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            sign(q)
    def test_sign_not_real(self):
        q = ComplexDecimal(1, 2)
        with self.assertRaises(UndefinedError):
            sign(q)
    def test_sign_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(sign(q), Rational(1, 1))

    def test_sqrt1(self):
        q = Rational(9, 4)
        self.assertEqual(sqrt(q), Rational(3, 2))
    def test_sqrt2(self):
        q = ComplexDecimal(0, 2)
        self.assertAlmostEqual(float(sqrt(q).re()), 1)
        self.assertAlmostEqual(float(sqrt(q).im()), 1)
    def test_sqrt_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            sqrt()
    def test_sqrt_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            sqrt(q1, q2)
    def test_sqrt_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            sqrt(q)
    def test_sqrt_negative(self):
        q = Decimal(-1)
        self.assertAlmostEqual(float(sqrt(q).re()), 0)
        self.assertAlmostEqual(float(sqrt(q).im()), 1)
    def test_sqrt_zero(self):
        q = Decimal(0)
        self.assertAlmostEqual(float(sqrt(q)), 0)
    def test_sqrt_variable(self):
        q = Variable('x', Rational(9, 4))
        self.assertEqual(sqrt(q), Rational(3, 2))

    def test_root1(self):
        q1 = ComplexRational(2, 3, 0, 1)
        q2 = Rational(9, 4)
        self.assertEqual(root(q1, q2), Rational(27, 8))
    def test_root2(self):
        q1 = Decimal(2)
        q2 = ComplexDecimal(0, 2)
        self.assertAlmostEqual(float(root(q1, q2).re()), 1)
        self.assertAlmostEqual(float(root(q1, q2).im()), 1)
    def test_root_wrong_number_of_arguments1(self):
        q = Rational(1, 5)
        with self.assertRaises(WrongNumberOfArgumentsError):
            root(q)
    def test_root_wrong_number_of_arguments2(self):
        q1 = Rational(3, 1)
        q2 = Rational(2, 1)
        q3 = Rational(5, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            root(q1, q2, q3)
    def test_root_two_parameters_wrong_type1(self):
        q1 = 2
        q2 = Decimal(8)
        with self.assertRaises(UndefinedError):
            root(q1, q2)
    def test_root_two_parameters_wrong_type2(self):
        q1 = Decimal(2)
        q2 = 8
        with self.assertRaises(UndefinedError):
            root(q1, q2)
    def test_root_two_parameters_zero1(self):
        q1 = Decimal(0)
        q2 = Decimal(8)
        with self.assertRaises(UndefinedError):
            root(q1, q2)
    def test_root_two_parameters_zero2(self):
        q1 = Decimal(2)
        q2 = Decimal(0)
        self.assertAlmostEqual(float(root(q1, q2)), 0)
    def test_root_two_parameters_variable1(self):
        q1 = Variable('q', Decimal(3))
        q2 = Decimal(8)
        self.assertAlmostEqual(float(root(q1, q2)), 2)
    def test_root_two_parameters_variable2(self):
        q1 = Decimal(3)
        q2 = Variable('q', Decimal(8))
        self.assertAlmostEqual(float(root(q1, q2)), 2)
    
    def test_floor1(self):
        q = Rational(4, 5)
        self.assertEqual(floor(q), Rational(0, 1))
    def test_floor2(self):
        q = ComplexDecimal(-0.5, 0)
        self.assertEqual(floor(q), Rational(-1, 1))
    def test_floor3(self):
        q = ComplexRational(3, 1, 0, 1)
        self.assertEqual(floor(q), Rational(3, 1))
    def test_floor_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            floor()
    def test_floor_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            floor(q1, q2)
    def test_floor_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            floor(q)
    def test_floor_not_real(self):
        q = ComplexDecimal(1, 2)
        with self.assertRaises(UndefinedError):
            floor(q)
    def test_floor_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(floor(q), Rational(0, 1))

    def test_ceil1(self):
        q = Rational(4, 5)
        self.assertEqual(ceil(q), Rational(1, 1))
    def test_ceil2(self):
        q = ComplexDecimal(-0.5, 0)
        self.assertEqual(ceil(q), Rational(0, 1))
    def test_ceil3(self):
        q = ComplexRational(3, 1, 0, 1)
        self.assertEqual(ceil(q), Rational(3, 1))
    def test_ceil_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            ceil()
    def test_ceil_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            ceil(q1, q2)
    def test_ceil_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            ceil(q)
    def test_ceil_not_real(self):
        q = ComplexDecimal(1, 2)
        with self.assertRaises(UndefinedError):
            ceil(q)
    def test_ceil_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertEqual(ceil(q), Rational(1, 1))

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
        self.assertAlmostEqual(float(sin(q)), math.sin(2/3))
    
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
        self.assertAlmostEqual(float(cos(q)), math.cos(2/3))
    
    def test_tan1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(tan(q)), math.tan(4/5))
    def test_tan2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(tan(q)), math.tan(0.5))
    def test_tan_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            tan()
    def test_tan_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            tan(q1, q2)
    def test_tan_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            tan(q)
    def test_tan_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            tan(q)
    def test_tan_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertAlmostEqual(float(tan(q)), math.tan(2/3))
    
    def test_cot1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(cot(q)), 1/math.tan(4/5))
    def test_cot2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(cot(q)), 1/math.tan(0.5))
    def test_cot_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            cot()
    def test_cot_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            cot(q1, q2)
    def test_cot_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            cot(q)
    def test_cot_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            cot(q)
    def test_cot_zero(self):
        q = Decimal(0)
        with self.assertRaises(UndefinedError):
            cot(q)
    def test_cot_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertAlmostEqual(float(cot(q)), 1/math.tan(2/3))
    
    def test_sec1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(sec(q)), 1/math.cos(4/5))
    def test_sec2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(sec(q)), 1/math.cos(0.5))
    def test_sec_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            sec()
    def test_sec_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            sec(q1, q2)
    def test_sec_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            sec(q)
    def test_sec_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            sec(q)
    def test_sec_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertAlmostEqual(float(sec(q)), 1/math.cos(2/3))
    
    def test_csc1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(csc(q)), 1/math.sin(4/5))
    def test_csc2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(csc(q)), 1/math.sin(0.5))
    def test_csc_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            csc()
    def test_csc_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            csc(q1, q2)
    def test_csc_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            csc(q)
    def test_csc_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            csc(q)
    def test_csc_zero(self):
        q = Decimal(0)
        with self.assertRaises(UndefinedError):
            csc(q)
    def test_csc_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertAlmostEqual(float(csc(q)), 1/math.sin(2/3))
    
    def test_arcsin1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(arcsin(q)), math.asin(4/5))
    def test_arcsin2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(arcsin(q)), math.asin(0.5))
    def test_arcsin_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            arcsin()
    def test_arcsin_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            arcsin(q1, q2)
    def test_arcsin_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            arcsin(q)
    def test_arcsin_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            arcsin(q)
    def test_arcsin_small(self):
        q = Decimal(-2)
        with self.assertRaises(UndefinedError):
            arcsin(q)
    def test_arcsin_negative_one(self):
        q = Rational(-1, 1)
        self.assertAlmostEqual(float(arcsin(q)), -math.pi/2)
    def test_arcsin_one(self):
        q = Rational(1, 1)
        self.assertAlmostEqual(float(arcsin(q)), math.pi/2)
    def test_arcsin_big(self):
        q = Decimal(2)
        with self.assertRaises(UndefinedError):
            arcsin(q)
    def test_arcsin_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertAlmostEqual(float(arcsin(q)), math.asin(2/3))
    
    def test_arccos1(self):
        q = Rational(4, 5)
        self.assertAlmostEqual(float(arccos(q)), math.acos(4/5))
    def test_arccos2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertAlmostEqual(float(arccos(q)), math.acos(0.5))
    def test_arccos_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            arccos()
    def test_arccos_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            arccos(q1, q2)
    def test_arccos_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            arccos(q)
    def test_arccos_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            arccos(q)
    def test_arccos_small(self):
        q = Decimal(-2)
        with self.assertRaises(UndefinedError):
            arccos(q)
    def test_arccos_negative_one(self):
        q = Rational(-1, 1)
        self.assertAlmostEqual(float(arccos(q)), math.pi)
    def test_arccos_one(self):
        q = Rational(1, 1)
        self.assertAlmostEqual(float(arccos(q)), 0)
    def test_arccos_big(self):
        q = Decimal(2)
        with self.assertRaises(UndefinedError):
            arccos(q)
    def test_arccos_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertAlmostEqual(float(arccos(q)), math.acos(2/3))
    
    def test_arctan1(self):
        q = Rational(6, 5)
        self.assertAlmostEqual(float(arctan(q)), math.atan(6/5))
    def test_arctan2(self):
        q = ComplexDecimal(-0.5, 0)
        self.assertAlmostEqual(float(arctan(q)), math.atan(-0.5))
    def test_arctan_wrong_number_of_arguments1(self):
        with self.assertRaises(WrongNumberOfArgumentsError):
            arctan()
    def test_arctan_wrong_number_of_arguments2(self):
        q1 = Rational(1, 1)
        q2 = Rational(2, 1)
        with self.assertRaises(WrongNumberOfArgumentsError):
            arctan(q1, q2)
    def test_arctan_wrong_type(self):
        q = 1
        with self.assertRaises(UndefinedError):
            arctan(q)
    def test_arctan_not_real(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(UndefinedError):
            arctan(q)
    def test_arctan_variable(self):
        q = Variable('x', Rational(2, 3))
        self.assertAlmostEqual(float(arctan(q)), math.atan(2/3))
    
    def test_gcd_two_numbers(self):
        m = Rational(4, 1)
        n = Rational(6, 1)
        self.assertEqual(gcd(m, n), Rational(2, 1))
    def test_gcd_coprime_numbers(self):
        m = Rational(5, 1)
        n = Rational(6, 1)
        self.assertEqual(gcd(m, n), Rational(1, 1))
    def test_gcd_equal_numbers(self):
        m = Rational(6, 1)
        n = Rational(6, 1)
        self.assertEqual(gcd(m, n), Rational(6, 1))
    def test_gcd_multiple(self):
        m = Rational(3, 1)
        n = Rational(6, 1)
        self.assertEqual(gcd(m, n), Rational(3, 1))
    def test_gcd_multiple2(self):
        m = Rational(6, 1)
        n = Rational(3, 1)
        self.assertEqual(gcd(m, n), Rational(3, 1))
    def test_gcd_zero(self):
        m = Rational(0, 1)
        n = Rational(6, 1)
        self.assertEqual(gcd(m, n), Rational(6, 1))
    def test_gcd_two_zeros(self):
        m = Rational(0, 1)
        n = Rational(0, 1)
        self.assertEqual(gcd(m, n), Rational(0, 1))
    def test_gcd_negative(self):
        m = Rational(-4, 1)
        n = Rational(6, 1)
        self.assertEqual(gcd(m, n), Rational(2, 1))
    def test_gcd_negative2(self):
        m = Rational(4, 1)
        n = Rational(-6, 1)
        self.assertEqual(gcd(m, n), Rational(2, 1))
    def test_gcd_negative3(self):
        m = Rational(-4, 1)
        n = Rational(-6, 1)
        self.assertEqual(gcd(m, n), Rational(2, 1))
    def test_gcd_wrong_type1(self):
        m = 4
        n = Rational(6, 1)
        with self.assertRaises(UndefinedError):
            gcd(m, n)
    def test_gcd_wrong_type2(self):
        m = Rational(4, 1)
        n = 6
        with self.assertRaises(UndefinedError):
            gcd(m, n)
    def test_gcd_not_real1(self):
        m = ComplexRational(4, 1, 2, 1)
        n = Rational(6, 1)
        with self.assertRaises(UndefinedError):
            gcd(m, n)
    def test_gcd_not_real2(self):
        m = Rational(4, 1)
        n = ComplexRational(6, 1, 3, 1)
        with self.assertRaises(UndefinedError):
            gcd(m, n)
    def test_gcd_not_int1(self):
        m = Rational(4, 3)
        n = Rational(6, 1)
        with self.assertRaises(UndefinedError):
            gcd(m, n)
    def test_gcd_not_int2(self):
        m = Rational(4, 1)
        n = Rational(6, 5)
        with self.assertRaises(UndefinedError):
            gcd(m, n)
    
    def test_lcm_two_numbers(self):
        m = Rational(4, 1)
        n = Rational(6, 1)
        self.assertEqual(lcm(m, n), Rational(12, 1))
    def test_lcm_coprime_numbers(self):
        m = Rational(5, 1)
        n = Rational(6, 1)
        self.assertEqual(lcm(m, n), Rational(30, 1))
    def test_lcm_equal_numbers(self):
        m = Rational(6, 1)
        n = Rational(6, 1)
        self.assertEqual(lcm(m, n), Rational(6, 1))
    def test_lcm_multiple(self):
        m = Rational(3, 1)
        n = Rational(6, 1)
        self.assertEqual(lcm(m, n), Rational(6, 1))
    def test_lcm_multiple2(self):
        m = Rational(6, 1)
        n = Rational(3, 1)
        self.assertEqual(lcm(m, n), Rational(6, 1))
    def test_lcm_zero(self):
        m = Rational(0, 1)
        n = Rational(6, 1)
        with self.assertRaises(UndefinedError):
            lcm(m, n)
    def test_lcm_zero2(self):
        m = Rational(6, 1)
        n = Rational(0, 1)
        with self.assertRaises(UndefinedError):
            lcm(m, n)
    def test_lcm_negative(self):
        m = Rational(-4, 1)
        n = Rational(6, 1)
        with self.assertRaises(UndefinedError):
            lcm(m, n)
    def test_lcm_negative2(self):
        m = Rational(4, 1)
        n = Rational(-6, 1)
        with self.assertRaises(UndefinedError):
            lcm(m, n)
    def test_lcm_wrong_type1(self):
        m = 4
        n = Rational(6, 1)
        with self.assertRaises(UndefinedError):
            lcm(m, n)
    def test_lcm_wrong_type2(self):
        m = Rational(4, 1)
        n = 6
        with self.assertRaises(UndefinedError):
            lcm(m, n)
    def test_lcm_not_real1(self):
        m = ComplexRational(4, 1, 2, 1)
        n = Rational(6, 1)
        with self.assertRaises(UndefinedError):
            lcm(m, n)
    def test_lcm_not_real2(self):
        m = Rational(4, 1)
        n = ComplexRational(6, 1, 3, 1)
        with self.assertRaises(UndefinedError):
            lcm(m, n)
    def test_lcm_not_int1(self):
        m = Rational(4, 3)
        n = Rational(6, 1)
        with self.assertRaises(UndefinedError):
            lcm(m, n)
    def test_lcm_not_int2(self):
        m = Rational(4, 1)
        n = Rational(6, 5)
        with self.assertRaises(UndefinedError):
            lcm(m, n)

if __name__ == '__main__':
    unittest.main()