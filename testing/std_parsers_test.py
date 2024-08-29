from functionality.std import parse_int, parse_decimal, Rational, Decimal
from arithmetic_expressions.functionality_database.exceptions import ParserError
import unittest

class STDParsersTest(unittest.TestCase):
    def test_parse_int1(self):
        self.assertEqual(parse_int('123'), Rational(123, 1))
    def test_parse_int2(self):
        self.assertEqual(parse_int('0'), Rational(0, 1))
    def test_parse_int_error(self):
        with self.assertRaises(ParserError):
            parse_int('12c')
    
    def test_parse_decimal1(self):
        self.assertEqual(parse_decimal('12.5'), Decimal(12.5))
    def test_parse_decimal2(self):
        self.assertEqual(parse_decimal('0.0'), Decimal(0.0))
    def test_parse_decimal3(self):
        self.assertEqual(parse_decimal('.25'), Decimal(0.25))
    def test_parse_float_error(self):
        with self.assertRaises(ParserError):
            parse_int('12.a')

if __name__ == '__main__':
    unittest.main()