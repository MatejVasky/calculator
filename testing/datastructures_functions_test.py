import unittest
from datastructures import gcd, pow_by_squaring, get_int_nth_root

class DatastructuresFunctionsTest(unittest.TestCase):
    def test_gcd_two_numbers(self):
        self.assertEqual(gcd(4, 6), 2)
    def test_gcd_coprime_numbers(self):
        self.assertEqual(gcd(5, 6), 1)
    def test_gcd_equal_numbers(self):
        self.assertEqual(gcd(6, 6), 6)
    def test_gcd_multiple(self):
        self.assertEqual(gcd(3, 6), 3)
    def test_gcd_multiple2(self):
        self.assertEqual(gcd(6, 3), 3)
    def test_gcd_zero(self):
        self.assertEqual(gcd(0, 6), 6)
    def test_gcd_two_zeros(self):
        self.assertEqual(gcd(0, 0), 0)
    def test_gcd_negative(self):
        self.assertEqual(gcd(-4, 6), 2)
    def test_gcd_negative2(self):
        self.assertEqual(gcd(4, -6), 2)
    def test_gcd_negative3(self):
        self.assertEqual(gcd(-4, -6), 2)
    def test_gcd_not_int(self):
        with self.assertRaises(TypeError):
            gcd('4', 6)
    def test_gcd_not_int2(self):
        with self.assertRaises(TypeError):
            gcd(4, '6')
    def test_gcd_not_int3(self):
        with self.assertRaises(TypeError):
            gcd('4', '6')
    
    def test_pow_by_squaring_exponent_one(self):
        self.assertEqual(pow_by_squaring(5, 1), 5)
    def test_pow_by_squaring_even_exponent1(self):
        self.assertEqual(pow_by_squaring(5, 2), 25)
    def test_pow_by_squaring_odd_exponent(self):
        self.assertEqual(pow_by_squaring(5, 3), 125)
    def test_pow_by_squaring_bigger_exponent(self):
        self.assertEqual(pow_by_squaring(2, 11), 2048)
    def test_pow_by_squaring_negative_base(self):
        self.assertEqual(pow_by_squaring(-2, 11), -2048)
    def test_pow_by_squaring_exponent_wrong_type(self):
        with self.assertRaises(TypeError):
            pow_by_squaring(5, '1')
    def test_pow_by_squaring_exponent_negative(self):
        with self.assertRaises(ValueError):
            pow_by_squaring(5, -1)
    def test_pow_by_squaring_exponent_zero(self):
        with self.assertRaises(ValueError):
            pow_by_squaring(5, 0)
    def test_pow_by_squaring_not_supporting_mutliplication(self):
        with self.assertRaises(ValueError):
            pow_by_squaring('5', 3)
    
    def test_get_int_nth_root1(self):
        self.assertEqual(get_int_nth_root(1, 4), 4)
    def test_get_int_nth_root2(self):
        self.assertEqual(get_int_nth_root(2, 4), 2)
    def test_get_int_nth_root3(self):
        self.assertEqual(get_int_nth_root(6, 64), 2)
    def test_get_int_nth_root4(self):
        self.assertEqual(get_int_nth_root(3, 64), 4)
    def test_get_int_nth_root_none(self):
        self.assertEqual(get_int_nth_root(3, 4), None)
    def test_get_int_nth_root_zero(self):
        self.assertEqual(get_int_nth_root(3, 0), 0)
    def test_get_int_nth_root_n_not_int(self):
        with self.assertRaises(TypeError):
            get_int_nth_root('1', 4)
    def test_get_int_nth_root_n_negative(self):
        with self.assertRaises(ValueError):
            get_int_nth_root(-1, 4)
    def test_get_int_nth_root_n_zero(self):
        with self.assertRaises(ValueError):
            get_int_nth_root(0, 4)
    def test_get_int_nth_root_x_not_int(self):
        with self.assertRaises(TypeError):
            get_int_nth_root(1, '4')
    def test_get_int_nth_root_x_negative(self):
        with self.assertRaises(ValueError):
            get_int_nth_root(1, -4)

if __name__ == '__main__':
    unittest.main()