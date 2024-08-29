from datastructures import TrieNode
from typing import Dict, Callable
from arithmetic_expressions.functionality_database.exceptions import ParserError, ParserEvaluationError
from .value import Value
from .variable import Variable
from .operations import Operation, BinaryOperation, PrefixUnaryOperation
from .function import Function

class FunctionalityDatabase:
    """A database for storing types of characters, functions, operations, constants, etc."""
    def __init__(self, implicit_operation : BinaryOperation, function_application_operation : BinaryOperation, function_bracket_left : str, function_bracket_right : str,
                 decimal_point : str, whitespace_chars : set[str], letters : set[str], digits : set[str], punctuation : set[str],
                 parse_int : Callable[[str], Value], parse_decimal : Callable[[str], Value]):
        """Creates a FunctionalityDatabase.\n
        implicit_operation is inserted between two consecutive operands with no operator between them.\n
        function_application_operation is inserted between a function name and the bracket with its arguments.\n
        function_bracket_left and function_bracket_right specify the type of brackets enclosing arguments of a function (they can be used for other things, if applicable).\n
        decimal_point is used to separate the whole part of a number from its decimal part.\n
        whitespace_chars, letters, digits and punctuation are used to specify different types of characters.\n
        parse_int and parse_decimal are functions for parsing integer and decimal literals."""

        # Check types
        if not isinstance(implicit_operation, BinaryOperation):
            raise TypeError("implicit_operation must be of type str")
        if not isinstance(function_application_operation, BinaryOperation):
            raise TypeError("function_application_operator must be of type str")
        if not isinstance(function_bracket_left, str):
            raise TypeError("function_bracket_left must be of type str")
        if not isinstance(function_bracket_right, str):
            raise TypeError("function_bracket_right must be of type str")
        if not isinstance(decimal_point, str):
            raise TypeError("decimal_point must be of type str")
        if not isinstance(whitespace_chars, set):
            raise TypeError("whitespace_chars must be a set")
        if not isinstance(letters, set):
            raise TypeError("letters must be a set")
        if not isinstance(digits, set):
            raise TypeError("digits must be a set")
        if not isinstance(punctuation, set):
            raise TypeError("punctuation must be a set")
        
        # Check whitespace characters' types, lengths and if they do not appear in letters, digits or punctuation
        for whitespace_char in whitespace_chars:
            if not isinstance(whitespace_char, str):
                raise TypeError("elements of whitespace_chars must be of type str")
            if len(whitespace_char) != 1:
                raise ValueError("elements of whitespace_chars must be of length 1")
            if whitespace_char in letters or whitespace_char in digits or whitespace_char in punctuation:
                raise ValueError("whitespace_chars, letters, digits and punctuation must be disjoint")

        # Check letters' types, lengths and if they do not appear in digits or punctuation
        for letter in letters:
            if not isinstance(letter, str):
                raise TypeError("elements of letters must be of type str")
            if len(letter) != 1:
                raise ValueError("elements of letters must be of length 1")
            if letter in digits or letter in punctuation:
                raise ValueError("whitespace_chars, letters, digits and punctuation must be disjoint")
        
        # Check digits' types, lengths and if they do not appear in punctuation
        for digit in digits:
            if not isinstance(digit, str):
                raise TypeError("elements of digits must be of type str")
            if len(digit) != 1:
                raise ValueError("elements of digits must be of length 1")
            if digit in punctuation:
                raise ValueError("whitespace_chars, letters, digits and punctuation must be disjoint")
        
        # Check whitespace characters' types and lengths
        for c in punctuation:
            if not isinstance(c, str):
                raise TypeError("elements of punctuation must be of type str")
            if len(c) != 1:
                raise ValueError("whitespace_chars, elements of punctuation must be of lengrh 1")

        # Check decimal point's length and if it does not appear in whitespace_chars, letters, digits or punctuation
        if len(decimal_point) != 1:
            raise ValueError("decimal_point must be of length 1")
        if decimal_point in whitespace_chars or decimal_point in letters or decimal_point in digits or decimal_point in punctuation:
            raise ValueError("decimal_point must not be in letters, digits or punctuation")

        # Assign class members
        self.implicit_operator = implicit_operation.token
        self.function_application_operator = function_application_operation.token
        self.function_bracket = function_bracket_left
        self.decimal_point = decimal_point
        self.letters = letters
        self.digits = digits
        self.punctuation = punctuation
        self.whitespace_chars = whitespace_chars
        self.__parse_int = parse_int
        self.__parse_decimal = parse_decimal

        # Create dictionaries
        self.operations : Dict[str, Operation] = {}
        self.constants : Dict[str, Value] = {}
        self.left_brackets : Dict[str, None] = {}
        self.right_brackets : Dict[str, str] = {}
        # Create tries
        self.bin_operators_trie : TrieNode[str] = TrieNode()
        self.pre_un_operators_trie : TrieNode[str] = TrieNode()
        self.constants_trie : TrieNode[str] = TrieNode()
        self.functions_trie : TrieNode[str] = TrieNode()

        # Register the implicit operation, the function application operation and the function brackets
        self.register_operation(implicit_operation)
        self.register_operation(function_application_operation)
        self.register_bracket(function_bracket_left, function_bracket_right)
    
    def register_operation(self, operation : Operation) -> None:
        """Adds the operation to the database"""
        # Check type
        if not isinstance(operation, Operation):
            raise TypeError("operation must be of type Operation")
        
        # Check if token is not taken
        if self.__is_token_registered(operation.token):
            raise ValueError("token already registered")
        
        # Process operation symbol
        if operation.symbol != None:
            # Check if symbol only contains punctuation
            for c in operation.symbol:
                if not self.is_punctuation(c):
                    raise ValueError("operation symbol may only contain punctuation")
            # Register binary operation symbol
            if isinstance(operation, BinaryOperation):
                # Check if symbol is not taken
                if operation.symbol in self.bin_operators_trie:
                    raise ValueError("Symbol already registered")
                # Register
                self.bin_operators_trie.append_key(operation.symbol, operation.token)
            # Register prefix unary operation symbol
            elif isinstance(operation, PrefixUnaryOperation):
                # Check if symbol is not taken
                if operation.symbol in self.pre_un_operators_trie:
                    raise ValueError("Symbol already registered")
                # Register
                self.pre_un_operators_trie.append_key(operation.symbol, operation.token)

        # Register token
        self.operations[operation.token] = operation

    def register_bracket(self, left : str, right : str) -> None:
        """Adds a pair of brackets to the database"""
        # Check type
        if not isinstance(left, str) or not isinstance(right, str):
            raise TypeError("left and right must be of type str")
        
        # Check if token is not taken
        if self.__is_token_registered(left) or self.__is_token_registered(right):
            raise ValueError("Token already registered")
        
        # Check length, if the brackets are different and if they are not in whitespace_chars, letters, digits or punctuation
        if len(left) != 1 or len(right) != 1:
            raise ValueError("left and right must be of length 1")
        if not self.__can_be_bracket(left) or not self.__can_be_bracket(right):
            raise ValueError("left and right must not be a whitespace characters, letters, digits, decimal point or punctuation")
        if left == right:
            raise ValueError("left and right must be different")
        
        # Register
        self.left_brackets[left] = None
        self.right_brackets[right] = left

    def register_constant(self, const_name : str, value : Value) -> None:
        """Adds the constant to the database"""
        # Check types
        if not isinstance(const_name, str) or not isinstance(value, Value):
            raise TypeError("const_name must be of type str and value must be of type Value")
        if len(const_name) == 0:
            raise ValueError("const_name must be of length at least 1")
        
        # Check if token is not taken
        if self.__is_token_registered(const_name):
            raise ValueError("Token already registered")
        
        # Check if the constant name only contains letters
        for c in const_name:
            if not self.is_letter(c):
                raise ValueError("constant name may only contain letters")

        # Register
        self.constants_trie.append_key(const_name, const_name)
        self.constants[const_name] = value
    
    def register_variable(self, variable_name : str) -> None:
        """Adds the variable to the database"""
        self.register_constant(variable_name, Variable(variable_name, None))

    def register_function(self, function : Function) -> None:
        """Adds the function to the database"""
        # Check type
        if not isinstance(function, Function):
            raise TypeError("function must be of type Function")
        
        # Check if token is not taken
        if self.__is_token_registered(function.name):
            raise ValueError("Token already registered")
        
        # Check if the function name only contains letters
        for c in function.name:
            if not self.is_letter(c):
                raise ValueError("function name may only contain letters")
        
        # Register
        self.functions_trie.append_key(function.name[::-1], function.name)
        self.constants[function.name] = function

    def is_whitespace(self, c : str) -> bool:
        """Checks if a given character is a whitespace character"""
        return c in self.whitespace_chars

    def is_letter(self, c : str) -> bool:
        """Checks if a given character is a letter"""
        return c in self.letters

    def is_digit(self, c : str) -> bool:
        """Checks if a given character is a digit"""
        return c in self.digits

    def is_punctuation(self, c : str) -> bool:
        """Checks if a given character is punctuation"""
        return c in self.punctuation
    
    def is_left_bracket(self, c : str) -> bool:
        """Checks if a given character/token is a left bracket"""
        return c in self.left_brackets
    
    def is_right_bracket(self, c : str) -> bool:
        """Checks if a given character/token is a right bracket"""
        return c in self.right_brackets
    
    def is_int(self, token : str) -> bool:
        """Checks if a given token is an integer"""
        # Check type
        if not isinstance(token, str):
            return False
        # Check if all haracters are digits
        for c in token:
            if not c in self.digits:
                return False
        return True
    
    def is_decimal(self, token : str) -> bool:
        """Checks if a given token is a decimal number"""
        # Check type
        if not isinstance(token, str):
            return False
        # Check if it is not a single decimal point
        if token == '.':
            return False
        
        # Check if all haracters are decimal points or digits and count decimal points
        decimal_points = 0
        for c in token:
            # A character is a decimal point
            if c == self.decimal_point:
                # Count the decimal point
                decimal_points += 1
                # Check if there are too many decimal points
                if decimal_points > 1:
                    return False
            # A character is not a decimal point or a digit
            elif not c in self.digits:
                return False
        return decimal_points == 1
    
    def is_constant(self, token : str) -> bool:
        """Checks if a given token is a constant"""
        return token in self.constants

    def is_operator(self, token : str) -> bool:
        """Checks if a given token is an operator"""
        return token in self.operations
    
    def brackets_match(self, left : str, right : str) -> bool:
        """Checks if brackets match. Returns False if either parameter is not a bracket"""
        # Check if right is a bracket
        if not right in self.right_brackets:
            return False
        # Check if left matches right
        return self.right_brackets[right] == left
    
    def parse_int(self, token : str) -> Value:
        """Parses an integer token"""
        # Check type
        if not isinstance(token, str):
            raise TypeError("token must be of type str")
        # Try parsing
        try:
            res = self.__parse_int(token)
        except Exception as e:
            # A ParserError is rethrown
            if isinstance(e, ParserError):
                raise e
            # Other errors cause a ParserEvaluationError
            else:
                raise ParserEvaluationError(e)
        else:
            # Check result type
            if isinstance(res, Value):
                return res
            # If result is not of type Value, throw an error
            else:
                raise ParserEvaluationError(e)
    
    def parse_decimal(self, token : str) -> Value:
        """Parses a decimal token"""
        # Check type
        if not isinstance(token, str):
            raise TypeError("token must be of type str")
        # Try parsing
        try:
            res = self.__parse_decimal(token)
        except Exception as e:
            # A ParserError is rethrown
            if isinstance(e, ParserError):
                raise e
            # Other errors cause a ParserEvaluationError
            else:
                raise ParserEvaluationError(e)
        else:
            # Check result type
            if isinstance(res, Value):
                return res
            # If result is not of type Value, throw an error
            else:
                raise ParserEvaluationError(e)
    
    def __can_be_bracket(self, c : str) -> bool:
        """Checks if a given character can be registered as a bracket. Returns True, if c is not a whitespace character, letter, digit, punctuation or the decimal point"""
        return not self.is_whitespace(c) and not self.is_letter(c) and not c in self.digits and not self.is_punctuation(c) and c != self.decimal_point

    def __is_token_registered(self, token : str) -> bool:
        """Checks if a token is already registered"""
        return token in self.operations or token in self.constants or token in self.left_brackets or token in self.right_brackets or self.is_int(token) or self.is_decimal(token)