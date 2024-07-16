from arithmetic_expressions.parsing import ExpressionParser
from arithmetic_expressions.functionality_database import FunctionalityDatabase, BinaryOperation, PrefixUnaryOperation, Function
from arithmetic_expressions.functionality_database.exceptions import ImplicitMultiplicationError, BracketsMismatchError, EmptyBracketsError, MissingOperandError, UnknownVariableError, UnknownOperatorError, TwoDecimalPointsError, IsolatedDecimalPointError
from functionality.std import Rational
import unittest

class ParserTest(unittest.TestCase):
    def test_needs_operation_no_tokens(self):
        parser = ExpressionParser(create_fd())
        tokens = []
        self.assertFalse(parser.needs_operation(tokens))
    def test_needs_operation_after_number(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5']
        self.assertTrue(parser.needs_operation(tokens))
    def test_needs_operation_after_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = ['x']
        self.assertTrue(parser.needs_operation(tokens))
    def test_needs_operation_after_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5', '+']
        self.assertFalse(parser.needs_operation(tokens))
    def test_needs_operation_after_left_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(']
        self.assertFalse(parser.needs_operation(tokens))
    def test_needs_operation_after_right_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '5', '+', '5', ')']
        self.assertTrue(parser.needs_operation(tokens))

    def test_process_number_first_token(self):
        parser = ExpressionParser(create_fd())
        tokens = []
        parser.process_number(tokens, '123')
        self.assertListEqual(tokens, ['123'])
    def test_process_number_after_left_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(']
        parser.process_number(tokens, '123')
        self.assertListEqual(tokens, ['(', '123'])
    def test_process_number_after_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = ['1', '+']
        parser.process_number(tokens, '123')
        self.assertListEqual(tokens, ['1', '+', '123'])
    def test_process_number_after_right_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '1', '+', '2', ')']
        with self.assertRaises(ImplicitMultiplicationError):
            parser.process_number(tokens, '123')
    def test_process_number_after_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = ['a']
        with self.assertRaises(ImplicitMultiplicationError):
            parser.process_number(tokens, '123')
    def test_process_number_after_number(self):
        parser = ExpressionParser(create_fd())
        tokens = ['456']
        with self.assertRaises(ImplicitMultiplicationError):
            parser.process_number(tokens, '123')
    def test_process_number_single_decimal_point(self):
        parser = ExpressionParser(create_fd())
        tokens = []
        with self.assertRaises(IsolatedDecimalPointError):
            parser.process_number(tokens, '.')
    
    def test_process_text_first_token(self):
        parser = ExpressionParser(create_fd())
        tokens = []
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['a'])
    def test_process_text_after_number(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['5', ' ', 'a'])
    def test_process_text_after_text(self):
        parser = ExpressionParser(create_fd())
        tokens = ['x']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['x', ' ', 'a'])
    def test_process_text_after_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5', '*']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['5', '*', 'a'])
    def test_process_text_after_left_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['(', 'a'])
    def test_process_text_after_right_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '5', '+', '5', ')']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['(', '5', '+', '5', ')', ' ', 'a'])
    def test_process_text_multiple_vars(self):
        parser = ExpressionParser(create_fd())
        tokens = []
        parser.process_text(tokens, 'abcdefg', '*')
        self.assertListEqual(tokens, ['a', ' ', 'b', ' ', 'c', ' ', 'd', ' ', 'e', ' ', 'f', ' ', 'g'])
    def test_process_text_long_vars(self):
        fd = create_fd()
        fd.register_constant('pie', Rational(7, 22))
        parser = ExpressionParser(fd)
        tokens = ['5']
        parser.process_text(tokens, 'apidpiefg', '*')
        self.assertListEqual(tokens, ['5', ' ', 'a', ' ', 'pi', ' ', 'd', ' ', 'pie', ' ', 'f', ' ', 'g'])
    def test_process_text_function(self):
        parser = ExpressionParser(create_fd())
        tokens = []
        parser.process_text(tokens, 'sin', '(')
        self.assertListEqual(tokens, ['sin', '()'])
    def test_process_text_vars_and_function(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5']
        parser.process_text(tokens, 'cosin', '(')
        self.assertListEqual(tokens, ['5', ' ', 'c', ' ', 'o', ' ', 'sin', '()'])
    def test_process_text_vars_and_function_ambiguous(self):
        fd = create_fd()
        fd.register_function(Function('cosin', None))
        parser = ExpressionParser(fd)
        tokens = ['5']
        parser.process_text(tokens, 'cosin', '(')
        self.assertListEqual(tokens, ['5', ' ', 'cosin', '()'])
    def test_process_text_unknown_variable(self):
        fd = create_fd()
        fd.constants_trie['p'].value = None
        parser = ExpressionParser(fd)
        tokens = ['5']
        with self.assertRaises(UnknownVariableError):
            parser.process_text(tokens, 'p', '*')

    def test_process_operator_first_token(self):
        parser = ExpressionParser(create_fd())
        tokens = []
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['+u'])
    def test_process_operator_after_number(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['5', '+'])
    def test_process_operator_after_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = ['x']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['x', '+'])
    def test_process_operator_after_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5', '+']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['5', '+', '+u'])
    def test_process_operator_after_left_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['(', '+u'])
    def test_process_operator_after_right_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '5', '+', '5', ')']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['(', '5', '+', '5', ')', '+'])
    def test_process_operator_long_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5']
        parser.process_operator(tokens, '//')
        self.assertListEqual(tokens, ['5', '//'])
    def test_process_operator_multiple_operators(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5']
        parser.process_operator(tokens, '//-')
        self.assertListEqual(tokens, ['5', '//', '-u'])
    def test_process_operator_unknown_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5']
        with self.assertRaises(UnknownOperatorError):
            parser.process_operator(tokens, '#')
    def test_process_operator_unknown_operator2(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5', '*']
        with self.assertRaises(UnknownOperatorError):
            parser.process_operator(tokens, '*')

    def test_process_left_bracket_first(self):
        parser = ExpressionParser(create_fd())
        tokens = []
        brackets = []
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['('])
        self.assertListEqual(brackets, ['('])
    def test_process_left_bracket_after_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = ['[', '5', '+']
        brackets = ['[']
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['[', '5', '+', '('])
        self.assertListEqual(brackets, ['[', '('])
    def test_process_left_bracket_after_left_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['[']
        brackets = ['[']
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['[', '('])
        self.assertListEqual(brackets, ['[', '('])
    def test_process_left_bracket_after_number(self):
        parser = ExpressionParser(create_fd())
        tokens = ['5']
        brackets = []
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['5', ' ', '('])
        self.assertListEqual(brackets, ['('])
    def test_process_left_bracket_after_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = ['x']
        brackets = []
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['x', ' ', '('])
        self.assertListEqual(brackets, ['('])
    def test_process_left_bracket_after_right_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '5', '+', '5', ')']
        brackets = []
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['(', '5', '+', '5', ')', ' ', '('])
        self.assertListEqual(brackets, ['('])
    
    def test_process_right_bracket_first(self):
        parser = ExpressionParser(create_fd())
        tokens = []
        brackets = []
        with self.assertRaises(BracketsMismatchError):
            parser.process_right_bracket(tokens, brackets, ')')
    def test_process_right_bracket_outside_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '5', '+', '5', ')']
        brackets = []
        with self.assertRaises(BracketsMismatchError):
            parser.process_right_bracket(tokens, brackets, ')')
    def test_process_right_bracket_mismatched_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '5', '+', '5']
        brackets = ['(']
        with self.assertRaises(BracketsMismatchError):
            parser.process_right_bracket(tokens, brackets, ']')
    def test_process_right_bracket_after_left_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(']
        brackets = ['(']
        with self.assertRaises(EmptyBracketsError):
            parser.process_right_bracket(tokens, brackets, ')')
    def test_process_right_bracket_after_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '5', '+']
        brackets = ['(']
        with self.assertRaises(MissingOperandError):
            parser.process_right_bracket(tokens, brackets, ')')
    def test_process_right_bracket_correct_after_number(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '5', '+', '5']
        brackets = ['(']
        parser.process_right_bracket(tokens, brackets, ')')
        self.assertListEqual(tokens, ['(', '5', '+', '5', ')'])
        self.assertListEqual(brackets, [])
    def test_process_right_bracket_correct_after_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '5', '+', 'a']
        brackets = ['(']
        parser.process_right_bracket(tokens, brackets, ')')
        self.assertListEqual(tokens, ['(', '5', '+', 'a', ')'])
        self.assertListEqual(brackets, [])
    def test_process_right_bracket_correct_after_right_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = ['(', '(', '4', '*', '(', '5', '+', '5', ')']
        brackets = ['(', '(']
        parser.process_right_bracket(tokens, brackets, ')')
        self.assertListEqual(tokens, ['(', '(', '4', '*', '(', '5', '+', '5', ')', ')'])
        self.assertListEqual(brackets, ['('])
    
    def test_parse_expression_empty(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('')
        self.assertListEqual(tokens, [])
    def test_parse_expression_whitespace(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('    ')
        self.assertListEqual(tokens, [])
    def test_parse_expression_int(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('123')
        self.assertListEqual(tokens, ['123'])
    def test_parse_expression_float(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('12.3')
        self.assertListEqual(tokens, ['12.3'])
    def test_parse_expression_float2(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('.123')
        self.assertListEqual(tokens, ['.123'])
    def test_parse_expression_two_decimal_points(self):
        parser = ExpressionParser(create_fd())
        with self.assertRaises(TwoDecimalPointsError):
            parser.parse_expression('1.2.3')
    def test_parse_expression_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('x')
        self.assertListEqual(tokens, ['x'])
    def test_parse_expression_multiple_variables(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('xyz')
        self.assertListEqual(tokens, ['x', ' ', 'y', ' ', 'z'])
    def test_parse_expression_number_with_spaces(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('500 000 000.000 001')
        self.assertListEqual(tokens, ['500000000.000001'])
    def test_parse_expression_variables_with_spaces(self):
        fd = create_fd()
        fd.register_constant('pie', Rational(7, 22))
        parser = ExpressionParser(fd)
        tokens = parser.parse_expression('xpi e')
        self.assertListEqual(tokens, ['x', ' ', 'pi', ' ', 'e'])
    def test_parse_expression_int_and_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('5x')
        self.assertListEqual(tokens, ['5', ' ', 'x'])
    def test_parse_expression_float_with_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('5.2x')
        self.assertListEqual(tokens, ['5.2', ' ', 'x'])
    def test_parse_expression_variable_with_int(self):
        parser = ExpressionParser(create_fd())
        with self.assertRaises(ImplicitMultiplicationError):
            parser.parse_expression('x2')
    def test_parse_expression_variable_with_int(self):
        parser = ExpressionParser(create_fd())
        with self.assertRaises(ImplicitMultiplicationError):
            parser.parse_expression('x.4')
    def test_parse_expression_int_and_spaces(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('1   ')
        self.assertListEqual(tokens, ['1'])
    def test_parse_expression_float_and_spaces(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('2.4   ')
        self.assertListEqual(tokens, ['2.4'])
    def test_parse_expression_variable_and_spaces(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('x   ')
        self.assertListEqual(tokens, ['x'])
    def test_parse_expression_operator_and_int(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('+5')
        self.assertListEqual(tokens, ['+u', '5'])
    def test_parse_expression_operator_and_float(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('+5.4')
        self.assertListEqual(tokens, ['+u', '5.4'])
    def test_parse_expression_operator_and_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('+x')
        self.assertListEqual(tokens, ['+u', 'x'])
    def test_parse_expression_ints_and_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('1+2')
        self.assertListEqual(tokens, ['1', '+', '2'])
    def test_parse_expression_floats_and_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('1.4+2.5')
        self.assertListEqual(tokens, ['1.4', '+', '2.5'])
    def test_parse_expression_variables_and_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('x+y')
        self.assertListEqual(tokens, ['x', '+', 'y'])
    def test_parse_expression_ints_and_operator_with_spaces(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression(' 1  + 2 ')
        self.assertListEqual(tokens, ['1', '+', '2'])
    def test_parse_expression_floats_and_operator_with_spaces(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression(' 1.2  + 2.3 ')
        self.assertListEqual(tokens, ['1.2', '+', '2.3'])
    def test_parse_expression_variabless_and_operator_with_spaces(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression(' x  + t ')
        self.assertListEqual(tokens, ['x', '+', 't'])
    def test_parse_expression_multiple_variables_numbers_and_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('xpi+2')
        self.assertListEqual(tokens, ['x', ' ', 'pi', '+', '2'])
    def test_parse_expression_multiple_operators(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('1*-2')
        self.assertListEqual(tokens, ['1', '*', '-u', '2'])
    def test_parse_expression_long_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('1//2')
        self.assertListEqual(tokens, ['1', '//', '2'])
    def test_parse_expression_multiple_operators_with_spaces(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('1 * -2')
        self.assertListEqual(tokens, ['1', '*', '-u', '2'])
    def test_parse_expression_in_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('(1*-2)')
        self.assertListEqual(tokens, ['(', '1', '*', '-u', '2', ')'])
    def test_parse_expression_ints_and_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('2(3+4)')
        self.assertListEqual(tokens, ['2', ' ', '(', '3', '+', '4', ')'])
    def test_parse_expression_floats_and_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('2.3(3.3+4.3)')
        self.assertListEqual(tokens, ['2.3', ' ', '(', '3.3', '+', '4.3', ')'])
    def test_parse_expression_variables_and_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('x(y+z)')
        self.assertListEqual(tokens, ['x', ' ', '(', 'y', '+', 'z', ')'])
    def test_parse_expression_function(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('sin(y+z)')
        self.assertListEqual(tokens, ['sin', '()', '(', 'y', '+', 'z', ')'])
    def test_parse_expression_variables_functions_and_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('xsin(y+z)')
        self.assertListEqual(tokens, ['x', ' ', 'sin', '()', '(', 'y', '+', 'z', ')'])
    def test_parse_expression_variables_no_function(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('(y+sin)')
        self.assertListEqual(tokens, ['(', 'y', '+', 's', ' ', 'i', ' ', 'n', ')'])
    def test_parse_expression_unary_operator_and_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('+(3+4)')
        self.assertListEqual(tokens, ['+u', '(', '3', '+', '4', ')'])
    def test_parse_expression_binary_operator_and_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('2//(3+4)')
        self.assertListEqual(tokens, ['2', '//', '(', '3', '+', '4', ')'])
    def test_parse_expression_multiple_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('(2-2)(3+4)')
        self.assertListEqual(tokens, ['(', '2', '-', '2', ')', ' ', '(', '3', '+', '4', ')'])
    def test_parse_expression_brackets_inside_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('((2-2+3)+4)')
        self.assertListEqual(tokens, ['(', '(', '2', '-', '2', '+', '3', ')', '+', '4', ')'])
    def test_parse_expression_double_brackets(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('((2-2+3+4))')
        self.assertListEqual(tokens, ['(', '(', '2', '-', '2', '+', '3', '+', '4', ')', ')'])
    def test_parse_expression_brackets_with_spaces(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression(' ( ( 2 - 2 + 3 ) + 4 ) ')
        self.assertListEqual(tokens, ['(', '(', '2', '-', '2', '+', '3', ')', '+', '4', ')'])
    def test_parse_expression_right_bracket_and_int(self):
        parser = ExpressionParser(create_fd())
        with self.assertRaises(ImplicitMultiplicationError):
            parser.parse_expression('(3+3)2')
    def test_parse_expression_right_bracket_and_float(self):
        parser = ExpressionParser(create_fd())
        with self.assertRaises(ImplicitMultiplicationError):
            parser.parse_expression('(3+3).2')
    def test_parse_expression_right_bracket_and_variable(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('(3+3)x')
        self.assertListEqual(tokens, ['(', '3', '+', '3', ')', ' ', 'x'])
    def test_parse_expression_right_bracket_and_operator(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('(3+3)+5')
        self.assertListEqual(tokens, ['(', '3', '+', '3', ')', '+', '5'])
    def test_parse_expression_right_bracket_and_left_bracket(self):
        parser = ExpressionParser(create_fd())
        tokens = parser.parse_expression('(3+3)(x)')
        self.assertListEqual(tokens, ['(', '3', '+', '3', ')', ' ', '(', 'x', ')'])
    def test_parse_expression_operator_at_the_end(self):
        parser = ExpressionParser(create_fd())
        with self.assertRaises(MissingOperandError):
            parser.parse_expression('x*3+')
    def test_parse_expression_operator_at_the_end_with_spaces(self):
        parser = ExpressionParser(create_fd())
        with self.assertRaises(MissingOperandError):
            parser.parse_expression('x*3+  ')
    def test_parse_expression_unclosed_brackets(self):
        parser = ExpressionParser(create_fd())
        with self.assertRaises(BracketsMismatchError):
            parser.parse_expression('(x+y')
    def test_parse_expression_unclosed_brackets2(self):
        parser = ExpressionParser(create_fd())
        with self.assertRaises(BracketsMismatchError):
            parser.parse_expression('((x+y)  ')

LETTERS = set([chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)])
DIGITS = set([str(i) for i in range(10)])
PUNCTUATION = set(['+', '-', '*', '/', '%', ','])

def create_fd() -> FunctionalityDatabase:
    fd = FunctionalityDatabase(' ', '()', '(', '.', LETTERS, DIGITS, PUNCTUATION)

    fd.register_operation(BinaryOperation(1, '+', '+', None))
    fd.register_operation(BinaryOperation(1, '-', '-', None))
    fd.register_operation(BinaryOperation(1, '*', '*', None))
    fd.register_operation(BinaryOperation(1, '/', '/', None))
    fd.register_operation(BinaryOperation(1, '//', '//', None))
    fd.register_operation(BinaryOperation(1, '%', '%', None))
    fd.register_operation(PrefixUnaryOperation(1, '+', '+u', None))
    fd.register_operation(PrefixUnaryOperation(1, '-', '-u', None))
    fd.register_operation(BinaryOperation(1, None, ' ', None))
    fd.register_operation(BinaryOperation(1, ',', ',', None))
    fd.register_operation(BinaryOperation(1, None, '()', None))

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

if __name__ == '__main__':
    unittest.main()