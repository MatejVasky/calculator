from functionality.std import Rational
from arithmetic_expressions.functionality_database import Parameters
import unittest

class ParametersTest(unittest.TestCase):
    def test_parameters_init_empty(self):
        params = Parameters()
        self.assertTupleEqual(params._Parameters__args, ())
    def test_parameters_init_one_param(self):
        params = Parameters(Rational(1, 2))
        self.assertTupleEqual(params._Parameters__args, (Rational(1, 2),))
    def test_parameters_init_two_params(self):
        params = Parameters(Rational(1, 2), Rational(3, 4))
        self.assertTupleEqual(params._Parameters__args, (Rational(1, 2), Rational(3, 4)))
    def test_parameters_init_error(self):
        with self.assertRaises(TypeError):
            Parameters(Rational(1, 2), 5)
    
    def test_parameters_getitem1(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        self.assertEqual(params[0], Rational(1, 2))
    def test_parameters_getitem2(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        self.assertEqual(params[1], Rational(1, 3))
    def test_parameters_getitem3(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        self.assertEqual(params[2], Rational(1, 4))
    def test_parameters_getitem4(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        self.assertEqual(params[-1], Rational(1, 4))
    def test_parameters_getitem5(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        self.assertEqual(params[-3], Rational(1, 2))
    def test_parameters_getitem_index_error1(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        with self.assertRaises(IndexError):
            params[3]
    def test_parameters_getitem_index_error2(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        with self.assertRaises(IndexError):
            params[-4]
    def test_parameters_getitem_type_error(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        with self.assertRaises(TypeError):
            params['1']
    
    def test_parameters_len1(self):
        params = Parameters()
        self.assertEqual(len(params), 0)
    def test_parameters_len2(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        self.assertEqual(len(params), 3)
    
    def test_parameters_add1(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        params += Rational(1, 5)
        self.assertTupleEqual(params._Parameters__args, (Rational(1, 2), Rational(1, 3), Rational(1, 4), Rational(1, 5)))
    def test_parameters_add2(self):
        params = Parameters()
        params += Rational(1, 5)
        self.assertTupleEqual(params._Parameters__args, (Rational(1, 5),))
    def test_parameters_add_type_error(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        with self.assertRaises(TypeError):
            params + 15
    
    def test_parameters_iter1(self):
        params = Parameters(Rational(1, 2), Rational(1, 3), Rational(1, 4))
        res = []
        for param in params:
            res.append(param)
        self.assertListEqual(res, [Rational(1, 2), Rational(1, 3), Rational(1, 4)])
    def test_parameters_iter2(self):
        params = Parameters()
        res = []
        for param in params:
            res.append(param)
        self.assertListEqual(res, [])

if __name__ == '__main__':
    unittest.main()