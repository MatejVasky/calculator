import unittest
from datastructures import gcd

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

if __name__ == '__main__':
    unittest.main()