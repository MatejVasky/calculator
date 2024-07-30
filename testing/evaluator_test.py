import unittest
from arithmetic_expressions.evaluation import ExpressionEvaluator
from arithmetic_expressions.evaluation.expression_evaluator import OpEntry
from arithmetic_expressions.functionality_database import FunctionalityDatabase, BinaryOperation, PrefixUnaryOperation, Function
from functionality.std import Rational, ComplexRational, Decimal, ComplexDecimal
import functionality.std
import math

class EvaluatorTest(unittest.TestCase):
    def test_process_prefix_unary_operator1(self):
        evaluator = ExpressionEvaluator(create_fd())
        operations = []
        op = PrefixUnaryOperation(1, '+', '+', None)
        evaluator._ExpressionEvaluator__process_prefix_unary_operator(op, operations)
        self.assertEqual(len(operations), 1)
        self.assertEqual(operations[-1].op, op)
        self.assertEqual(operations[-1].priority, 1)
    def test_process_prefix_unary_operator2(self):
        evaluator = ExpressionEvaluator(create_fd())
        op1 = PrefixUnaryOperation(1, '+', '+', None)
        op2 = PrefixUnaryOperation(2, '*', '*', None)
        op3 = PrefixUnaryOperation(3, '^', '^', None)
        operations = [OpEntry(op1, 1), OpEntry(op2, 2)]
        evaluator._ExpressionEvaluator__process_prefix_unary_operator(op3, operations)
        self.assertEqual(len(operations), 3)
        self.assertEqual(operations[-1].op, op3)
        self.assertEqual(operations[-1].priority, 3)
    def test_process_prefix_unary_operator3(self):
        evaluator = ExpressionEvaluator(create_fd())
        op1 = PrefixUnaryOperation(1, '+', '+', None)
        op2 = PrefixUnaryOperation(3, '^', '^', None)
        op3 = PrefixUnaryOperation(2, '*', '*', None)
        operations = [OpEntry(op1, 1), OpEntry(op2, 3)]
        evaluator._ExpressionEvaluator__process_prefix_unary_operator(op3, operations)
        self.assertEqual(len(operations), 3)
        self.assertEqual(operations[-1].op, op3)
        self.assertEqual(operations[-1].priority, 3)
    
    def test_evaluate_top_operation_unary1(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1)]
        results = [Rational(3, 1)]
        evaluator._ExpressionEvaluator__evaluate_top_operation(results, operations)
        self.assertListEqual(operations, [])
        self.assertListEqual(results, [Rational(-3, 1)])
    def test_evaluate_top_operation_unary2(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        op_entry = OpEntry(fd.operations['+'], 1)
        operations = [op_entry, OpEntry(fd.operations['-u'], 1)]
        results = [Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__evaluate_top_operation(results, operations)
        self.assertListEqual(operations, [op_entry])
        self.assertListEqual(results, [Rational(2, 1), Rational(-3, 1)])
    def test_evaluate_top_operation_binary1(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-'], 1)]
        results = [Rational(3, 1), Rational(1, 1)]
        evaluator._ExpressionEvaluator__evaluate_top_operation(results, operations)
        self.assertListEqual(operations, [])
        self.assertEqual(results, [Rational(2, 1)])
    def test_evaluate_top_operation_binary2(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        op_entry = OpEntry(fd.operations['+'], 1)
        operations = [op_entry, OpEntry(fd.operations['//'], 2)]
        results = [Rational(5, 1), Rational(3, 1), Rational(2, 1)]
        evaluator._ExpressionEvaluator__evaluate_top_operation(results, operations)
        self.assertListEqual(operations, [op_entry])
        self.assertEqual(results, [Rational(5, 1), Rational(1, 1)])
    
    def test_process_binary_operator1(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-'], 1)]
        results = [Rational(3, 1), Rational(1, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['+'], results, operations)
        self.assertEqual(len(operations), 1)
        self.assertEqual(operations[-1].op, fd.operations['+'])
        self.assertEqual(operations[-1].priority, 1)
        self.assertListEqual(results, [Rational(2, 1)])
    def test_process_binary_operator2(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-'], 1), OpEntry(fd.operations['*'], 2)]
        results = [Rational(10, 1), Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['+'], results, operations)
        self.assertEqual(len(operations), 1)
        self.assertEqual(operations[-1].op, fd.operations['+'])
        self.assertEqual(operations[-1].priority, 1)
        self.assertListEqual(results, [Rational(4, 1)])
    def test_process_binary_operator3(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-'], 1), OpEntry(fd.operations['*'], 2)]
        results = [Rational(10, 1), Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['/'], results, operations)
        self.assertEqual(len(operations), 2)
        self.assertEqual(operations[0].op, fd.operations['-'])
        self.assertEqual(operations[0].priority, 1)
        self.assertEqual(operations[1].op, fd.operations['/'])
        self.assertEqual(operations[1].priority, 2)
        self.assertListEqual(results, [Rational(10, 1), Rational(6, 1)])
    def test_process_binary_operator4(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-'], 1), OpEntry(fd.operations['*'], 2)]
        results = [Rational(10, 1), Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['()'], results, operations)
        self.assertEqual(len(operations), 3)
        self.assertEqual(operations[0].op, fd.operations['-'])
        self.assertEqual(operations[0].priority, 1)
        self.assertEqual(operations[1].op, fd.operations['*'])
        self.assertEqual(operations[1].priority, 2)
        self.assertEqual(operations[2].op, fd.operations['()'])
        self.assertEqual(operations[2].priority, 3)
        self.assertListEqual(results, [Rational(10, 1), Rational(2, 1), Rational(3, 1)])
    def test_process_binary_operator5(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1)]
        results = [Rational(10, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['*'], results, operations)
        self.assertEqual(len(operations), 2)
        self.assertEqual(operations[0].op, fd.operations['-u'])
        self.assertEqual(operations[0].priority, 1)
        self.assertEqual(operations[1].op, fd.operations['*'])
        self.assertEqual(operations[1].priority, 2)
        self.assertListEqual(results, [Rational(10, 1)])
    def test_process_binary_operator6(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1)]
        results = [Rational(10, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['+'], results, operations)
        self.assertEqual(len(operations), 1)
        self.assertEqual(operations[0].op, fd.operations['+'])
        self.assertEqual(operations[0].priority, 1)
        self.assertListEqual(results, [Rational(-10, 1)])
    def test_process_binary_operator7(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1), OpEntry(fd.operations['*'], 2), OpEntry(fd.operations['-u'], 2)]
        results = [Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['*'], results, operations)
        self.assertEqual(len(operations), 2)
        self.assertEqual(operations[0].op, fd.operations['-u'])
        self.assertEqual(operations[0].priority, 1)
        self.assertEqual(operations[1].op, fd.operations['*'])
        self.assertEqual(operations[1].priority, 2)
        self.assertListEqual(results, [Rational(-6, 1)])
    def test_process_binary_operator8(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1), OpEntry(fd.operations['*'], 2), OpEntry(fd.operations['-u'], 2)]
        results = [Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['+'], results, operations)
        self.assertEqual(len(operations), 1)
        self.assertEqual(operations[0].op, fd.operations['+'])
        self.assertEqual(operations[0].priority, 1)
        self.assertListEqual(results, [Rational(6, 1)])
    def test_process_binary_operator9(self):
        fd = create_fd()
        fd.register_operation(PrefixUnaryOperation(2, '/', '/u', lambda x: x.inv()))
        fd.register_operation(BinaryOperation(3, '**', '^', lambda x, y: Decimal(math.exp(float(y) * math.log(float(x))))))
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1), OpEntry(fd.operations['/u'], 2), OpEntry(fd.operations['-u'], 2), OpEntry(fd.operations['^'], 3), OpEntry(fd.operations['-u'], 3)]
        results = [Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['^'], results, operations)
        self.assertEqual(len(operations), 4)
        self.assertEqual(operations[0].op, fd.operations['-u'])
        self.assertEqual(operations[0].priority, 1)
        self.assertEqual(operations[1].op, fd.operations['/u'])
        self.assertEqual(operations[1].priority, 2)
        self.assertEqual(operations[2].op, fd.operations['-u'])
        self.assertEqual(operations[2].priority, 2)
        self.assertEqual(operations[3].op, fd.operations['^'])
        self.assertEqual(operations[3].priority, 3)
        self.assertEqual(len(results), 1)
        self.assertAlmostEqual(float(results[0]), 0.125)
    def test_process_binary_operator10(self):
        fd = create_fd()
        fd.register_operation(PrefixUnaryOperation(2, '/', '/u', lambda x: x.inv()))
        fd.register_operation(BinaryOperation(3, '**', '^', lambda x, y: Decimal(math.exp(float(y) * math.log(float(x))))))
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1), OpEntry(fd.operations['/u'], 2), OpEntry(fd.operations['-u'], 2), OpEntry(fd.operations['^'], 3), OpEntry(fd.operations['-u'], 3)]
        results = [Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['*'], results, operations)
        self.assertEqual(len(operations), 2)
        self.assertEqual(operations[0].op, fd.operations['-u'])
        self.assertEqual(operations[0].priority, 1)
        self.assertEqual(operations[1].op, fd.operations['*'])
        self.assertEqual(operations[1].priority, 2)
        self.assertEqual(len(results), 1)
        self.assertAlmostEqual(float(results[0]), -8)
    def test_process_binary_operator11(self):
        fd = create_fd()
        fd.register_operation(PrefixUnaryOperation(2, '/', '/u', lambda x: x.inv()))
        fd.register_operation(BinaryOperation(3, '**', '^', lambda x, y: Decimal(math.exp(float(y) * math.log(float(x))))))
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1), OpEntry(fd.operations['/u'], 2), OpEntry(fd.operations['-u'], 2), OpEntry(fd.operations['^'], 3), OpEntry(fd.operations['-u'], 3)]
        results = [Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['+'], results, operations)
        self.assertEqual(len(operations), 1)
        self.assertEqual(operations[0].op, fd.operations['+'])
        self.assertEqual(operations[0].priority, 1)
        self.assertEqual(len(results), 1)
        self.assertAlmostEqual(float(results[0]), 8)
    def test_process_binary_operator12(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1), OpEntry(None, -1), OpEntry(fd.operations['*'], 2)]
        results = [Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_binary_operator(fd.operations['+'], results, operations)
        self.assertEqual(len(operations), 3)
        self.assertEqual(operations[0].op, fd.operations['-u'])
        self.assertEqual(operations[0].priority, 1)
        self.assertEqual(operations[1].op, None)
        self.assertEqual(operations[1].priority, -1)
        self.assertEqual(operations[2].op, fd.operations['+'])
        self.assertEqual(operations[2].priority, 1)
        self.assertListEqual(results, [Rational(6, 1)])

    def test_process_right_bracket1(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(None, -1), OpEntry(fd.operations['*'], 2)]
        results = [Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_right_bracket(results, operations)
        self.assertListEqual(operations, [])
        self.assertListEqual(results, [Rational(6, 1)])
    def test_process_right_bracket2(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        operations = [OpEntry(fd.operations['-u'], 1), OpEntry(None, -1), OpEntry(fd.operations['*'], 2)]
        results = [Rational(2, 1), Rational(3, 1)]
        evaluator._ExpressionEvaluator__process_right_bracket(results, operations)
        self.assertEqual(len(operations), 1)
        self.assertEqual(operations[0].op, fd.operations['-u'])
        self.assertEqual(operations[0].priority, 1)
        self.assertListEqual(results, [Rational(6, 1)])

    def test_evaluate_integer(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertEqual(evaluator.evaluate(['123']), Rational(123, 1))
    def test_evaluate_float(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertEqual(evaluator.evaluate(['12.5']), Decimal(12.5))
    def test_evaluate_constant(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertEqual(evaluator.evaluate(['pi']), Rational(22, 7))
    def test_evaluate_variable(self):
        fd = create_fd()
        fd.constants['a'].set_value(Rational(11, 7))
        evaluator = ExpressionEvaluator(fd)
        self.assertEqual(evaluator.evaluate(['a']), Rational(11, 7))
    def test_evaluate_addition(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertEqual(evaluator.evaluate(['12', '+', '21']), Rational(33, 1))
    def test_evaluate_addition_multiplication(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertEqual(evaluator.evaluate(['12', '+', '3', '*', '2']), Rational(18, 1))
    def test_evaluate_neg(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertEqual(evaluator.evaluate(['-u', '21']), Rational(-21, 1))
    def test_evaluate_addition_multiplication_neg(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertEqual(evaluator.evaluate(['-u', '21', '+', '2', '*', '-u', '3']), Rational(-27, 1))
    def test_evaluate_brackets(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertEqual(evaluator.evaluate(['-u', '(', '5', '+', '3', ')', '*', '2']), Rational(-16, 1))
    def test_evaluate_function(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertAlmostEqual(float(evaluator.evaluate(['sin', '()', '(', 'pi', ')'])), math.sin(22/7))
    def test_evaluate_everything(self):
        fd = create_fd()
        evaluator = ExpressionEvaluator(fd)
        self.assertAlmostEqual(float(evaluator.evaluate(['5', ' ', 'sin', '()', '(', 'pi', '/', '2', ')'])), 5 * math.sin(11/7), places=2)

LETTERS = set([chr(i) for i in range(ord('A'), ord('Z') + 1)] + [chr(i) for i in range(ord('a'), ord('z') + 1)])
DIGITS = set([str(i) for i in range(10)])
PUNCTUATION = set(['+', '-', '*', '/', '%', ','])

def create_fd() -> FunctionalityDatabase:
    fd = FunctionalityDatabase(' ', '()', '(', '.', LETTERS, DIGITS, PUNCTUATION, functionality.std.parse_int, functionality.std.parse_decimal)

    fd.register_operation(BinaryOperation(1, '+', '+', functionality.std.add))
    fd.register_operation(BinaryOperation(1, '-', '-', functionality.std.subtract))
    fd.register_operation(BinaryOperation(2, '*', '*', functionality.std.multiply))
    fd.register_operation(BinaryOperation(2, '/', '/', functionality.std.divide))
    fd.register_operation(BinaryOperation(2, '//', '//', functionality.std.floordivide))
    fd.register_operation(BinaryOperation(2, '%', '%', functionality.std.modulo))
    fd.register_operation(PrefixUnaryOperation(1, '+', '+u', functionality.std.pos))
    fd.register_operation(PrefixUnaryOperation(1, '-', '-u', functionality.std.neg))
    fd.register_operation(BinaryOperation(2, None, ' ', functionality.std.multiply))
    fd.register_operation(BinaryOperation(0, ',', ',', functionality.std.add_parameter))
    fd.register_operation(BinaryOperation(3, None, '()', functionality.std.evaluate_function))

    fd.register_bracket('(', ')')
    fd.register_bracket('[', ']')

    fd.register_constant('pi', Rational(22, 7))
    for i in range(ord('a'), ord('z') + 1):
        fd.register_variable(chr(i))
    for i in range(ord('A'), ord('Z') + 1):
        fd.register_variable(chr(i))
    
    fd.register_function(Function('sin', functionality.std.sin))
    fd.register_function(Function('cos', functionality.std.cos))
    fd.register_function(Function('exp', functionality.std.exp))
    fd.register_function(Function('log', functionality.std.ln))

    return fd

if __name__ == '__main__':
    unittest.main()