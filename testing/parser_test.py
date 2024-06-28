from arithmetic_expression_parser import ExpressionParser, ImplicitMultiplicationError, BracketsMismatchError, EmptyBracketsError, MissingOperandError, UnknownVariableError, UnknownOperatorError
from functionality_database import FunctionalityDatabase
import unittest

class ParserTest(unittest.TestCase):
    def test_process_number_first_token(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = []
        parser.process_number(tokens, '123')
        self.assertListEqual(tokens, ['123'])
    def test_process_number_after_left_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(']
        parser.process_number(tokens, '123')
        self.assertListEqual(tokens, ['(', '123'])
    def test_process_number_after_operator(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['1', '+']
        parser.process_number(tokens, '123')
        self.assertListEqual(tokens, ['1', '+', '123'])
    def test_process_number_after_right_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '1', '+', '2', ')']
        with self.assertRaises(ImplicitMultiplicationError):
            parser.process_number(tokens, '123')
    def test_process_number_after_variable(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['a']
        with self.assertRaises(ImplicitMultiplicationError):
            parser.process_number(tokens, '123')
    def test_process_number_after_number(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['456']
        with self.assertRaises(ImplicitMultiplicationError):
            parser.process_number(tokens, '123')
    
    def test_process_text_first_token(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = []
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['a'])
    def test_process_text_after_number(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['5', ' ', 'a'])
    def test_process_text_after_text(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['x']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['x', ' ', 'a'])
    def test_process_text_after_operator(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5', '*']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['5', '*', 'a'])
    def test_process_text_after_left_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['(', 'a'])
    def test_process_text_after_right_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '5', '+', '5', ')']
        parser.process_text(tokens, 'a', '*')
        self.assertListEqual(tokens, ['(', '5', '+', '5', ')', ' ', 'a'])
    def test_process_text_multiple_vars(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = []
        parser.process_text(tokens, 'abcdefg', '*')
        self.assertListEqual(tokens, ['a', ' ', 'b', ' ', 'c', ' ', 'd', ' ', 'e', ' ', 'f', ' ', 'g'])
    def test_process_text_long_vars(self):
        fd = FunctionalityDatabase()
        fd.constants_trie.append_key('pie', True)
        parser = ExpressionParser(fd)
        tokens = ['5']
        parser.process_text(tokens, 'apidpiefg', '*')
        self.assertListEqual(tokens, ['5', ' ', 'a', ' ', 'pi', ' ', 'd', ' ', 'pie', ' ', 'f', ' ', 'g'])
    def test_process_text_function(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = []
        parser.process_text(tokens, 'sin', '(')
        self.assertListEqual(tokens, ['sin', '()'])
    def test_process_text_vars_and_function(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5']
        parser.process_text(tokens, 'cosin', '(')
        self.assertListEqual(tokens, ['5', ' ', 'c', ' ', 'o', ' ', 'sin', '()'])
    def test_process_text_vars_and_function_ambiguous(self):
        fd = FunctionalityDatabase()
        fd.functions_trie.append_key('nisoc', True)
        parser = ExpressionParser(fd)
        tokens = ['5']
        parser.process_text(tokens, 'cosin', '(')
        self.assertListEqual(tokens, ['5', ' ', 'cosin', '()'])
    def test_process_text_unknown_variable(self):
        fd = FunctionalityDatabase()
        fd.constants_trie['p'].value = None
        parser = ExpressionParser(fd)
        tokens = ['5']
        with self.assertRaises(UnknownVariableError):
            parser.process_text(tokens, 'p', '*')

    def test_process_operator_first_token(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = []
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['+u'])
    def test_process_operator_after_number(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['5', '+'])
    def test_process_operator_after_variable(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['x']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['x', '+'])
    def test_process_operator_after_operator(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5', '+']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['5', '+', '+u'])
    def test_process_operator_after_left_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['(', '+u'])
    def test_process_operator_after_right_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '5', '+', '5', ')']
        parser.process_operator(tokens, '+')
        self.assertListEqual(tokens, ['(', '5', '+', '5', ')', '+'])
    def test_process_operator_long_operator(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5']
        parser.process_operator(tokens, '//')
        self.assertListEqual(tokens, ['5', '//'])
    def test_process_operator_multiple_operators(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5']
        parser.process_operator(tokens, '//-')
        self.assertListEqual(tokens, ['5', '//', '-u'])
    def test_process_operator_unknown_operator(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5']
        with self.assertRaises(UnknownOperatorError):
            parser.process_operator(tokens, '#')
    def test_process_operator_unknown_operator2(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5', '*']
        with self.assertRaises(UnknownOperatorError):
            parser.process_operator(tokens, '*')

    def test_process_left_bracket_first(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = []
        brackets = []
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['('])
        self.assertListEqual(brackets, ['('])
    def test_process_left_bracket_after_operator(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['[', '5', '+']
        brackets = ['[']
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['[', '5', '+', '('])
        self.assertListEqual(brackets, ['[', '('])
    def test_process_left_bracket_after_left_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['[']
        brackets = ['[']
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['[', '('])
        self.assertListEqual(brackets, ['[', '('])
    def test_process_left_bracket_after_number(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['5']
        brackets = []
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['5', ' ', '('])
        self.assertListEqual(brackets, ['('])
    def test_process_left_bracket_after_variable(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['x']
        brackets = []
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['x', ' ', '('])
        self.assertListEqual(brackets, ['('])
    def test_process_left_bracket_after_right_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '5', '+', '5', ')']
        brackets = []
        parser.process_left_bracket(tokens, brackets, '(')
        self.assertListEqual(tokens, ['(', '5', '+', '5', ')', ' ', '('])
        self.assertListEqual(brackets, ['('])
    
    def test_process_right_bracket_first(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = []
        brackets = []
        with self.assertRaises(BracketsMismatchError):
            parser.process_right_bracket(tokens, brackets, ')')
    def test_process_right_bracket_outside_brackets(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '5', '+', '5', ')']
        brackets = []
        with self.assertRaises(BracketsMismatchError):
            parser.process_right_bracket(tokens, brackets, ')')
    def test_process_right_bracket_mismatched_brackets(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '5', '+', '5']
        brackets = ['(']
        with self.assertRaises(BracketsMismatchError):
            parser.process_right_bracket(tokens, brackets, ']')
    def test_process_right_bracket_after_left_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(']
        brackets = ['(']
        with self.assertRaises(EmptyBracketsError):
            parser.process_right_bracket(tokens, brackets, ')')
    def test_process_right_bracket_after_operator(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '5', '+']
        brackets = ['(']
        with self.assertRaises(MissingOperandError):
            parser.process_right_bracket(tokens, brackets, ')')
    def test_process_right_bracket_correct_after_number(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '5', '+', '5']
        brackets = ['(']
        parser.process_right_bracket(tokens, brackets, ')')
        self.assertListEqual(tokens, ['(', '5', '+', '5', ')'])
        self.assertListEqual(brackets, [])
    def test_process_right_bracket_correct_after_variable(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '5', '+', 'a']
        brackets = ['(']
        parser.process_right_bracket(tokens, brackets, ')')
        self.assertListEqual(tokens, ['(', '5', '+', 'a', ')'])
        self.assertListEqual(brackets, [])
    def test_process_right_bracket_correct_after_right_bracket(self):
        parser = ExpressionParser(FunctionalityDatabase())
        tokens = ['(', '(', '4', '*', '(', '5', '+', '5', ')']
        brackets = ['(', '(']
        parser.process_right_bracket(tokens, brackets, ')')
        self.assertListEqual(tokens, ['(', '(', '4', '*', '(', '5', '+', '5', ')', ')'])
        self.assertListEqual(brackets, ['('])

if __name__ == '__main__':
    unittest.main()