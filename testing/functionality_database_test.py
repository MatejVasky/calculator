from arithmetic_expressions.functionality_database import FunctionalityDatabase, BinaryOperation, PrefixUnaryOperation, Function, Variable, Value
from arithmetic_expressions.functionality_database.exceptions import ParserError, ParserEvaluationError
from functionality.std import Rational, Decimal
import unittest

WHITESPACE_CHARS = set([' ', '\t', '\r', '\n'])
LETTERS = set([chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)])
DIGITS = set([str(i) for i in range(10)])
PUNCTUATION = set(['+', '-', '*', '/', '%', ','])

class FunctionalityDatabaseTest(unittest.TestCase):
    def test_init(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        self.assertDictEqual(fd.constants, {})
        self.assertEqual(fd.decimal_point, '.')
        self.assertEqual(fd.function_application_operator, '()')
        self.assertEqual(fd.function_bracket, '(')
        self.assertEqual(fd.implicit_operation, ' ')
        self.assertSetEqual(fd.whitespace_chars, WHITESPACE_CHARS)
        self.assertSetEqual(fd.letters, LETTERS)
        self.assertSetEqual(fd.digits, DIGITS)
        self.assertSetEqual(fd.punctuation, PUNCTUATION)
        self.assertDictEqual(fd.left_brackets, {})
        self.assertDictEqual(fd.operations, {})
        self.assertDictEqual(fd.right_brackets, {})
        self.assertEqual(fd._FunctionalityDatabase__parse_int, parse_int)
        self.assertEqual(fd._FunctionalityDatabase__parse_decimal, parse_decimal)
    def test_init_wrong_type1(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(1, '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type2(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', 1, '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type3(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', 1, '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type4(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', '(', 1, WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type5(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', '(', '.', 1, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type6(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, 1, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type7(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, 1, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type8(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, 1, parse_int, parse_decimal)
    def test_init_wrong_type9(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', '(', '.', set([' ', '\t', 3]), LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type10(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, set(['a', 'b', 3]), DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type11(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, set(['0', 1, '2']), PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_type12(self):
        with self.assertRaises(TypeError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, set([',', '+', 2]), parse_int, parse_decimal)
    def test_init_wrong_len1(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', set([' ', '\t\t', '\n']), LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_len2(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, set(['a', 'b', 'cd']), DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_len3(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, set(['0', '12', '2']), PUNCTUATION, parse_int, parse_decimal)
    def test_init_wrong_len4(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, set([',', '+', '+-']), parse_int, parse_decimal)
    def test_init_not_disjoint1(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', set([' ', '\t', 'c']), LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_not_disjoint2(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', set([' ', '9', '\n']), LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_not_disjoint3(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', set(['+', '\t', '\n']), LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_not_disjoint4(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, set(['a', '1', 'c']), DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_not_disjoint5(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, set(['0', '1', '+']), PUNCTUATION, parse_int, parse_decimal)
    def test_init_not_disjoint6(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, set(['a', '+', '+']), parse_int, parse_decimal)
    def test_init_decimal_point_in_whitespace_chars(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', set([' ', '\t', '.']), LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_decimal_point_in_letters(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, set(['a', 'b', '.']), DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_decimal_point_in_digits(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, set(['0', '.', '2']), PUNCTUATION, parse_int, parse_decimal)
    def test_init_decimal_point_in_punctuation(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, set(['.', '+', '-']), parse_int, parse_decimal)
    def test_init_decimal_point_wrong_len(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '...', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_function_bracket_in_whitespace_chars(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', set([' ', '(', '\t']), LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_function_bracket_in_letters(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, set(['a', 'b', '(']), DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_function_bracket_in_digits(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, set(['0', '(', '2']), PUNCTUATION, parse_int, parse_decimal)
    def test_init_function_bracket_in_punctuation(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, set(['(', '+', '-']), parse_int, parse_decimal)
    def test_init_function_bracket_wrong_len(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '(..', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_same_function_bracket_decimal_point(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '()', '.', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_same_function_bracket_implicit_operation(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase('(', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
    def test_init_same_function_bracket_function_application_operator(self):
        with self.assertRaises(ValueError):
            FunctionalityDatabase(' ', '(', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)

    def test_register_operation_binary1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        op = BinaryOperation(1, '+', '+b', [], None)
        fd.register_operation(op)
        self.assertEqual(fd.operations['+b'], op)
        self.assertTupleEqual(fd.bin_operators_trie.find_longest_match('+'), (1, '+b'))
    def test_register_operation_binary2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        op = BinaryOperation(1, None, '+b', [], None)
        fd.register_operation(op)
        self.assertEqual(fd.operations['+b'], op)
    def test_register_operation_prefix_unary1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        op = PrefixUnaryOperation(1, '+', '+u', None)
        fd.register_operation(op)
        self.assertEqual(fd.operations['+u'], op)
        self.assertTupleEqual(fd.pre_un_operators_trie.find_longest_match('+'), (1, '+u'))
    def test_register_operation_prefix_unary2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        op = PrefixUnaryOperation(1, None, '+u', None)
        fd.register_operation(op)
        self.assertEqual(fd.operations['+u'], op)
    def test_register_operation_wrong_type(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(TypeError):
            fd.register_operation(1)
    def test_register_operation_same_symbol1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(BinaryOperation(1, '+', '+b', [], None))
        with self.assertRaises(ValueError):
            fd.register_operation(BinaryOperation(1, '+', '+2', [], None))
    def test_register_operation_same_symbol2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(PrefixUnaryOperation(1, '+', '+u', None))
        fd.register_operation(BinaryOperation(1, '+', '+b', [], None))
        self.assertTrue('+u' in fd.operations)
        self.assertTrue('+b' in fd.operations)
    def test_register_operation_same_symbol3(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(PrefixUnaryOperation(1, '+', '+u', None))
        with self.assertRaises(ValueError):
            fd.register_operation(PrefixUnaryOperation(1, '+', '+2', None))
    def test_register_operation_same_symbol4(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(BinaryOperation(1, '+', '+b', [], None))
        fd.register_operation(PrefixUnaryOperation(1, '+', '+u', None))
        self.assertTrue('+b' in fd.operations)
        self.assertTrue('+u' in fd.operations)
    def test_register_operation_same_token1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(BinaryOperation(1, '+', '+b', [], None))
        with self.assertRaises(ValueError):
            fd.register_operation(BinaryOperation(1, '-', '+b', [], None))
    def test_register_operation_same_token2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(PrefixUnaryOperation(1, '+', '+u', None))
        with self.assertRaises(ValueError):
            fd.register_operation(BinaryOperation(1, '-', '+u', [], None))
    def test_register_operation_same_token3(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_function(Function('f', None))
        with self.assertRaises(ValueError):
            fd.register_operation(BinaryOperation(1, '-', 'f', [], None))
    def test_register_operation_same_token4(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_constant('x', Rational(1, 2))
        with self.assertRaises(ValueError):
            fd.register_operation(BinaryOperation(1, '-', 'x', [], None))
    def test_register_operation_same_token5(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('[', ']')
        with self.assertRaises(ValueError):
            fd.register_operation(BinaryOperation(1, '-', '[', [], None))
    def test_register_operation_same_token6(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('[', ']')
        with self.assertRaises(ValueError):
            fd.register_operation(BinaryOperation(1, '-', ']', [], None))
    def test_register_operation_same_token7(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_operation(BinaryOperation(1, '-', '(', [], None))
    def test_register_operation_bad_symbol(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_operation(PrefixUnaryOperation(1, '-u', '-', None))
    
    def test_register_bracket(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        self.assertEqual(fd.left_brackets['('], None)
        self.assertEqual(fd.right_brackets[')'], '(')
    def test_register_bracket_wrong_type1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(TypeError):
            fd.register_operation(1, ')')
    def test_register_bracket_wrong_type2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(TypeError):
            fd.register_operation('(', 2)
    def test_register_bracket_same_token1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(BinaryOperation(1, '+', '[', [], None))
        with self.assertRaises(ValueError):
            fd.register_bracket('[', ']')
    def test_register_bracket_same_token2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(PrefixUnaryOperation(1, '+', '[', None))
        with self.assertRaises(ValueError):
            fd.register_bracket('[', ']')
    def test_register_bracket_same_token3(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_function(Function('f', None))
        with self.assertRaises(ValueError):
            fd.register_bracket('f', ')')
    def test_register_bracket_same_token4(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_constant('x', Rational(1, 2))
        with self.assertRaises(ValueError):
            fd.register_bracket('x', ')')
    def test_register_bracket_same_token5(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_bracket('(', ']')
    def test_register_bracket_same_token6(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_bracket(')', ']')
    def test_register_bracket_same_token7(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(BinaryOperation(1, '+', '+', [], None))
        with self.assertRaises(ValueError):
            fd.register_bracket('(', '+')
    def test_register_bracket_same_token8(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(PrefixUnaryOperation(1, '+', '+', None))
        with self.assertRaises(ValueError):
            fd.register_bracket('(', '+')
    def test_register_bracket_same_token9(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_function(Function('f', None))
        with self.assertRaises(ValueError):
            fd.register_bracket('(', 'f')
    def test_register_bracket_same_token10(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_constant('x', Rational(1, 2))
        with self.assertRaises(ValueError):
            fd.register_bracket('(', 'x')
    def test_register_bracket_same_token11(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_bracket('[', '(')
    def test_register_bracket_same_token12(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_bracket('[', ')')
    def test_register_bracket_same_token12(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket(']', ']')
    def test_register_bracket_same_token13(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket(' ', ']')
    def test_register_bracket_same_token14(self):
        fd = FunctionalityDatabase(' ', '[', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('[', ']')
    def test_register_bracket_same_token15(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('.', ']')
    def test_register_bracket_same_token16(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('[', ' ')
    def test_register_bracket_same_token17(self):
        fd = FunctionalityDatabase(' ', ']', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('[', ']')
    def test_register_bracket_same_token18(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('[', '.')
    def test_register_bracket_bad_left1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('((', ')')
    def test_register_bracket_bad_left2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('9', ')')
    def test_register_bracket_bad_left3(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('x', ')')
    def test_register_bracket_bad_left4(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('+', ')')
    def test_register_bracket_bad_left5(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('.', ')')
    def test_register_bracket_bad_right1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('(', '))')
    def test_register_bracket_bad_right2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('(', '0')
    def test_register_bracket_bad_right3(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('(', 'x')
    def test_register_bracket_bad_right4(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('(', '+')
    def test_register_bracket_bad_right5(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('(', '.')
    def test_register_bracket_same_left_right(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_bracket('(', '(')
    
    def test_register_constant(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_constant('con', Rational(6, 1))
        self.assertEqual(fd.constants['con'], Rational(6, 1))
        self.assertTupleEqual(fd.constants_trie.find_longest_match('con'), (3, 'con'))
    def test_register_constant_wrong_type1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(TypeError):
            fd.register_constant(1, Rational(5, 1))
    def test_register_constant_wrong_type2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(TypeError):
            fd.register_constant('x', 1)
    def test_register_constant_same_token1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(BinaryOperation(1, '+', 'x', [], None))
        with self.assertRaises(ValueError):
            fd.register_constant('x', Rational(5, 1))
    def test_register_constant_same_token2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(PrefixUnaryOperation(1, '+', 'x', None))
        with self.assertRaises(ValueError):
            fd.register_constant('x', Rational(5, 1))
    def test_register_constant_same_token3(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_function(Function('f', None))
        with self.assertRaises(ValueError):
            fd.register_constant('f', Rational(5, 1))
    def test_register_constant_same_token4(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_constant('x', Rational(1, 2))
        with self.assertRaises(ValueError):
            fd.register_constant('x', Rational(5, 1))
    def test_register_constant_same_token5(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_constant('(', Rational(5, 1))
    def test_register_constant_same_token6(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_constant(')', Rational(5, 1))
    def test_register_constant_same_token7(self):
        fd = FunctionalityDatabase('x', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_constant('x', Rational(5, 1))
    def test_register_constant_same_token8(self):
        fd = FunctionalityDatabase(' ', 'x', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_constant('x', Rational(5, 1))
    def test_register_constant_bad_name(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_constant('x)', Rational(5, 1))

    def test_register_variable(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_variable('var')
        self.assertTrue(isinstance(fd.constants['var'], Variable))
        self.assertTupleEqual(fd.constants_trie.find_longest_match('var'), (3, 'var'))
    def test_register_variable_wrong_type(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(TypeError):
            fd.register_variable(1)
    def test_register_variable_same_token1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(BinaryOperation(1, '+', 'x', [], None))
        with self.assertRaises(ValueError):
            fd.register_variable('x')
    def test_register_variable_same_token2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(PrefixUnaryOperation(1, '+', 'x', None))
        with self.assertRaises(ValueError):
            fd.register_variable('x')
    def test_register_variable_same_token3(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_function(Function('f', None))
        with self.assertRaises(ValueError):
            fd.register_variable('f')
    def test_register_variable_same_token4(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_constant('x', Rational(1, 2))
        with self.assertRaises(ValueError):
            fd.register_variable('x')
    def test_register_variable_same_token5(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_variable('(')
    def test_register_variable_same_token6(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_variable(')')
    def test_register_variable_same_token7(self):
        fd = FunctionalityDatabase('x', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_variable('x')
    def test_register_variable_same_token8(self):
        fd = FunctionalityDatabase(' ', 'x', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_variable('x')
    def test_register_variable_bad_name(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_variable('x)')
    
    def test_register_function(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        f = Function('fun', None)
        fd.register_function(f)
        self.assertEqual(fd.constants['fun'], f)
        self.assertTupleEqual(fd.functions_trie.find_longest_match('nuf'), (3, 'fun'))
    def test_register_function_wrong_type(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(TypeError):
            fd.register_function(1)
    def test_register_function_same_token1(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(BinaryOperation(1, '+', 'f', [], None))
        with self.assertRaises(ValueError):
            fd.register_function(Function('f', None))
    def test_register_function_same_token2(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_operation(PrefixUnaryOperation(1, '+', 'f', None))
        with self.assertRaises(ValueError):
            fd.register_function(Function('f', None))
    def test_register_function_same_token3(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_function(Function('f', None))
        with self.assertRaises(ValueError):
            fd.register_function(Function('f', None))
    def test_register_function_same_token4(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_constant('x', Rational(1, 2))
        with self.assertRaises(ValueError):
            fd.register_function(Function('x', None))
    def test_register_function_same_token5(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_function(Function('(', None))
    def test_register_function_same_token6(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        fd.register_bracket('(', ')')
        with self.assertRaises(ValueError):
            fd.register_function(Function(')', None))
    def test_register_function_same_token7(self):
        fd = FunctionalityDatabase('f', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_function(Function('f', None))
    def test_register_function_same_token8(self):
        fd = FunctionalityDatabase(' ', 'f', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_function(Function('f', None))
    def test_register_function_bad_symbol(self):
        fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)
        with self.assertRaises(ValueError):
            fd.register_function(Function('f(', None))

    def test_is_whitespace_space(self):
        fd = create_fd()
        self.assertTrue(fd.is_whitespace(' '))
    def test_is_whitespace_letter(self):
        fd = create_fd()
        self.assertFalse(fd.is_whitespace('a'))
    def test_is_whitespace_digit(self):
        fd = create_fd()
        self.assertFalse(fd.is_whitespace('5'))
    def test_is_whitespace_comma(self):
        fd = create_fd()
        self.assertFalse(fd.is_whitespace(','))

    def test_is_letter_uppercase_letter(self):
        fd = create_fd()
        self.assertTrue(fd.is_letter('X'))
    def test_is_letter_lowercase_letter(self):
        fd = create_fd()
        self.assertTrue(fd.is_letter('x'))
    def test_is_letter_A(self):
        fd = create_fd()
        self.assertTrue(fd.is_letter('A'))
    def test_is_letter_a(self):
        fd = create_fd()
        self.assertTrue(fd.is_letter('a'))
    def test_is_letter_Z(self):
        fd = create_fd()
        self.assertTrue(fd.is_letter('Z'))
    def test_is_letter_z(self):
        fd = create_fd()
        self.assertTrue(fd.is_letter('z'))
    def test_is_letter_digit(self):
        fd = create_fd()
        self.assertFalse(fd.is_letter('5'))
    def test_is_letter_comma(self):
        fd = create_fd()
        self.assertFalse(fd.is_letter(','))
    def test_is_letter_space(self):
        fd = create_fd()
        self.assertFalse(fd.is_letter(' '))
    
    def test_isdigit_digit(self):
        fd = create_fd()
        self.assertTrue(fd.is_digit('4'))
    def test_isdigit_zero(self):
        fd = create_fd()
        self.assertTrue(fd.is_digit('0'))
    def test_isdigit_nine(self):
        fd = create_fd()
        self.assertTrue(fd.is_digit('9'))
    def test_isdigit_letter(self):
        fd = create_fd()
        self.assertFalse(fd.is_digit('a'))
    def test_isdigit_comma(self):
        fd = create_fd()
        self.assertFalse(fd.is_digit(','))
    def test_isdigit_space(self):
        fd = create_fd()
        self.assertFalse(fd.is_digit(' '))
    
    def test_brackets_match_matching(self):
        fd = create_fd()
        self.assertTrue(fd.brackets_match('(', ')'))
    def test_brackets_match_not_matching(self):
        fd = create_fd()
        self.assertFalse(fd.brackets_match('(', ']'))
    def test_brackets_match_not_a_bracket(self):
        fd = create_fd()
        self.assertFalse(fd.brackets_match('(', '.'))
    
    def test_is_int_true(self):
        fd = create_fd()
        self.assertTrue(fd.is_int('123'))
    def test_is_int_false1(self):
        fd = create_fd()
        self.assertTrue(fd.is_decimal('.123'))
    def test_is_int_false2(self):
        fd = create_fd()
        self.assertTrue(fd.is_decimal('12.3'))

    def test_is_float_true1(self):
        fd = create_fd()
        self.assertTrue(fd.is_decimal('1.23'))
    def test_is_float_true2(self):
        fd = create_fd()
        self.assertTrue(fd.is_decimal('.123'))
    def test_is_float_false1(self):
        fd = create_fd()
        self.assertFalse(fd.is_decimal('123'))
    
    def test_parse_int(self):
        fd = create_fd()
        self.assertEqual(fd.parse_int('123'), Rational(123, 1))
    def test_parse_int_wrong_type(self):
        fd = create_fd()
        with self.assertRaises(TypeError):
            fd.parse_int(0)
    def test_parse_int_parser_error(self):
        fd = create_fd()
        with self.assertRaises(ParserError):
            fd.parse_int('0')
    def test_parse_int_parser_evaluation_error(self):
        fd = create_fd()
        with self.assertRaises(ParserEvaluationError):
            fd.parse_int('a')
    
    def test_parse_decimal(self):
        fd = create_fd()
        self.assertEqual(fd.parse_decimal('1.25'), Decimal(1.25))
    def test_parse_decimal_wrong_type(self):
        fd = create_fd()
        with self.assertRaises(TypeError):
            fd.parse_decimal(0)
    def test_parse_decimal_parser_error(self):
        fd = create_fd()
        with self.assertRaises(ParserError):
            fd.parse_decimal('0.0')
    def test_parse_decimal_parser_evaluation_error(self):
        fd = create_fd()
        with self.assertRaises(ParserEvaluationError):
            fd.parse_decimal('a')

def create_fd() -> FunctionalityDatabase:
    fd = FunctionalityDatabase(' ', '()', '(', '.', WHITESPACE_CHARS, LETTERS, DIGITS, PUNCTUATION, parse_int, parse_decimal)

    fd.register_operation(BinaryOperation(1, '+', '+', [], None))
    fd.register_operation(BinaryOperation(1, '-', '-', [], None))
    fd.register_operation(BinaryOperation(1, '*', '*', [], None))
    fd.register_operation(BinaryOperation(1, '/', '/', [], None))
    fd.register_operation(BinaryOperation(1, '//', '//', [], None))
    fd.register_operation(BinaryOperation(1, '%', '%', [], None))
    fd.register_operation(PrefixUnaryOperation(1, '+', '+u', None))
    fd.register_operation(PrefixUnaryOperation(1, '-', '-u', None))
    fd.register_operation(BinaryOperation(1, None, ' ', ['/', '//', '%'], None))
    fd.register_operation(BinaryOperation(1, ',', ',', [], None))
    fd.register_operation(BinaryOperation(1, None, '()', [], None))

    fd.register_bracket('(', ')')
    fd.register_bracket('[', ']')

    fd.register_constant('pi', Rational(22, 7))
    for i in range(ord('a'), ord('z') + 1):
        fd.register_variable(chr(i))
    for i in range(ord('A'), ord('Z') + 1):
        fd.register_variable(chr(i))
    
    fd.register_function(Function('sin', None))
    fd.register_function(Function('cos', None))
    fd.register_function(Function('exp', None))
    fd.register_function(Function('log', None))

    return fd

def parse_int(token : str) -> Value:
    if token == '0':
        raise ParserError()
    return Rational(int(token), 1)

def parse_decimal(token : str) -> Value:
    if token == '0.0':
        raise ParserError()
    return Decimal(float(token))

if __name__ == '__main__':
    unittest.main()