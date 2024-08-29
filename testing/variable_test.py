from arithmetic_expressions.functionality_database import Variable, unpack_variables
from arithmetic_expressions.functionality_database.exceptions import VariableUndefinedError
from functionality.std import Rational
import unittest

class VariableTest(unittest.TestCase):
    def test_init_get(self):
        v = Variable('x', Rational(4, 5))
        self.assertEqual(v.name, 'x')
        self.assertEqual(v.get_value(), Rational(4, 5))
    def test_init_error1(self):
        with self.assertRaises(TypeError):
            Variable(5, Rational(1, 5))
    def test_init_error2(self):
        with self.assertRaises(TypeError):
            Variable('x', 45)
    def test_value_none(self):
        x = Variable('x', None)
        with self.assertRaises(VariableUndefinedError):
            x.get_value()
    def test_set(self):
        v = Variable('x', Rational(4, 5))
        v.set_value(Rational(3, 5))
        self.assertEqual(v.get_value(), Rational(3, 5))
    def test_set_error(self):
        v = Variable('x', Rational(4, 5))
        with self.assertRaises(TypeError):
            v.set_value(35)
    
    def test_no_assignment(self):
        @unpack_variables
        def f(a, b):
            return (a, b)
        res = f(Variable('x', Rational(5, 1)), Rational(4, 3))
        self.assertEqual(res[0], Rational(5, 1))
        self.assertEqual(res[1], Rational(4, 3))

if __name__ == '__main__':
    unittest.main()