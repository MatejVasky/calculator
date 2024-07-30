from functionality.std import Rational, ComplexRational, Decimal, ComplexDecimal
import unittest
from math import sqrt, pi, log, exp, cos, sin

class STDNumbersTest(unittest.TestCase):
    def test_rational_init_coprime(self):
        q = Rational(4, 5) # 4/5
        self.assertEqual(q.a, 4)
        self.assertEqual(q.b, 5)
    def test_rational_init_not_coprime(self):
        q = Rational(4, 6) # 2/3
        self.assertEqual(q.a, 2)
        self.assertEqual(q.b, 3)
    def test_rational_init_zero(self):
        q = Rational(0, 4) # 0
        self.assertEqual(q.a, 0)
        self.assertEqual(q.b, 1)
    def test_rational_init_negative_numerator(self):
        q = Rational(-4, 5) # -4/5
        self.assertEqual(q.a, -4)
        self.assertEqual(q.b, 5)
    def test_rational_init_negative_denominator(self):
        q = Rational(4, -5) # -4/5
        self.assertEqual(q.a, -4)
        self.assertEqual(q.b, 5)
    def test_rational_init_negative_numerator_and_denominator(self):
        q = Rational(-4, -5) # 4/5
        self.assertEqual(q.a, 4)
        self.assertEqual(q.b, 5)
    def test_rational_init_zero_denominator(self):
        with self.assertRaises(ValueError):
            Rational(-4, 0) # undef
    def test_rational_init_not_int1(self):
        with self.assertRaises(TypeError):
            Rational('-4', 1) # undef
    def test_rational_init_not_int2(self):
        with self.assertRaises(TypeError):
            Rational(-4, '1') # undef
    
    def test_rational_is_real(self):
        q = Rational(2, 3) # 2/3
        self.assertTrue(q.is_real())
    def test_rational_is_real2(self):
        q = Rational(-2, 3) # -2/3
        self.assertTrue(q.is_real())
    
    def test_rational_is_rational(self):
        q = Rational(2, 3) # 2/3
        self.assertTrue(q.is_rational())
    def test_rational_is_rational2(self):
        q = Rational(-2, 3) # -2/3
        self.assertTrue(q.is_rational())
    
    def test_rational_is_complex_rational(self):
        q = Rational(2, 3) # 2/3
        self.assertTrue(q.is_complex_rational())
    def test_rational_is_complex_rational2(self):
        q = Rational(-2, 3) # -2/3
        self.assertTrue(q.is_complex_rational())
    
    def test_rational_is_int_true(self):
        q = Rational(2, 1) # 2
        self.assertTrue(q.is_int())
    def test_rational_is_int_true2(self):
        q = Rational(-4, 2) # -2
        self.assertTrue(q.is_int())
    def test_rational_is_int_false(self):
        q = Rational(1, 2) # 1/2
        self.assertFalse(q.is_int())
    def test_rational_is_int_false2(self):
        q = Rational(-2, 4) # -1/2
        self.assertFalse(q.is_int())
    
    def test_rational_is_gaussian_int_true(self):
        q = Rational(2, 1) # 2
        self.assertTrue(q.is_gaussian_int())
    def test_rational_is_gaussian_int_true2(self):
        q = Rational(-4, 2) # -2
        self.assertTrue(q.is_gaussian_int())
    def test_rational_is_gaussian_int_false(self):
        q = Rational(1, 2) # 2
        self.assertFalse(q.is_gaussian_int())
    def test_rational_is_gaussian_int_false2(self):
        q = Rational(-2, 4) # -1/2
        self.assertFalse(q.is_gaussian_int())
    
    def test_rational_is_positive_true(self):
        q = Rational(2, 1) # 2
        self.assertTrue(q.is_positive())
    def test_rational_is_positive_true2(self):
        q = Rational(1, 2) # 1/2
        self.assertTrue(q.is_positive())
    def test_rational_is_positive_false(self):
        q = Rational(-4, 2) # -2
        self.assertFalse(q.is_positive())
    def test_rational_is_positive_false2(self):
        q = Rational(-2, 4) # -1/2
        self.assertFalse(q.is_positive())
    def test_rational_is_positive_false3(self):
        q = Rational(0, 1) # 0
        self.assertFalse(q.is_positive())
    
    def test_rational_is_negative_true(self):
        q = Rational(-4, 2) # -2
        self.assertTrue(q.is_negative())
    def test_rational_is_negative_true2(self):
        q = Rational(-2, 4) # -1/2
        self.assertTrue(q.is_negative())
    def test_rational_is_negative_false(self):
        q = Rational(2, 1) # 2
        self.assertFalse(q.is_negative())
    def test_rational_is_negative_false2(self):
        q = Rational(1, 2) # 1/2
        self.assertFalse(q.is_negative())
    def test_rational_is_negative_false3(self):
        q = Rational(0, 1) # 0
        self.assertFalse(q.is_negative())
    
    def test_rational_is_zero_true(self):
        q = Rational(0, 1) # 0
        self.assertTrue(q.is_zero())
    def test_rational_is_zero_false(self):
        q = Rational(-2, 1) # -2
        self.assertFalse(q.is_zero())
    def test_rational_is_zero_false2(self):
        q = Rational(1, 2) # 1/2
        self.assertFalse(q.is_zero())
    
    def test_complex_rational_init_coprime(self):
        q = ComplexRational(4, 5, 3, 2) # 4/5 + (3/2)i
        self.assertEqual(q.a, 4)
        self.assertEqual(q.b, 5)
        self.assertEqual(q.c, 3)
        self.assertEqual(q.d, 2)
    def test_complex_rational_init_not_coprime(self):
        q = ComplexRational(4, 6, 12, 18) # 2/3 + (2/3)i
        self.assertEqual(q.a, 2)
        self.assertEqual(q.b, 3)
        self.assertEqual(q.c, 2)
        self.assertEqual(q.d, 3)
    def test_complex_rational_init_zero(self):
        q = ComplexRational(0, 1, 0, 1) # 0
        self.assertEqual(q.a, 0)
        self.assertEqual(q.b, 1)
        self.assertEqual(q.c, 0)
        self.assertEqual(q.d, 1)
    def test_complex_rational_init_negative_numerator(self):
        q = ComplexRational(-4, 5, 3, 2) # -4/5 + (3/2)i
        self.assertEqual(q.a, -4)
        self.assertEqual(q.b, 5)
        self.assertEqual(q.c, 3)
        self.assertEqual(q.d, 2)
    def test_complex_rational_init_negative_numerator2(self):
        q = ComplexRational(4, 5, -3, 2) # 4/5 - (3/2)i
        self.assertEqual(q.a, 4)
        self.assertEqual(q.b, 5)
        self.assertEqual(q.c, -3)
        self.assertEqual(q.d, 2)
    def test_complex_rational_init_negative_denominator(self):
        q = ComplexRational(4, -5, 3, 2) # -4/5 + (3/2)i
        self.assertEqual(q.a, -4)
        self.assertEqual(q.b, 5)
        self.assertEqual(q.c, 3)
        self.assertEqual(q.d, 2)
    def test_complex_rational_init_negative_denominator2(self):
        q = ComplexRational(4, 5, 3, -2) # 4/5 - (3/2)i
        self.assertEqual(q.a, 4)
        self.assertEqual(q.b, 5)
        self.assertEqual(q.c, -3)
        self.assertEqual(q.d, 2)
    def test_complex_rational_init_negative_numerator_and_denominator(self):
        q = ComplexRational(-4, -5, -3, -2) # 4/5 + (3/2)i
        self.assertEqual(q.a, 4)
        self.assertEqual(q.b, 5)
        self.assertEqual(q.c, 3)
        self.assertEqual(q.d, 2)
    def test_complex_rational_init_zero_denominator(self):
        with self.assertRaises(ValueError):
            ComplexRational(-4, 0, 0, 1) # undef
    def test_complex_rational_init_zero_denominator2(self):
        with self.assertRaises(ValueError):
            ComplexRational(-4, -1, 3, 0) # undef
    def test_complex_rational_init_not_int1(self):
        with self.assertRaises(TypeError):
            ComplexRational('-4', 1, 3, 2) # undef
    def test_complex_rational_init_not_int2(self):
        with self.assertRaises(TypeError):
            ComplexRational(-4, '1', 3, 2) # undef
    def test_complex_rational_init_not_int3(self):
        with self.assertRaises(TypeError):
            ComplexRational(-4, 1, '3', 2) # undef
    def test_complex_rational_init_not_int4(self):
        with self.assertRaises(TypeError):
            ComplexRational(-4, 1, 3, '2') # undef
    
    def test_complex_rational_is_real_true(self):
        q = ComplexRational(2, 3, 0, 1) # 2/3
        self.assertTrue(q.is_real())
    def test_complex_rational_is_real_true2(self):
        q = ComplexRational(0, 1, 0, 1) # 0
        self.assertTrue(q.is_real())
    def test_complex_rational_is_real_false(self):
        q = ComplexRational(0, 1, 5, 1) # 5i
        self.assertFalse(q.is_real())
    def test_complex_rational_is_real_false2(self):
        q = ComplexRational(2, 3, 8, -2) # 2/3 - 4i
        self.assertFalse(q.is_real())
    
    def test_complex_rational_is_rational_true(self):
        q = ComplexRational(2, 3, 0, 1) # 2/3
        self.assertTrue(q.is_rational())
    def test_complex_rational_is_rational_true2(self):
        q = ComplexRational(-2, 3, 0, 1) # -2/3
        self.assertTrue(q.is_rational())
    def test_complex_rational_is_rational_false(self):
        q = ComplexRational(0, 1, 5, 1) # 5i
        self.assertFalse(q.is_rational())
    def test_complex_rational_is_rational_false2(self):
        q = ComplexRational(-2, 3, 10, 2) # -2/3 + 5i
        self.assertFalse(q.is_rational())
    
    def test_complex_rational_is_complex_rational(self):
        q = ComplexRational(2, 3, 0, 1) # 2/3
        self.assertTrue(q.is_complex_rational())
    def test_complex_rational_is_complex_rational2(self):
        q = ComplexRational(-2, 3, 5, 1) # -2/3 + 5i
        self.assertTrue(q.is_complex_rational())

    def test_complex_rational_is_int_true(self):
        q = ComplexRational(2, 1, 0, 1) # 2
        self.assertTrue(q.is_int())
    def test_complex_rational_is_int_true2(self):
        q = ComplexRational(-4, 2, 0, 4) # -2
        self.assertTrue(q.is_int())
    def test_complex_rational_is_int_false(self):
        q = ComplexRational(1, 2, 0, 1) # 1/2
        self.assertFalse(q.is_int())
    def test_complex_rational_is_int_false2(self):
        q = ComplexRational(-2, 2, 4, 1) # -1 + 4i
        self.assertFalse(q.is_int())
    
    def test_complex_rational_is_gaussian_int_true(self):
        q = ComplexRational(2, 1, 0, 1) # 2
        self.assertTrue(q.is_gaussian_int())
    def test_complex_rational_is_gaussian_int_true2(self):
        q = ComplexRational(-2, 2, 4, 1) # -1 + 4i
        self.assertTrue(q.is_gaussian_int())
    def test_complex_rational_is_gaussian_int_false(self):
        q = ComplexRational(1, 2, 0, 1) # 1/2
        self.assertFalse(q.is_gaussian_int())
    def test_complex_rational_is_gaussian_int_false2(self):
        q = ComplexRational(-2, 2, 1, -2) # -1 - (1/2)i
        self.assertFalse(q.is_gaussian_int())
    
    def test_complex_rational_is_positive_true(self):
        q = ComplexRational(2, 1, 0, 1) # 2
        self.assertTrue(q.is_positive())
    def test_complex_rational_is_positive_true2(self):
        q = ComplexRational(1, 2, 0, 1) # 1/2
        self.assertTrue(q.is_positive())
    def test_complex_rational_is_positive_false(self):
        q = ComplexRational(-4, 2, 0, 2) # -2
        self.assertFalse(q.is_positive())
    def test_complex_rational_is_positive_false2(self):
        q = ComplexRational(2, 4, 1, 1) # 1/2 + i
        self.assertFalse(q.is_positive())
    def test_complex_rational_is_positive_false3(self):
        q = ComplexRational(0, 1, 0, 1) # 0
        self.assertFalse(q.is_positive())
    
    def test_complex_rational_is_negative_true(self):
        q = ComplexRational(-4, 2, 0, 1) # -2
        self.assertTrue(q.is_negative())
    def test_complex_rational_is_negative_true2(self):
        q = ComplexRational(-2, 4, 0, 1) # -1/2
        self.assertTrue(q.is_negative())
    def test_complex_rational_is_negative_false(self):
        q = ComplexRational(2, 1, 0, 1) # 2
        self.assertFalse(q.is_negative())
    def test_complex_rational_is_negative_false2(self):
        q = ComplexRational(1, -2, -1, 1) # -1/2 - i
        self.assertFalse(q.is_negative())
    def test_complex_rational_is_negative_false3(self):
        q = ComplexRational(0, 1, 0, 1) # 0
        self.assertFalse(q.is_negative())
    
    def test_complex_rational_is_zero_true(self):
        q = ComplexRational(0, 1, 0, 2) # 0
        self.assertTrue(q.is_zero())
    def test_complex_rational_is_zero_false(self):
        q = ComplexRational(-2, 1, 0, 1) # -2
        self.assertFalse(q.is_zero())
    def test_complex_rational_is_zero_false2(self):
        q = ComplexRational(0, 1, 1, 2) # (1/2)i
        self.assertFalse(q.is_zero())
    
    def test_decimal_init_int(self):
        q = Decimal(4)
        self.assertEqual(q.val, 4)
    def test_decimal_init_float(self):
        q = Decimal(0.5)
        self.assertEqual(q.val, 0.5)
    def test_decimal_init_wrong_type(self):
        with self.assertRaises(TypeError):
            Decimal('-4')
    
    def test_decimal_is_real(self):
        q = Decimal(0.5)
        self.assertTrue(q.is_real())
    def test_decimal_is_real2(self):
        q = Decimal(-2.3)
        self.assertTrue(q.is_real())
    
    def test_decimal_is_rational(self):
        q = Decimal(2.3) # 2.3
        self.assertFalse(q.is_rational())
    def test_decimal_is_rational2(self):
        q = Decimal(-2.3) # -2/3
        self.assertFalse(q.is_rational())
    
    def test_decimal_is_complex_rational(self):
        q = Decimal(2.3)
        self.assertFalse(q.is_complex_rational())
    def test_decimal_is_complex_rational2(self):
        q = Decimal(-2.3)
        self.assertFalse(q.is_complex_rational())
    
    def test_decimal_is_int(self):
        q = Decimal(2)
        self.assertFalse(q.is_int())
    def test_decimal_is_int2(self):
        q = Decimal(-4.2)
        self.assertFalse(q.is_int())
    
    def test_decimal_is_gaussian_int(self):
        q = Decimal(2)
        self.assertFalse(q.is_gaussian_int())
    def test_decimal_is_gaussian_int2(self):
        q = Decimal(-4.2)
        self.assertFalse(q.is_gaussian_int())
    
    def test_decimal_is_positive_true(self):
        q = Decimal(2)
        self.assertTrue(q.is_positive())
    def test_decimal_is_positive_true2(self):
        q = Decimal(0.5)
        self.assertTrue(q.is_positive())
    def test_decimal_is_positive_false(self):
        q = Decimal(-2)
        self.assertFalse(q.is_positive())
    def test_decimal_is_positive_false2(self):
        q = Decimal(-0.5)
        self.assertFalse(q.is_positive())
    def test_decimal_is_positive_false3(self):
        q = Decimal(0)
        self.assertFalse(q.is_positive())
    
    def test_decimal_is_negative_true(self):
        q = Decimal(-2)
        self.assertTrue(q.is_negative())
    def test_decimal_is_negative_true2(self):
        q = Decimal(-0.5)
        self.assertTrue(q.is_negative())
    def test_decimal_is_negative_false(self):
        q = Decimal(2)
        self.assertFalse(q.is_negative())
    def test_decimal_is_negative_false2(self):
        q = Decimal(0.5)
        self.assertFalse(q.is_negative())
    def test_decimal_is_negative_false3(self):
        q = Decimal(0)
        self.assertFalse(q.is_negative())
    
    def test_decimal_is_zero_true(self):
        q = Decimal(0)
        self.assertTrue(q.is_zero())
    def test_decimal_is_zero_false(self):
        q = Decimal(-2)
        self.assertFalse(q.is_zero())
    def test_decimal_is_zero_false2(self):
        q = Decimal(0.5)
        self.assertFalse(q.is_zero())
    
    def test_complex_decimal_init_int_int(self):
        q = ComplexDecimal(4, 5)
        self.assertEqual(q.a, 4)
        self.assertEqual(q.b, 5)
    def test_complex_decimal_init_int_float(self):
        q = ComplexDecimal(4, 6.5)
        self.assertEqual(q.a, 4)
        self.assertEqual(q.b, 6.5)
    def test_complex_decimal_init_float_int(self):
        q = ComplexDecimal(4.3, 5)
        self.assertEqual(q.a, 4.3)
        self.assertEqual(q.b, 5)
    def test_complex_decimal_init_float_float(self):
        q = ComplexDecimal(4.3, 6.5)
        self.assertEqual(q.a, 4.3)
        self.assertEqual(q.b, 6.5)
    def test_complex_decimal_init_zero(self):
        q = ComplexDecimal(0, 0)
        self.assertEqual(q.a, 0)
        self.assertEqual(q.b, 0)
    def test_complex_decimal_init_wrong_type1(self):
        with self.assertRaises(TypeError):
            ComplexDecimal('4.3', 6.5)
    def test_complex_decimal_init_wrong_type2(self):
        with self.assertRaises(TypeError):
            ComplexDecimal(4.3, '6.5')
    
    def test_complex_decimal_is_real_true(self):
        q = ComplexDecimal(2, 0)
        self.assertTrue(q.is_real())
    def test_complex_decimal_is_real_true2(self):
        q = ComplexDecimal(0, 0.0)
        self.assertTrue(q.is_real())
    def test_complex_decimal_is_real_false(self):
        q = ComplexDecimal(0, 5)
        self.assertFalse(q.is_real())
    def test_complex_decimal_is_real_false2(self):
        q = ComplexDecimal(2.3, 3.2)
        self.assertFalse(q.is_real())
    
    def test_complex_decimal_is_rational_false(self):
        q = ComplexDecimal(0.1, 5)
        self.assertFalse(q.is_rational())
    def test_complex_decimal_is_rational_false2(self):
        q = ComplexDecimal(-2, 0)
        self.assertFalse(q.is_rational())
    
    def test_complex_decimal_is_complex_rational(self):
        q = ComplexDecimal(2, 3)
        self.assertFalse(q.is_complex_rational())
    def test_complex_decimal_is_complex_rational2(self):
        q = ComplexDecimal(-2.3, 5.1)
        self.assertFalse(q.is_complex_rational())

    def test_complex_decimal_is_int(self):
        q = ComplexDecimal(1.2, 0.1)
        self.assertFalse(q.is_int())
    def test_complex_decimal_is_int2(self):
        q = ComplexDecimal(-2, 1)
        self.assertFalse(q.is_int())
    
    def test_complex_decimal_is_gaussian_int(self):
        q = ComplexDecimal(1.2, 0.1)
        self.assertFalse(q.is_gaussian_int())
    def test_complex_decimal_is_gaussian_int2(self):
        q = ComplexDecimal(-2, 1)
        self.assertFalse(q.is_gaussian_int())
    
    def test_complex_decimal_is_positive_true(self):
        q = ComplexDecimal(2, 0)
        self.assertTrue(q.is_positive())
    def test_complex_decimal_is_positive_true2(self):
        q = ComplexDecimal(1.2, 0.0)
        self.assertTrue(q.is_positive())
    def test_complex_decimal_is_positive_false(self):
        q = ComplexDecimal(-4, 0)
        self.assertFalse(q.is_positive())
    def test_complex_decimal_is_positive_false2(self):
        q = ComplexDecimal(2.4, 1.3)
        self.assertFalse(q.is_positive())
    def test_complex_decimal_is_positive_false3(self):
        q = ComplexDecimal(0, 0)
        self.assertFalse(q.is_positive())
    
    def test_complex_decimal_is_negative_true(self):
        q = ComplexDecimal(-2, 0)
        self.assertTrue(q.is_negative())
    def test_complex_decimal_is_negative_true2(self):
        q = ComplexDecimal(-4.2, 0.0)
        self.assertTrue(q.is_negative())
    def test_complex_decimal_is_negative_false(self):
        q = ComplexDecimal(2, 0)
        self.assertFalse(q.is_negative())
    def test_complex_decimal_is_negative_false2(self):
        q = ComplexDecimal(-1.2, 1.2)
        self.assertFalse(q.is_negative())
    def test_complex_decimal_is_negative_false3(self):
        q = ComplexDecimal(0, 0)
        self.assertFalse(q.is_negative())
    
    def test_complex_decimal_is_zero_true(self):
        q = ComplexDecimal(0, 0) # 0
        self.assertTrue(q.is_zero())
    def test_complex_decimal_is_zero_false(self):
        q = ComplexDecimal(-2, 0)
        self.assertFalse(q.is_zero())
    def test_complex_decimal_is_zero_false2(self):
        q = ComplexDecimal(0, 3.1)
        self.assertFalse(q.is_zero())
    
    def test_eq_rational_rational_true(self):
        q1 = Rational(2, 5)
        q2 = Rational(-4, -10)
        self.assertTrue(q1 == q2)
    def test_eq_rational_rational_false1(self):
        q1 = Rational(2, 5)
        q2 = Rational(2, 3)
        self.assertFalse(q1 == q2)
    def test_eq_rational_rational_false2(self):
        q1 = Rational(2, 5)
        q2 = Rational(3, 5)
        self.assertFalse(q1 == q2)
    def test_eq_rational_complex_rational_true(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(-4, -10, 0, 1)
        self.assertTrue(q1 == q2)
    def test_eq_rational_complex_rational_false1(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(2, 3, 0, 1)
        self.assertFalse(q1 == q2)
    def test_eq_rational_complex_rational_false2(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(3, 5, 0, 1)
        self.assertFalse(q1 == q2)
    def test_eq_rational_complex_rational_false3(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(2, 5, -3, 2)
        self.assertFalse(q1 == q2)
    def test_eq_rational_decimal_true(self):
        q1 = Rational(1, 2)
        q2 = Decimal(0.5)
        self.assertTrue(q1 == q2)
    def test_eq_rational_decimal_false(self):
        q1 = Rational(1, 2)
        q2 = Decimal(0.3)
        self.assertFalse(q1 == q2)
    def test_eq_rational_complex_decimal_true(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.5, 0)
        self.assertTrue(q1 == q2)
    def test_eq_rational_complex_decimal_false1(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.3, 0)
        self.assertFalse(q1 == q2)
    def test_eq_rational_complex_decimal_false2(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.5, 1)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_rational_true(self):
        q1 = ComplexRational(2, 5, 0, 1)
        q2 = Rational(-4, -10)
        self.assertTrue(q1 == q2)
    def test_eq_complex_rational_rational_false1(self):
        q1 = ComplexRational(2, 5, 0, 1)
        q2 = Rational(2, 3)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_rational_false2(self):
        q1 = ComplexRational(2, 5, 0, 1)
        q2 = Rational(3, 5)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_rational_false3(self):
        q1 = ComplexRational(2, 5, -1, 1)
        q2 = Rational(2, 5)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_complex_rational_true(self):
        q1 = ComplexRational(2, 5, -1, 1)
        q2 = ComplexRational(-4, -10, 1, -1)
        self.assertTrue(q1 == q2)
    def test_eq_complex_rational_complex_rational_false1(self):
        q1 = ComplexRational(2, 5, -1, 1)
        q2 = ComplexRational(3, 5, -1, 1)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_complex_rational_false2(self):
        q1 = ComplexRational(2, 5, -1, 1)
        q2 = ComplexRational(2, 7, -1, 1)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_complex_rational_false3(self):
        q1 = ComplexRational(2, 5, -1, 1)
        q2 = ComplexRational(2, 5, 1, 1)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_complex_rational_false4(self):
        q1 = ComplexRational(2, 5, -1, 1)
        q2 = ComplexRational(2, 5, -1, 2)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_decimal_true(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = Decimal(0.5)
        self.assertTrue(q1 == q2)
    def test_eq_complex_rational_decimal_false1(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = Decimal(0.3)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_decimal_false2(self):
        q1 = ComplexRational(1, 2, 1, 1)
        q2 = Decimal(0.5)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_complex_decimal_true(self):
        q1 = ComplexRational(1, 2, 1, 4)
        q2 = ComplexDecimal(0.5, 0.25)
        self.assertTrue(q1 == q2)
    def test_eq_complex_rational_complex_decimal_false1(self):
        q1 = ComplexRational(1, 2, 1, 4)
        q2 = ComplexDecimal(0.3, 0.25)
        self.assertFalse(q1 == q2)
    def test_eq_complex_rational_complex_decimal_false2(self):
        q1 = ComplexRational(1, 2, 1, 4)
        q2 = ComplexDecimal(0.5, 0.3)
        self.assertFalse(q1 == q2)
    def test_eq_decimal_rational_true(self):
        q1 = Decimal(0.5)
        q2 = Rational(1, 2)
        self.assertTrue(q1 == q2)
    def test_eq_decimal_rational_false(self):
        q1 = Decimal(0.3)
        q2 = Rational(1, 2)
        self.assertFalse(q1 == q2)
    def test_eq_decimal_complex_rational_true(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(1, 2, 0, 1)
        self.assertTrue(q1 == q2)
    def test_eq_decimal_complex_rational_false1(self):
        q1 = Decimal(0.3)
        q2 = ComplexRational(1, 2, 0, 1)
        self.assertFalse(q1 == q2)
    def test_eq_decimal_complex_rational_false2(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(1, 2, 1, 2)
        self.assertFalse(q1 == q2)
    def test_eq_decimal_decimal_true(self):
        q1 = Decimal(0.5)
        q2 = Decimal(0.5)
        self.assertTrue(q1 == q2)
    def test_eq_decimal_decimal_false(self):
        q1 = Decimal(0.5)
        q2 = Decimal(0.3)
        self.assertFalse(q1 == q2)
    def test_eq_decimal_complex_decimal_true(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.5, 0)
        self.assertTrue(q1 == q2)
    def test_eq_decimal_complex_decimal_false1(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.3, 0)
        self.assertFalse(q1 == q2)
    def test_eq_decimal_complex_decimal_false2(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.5, 1)
        self.assertFalse(q1 == q2)
    def test_eq_complex_decimal_rational_true(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Rational(1, 2)
        self.assertTrue(q1 == q2)
    def test_eq_complex_decimal_rational_false1(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Rational(1, 3)
        self.assertFalse(q1 == q2)
    def test_eq_complex_decimal_rational_false2(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = Rational(1, 2)
        self.assertFalse(q1 == q2)
    def test_eq_complex_decimal_complex_rational_true(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = ComplexRational(-2, -4, 1, 1)
        self.assertTrue(q1 == q2)
    def test_eq_complex_decimal_complex_rational_false1(self):
        q1 = ComplexDecimal(0.3, 1)
        q2 = ComplexRational(-2, -4, 1, 1)
        self.assertFalse(q1 == q2)
    def test_eq_complex_decimal_complex_rational_false2(self):
        q1 = ComplexDecimal(0.5, 0.75)
        q2 = ComplexRational(-2, -4, 1, 1)
        self.assertFalse(q1 == q2)
    def test_eq_complex_decimal_decimal_true(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Decimal(0.5)
        self.assertTrue(q1 == q2)
    def test_eq_complex_decimal_decimal_false1(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Decimal(0.3)
        self.assertFalse(q1 == q2)
    def test_eq_complex_decimal_decimal_false2(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = Decimal(0.5)
        self.assertFalse(q1 == q2)
    def test_eq_complex_decimal_complex_decimal_true(self):
        q1 = ComplexDecimal(0.5, 0.25)
        q2 = ComplexDecimal(0.5, 0.25)
        self.assertTrue(q1 == q2)
    def test_eq_complex_decimal_complex_decimal_false1(self):
        q1 = ComplexDecimal(0.5, 0.25)
        q2 = ComplexDecimal(0.3, 0.25)
        self.assertFalse(q1 == q2)
    def test_eq_complex_decimal_complex_decimal_false2(self):
        q1 = ComplexDecimal(0.5, 0.25)
        q2 = ComplexDecimal(0.5, 0.3)
        self.assertFalse(q1 == q2)
    
    def test_rational_re(self):
        q = Rational(1, 2)
        self.assertEqual(q.re(), Rational(1, 2))
    def test_complex_rational_re(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertEqual(q.re(), Rational(1, 2))
    def test_decimal_re(self):
        q = Decimal(0.5)
        self.assertEqual(q.re(), Decimal(0.5))
    def test_complex_decimal_re(self):
        q = ComplexDecimal(0.5, -0.75)
        self.assertEqual(q.re(), Decimal(0.5))
    
    def test_rational_im(self):
        q = Rational(1, 2)
        self.assertEqual(q.im(), Rational(0, 1))
    def test_complex_rational_im(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertEqual(q.im(), Rational(-3, 4))
    def test_decimal_im(self):
        q = Decimal(0.5)
        self.assertEqual(q.im(), Decimal(0))
    def test_complex_decimal_im(self):
        q = ComplexDecimal(0.5, -0.75)
        self.assertEqual(q.im(), Decimal(-0.75))
    
    def test_rational_to_decimal(self):
        q = Rational(1, 2)
        self.assertEqual(q.to_decimal(), Decimal(0.5))
    def test_complex_rational_to_decimal(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertEqual(q.to_decimal(), ComplexDecimal(0.5, -0.75))
    def test_decimal_to_decimal(self):
        q = Decimal(0.5)
        self.assertEqual(q.to_decimal(), Decimal(0.5))
    def test_complex_decimal_to_decimal(self):
        q = ComplexDecimal(0.5, -0.75)
        self.assertEqual(q.to_decimal(), ComplexDecimal(0.5, -0.75))
    
    def test_rational_conj(self):
        q = Rational(1, 2)
        self.assertEqual(q.conj(), Rational(1, 2))
    def test_complex_rational_conj(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertEqual(q.conj(), ComplexRational(1, 2, 3, 4))
    def test_decimal_conj(self):
        q = Decimal(0.5)
        self.assertEqual(q.conj(), Decimal(0.5))
    def test_complex_decimal_conj(self):
        q = ComplexDecimal(0.5, -0.75)
        self.assertEqual(q.conj(), ComplexDecimal(0.5, 0.75))
    
    def test_rational_abs_squared(self):
        q = Rational(1, 2)
        self.assertEqual(q.abs_squared(), Rational(1, 4))
    def test_complex_rational_abs_squared(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertEqual(q.abs_squared(), Rational(13, 16))
    def test_decimal_abs_squared(self):
        q = Decimal(0.5)
        self.assertEqual(q.abs_squared(), Decimal(0.25))
    def test_complex_decimal_abs_squared(self):
        q = ComplexDecimal(0.5, -0.75)
        self.assertEqual(q.abs_squared(), Decimal(0.8125))
    
    def test_rational_inv(self):
        q = Rational(1, 2)
        self.assertEqual(q.inv(), Rational(2, 1))
    def test_rational_inv_zero(self):
        q = Rational(0, 1)
        with self.assertRaises(ZeroDivisionError):
            q.inv()
    def test_complex_rational_inv(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertEqual(q.inv(), ComplexRational(8, 13, 12, 13))
    def test_complex_rational_inv_zero(self):
        q = ComplexRational(0, 1, 0, 1)
        with self.assertRaises(ZeroDivisionError):
            q.inv()
    def test_decimal_inv(self):
        q = Decimal(0.5)
        self.assertAlmostEqual(q.inv().val, 2)
    def test_decimal_inv_zero(self):
        q = Decimal(0)
        with self.assertRaises(ZeroDivisionError):
            q.inv()
    def test_complex_decimal_inv(self):
        q = ComplexDecimal(0.5, -0.75)
        inv = q.inv()
        self.assertAlmostEqual(inv.a, 8/13)
        self.assertAlmostEqual(inv.b, 12/13)
    def test_complex_decimal_inv_zero(self):
        q = ComplexDecimal(0, 0)
        with self.assertRaises(ZeroDivisionError):
            q.inv()
    
    def test_gt_rational_rational_true(self):
        q1 = Rational(2, 5)
        q2 = Rational(1, 3)
        self.assertTrue(q1 > q2)
    def test_gt_rational_rational_false1(self):
        q1 = Rational(2, 5)
        q2 = Rational(2, 5)
        self.assertFalse(q1 > q2)
    def test_gt_rational_rational_false2(self):
        q1 = Rational(2, 5)
        q2 = Rational(3, 5)
        self.assertFalse(q1 > q2)
    def test_gt_rational_complex_rational_true(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(1, 3, 0, 1)
        self.assertTrue(q1 > q2)
    def test_gt_rational_complex_rational_false1(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(2, 5, 0, 1)
        self.assertFalse(q1 > q2)
    def test_gt_rational_complex_rational_false2(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(3, 5, 0, 1)
        self.assertFalse(q1 > q2)
    def test_gt_rational_complex_rational_not_implemented(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(1, 5, -3, 2)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_rational_decimal_true(self):
        q1 = Rational(3, 4)
        q2 = Decimal(0.5)
        self.assertTrue(q1 > q2)
    def test_gt_rational_decimal_false1(self):
        q1 = Rational(1, 2)
        q2 = Decimal(0.5)
        self.assertFalse(q1 > q2)
    def test_gt_rational_decimal_false2(self):
        q1 = Rational(1, 2)
        q2 = Decimal(0.75)
        self.assertFalse(q1 > q2)
    def test_gt_rational_complex_decimal_true(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.3, 0)
        self.assertTrue(q1 > q2)
    def test_gt_rational_complex_decimal_false1(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.5, 0)
        self.assertFalse(q1 > q2)
    def test_gt_rational_complex_decimal_false2(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.75, 0)
        self.assertFalse(q1 > q2)
    def test_gt_rational_complex_decimal_not_implemented(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.3, 1)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_rational_rational_true(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = Rational(1, 3)
        self.assertTrue(q1 > q2)
    def test_gt_complex_rational_rational_false1(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = Rational(1, 2)
        self.assertFalse(q1 > q2)
    def test_gt_complex_rational_rational_false2(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = Rational(2, 3)
        self.assertFalse(q1 > q2)
    def test_gt_complex_rational_rational_not_implemented(self):
        q1 = ComplexRational(1, 2, 1, 1)
        q2 = Rational(1, 3)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_rational_complex_rational_true(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = ComplexRational(1, 3, 0, 1)
        self.assertTrue(q1 > q2)
    def test_gt_complex_rational_complex_rational_false1(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = ComplexRational(1, 2, 0, 1)
        self.assertFalse(q1 > q2)
    def test_gt_complex_rational_complex_rational_false2(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = ComplexRational(2, 3, 0, 1)
        self.assertFalse(q1 > q2)
    def test_gt_complex_rational_complex_rational_not_implemented1(self):
        q1 = ComplexRational(1, 2, 1, 1)
        q2 = ComplexRational(1, 3, 0, 1)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_rational_complex_rational_not_implemented2(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = ComplexRational(1, 3, 1, 1)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_rational_decimal_true(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = Decimal(0.3)
        self.assertTrue(q1 > q2)
    def test_gt_complex_rational_decimal_false1(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = Decimal(0.5)
        self.assertFalse(q1 > q2)
    def test_gt_complex_rational_decimal_false2(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = Decimal(0.75)
        self.assertFalse(q1 > q2)
    def test_gt_complex_rational_decimal_not_implemented(self):
        q1 = ComplexRational(1, 2, 1, 1)
        q2 = Decimal(0.3)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_rational_complex_decimal_true(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = ComplexDecimal(0.3, 0)
        self.assertTrue(q1 > q2)
    def test_gt_complex_rational_complex_decimal_false1(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = ComplexDecimal(0.5, 0)
        self.assertFalse(q1 > q2)
    def test_gt_complex_rational_complex_decimal_false2(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = ComplexDecimal(0.75, 0)
        self.assertFalse(q1 > q2)
    def test_gt_complex_rational_complex_decimal_not_implemented1(self):
        q1 = ComplexRational(1, 2, 1, 1)
        q2 = ComplexDecimal(0.3, 0)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_rational_complex_decimal_not_implemented2(self):
        q1 = ComplexRational(1, 2, 0, 1)
        q2 = ComplexDecimal(0.3, -1)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_decimal_rational_true(self):
        q1 = Decimal(0.5)
        q2 = Rational(1, 3)
        self.assertTrue(q1 > q2)
    def test_gt_decimal_rational_false1(self):
        q1 = Decimal(0.5)
        q2 = Rational(1, 2)
        self.assertFalse(q1 > q2)
    def test_gt_decimal_rational_false2(self):
        q1 = Decimal(0.5)
        q2 = Rational(2, 3)
        self.assertFalse(q1 > q2)
    def test_gt_decimal_complex_rational_true(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(1, 3, 0, 1)
        self.assertTrue(q1 > q2)
    def test_gt_decimal_complex_rational_false1(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(1, 2, 0, 1)
        self.assertFalse(q1 > q2)
    def test_gt_decimal_complex_rational_false2(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(2, 3, 0, 1)
        self.assertFalse(q1 > q2)
    def test_gt_decimal_complex_rational_not_implemented(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(1, 3, 1, 1)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_decimal_decimal_true(self):
        q1 = Decimal(0.5)
        q2 = Decimal(0.3)
        self.assertTrue(q1 > q2)
    def test_gt_decimal_decimal_false1(self):
        q1 = Decimal(0.5)
        q2 = Decimal(0.5)
        self.assertFalse(q1 > q2)
    def test_gt_decimal_decimal_false2(self):
        q1 = Decimal(0.5)
        q2 = Decimal(0.75)
        self.assertFalse(q1 > q2)
    def test_gt_decimal_complex_decimal_true(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.3, 0)
        self.assertTrue(q1 > q2)
    def test_gt_decimal_complex_decimal_false1(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.5, 0)
        self.assertFalse(q1 > q2)
    def test_gt_decimal_complex_decimal_false2(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.75, 0)
        self.assertFalse(q1 > q2)
    def test_gt_decimal_complex_decimal_not_implemented(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.35, 1)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_decimal_rational_true(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Rational(1, 3)
        self.assertTrue(q1 > q2)
    def test_gt_complex_decimal_rational_false1(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Rational(1, 2)
        self.assertFalse(q1 > q2)
    def test_gt_complex_decimal_rational_false2(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Rational(2, 3)
        self.assertFalse(q1 > q2)
    def test_gt_complex_decimal_rational_not_implemented(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = Rational(1, 3)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_decimal_complex_rational_true(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = ComplexRational(1, 3, 0, 1)
        self.assertTrue(q1 > q2)
    def test_gt_complex_decimal_complex_rational_false1(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = ComplexRational(1, 2, 0, 1)
        self.assertFalse(q1 > q2)
    def test_gt_complex_decimal_complex_rational_false2(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = ComplexRational(2, 3, 0, 1)
        self.assertFalse(q1 > q2)
    def test_gt_complex_decimal_complex_rational_not_implemented1(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = ComplexRational(1, 3, 0, 1)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_decimal_complex_rational_not_implemented2(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = ComplexRational(1, 3, 1, 1)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_decimal_decimal_true(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Decimal(0.3)
        self.assertTrue(q1 > q2)
    def test_gt_complex_decimal_decimal_false1(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Decimal(0.5)
        self.assertFalse(q1 > q2)
    def test_gt_complex_decimal_decimal_false2(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = Decimal(0.75)
        self.assertFalse(q1 > q2)
    def test_gt_complex_decimal_decimal_not_implemented(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = Decimal(0.3)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_decimal_complex_decimal_true(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = ComplexDecimal(0.3, 0)
        self.assertTrue(q1 > q2)
    def test_gt_complex_decimal_complex_decimal_false1(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = ComplexDecimal(0.5, 0)
        self.assertFalse(q1 > q2)
    def test_gt_complex_decimal_complex_decimal_false2(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = ComplexDecimal(0.75, 0)
        self.assertFalse(q1 > q2)
    def test_gt_complex_decimal_complex_decimal_not_implemented1(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = ComplexDecimal(0.3, 0)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    def test_gt_complex_decimal_complex_decimal_not_implemented2(self):
        q1 = ComplexDecimal(0.5, 0)
        q2 = ComplexDecimal(0.3, 1)
        self.assertEqual(q1.__gt__(q2), NotImplemented)
    
    def test_rational_pos(self):
        q = Rational(1, 2)
        self.assertEqual(+q, Rational(1, 2))
    def test_complex_rational_pos(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertEqual(+q, ComplexRational(1, 2, -3, 4))
    def test_decimal_pos(self):
        q = Decimal(0.5)
        self.assertEqual(+q, Decimal(0.5))
    def test_complex_decimal_pos(self):
        q = ComplexDecimal(0.5, -0.75)
        self.assertEqual(+q, ComplexDecimal(0.5, -0.75))
    
    def test_rational_neg(self):
        q = Rational(1, 2)
        self.assertEqual(-q, Rational(-1, 2))
    def test_complex_rational_neg(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertEqual(-q, ComplexRational(-1, 2, 3, 4))
    def test_decimal_neg(self):
        q = Decimal(0.5)
        self.assertEqual(-q, Decimal(-0.5))
    def test_complex_decimal_neg(self):
        q = ComplexDecimal(0.5, -0.75)
        self.assertEqual(-q, ComplexDecimal(-0.5, 0.75))
    
    def test_rational_abs(self):
        q = Rational(1, 2)
        self.assertEqual(abs(q), Rational(1, 2))
    def test_complex_rational_abs(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertAlmostEqual(abs(q).val, sqrt(0.8125))
    def test_decimal_abs(self):
        q = Decimal(0.5)
        self.assertEqual(abs(q), Decimal(0.5))
    def test_complex_decimal_abs(self):
        q = ComplexDecimal(0.5, -0.75)
        self.assertAlmostEqual(abs(q).val, sqrt(0.8125))
    
    def test_add_rational_rational(self):
        q1 = Rational(2, 5)
        q2 = Rational(1, 3)
        self.assertEqual(q1 + q2, Rational(11, 15)) # 2/5 + 1/3 = 11/15
    def test_add_rational_complex_rational(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(1, 3, 4, 5)
        self.assertEqual(q1 + q2, ComplexRational(11, 15, 4, 5)) # 2/5 + (1/3 + (4/5)i) = 11/15 + (4/5)i
    def test_add_rational_decimal(self):
        q1 = Rational(3, 4)
        q2 = Decimal(0.5)
        self.assertEqual(q1 + q2, Decimal(1.25)) # 3/4 + 0.5 = 1.25
    def test_add_rational_complex_decimal(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.75, -0.5)
        self.assertEqual(q1 + q2, ComplexDecimal(1.25, -0.5)) # 1/2 + (0.75 - 0.5i) = 1.25 - 0.5i
    def test_add_complex_rational_rational(self):
        q1 = ComplexRational(1, 2, 4, 5)
        q2 = Rational(1, 3)
        self.assertEqual(q1 + q2, ComplexRational(5, 6, 4, 5)) # (1/2 + (4/5)i) + 1/3 = 5/6 + (4/5)i
    def test_add_complex_rational_complex_rational(self):
        q1 = ComplexRational(1, 2, 4, 5)
        q2 = ComplexRational(1, 3, 3, 1)
        self.assertEqual(q1 + q2, ComplexRational(5, 6, 19, 5)) # (1/2 + (4/5)i) + (1/3 + 3i) = 5/6 + (19/5)i
    def test_add_complex_rational_decimal(self):
        q1 = ComplexRational(1, 2, 3, 4)
        q2 = Decimal(0.5)
        self.assertEqual(q1 + q2, ComplexDecimal(1, 0.75)) # (1/2 + (3/4)i) + 0.5 = 1 + 0.75i
    def test_add_complex_rational_complex_decimal(self):
        q1 = ComplexRational(1, 2, 3, 4)
        q2 = ComplexDecimal(0.5, 1.25)
        self.assertEqual(q1 + q2, ComplexDecimal(1, 2)) # (1/2 + (3/4)i) + (0.5 + 1.25i) = 1 + 2i
    def test_add_decimal_rational(self):
        q1 = Decimal(0.5)
        q2 = Rational(1, 4)
        self.assertEqual(q1 + q2, Decimal(0.75)) # 0.5 + 1/4 = 0.75
    def test_add_decimal_complex_rational(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(1, 4, 3, 2)
        self.assertEqual(q1 + q2, ComplexDecimal(0.75, 1.5)) # 0.5 + (1/4 + (3/2)i) = 0.75 + 1.5i
    def test_add_decimal_decimal(self):
        q1 = Decimal(0.5)
        q2 = Decimal(0.25)
        self.assertEqual(q1 + q2, Decimal(0.75)) # 0.5 + 0.25 = 0.75
    def test_add_decimal_complex_decimal(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.25, 1.75)
        self.assertEqual(q1 + q2, ComplexDecimal(0.75, 1.75)) # 0.5 + (0.25 + 1.75i) = 0.75 + 1.75i
    def test_add_complex_decimal_rational(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = Rational(3, 4)
        self.assertEqual(q1 + q2, ComplexDecimal(1.25, 1)) # (0.5 + i) + 3/4 = 1.25 + i
    def test_add_complex_decimal_complex_rational(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = ComplexRational(3, 4, 1, 2)
        self.assertEqual(q1 + q2, ComplexDecimal(1.25, 1.5)) # (0.5 + i) + (3/4 + (1/2)i) = 1.25 + 1.5i
    def test_add_complex_decimal_decimal(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = Decimal(0.25)
        self.assertEqual(q1 + q2, ComplexDecimal(0.75, 1)) # (0.5 + i) + 0.25 = 0.75 + i
    def test_add_complex_decimal_complex_decimal(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = ComplexDecimal(0.25, 1.75)
        self.assertEqual(q1 + q2, ComplexDecimal(0.75, 2.75)) # (0.5 + i) + (0.25 + 1.75i) = 0.75 + 2.75i
    
    def test_sub_rational_rational(self):
        q1 = Rational(2, 5)
        q2 = Rational(1, 3)
        self.assertEqual(q1 - q2, Rational(1, 15)) # 2/5 - 1/3 = 1/15
    def test_sub_rational_complex_rational(self):
        q1 = Rational(2, 5)
        q2 = ComplexRational(1, 3, 4, 5)
        self.assertEqual(q1 - q2, ComplexRational(1, 15, -4, 5)) # 2/5 - (1/3 + (4/5)i) = 1/15 - (4/5)i
    def test_sub_rational_decimal(self):
        q1 = Rational(3, 4)
        q2 = Decimal(0.5)
        self.assertEqual(q1 - q2, Decimal(0.25)) # 3/4 - 0.5 = 0.25
    def test_sub_rational_complex_decimal(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.75, -0.5)
        self.assertEqual(q1 - q2, ComplexDecimal(-0.25, 0.5)) # 1/2 - (0.75 - 0.5i) = -0.25 + 0.5i
    def test_sub_complex_rational_rational(self):
        q1 = ComplexRational(1, 2, 4, 5)
        q2 = Rational(1, 3)
        self.assertEqual(q1 - q2, ComplexRational(1, 6, 4, 5)) # (1/2 + (4/5)i) - 1/3 = 1/6 + (4/5)i
    def test_sub_complex_rational_complex_rational(self):
        q1 = ComplexRational(1, 2, 4, 5)
        q2 = ComplexRational(1, 3, 3, 1)
        self.assertEqual(q1 - q2, ComplexRational(1, 6, -11, 5)) # (1/2 + (4/5)i) - (1/3 + 3i) = 1/6 - (11/5)i
    def test_sub_complex_rational_decimal(self):
        q1 = ComplexRational(1, 2, 3, 4)
        q2 = Decimal(0.5)
        self.assertEqual(q1 - q2, ComplexDecimal(0, 0.75)) # (1/2 + (3/4)i) - 0.5 = 0.75i
    def test_sub_complex_rational_complex_decimal(self):
        q1 = ComplexRational(1, 2, 3, 4)
        q2 = ComplexDecimal(0.5, 0.25)
        self.assertEqual(q1 - q2, ComplexDecimal(0, 0.5)) # (1/2 + (3/4)i) - (0.5 + 0.25i) = 0.5i
    def test_sub_decimal_rational(self):
        q1 = Decimal(0.5)
        q2 = Rational(1, 4)
        self.assertEqual(q1 - q2, Decimal(0.25)) # 0.5 - 1/4 = 0.25
    def test_sub_decimal_complex_rational(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(1, 4, 3, 2)
        self.assertEqual(q1 - q2, ComplexDecimal(0.25, -1.5)) # 0.5 - (1/4 + (3/2)i) = 0.25 - 1.5i
    def test_sub_decimal_decimal(self):
        q1 = Decimal(1)
        q2 = Decimal(0.25)
        self.assertEqual(q1 - q2, Decimal(0.75)) # 1 - 0.25 = 0.75
    def test_sub_decimal_complex_decimal(self):
        q1 = Decimal(1)
        q2 = ComplexDecimal(0.25, 1.75)
        self.assertEqual(q1 - q2, ComplexDecimal(0.75, -1.75)) # 1 - (0.25 + 1.75i) = 0.75 - 1.75i
    def test_sub_complex_decimal_rational(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = Rational(3, 4)
        self.assertEqual(q1 - q2, ComplexDecimal(-0.25, 1)) # (0.5 + i) - 3/4 = -0.25 + i
    def test_sub_complex_decimal_complex_rational(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = ComplexRational(3, 4, 1, 2)
        self.assertEqual(q1 - q2, ComplexDecimal(-0.25, 0.5)) # (0.5 + i) - (3/4 + (1/2)i) = -0.25 + 0.5i
    def test_sub_complex_decimal_decimal(self):
        q1 = ComplexDecimal(1.5, 1)
        q2 = Decimal(0.25)
        self.assertEqual(q1 - q2, ComplexDecimal(1.25, 1)) # (1.5 + i) - 0.25 = 1.25 + i
    def test_sub_complex_decimal_complex_decimal(self):
        q1 = ComplexDecimal(1.5, 1)
        q2 = ComplexDecimal(0.25, 1.75)
        self.assertEqual(q1 - q2, ComplexDecimal(1.25, -0.75)) # (1.5 + i) - (0.25 + 1.75i) = 1.25 - 0.75i

    def test_mul_rational_rational(self):
        q1 = Rational(4, 5)
        q2 = Rational(15, 2)
        self.assertEqual(q1 * q2, Rational(6, 1)) # 4/5 * 15/2 = 6
    def test_mul_rational_complex_rational(self):
        q1 = Rational(5, 2)
        q2 = ComplexRational(1, 3, 4, 5)
        self.assertEqual(q1 * q2, ComplexRational(5, 6, 2, 1)) # 5/2 * (1/3 + (4/5)i) = 5/6 + 2i
    def test_mul_rational_decimal(self):
        q1 = Rational(3, 4)
        q2 = Decimal(0.5)
        self.assertEqual(q1 * q2, Decimal(0.375)) # 3/4 * 0.5 = 0.375
    def test_mul_rational_complex_decimal(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.75, -0.5)
        self.assertEqual(q1 * q2, ComplexDecimal(0.375, -0.25)) # 1/2 * (0.75 - 0.5i) = 0.375 - 0.25i
    def test_mul_complex_rational_rational(self):
        q1 = ComplexRational(1, 2, 4, 5)
        q2 = Rational(1, 2)
        self.assertEqual(q1 * q2, ComplexRational(1, 4, 2, 5)) # (1/2 + (4/5)i) * 1/2 = 1/4 + (2/5)i
    def test_mul_complex_rational_complex_rational(self):
        q1 = ComplexRational(1, 2, 4, 5)
        q2 = ComplexRational(1, 3, 3, 1)
        self.assertEqual(q1 * q2, ComplexRational(-67, 30, 53, 30)) # (1/2 + (4/5)i) * (1/3 + 3i) = -67/30 + (53/30)i
    def test_mul_complex_rational_decimal(self):
        q1 = ComplexRational(1, 2, 3, 4)
        q2 = Decimal(0.5)
        self.assertEqual(q1 * q2, ComplexDecimal(0.25, 0.375)) # (1/2 + (3/4)i) * 0.5 = 0.25 + 0.375i
    def test_mul_complex_rational_complex_decimal(self):
        q1 = ComplexRational(1, 2, 3, 4)
        q2 = ComplexDecimal(0.5, 0.25)
        self.assertEqual(q1 * q2, ComplexDecimal(0.0625, 0.5)) # (1/2 + (3/4)i) * (0.5 + 0.25i) = 0.0625 + 0.5i
    def test_mul_decimal_rational(self):
        q1 = Decimal(0.5)
        q2 = Rational(1, 4)
        self.assertEqual(q1 * q2, Decimal(0.125)) # 0.5 * 1/4 = 0.125
    def test_mul_decimal_complex_rational(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(1, 4, 3, 2)
        self.assertEqual(q1 * q2, ComplexDecimal(0.125, 0.75)) # 0.5 * (1/4 + (3/2)i) = 0.125 + 0.75i
    def test_mul_decimal_decimal(self):
        q1 = Decimal(1.5)
        q2 = Decimal(0.25)
        self.assertEqual(q1 * q2, Decimal(0.375)) # 1.5 * 0.25 = 0.375
    def test_mul_decimal_complex_decimal(self):
        q1 = Decimal(2)
        q2 = ComplexDecimal(0.25, 1.75)
        self.assertEqual(q1 * q2, ComplexDecimal(0.5, 3.5)) # 2 * (0.25 + 1.75i) = 0.5 + 3.5i
    def test_mul_complex_decimal_rational(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = Rational(3, 4)
        self.assertEqual(q1 * q2, ComplexDecimal(0.375, 0.75)) # (0.5 + i) * 3/4 = 0.375 + 0.75i
    def test_mul_complex_decimal_complex_rational(self):
        q1 = ComplexDecimal(0.5, 1)
        q2 = ComplexRational(3, 4, 1, 2)
        self.assertEqual(q1 * q2, ComplexDecimal(-0.125, 1)) # (0.5 + i) * (3/4 + (1/2)i) = -0.125 + i
    def test_mul_complex_decimal_decimal(self):
        q1 = ComplexDecimal(1.5, 1)
        q2 = Decimal(0.25)
        self.assertEqual(q1 * q2, ComplexDecimal(0.375, 0.25)) # (1.5 + i) * 0.25 = 0.375 + 0.25i
    def test_mul_complex_decimal_complex_decimal(self):
        q1 = ComplexDecimal(1.5, 1)
        q2 = ComplexDecimal(0.25, 1.75)
        self.assertEqual(q1 * q2, ComplexDecimal(-1.375, 2.875)) # (1.5 + i) * (0.25 + 1.75i) = -1.375 + 2.875i
    
    # (1/2 + (1/4)i) / ((3/8) + (1/2)i) = (4/5) - (2/5)i
    def test_truediv_rational_rational(self):
        q1 = Rational(1, 2)
        q2 = Rational(3, 8)
        self.assertEqual(q1 / q2, Rational(4, 3)) # (1/2) / (3/8) = 4/3
    def test_truediv_rational_complex_rational(self):
        q1 = Rational(1, 2)
        q2 = ComplexRational(3, 8, 1, 2)
        self.assertEqual(q1 / q2, ComplexRational(12, 25, -16, 25)) # (1/2) / ((3/8) + (1/2)i) = 12/25 - (16/25)i
    def test_truediv_rational_decimal(self):
        q1 = Rational(1, 2)
        q2 = Decimal(0.375)
        res = q1 / q2
        self.assertAlmostEqual(res.val, 4/3) # (1/2) / 0.375 = 4/3
    def test_truediv_rational_complex_decimal(self):
        q1 = Rational(1, 2)
        q2 = ComplexDecimal(0.375, 0.5)
        res = q1 / q2
        self.assertAlmostEqual(res.a, 12/25)
        self.assertAlmostEqual(res.b, -16/25) # (1/2) / (0.375 + 0.5i) = 12/25 - (16/25)i
    def test_truediv_complex_rational_rational(self):
        q1 = ComplexRational(1, 2, 1, 4)
        q2 = Rational(3, 8)
        self.assertEqual(q1 / q2, ComplexRational(4, 3, 2, 3)) # (1/2 + (1/4)i) / (3/8) = 4/3 + (2/3)i
    def test_truediv_complex_rational_complex_rational(self):
        q1 = ComplexRational(1, 2, 1, 4)
        q2 = ComplexRational(3, 8, 1, 2)
        self.assertEqual(q1 / q2, ComplexRational(4, 5, -2, 5)) # (1/2 + (1/4)i) / ((3/8) + (1/2)i) = (4/5) - (2/5)i
    def test_truediv_complex_rational_decimal(self):
        q1 = ComplexRational(1, 2, 1, 4)
        q2 = Decimal(0.375)
        res = q1 / q2
        self.assertAlmostEqual(res.a, 4/3)
        self.assertAlmostEqual(res.b, 2/3) # (1/2 + (1/4)i) / 0.375 = 4/3 + (2/3)i
    def test_truediv_complex_rational_complex_decimal(self):
        q1 = ComplexRational(1, 2, 1, 4)
        q2 = ComplexDecimal(0.375, 0.5)
        res = q1 / q2
        self.assertAlmostEqual(res.a, 4/5)
        self.assertAlmostEqual(res.b, -2/5) # (1/2 + (1/4)i) / (0.375 + 0.5i) = (4/5) - (2/5)i
    def test_truediv_decimal_rational(self):
        q1 = Decimal(0.5)
        q2 = Rational(3, 8)
        res = q1 / q2
        self.assertAlmostEqual(res.val, 4/3) # 0.5 / (3/8) = 4/3
    def test_truediv_decimal_complex_rational(self):
        q1 = Decimal(0.5)
        q2 = ComplexRational(3, 8, 1, 2)
        res = q1 / q2
        self.assertAlmostEqual(res.a, 12/25)
        self.assertAlmostEqual(res.b, -16/25) # 0.5 / ((3/8) + (1/2)i) = 12/25 - (16/25)i
    def test_truediv_decimal_decimal(self):
        q1 = Decimal(0.5)
        q2 = Decimal(0.375)
        res = q1 / q2
        self.assertAlmostEqual(res.val, 4/3) # 0.5 / 0.375 = 4/3
    def test_truediv_decimal_complex_decimal(self):
        q1 = Decimal(0.5)
        q2 = ComplexDecimal(0.375, 0.5)
        res = q1 / q2
        self.assertAlmostEqual(res.a, 12/25)
        self.assertAlmostEqual(res.b, -16/25) # 0.5 / (0.375 + 0.5i) = 12/25 - (16/25)i
    def test_truediv_complex_decimal_rational(self):
        q1 = ComplexDecimal(0.5, 0.25)
        q2 = Rational(3, 8)
        res = q1 / q2
        self.assertAlmostEqual(res.a, 4/3)
        self.assertAlmostEqual(res.b, 2/3) # (0.5 + 0.25i) / (3/8) = 4/3 + (2/3)i
    def test_truediv_complex_decimal_complex_rational(self):
        q1 = ComplexDecimal(0.5, 0.25)
        q2 = ComplexRational(3, 8, 1, 2)
        res = q1 / q2
        self.assertAlmostEqual(res.a, 4/5)
        self.assertAlmostEqual(res.b, -2/5) # (0.5 + 0.25i) / (3/8 + (1/2)i) = (4/5) - (2/5)i
    def test_truediv_complex_decimal_decimal(self):
        q1 = ComplexDecimal(0.5, 0.25)
        q2 = Decimal(0.375)
        res = q1 / q2
        self.assertAlmostEqual(res.a, 4/3)
        self.assertAlmostEqual(res.b, 2/3) # (0.5 + 0.25i) / 0.375 = 4/3 + (2/3)i
    def test_truediv_complex_decimal(self):
        q1 = ComplexDecimal(0.5, 0.25)
        q2 = ComplexDecimal(0.375, 0.5)
        res = q1 / q2
        self.assertAlmostEqual(res.a, 4/5)
        self.assertAlmostEqual(res.b, -2/5) # (0.5 + 0.25i) / (0.375 + 0.5i) = (4/5) - (2/5)i
    
    def test_rational_str1(self):
        q = Rational(1, 2)
        self.assertEqual(str(q), '1/2')
    def test_rational_str2(self):
        q = Rational(2, 1)
        self.assertEqual(str(q), '2')
    def test_rational_str3(self):
        q = Rational(-1, 2)
        self.assertEqual(str(q), '-1/2')
    def test_rational_str4(self):
        q = Rational(-2, 1)
        self.assertEqual(str(q), '-2')
    def test_rational_str5(self):
        q = Rational(0, 1)
        self.assertEqual(str(q), '0')

    def test_complex_rational_str1(self):
        q = ComplexRational(1, 2, 3, 4)
        self.assertEqual(str(q), '1/2 + (3/4)i')
    def test_complex_rational_str2(self):
        q = ComplexRational(1, 2, -3, 4)
        self.assertEqual(str(q), '1/2 - (3/4)i')
    def test_complex_rational_str3(self):
        q = ComplexRational(-1, 2, 3, 4)
        self.assertEqual(str(q), '-1/2 + (3/4)i')
    def test_complex_rational_str4(self):
        q = ComplexRational(1, 1, 3, 4)
        self.assertEqual(str(q), '1 + (3/4)i')
    def test_complex_rational_str5(self):
        q = ComplexRational(1, 1, 2, 1)
        self.assertEqual(str(q), '1 + 2i')
    def test_complex_rational_str6(self):
        q = ComplexRational(1, 1, -2, 1)
        self.assertEqual(str(q), '1 - 2i')
    def test_complex_rational_str7(self):
        q = ComplexRational(1, 1, 1, 1)
        self.assertEqual(str(q), '1 + i')
    def test_complex_rational_str8(self):
        q = ComplexRational(1, 1, -1, 1)
        self.assertEqual(str(q), '1 - i')
    def test_complex_rational_str9(self):
        q = ComplexRational(0, 1, 3, 4)
        self.assertEqual(str(q), '(3/4)i')
    def test_complex_rational_str10(self):
        q = ComplexRational(0, 1, -3, 4)
        self.assertEqual(str(q), '-(3/4)i')
    def test_complex_rational_str11(self):
        q = ComplexRational(0, 1, 2, 1)
        self.assertEqual(str(q), '2i')
    def test_complex_rational_str12(self):
        q = ComplexRational(0, 1, -2, 1)
        self.assertEqual(str(q), '-2i')
    def test_complex_rational_str13(self):
        q = ComplexRational(0, 1, 1, 1)
        self.assertEqual(str(q), 'i')
    def test_complex_rational_str14(self):
        q = ComplexRational(0, 1, -1, 1)
        self.assertEqual(str(q), '-i')
    def test_complex_rational_str15(self):
        q = ComplexRational(1, 2, 0, 1)
        self.assertEqual(str(q), '1/2')
    def test_complex_rational_str16(self):
        q = ComplexRational(2, 1, 0, 1)
        self.assertEqual(str(q), '2')
    def test_complex_rational_str17(self):
        q = ComplexRational(-1, 2, 0, 1)
        self.assertEqual(str(q), '-1/2')
    def test_complex_rational_str18(self):
        q = ComplexRational(-2, 1, 0, 1)
        self.assertEqual(str(q), '-2')
    def test_complex_rational_str19(self):
        q = ComplexRational(0, 1, 0, 1)
        self.assertEqual(str(q), '0')

    def test_decimal_str1(self):
        q = Decimal(0.5)
        self.assertEqual(str(q), '0.5')
    def test_decimal_str2(self):
        q = Decimal(-0.5)
        self.assertEqual(str(q), '-0.5')
    def test_decimal_str3(self):
        q = Decimal(0)
        self.assertEqual(str(q), '0.0')

    def test_complex_decimal_str1(self):
        q = ComplexDecimal(0.5, 0.75)
        self.assertEqual(str(q), '0.5 + 0.75i')
    def test_complex_decimal_str2(self):
        q = ComplexDecimal(0.5, -0.75)
        self.assertEqual(str(q), '0.5 - 0.75i')
    def test_complex_decimal_str3(self):
        q = ComplexDecimal(0.5, 1)
        self.assertEqual(str(q), '0.5 + i')
    def test_complex_decimal_str4(self):
        q = ComplexDecimal(0.5, -1)
        self.assertEqual(str(q), '0.5 - i')
    def test_complex_decimal_str5(self):
        q = ComplexDecimal(0, 0.75)
        self.assertEqual(str(q), '0.75i')
    def test_complex_decimal_str6(self):
        q = ComplexDecimal(0, -0.75)
        self.assertEqual(str(q), '-0.75i')
    def test_complex_decimal_str7(self):
        q = ComplexDecimal(0, 1)
        self.assertEqual(str(q), 'i')
    def test_complex_decimal_str8(self):
        q = ComplexDecimal(0, -1)
        self.assertEqual(str(q), '-i')
    def test_complex_decimal_str9(self):
        q = ComplexDecimal(0.5, 0)
        self.assertEqual(str(q), '0.5')
    def test_complex_decimal_str10(self):
        q = ComplexDecimal(-0.5, 0)
        self.assertEqual(str(q), '-0.5')
    def test_complex_decimal_str11(self):
        q = ComplexDecimal(0, 0)
        self.assertEqual(str(q), '0.0')
    
    def test_rational_int1(self):
        q = Rational(1, 1)
        self.assertEqual(int(q), 1)
    def test_rational_int2(self):
        q = Rational(2, 1)
        self.assertEqual(int(q), 2)
    def test_rational_int3(self):
        q = Rational(-1, 1)
        self.assertEqual(int(q), -1)
    def test_rational_int4(self):
        q = Rational(-2, 1)
        self.assertEqual(int(q), -2)
    def test_rational_int5(self):
        q = Rational(0, 1)
        self.assertEqual(int(q), 0)
    def test_rational_int6(self):
        q = Rational(5, 3)
        with self.assertRaises(ValueError):
            int(q)
    def test_rational_int7(self):
        q = Rational(-5, 10)
        with self.assertRaises(ValueError):
            int(q)

    def test_complex_rational_int1(self):
        q = ComplexRational(1, 1, 0, 1)
        self.assertEqual(int(q), 1)
    def test_complex_rational_int2(self):
        q = ComplexRational(2, 1, 0, 1)
        self.assertEqual(int(q), 2)
    def test_complex_rational_int3(self):
        q = ComplexRational(-1, 1, 0, 1)
        self.assertEqual(int(q), -1)
    def test_complex_rational_int4(self):
        q = ComplexRational(-2, 1, 0, 1)
        self.assertEqual(int(q), -2)
    def test_complex_rational_int5(self):
        q = ComplexRational(5, 3, 0, 1)
        with self.assertRaises(ValueError):
            int(q)
    def test_complex_rational_int6(self):
        q = ComplexRational(-5, 10, 0, 1)
        with self.assertRaises(ValueError):
            int(q)
    def test_complex_rational_int7(self):
        q = ComplexRational(1, 1, 1, 1)
        with self.assertRaises(ValueError):
            int(q)
    
    def test_rational_float1(self):
        q = Rational(1, 1)
        self.assertEqual(float(q), 1)
    def test_rational_float2(self):
        q = Rational(1, 2)
        self.assertEqual(float(q), 0.5)
    def test_rational_float3(self):
        q = Rational(-1, 1)
        self.assertEqual(float(q), -1)
    def test_rational_float4(self):
        q = Rational(-1, 2)
        self.assertEqual(float(q), -0.5)
    def test_rational_float5(self):
        q = Rational(0, 1)
        self.assertEqual(float(q), 0)

    def test_complex_rational_float1(self):
        q = ComplexRational(1, 1, 0, 1)
        self.assertEqual(float(q), 1)
    def test_complex_rational_float2(self):
        q = ComplexRational(1, 2, 0, 1)
        self.assertEqual(float(q), 0.5)
    def test_complex_rational_float3(self):
        q = ComplexRational(-1, 1, 0, 1)
        self.assertEqual(float(q), -1)
    def test_complex_rational_float4(self):
        q = ComplexRational(-1, 2, 0, 1)
        self.assertEqual(float(q), -0.5)
    def test_complex_rational_float7(self):
        q = ComplexRational(1, 1, 1, 1)
        with self.assertRaises(ValueError):
            float(q)
    
    def test_decimal_float1(self):
        q = Decimal(1)
        self.assertEqual(float(q), 1)
    def test_decimal_float2(self):
        q = Decimal(0.5)
        self.assertEqual(float(q), 0.5)
    def test_decimal_float3(self):
        q = Decimal(-1)
        self.assertEqual(float(q), -1)
    def test_decimal_float4(self):
        q = Decimal(-0.5)
        self.assertEqual(float(q), -0.5)
    def test_decimal_float5(self):
        q = Decimal(0)
        self.assertEqual(float(q), 0)

    def test_complex_decimal_float1(self):
        q = ComplexDecimal(1, 0)
        self.assertEqual(float(q), 1)
    def test_complex_decimal_float2(self):
        q = ComplexDecimal(0.5, 0)
        self.assertEqual(float(q), 0.5)
    def test_complex_decimal_float3(self):
        q = ComplexDecimal(-1, 0)
        self.assertEqual(float(q), -1)
    def test_complex_decimal_float4(self):
        q = ComplexDecimal(-0.5, 0)
        self.assertEqual(float(q), -0.5)
    def test_complex_decimal_float7(self):
        q = ComplexDecimal(1, 1)
        with self.assertRaises(ValueError):
            float(q)
    
    def test_rational_numerator(self):
        q = Rational(5, 3)
        self.assertEqual(q.numerator(), 5)
    def test_complex_rational_numerator1(self):
        q = ComplexRational(5, 3, 0, 1)
        self.assertEqual(q.numerator(), 5)
    def test_complex_rational_numerator2(self):
        q = ComplexRational(5, 3, 2, 7)
        with self.assertRaises(ValueError):
            q.numerator()
    def test_decimal_numerator(self):
        q = Decimal(1)
        with self.assertRaises(ValueError):
            q.numerator()
    def test_complex_decimal_numerator(self):
        q = ComplexDecimal(1, 0)
        with self.assertRaises(ValueError):
            q.numerator()
    
    def test_rational_denominator(self):
        q = Rational(5, 3)
        self.assertEqual(q.denominator(), 3)
    def test_complex_rational_denominator1(self):
        q = ComplexRational(5, 3, 0, 1)
        self.assertEqual(q.denominator(), 3)
    def test_complex_rational_denominator2(self):
        q = ComplexRational(5, 3, 2, 7)
        with self.assertRaises(ValueError):
            q.denominator()
    def test_decimal_denominator(self):
        q = Decimal(1)
        with self.assertRaises(ValueError):
            q.denominator()
    def test_complex_decimal_denominator(self):
        q = ComplexDecimal(1, 0)
        with self.assertRaises(ValueError):
            q.denominator()
    
    def test_rational_arg1(self):
        q = Rational(5, 3)
        self.assertAlmostEqual(float(q.arg()), 0)
    def test_rational_arg2(self):
        q = Rational(-5, 3)
        self.assertAlmostEqual(float(q.arg()), pi)
    def test_rational_arg_zero(self):
        q = Rational(0, 1)
        with self.assertRaises(ValueError):
            q.arg()
    def test_complex_rational_arg1(self):
        q = ComplexRational(5, 3, 0, 1)
        self.assertAlmostEqual(float(q.arg()), 0)
    def test_complex_rational_arg2(self):
        q = ComplexRational(-5, 3, 0, 1)
        self.assertAlmostEqual(float(q.arg()), pi)
    def test_complex_rational_arg3(self):
        q = ComplexRational(0, 1, 1, 1)
        self.assertAlmostEqual(float(q.arg()), pi/2)
    def test_complex_rational_arg4(self):
        q = ComplexRational(0, 1, -1, 1)
        self.assertAlmostEqual(float(q.arg()), -pi/2)
    def test_complex_rational_arg5(self):
        q = ComplexRational(1, 1, 1, 1)
        self.assertAlmostEqual(float(q.arg()), pi/4)
    def test_complex_rational_arg_zero(self):
        q = ComplexRational(0, 1, 0, 1)
        with self.assertRaises(ValueError):
            q.arg()
    def test_decimal_arg1(self):
        q = Decimal(1.25)
        self.assertAlmostEqual(float(q.arg()), 0)
    def test_decimal_arg2(self):
        q = Decimal(-1.25)
        self.assertAlmostEqual(float(q.arg()), pi)
    def test_decimal_arg_zero(self):
        q = Decimal(0)
        with self.assertRaises(ValueError):
            q.arg()
    def test_complex_decimal_arg1(self):
        q = ComplexDecimal(1.25, 0)
        self.assertAlmostEqual(float(q.arg()), 0)
    def test_complex_decimal_arg2(self):
        q = ComplexDecimal(-1.25, 0)
        self.assertAlmostEqual(float(q.arg()), pi)
    def test_complex_decimal_arg3(self):
        q = ComplexDecimal(0, 1)
        self.assertAlmostEqual(float(q.arg()), pi/2)
    def test_complex_decimal_arg4(self):
        q = ComplexDecimal(0, -1)
        self.assertAlmostEqual(float(q.arg()), -pi/2)
    def test_complex_decimal_arg5(self):
        q = ComplexDecimal(1, 1)
        self.assertAlmostEqual(float(q.arg()), pi/4)
    def test_complex_decimal_arg_zero(self):
        q = ComplexDecimal(0, 0)
        with self.assertRaises(ValueError):
            q.arg()
    
    def test_rational_log1(self):
        q = Rational(5, 3)
        self.assertAlmostEqual(float(q.log().re()), log(5 / 3))
        self.assertAlmostEqual(float(q.log().im()), 0)
    def test_rational_log2(self):
        q = Rational(-5, 3)
        self.assertAlmostEqual(float(q.log().re()), log(5 / 3))
        self.assertAlmostEqual(float(q.log().im()), pi)
    def test_rational_log_zero(self):
        q = Rational(0, 1)
        with self.assertRaises(ValueError):
            q.log()
    def test_complex_rational_log1(self):
        q = ComplexRational(5, 3, 0, 1)
        self.assertAlmostEqual(float(q.log().re()), log(5 / 3))
        self.assertAlmostEqual(float(q.log().im()), 0)
    def test_complex_rational_log2(self):
        q = ComplexRational(-5, 3, 0, 1)
        self.assertAlmostEqual(float(q.log().re()), log(5 / 3))
        self.assertAlmostEqual(float(q.log().im()), pi)
    def test_complex_rational_log3(self):
        q = ComplexRational(0, 1, 1, 1)
        self.assertAlmostEqual(float(q.log().re()), 0)
        self.assertAlmostEqual(float(q.log().im()), pi/2)
    def test_complex_rational_log4(self):
        q = ComplexRational(0, 1, -1, 1)
        self.assertAlmostEqual(float(q.log().re()), 0)
        self.assertAlmostEqual(float(q.log().im()), -pi/2)
    def test_complex_rational_log5(self):
        q = ComplexRational(1, 1, 1, 1)
        self.assertAlmostEqual(float(q.log().re()), log(sqrt(2)))
        self.assertAlmostEqual(float(q.log().im()), pi/4)
    def test_complex_rational_log_zero(self):
        q = ComplexRational(0, 1, 0, 1)
        with self.assertRaises(ValueError):
            q.log()
    def test_decimal_log1(self):
        q = Decimal(1.25)
        self.assertAlmostEqual(float(q.log().re()), log(1.25))
        self.assertAlmostEqual(float(q.log().im()), 0)
    def test_decimal_log2(self):
        q = Decimal(-1.25)
        self.assertAlmostEqual(float(q.log().re()), log(1.25))
        self.assertAlmostEqual(float(q.log().im()), pi)
    def test_decimal_log_zero(self):
        q = Decimal(0)
        with self.assertRaises(ValueError):
            q.log()
    def test_complex_decimal_log1(self):
        q = ComplexDecimal(1.25, 0)
        self.assertAlmostEqual(float(q.log().re()), log(1.25))
        self.assertAlmostEqual(float(q.log().im()), 0)
    def test_complex_decimal_log2(self):
        q = ComplexDecimal(-1.25, 0)
        self.assertAlmostEqual(float(q.log().re()), log(1.25))
        self.assertAlmostEqual(float(q.log().im()), pi)
    def test_complex_decimal_log3(self):
        q = ComplexDecimal(0, 1)
        self.assertAlmostEqual(float(q.log().re()), 0)
        self.assertAlmostEqual(float(q.log().im()), pi/2)
    def test_complex_decimal_log4(self):
        q = ComplexDecimal(0, -1)
        self.assertAlmostEqual(float(q.log().re()), 0)
        self.assertAlmostEqual(float(q.log().im()), -pi/2)
    def test_complex_decimal_log5(self):
        q = ComplexDecimal(1, 1)
        self.assertAlmostEqual(float(q.log().re()), log(sqrt(2)))
        self.assertAlmostEqual(float(q.log().im()), pi/4)
    def test_complex_decimal_log_zero(self):
        q = ComplexDecimal(0, 0)
        with self.assertRaises(ValueError):
            q.log()
    
    def test_rational_exp1(self):
        q = Rational(5, 3)
        self.assertAlmostEqual(float(q.exp().re()), exp(5 / 3))
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_rational_exp2(self):
        q = Rational(-5, 3)
        self.assertAlmostEqual(float(q.exp().re()), exp(-5 / 3))
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_rational_exp_zero(self):
        q = Rational(0, 1)
        self.assertAlmostEqual(float(q.exp().re()), 1)
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_complex_rational_exp1(self):
        q = ComplexRational(5, 3, 0, 1)
        self.assertAlmostEqual(float(q.exp().re()), exp(5 / 3))
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_complex_rational_exp2(self):
        q = ComplexRational(-5, 3, 0, 1)
        self.assertAlmostEqual(float(q.exp().re()), exp(-5 / 3))
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_complex_rational_exp3(self):
        q = ComplexRational(0, 1, 1, 1)
        self.assertAlmostEqual(float(q.exp().re()), cos(1))
        self.assertAlmostEqual(float(q.exp().im()), sin(1))
    def test_complex_rational_exp4(self):
        q = ComplexRational(0, 1, -1, 1)
        self.assertAlmostEqual(float(q.exp().re()), cos(1))
        self.assertAlmostEqual(float(q.exp().im()), -sin(1))
    def test_complex_rational_exp5(self):
        q = ComplexRational(1, 1, 2, 1)
        self.assertAlmostEqual(float(q.exp().re()), exp(1) * cos(2))
        self.assertAlmostEqual(float(q.exp().im()), exp(1) * sin(2))
    def test_complex_rational_exp_zero(self):
        q = ComplexRational(0, 1, 0, 1)
        self.assertAlmostEqual(float(q.exp().re()), 1)
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_decimal_exp1(self):
        q = Decimal(1.25)
        self.assertAlmostEqual(float(q.exp().re()), exp(1.25))
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_decimal_exp2(self):
        q = Decimal(-1.25)
        self.assertAlmostEqual(float(q.exp().re()), exp(-1.25))
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_decimal_exp_zero(self):
        q = Decimal(0)
        self.assertAlmostEqual(float(q.exp().re()), 1)
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_complex_decimal_exp1(self):
        q = ComplexDecimal(1.25, 0)
        self.assertAlmostEqual(float(q.exp().re()), exp(1.25))
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_complex_decimal_exp2(self):
        q = ComplexDecimal(-1.25, 0)
        self.assertAlmostEqual(float(q.exp().re()), exp(-1.25))
        self.assertAlmostEqual(float(q.exp().im()), 0)
    def test_complex_decimal_exp3(self):
        q = ComplexDecimal(0, 1)
        self.assertAlmostEqual(float(q.exp().re()), cos(1))
        self.assertAlmostEqual(float(q.exp().im()), sin(1))
    def test_complex_decimal_exp4(self):
        q = ComplexDecimal(0, -1)
        self.assertAlmostEqual(float(q.exp().re()), cos(1))
        self.assertAlmostEqual(float(q.exp().im()), -sin(1))
    def test_complex_decimal_exp5(self):
        q = ComplexDecimal(1, 2)
        self.assertAlmostEqual(float(q.exp().re()), exp(1) * cos(2))
        self.assertAlmostEqual(float(q.exp().im()), exp(1) * sin(2))
    def test_complex_decimal_exp_zero(self):
        q = ComplexDecimal(0, 0)
        self.assertAlmostEqual(float(q.exp().re()), 1)
        self.assertAlmostEqual(float(q.exp().im()), 0)
    
    def test_pow_rational_rational_positive_base_positive_int_exponent(self):
        a = Rational(2, 3)
        b = Rational(2, 1)
        self.assertEqual(a ** b, Rational(4, 9))
    def test_pow_rational_rational_positive_base_negative_int_exponent(self):
        a = Rational(2, 3)
        b = Rational(-2, 1)
        self.assertEqual(a ** b, Rational(9, 4))
    def test_pow_rational_rational_positive_base_zero_exponent(self):
        a = Rational(2, 3)
        b = Rational(0, 1)
        self.assertEqual(a ** b, Rational(1, 1))
    def test_pow_rational_rational_negative_base_positive_int_exponent(self):
        a = Rational(-2, 3)
        b = Rational(3, 1)
        self.assertEqual(a ** b, Rational(-8, 27))
    def test_pow_rational_rational_zero_base_positive_int_exponent(self):
        a = Rational(0, 1)
        b = Rational(2, 1)
        self.assertEqual(a ** b, Rational(0, 1))
    def test_pow_rational_rational_zero_base_zero_exponent(self):
        a = Rational(0, 1)
        b = Rational(0, 1)
        with self.assertRaises(ValueError):
            a ** b
    def test_pow_rational_rational_zero_base_negative_int_exponent(self):
        a = Rational(0, 1)
        b = Rational(-2, 1)
        with self.assertRaises(ValueError):
            a ** b
    def test_pow_rational_rational_positive_base_positive_exponent_rational_result(self):
        a = Rational(4, 9)
        b = Rational(3, 2)
        self.assertEqual(a ** b, Rational(8, 27))
    def test_pow_rational_rational_positive_base_negative_exponent_rational_result(self):
        a = Rational(4, 9)
        b = Rational(-1, 2)
        self.assertEqual(a ** b, Rational(3, 2))
    def test_pow_rational_rational_positive_base_positive_exponent_irrational_numerator(self):
        a = Rational(2, 9)
        b = Rational(3, 2)
        self.assertAlmostEqual(float(a ** b), sqrt(8/729))
    def test_pow_rational_rational_positive_base_negative_exponent_irrational_denominator(self):
        a = Rational(4, 3)
        b = Rational(-1, 2)
        self.assertAlmostEqual(float(a ** b), sqrt(3/4))
    def test_pow_rational_rational_negative_base_positive_exponent_rational_result(self):
        a = Rational(-8, 27)
        b = Rational(1, 3)
        self.assertEqual(a ** b, Rational(-2, 3))
    def test_pow_rational_rational_negative_base_positive_exponent_irrational_result(self):
        a = Rational(-4, 27)
        b = Rational(1, 3)
        self.assertAlmostEqual(float(a ** b), -4**(1/3) / 3)
    def test_pow_rational_rational_negative_base_positive_exponent_imaginary_result(self):
        a = Rational(-1, 1)
        b = Rational(1, 2)
        self.assertAlmostEqual(float((a ** b).re()), 0)
        self.assertAlmostEqual(float((a ** b).im()), 1)
    def test_pow_rational_rational_zero_base_positive_exponent(self):
        a = Rational(0, 1)
        b = Rational(2, 3)
        self.assertEqual(a ** b, Rational(0, 1))
    def test_pow_rational_rational_zero_base_negative_exponent(self):
        a = Rational(0, 1)
        b = Rational(-2, 3)
        with self.assertRaises(ValueError):
            a ** b
    def test_pow_rational_complex_rational_imaginary_exponent(self):
        a = Rational(2, 1)
        b = ComplexRational(1, 1, 2, 1)
        self.assertAlmostEqual(float((a ** b).re()), 2 * cos(log(4)))
        self.assertAlmostEqual(float((a ** b).im()), 2 * sin(log(4)))
    def test_pow_rational_complex_rational_real_exponent(self):
        a = Rational(-8, 27)
        b = ComplexRational(2, 3, 0, 1)
        self.assertEqual(a ** b, Rational(4, 9))
    def test_pow_complex_rational_rational_positive_integer_exponent(self):
        a = ComplexRational(1, 1, 1, 1)
        b = Rational(2, 1)
        self.assertEqual(a ** b, ComplexRational(0, 1, 2, 1))
    def test_pow_complex_rational_rational_zero_exponent(self):
        a = ComplexRational(1, 1, 1, 1)
        b = Rational(0, 1)
        self.assertEqual(a ** b, Rational(1, 1))
    def test_pow_complex_rational_rational_negative_integer_exponent(self):
        a = ComplexRational(1, 1, 1, 1)
        b = Rational(-1, 1)
        self.assertEqual(a ** b, ComplexRational(1, 2, -1, 2))
    def test_pow_complex_rational_rational_rational_exponent(self):
        a = ComplexRational(0, 1, 2, 1)
        b = Rational(3, 2)
        self.assertAlmostEqual(float((a ** b).re()), -2)
        self.assertAlmostEqual(float((a ** b).im()), 2)
    def test_pow_complex_rational_complex_rational_integer_exponent(self):
        a = ComplexRational(1, 1, 1, 1)
        b = ComplexRational(2, 1, 0, 1)
        self.assertEqual(a ** b, ComplexRational(0, 1, 2, 1))
    def test_pow_complex_rational_complex_rational_real_base_rational_exponent(self):
        a = ComplexRational(9, 4, 0, 1)
        b = ComplexRational(3, 2, 0, 1)
        self.assertEqual(a ** b, Rational(27, 8))
    def test_pow_complex_rational_complex_rational_imaginary_exponent(self):
        a = ComplexRational(1, 1, 1, 1)
        b = ComplexRational(2, 1, 3, 1)
        self.assertAlmostEqual(float((a ** b).re()), exp(log(2) - 3/4 * pi) * cos((pi/2) + log(sqrt(8))))
        self.assertAlmostEqual(float((a ** b).im()), exp(log(2) - 3/4 * pi) * sin((pi/2) + log(sqrt(8))))
    def test_pow_rational_decimal(self):
        a = Rational(9, 4)
        b = Decimal(0.5)
        self.assertAlmostEqual(float(a ** b), 1.5)
    def test_pow_rational_complex_decimal(self):
        a = Rational(2, 1)
        b = ComplexDecimal(1, 2)
        self.assertAlmostEqual(float((a ** b).re()), 2 * cos(log(4)))
        self.assertAlmostEqual(float((a ** b).im()), 2 * sin(log(4)))
    def test_pow_complex_rational_decimal(self):
        a = ComplexRational(0, 1, 2, 1)
        b = Decimal(-0.5)
        self.assertAlmostEqual(float((a ** b).re()), 1/2)
        self.assertAlmostEqual(float((a ** b).im()), -1/2)
    def test_pow_complex_rational_complex_decimal(self):
        a = ComplexRational(1, 1, 1, 1)
        b = ComplexDecimal(2, 3)
        self.assertAlmostEqual(float((a ** b).re()), exp(log(2) - 3/4 * pi) * cos((pi/2) + log(sqrt(8))))
        self.assertAlmostEqual(float((a ** b).im()), exp(log(2) - 3/4 * pi) * sin((pi/2) + log(sqrt(8))))
    def test_pow_decimal_decimal(self):
        a = Decimal(2.25)
        b = Decimal(0.5)
        self.assertAlmostEqual(float(a ** b), 1.5)
    def test_pow_decimal_decimal_zero_base_positive_numerator(self):
        a = Decimal(0)
        b = Decimal(1.234)
        self.assertAlmostEqual(float(a ** b), 0)
    def test_pow_decimal_decimal_zero_base_zero_exponent(self):
        a = Decimal(0)
        b = Decimal(0)
        with self.assertRaises(ValueError):
            a ** b
    def test_pow_decimal_decimal_zero_base_negative_exponent(self):
        a = Decimal(0)
        b = Decimal(-2.34)
        with self.assertRaises(ValueError):
            a ** b
    def test_pow_decimal_decimal_negative_base(self):
        a = Decimal(-1)
        b = Decimal(0.5)
        self.assertAlmostEqual(float((a ** b).re()), 0)
        self.assertAlmostEqual(float((a ** b).im()), 1)
    def test_pow_decimal_rational(self):
        a = Decimal(2.25)
        b = Rational(3, 2)
        self.assertAlmostEqual(float(a ** b), 27 / 8)
    def test_pow_decimal_rational_negative_base(self):
        a = Decimal(-27/8)
        b = Rational(1, 3)
        self.assertAlmostEqual(float(a ** b), -3/2)
    def test_pow_decimal_complex_rational(self):
        a = Decimal(exp(1))
        b = ComplexRational(2, 1, 1, 1)
        self.assertAlmostEqual(float((a ** b).re()), exp(2) * cos(1))
        self.assertAlmostEqual(float((a ** b).im()), exp(2) * sin(1))
    def test_pow_decimal_complex_decimal(self):
        a = Decimal(exp(1))
        b = ComplexDecimal(2, pi/2)
        self.assertAlmostEqual(float((a ** b).re()), 0)
        self.assertAlmostEqual(float((a ** b).im()), exp(2))
    def test_pow_complex_decimal_decimal(self):
        a = ComplexDecimal(0, 2)
        b = Decimal(0.5)
        self.assertAlmostEqual(float((a ** b).re()), 1)
        self.assertAlmostEqual(float((a ** b).im()), 1)
    def test_pow_complex_decimal_decimal_zero_base_positive_exponent(self):
        a = ComplexDecimal(0, 0)
        b = Decimal(1.4)
        self.assertAlmostEqual(float(a ** b), 0)
    def test_pow_complex_decimal_decimal_zero_base_zero_exponent(self):
        a = ComplexDecimal(0, 0)
        b = Decimal(0)
        with self.assertRaises(ValueError):
            a ** b
    def test_pow_complex_decimal_decimal_zero_base_negative_exponent(self):
        a = ComplexDecimal(0, 0)
        b = Decimal(-1.4)
        with self.assertRaises(ValueError):
            a ** b
    def test_pow_complex_decimal_rational(self):
        a = ComplexDecimal(0, 2)
        b = Rational(1, 2)
        self.assertAlmostEqual(float((a ** b).re()), 1)
        self.assertAlmostEqual(float((a ** b).im()), 1)
    def test_pow_complex_decimal_rational_negative_base(self):
        a = ComplexDecimal(-8, 0)
        b = Rational(1, 3)
        self.assertAlmostEqual(float(a ** b), -2)
    def test_pow_complex_decimal_complex_rational(self):
        a = ComplexDecimal(0, 2)
        b = ComplexRational(1, 2, -1, 1)
        self.assertAlmostEqual(float((a ** b).re()), sqrt(2) * exp(pi/2) * cos(pi/4 - log(2)))
        self.assertAlmostEqual(float((a ** b).im()), sqrt(2) * exp(pi/2) * sin(pi/4 - log(2)))
    def test_pow_complex_decimal_complex_decimal(self):
        a = ComplexDecimal(0, 2)
        b = ComplexDecimal(0.5, -1)
        self.assertAlmostEqual(float((a ** b).re()), sqrt(2) * exp(pi/2) * cos(pi/4 - log(2)))
        self.assertAlmostEqual(float((a ** b).im()), sqrt(2) * exp(pi/2) * sin(pi/4 - log(2)))

if __name__ == '__main__':
    unittest.main()