from typing import List
from arithmetic_expressions.functionality_database import FunctionalityDatabase
from arithmetic_expressions.functionality_database.exceptions import ImplicitMultiplicationError, InvalidCharacterError, BracketsMismatchError, EmptyBracketsError, MissingOperandError, UnknownVariableError, UnknownOperatorError, TwoDecimalPointsError, IsolatedDecimalPointError

NONE = 0
INT = 1
FLOAT = 2
TEXT = 3
OPERATOR = 4

class ExpressionParser():
    """A class for splitting arithmetic expressions into tokens"""
    def __init__(self, fd : FunctionalityDatabase):
        """Creates an ExpressionParser. fd specifies the functionality database which should be used during evaluation"""
        # Type check
        if not isinstance(fd, FunctionalityDatabase):
            raise TypeError("fd must be of type FunctionalityDatabase")
        # Assignment
        self.fd = fd

    def parse_expression(self, expression : str) -> List[str]:
        """Splits a given arithmetic expression into tokens"""
        # Type check
        if not isinstance(expression, str):
            raise TypeError("expression must be of type str")
        
        # Variable initialization
        state = NONE
        word = ''
        prev_word = None
        tokens : List[str] = []
        brackets : List[str] = []

        # Main loop (fairly long, because it needs to deal with every (state, character_type) combination)
        for c in expression:
            if state == NONE:
                if self.fd.is_whitespace(c):
                    pass
                elif self.fd.is_letter(c):
                    if prev_word != None:
                        self.__process_text(tokens, prev_word, c)
                        prev_word = None
                    word += c
                    state = TEXT
                elif self.fd.is_digit(c):
                    if prev_word != None:
                        self.__process_text(tokens, prev_word, c)
                        prev_word = None
                    word += c
                    state = INT
                elif c == self.fd.decimal_point:
                    if prev_word != None:
                        self.__process_text(tokens, prev_word, c)
                        prev_word = None
                    word += c
                    state = FLOAT
                elif self.fd.is_punctuation(c):
                    if prev_word != None:
                        self.__process_text(tokens, prev_word, c)
                        prev_word = None
                    word += c
                    state = OPERATOR
                elif self.fd.is_left_bracket(c):
                    if prev_word != None:
                        self.__process_text(tokens, prev_word, c)
                        prev_word = None
                    self.__process_left_bracket(tokens, brackets, c)
                elif self.fd.is_right_bracket(c):
                    if prev_word != None:
                        self.__process_text(tokens, prev_word, c)
                        prev_word = None
                    self.__process_right_bracket(tokens, brackets, c)
                else:
                    raise InvalidCharacterError
            elif state == INT:
                if self.fd.is_whitespace(c):
                    pass
                elif self.fd.is_letter(c):
                    self.__process_number(tokens, word)
                    word = c
                    state = TEXT
                elif self.fd.is_digit(c):
                    word += c
                elif c == self.fd.decimal_point:
                    word += c
                    state = FLOAT
                elif self.fd.is_punctuation(c):
                    self.__process_number(tokens, word)
                    word = c
                    state = OPERATOR
                elif self.fd.is_left_bracket(c):
                    self.__process_number(tokens, word)
                    word = ''
                    self.__process_left_bracket(tokens, brackets, c)
                    state = NONE
                elif self.fd.is_right_bracket(c):
                    self.__process_number(tokens, word)
                    word = ''
                    self.__process_right_bracket(tokens, brackets, c)
                    state = NONE
                else:
                    raise InvalidCharacterError
            elif state == FLOAT:
                if self.fd.is_whitespace(c):
                    pass
                elif self.fd.is_letter(c):
                    self.__process_number(tokens, word)
                    word = c
                    state = TEXT
                elif self.fd.is_digit(c):
                    word += c
                elif c == self.fd.decimal_point:
                    raise TwoDecimalPointsError()
                elif self.fd.is_punctuation(c):
                    self.__process_number(tokens, word)
                    word = c
                    state = OPERATOR
                elif self.fd.is_left_bracket(c):
                    self.__process_number(tokens, word)
                    word = ''
                    self.__process_left_bracket(tokens, brackets, c)
                    state = NONE
                elif self.fd.is_right_bracket(c):
                    self.__process_number(tokens, word)
                    word = ''
                    self.__process_right_bracket(tokens, brackets, c)
                    state = NONE
                else:
                    raise InvalidCharacterError
            elif state == TEXT:
                if self.fd.is_whitespace(c):
                    prev_word = word
                    word = ''
                    state = NONE
                elif self.fd.is_letter(c):
                    word += c
                elif self.fd.is_digit(c):
                    raise ImplicitMultiplicationError()
                elif c == self.fd.decimal_point:
                    raise ImplicitMultiplicationError()
                elif self.fd.is_punctuation(c):
                    self.__process_text(tokens, word, c)
                    word = c
                    state = OPERATOR
                elif self.fd.is_left_bracket(c):
                    self.__process_text(tokens, word, c)
                    word = ''
                    self.__process_left_bracket(tokens, brackets, c)
                    state = NONE
                elif self.fd.is_right_bracket(c):
                    self.__process_text(tokens, word, c)
                    word = ''
                    self.__process_right_bracket(tokens, brackets, c)
                    state = NONE
                else:
                    raise InvalidCharacterError
            elif state == OPERATOR:
                if self.fd.is_whitespace(c):
                    self.__process_operator(tokens, word)
                    word = ''
                    state = NONE
                elif self.fd.is_letter(c):
                    self.__process_operator(tokens, word)
                    word = c
                    state = TEXT
                elif self.fd.is_digit(c):
                    self.__process_operator(tokens, word)
                    word = c
                    state = INT
                elif c == self.fd.decimal_point:
                    self.__process_operator(tokens, word)
                    word = c
                    state = FLOAT
                elif self.fd.is_punctuation(c):
                    word += c
                elif self.fd.is_left_bracket(c):
                    self.__process_operator(tokens, word)
                    word = ''
                    self.__process_left_bracket(tokens, brackets, c)
                    state = NONE
                elif self.fd.is_right_bracket(c):
                    self.__process_operator(tokens, word)
                    word = ''
                    self.__process_right_bracket(tokens, brackets, c)
                    state = NONE
                else:
                    raise InvalidCharacterError

        # Process the final token
        if state == NONE:
            if prev_word != None:
                self.__process_text(tokens, prev_word, ' ')
        elif state == INT:
            self.__process_number(tokens, word)
        elif state == FLOAT:
            self.__process_number(tokens, word)
        elif state == TEXT:
            self.__process_text(tokens, word, ' ')
        elif state == OPERATOR:
            raise MissingOperandError()
        
        # Check if it does not end in an operator
        if len(tokens) != 0 and self.fd.is_operator(tokens[-1]):
            raise MissingOperandError()
        
        # Check if no right brackets are missing
        if len(brackets) != 0:
            raise BracketsMismatchError()
        
        # Return
        return tokens
    
    def __process_number(self, tokens : List[str], word : str) -> None:
        """Adds a number (int or float) to tokens"""
        # If the last token is an operand, raise an error (you cannot implicitly multiply by a number from the right)
        if self.__needs_operation(tokens):
            raise ImplicitMultiplicationError()
        # Check if the literal is not a single decimal point
        if word == self.fd.decimal_point:
            raise IsolatedDecimalPointError()
        # Add to tokens
        tokens.append(word)

    def __process_text(self, tokens : List[str], word : str, next_char : str) -> None:
        """Splits sequence of letters into individual tokens and adds them to tokens"""
        # Add implicit multiplication before, if necessary
        if self.__needs_operation(tokens):
            tokens.append(self.fd.implicit_operator)

        # Find function name, if applicable
        if next_char == self.fd.function_bracket:
            func_name_start, func_name = self.fd.functions_trie.find_longest_match(word, start=len(word) - 1, end=-1, step=-1)
            func_name_start += 1
            # func_name = word[func_name_start:] if (func_name_start < len(word)) else None
        else:
            func_name_start = len(word)
            func_name = None
        
        # Parse the rest of the expression
        token_start = 0
        while token_start < func_name_start:
            # Find variable name
            token_end, token = self.fd.constants_trie.find_longest_match(word, start=token_start, end=func_name_start)
            # If variable not found
            if token_start == token_end:
                raise UnknownVariableError(word)
            # Add variable and implicit multiplication operator, if needed
            tokens.append(token)
            if token_end < len(word):
                tokens.append(self.fd.implicit_operator)
            token_start = token_end
        
        # Add the function from the end, if necessary
        if func_name != None:
            tokens.append(func_name)
            tokens.append(self.fd.function_application_operator)

    def __process_operator(self, tokens : List[str], word : str) -> None:
        """Splits sequence of punctuation into individual operator tokens and adds them to tokens"""
        token_start = 0
        while token_start < len(word):
            if self.__needs_operation(tokens): # Look for a binary operator
                token_end, operator = self.fd.bin_operators_trie.find_longest_match(word, start=token_start)
            else: # Look for a prefix unary operator
                token_end, operator = self.fd.pre_un_operators_trie.find_longest_match(word, start=token_start)
            # If operator not found
            if token_start == token_end:
                raise UnknownOperatorError(word)
            # Add operator to tokens
            tokens.append(operator)
            token_start = token_end

    def __process_left_bracket(self, tokens : List[str], brackets : List[str], char : str) -> None:
        """Adds a left bracket to tokens"""
        # Insert implicit operation if necessary
        if self.__needs_operation(tokens):
            tokens.append(self.fd.implicit_operator)
        # Add to tokens and brackets
        tokens.append(char)
        brackets.append(char)

    def __process_right_bracket(self, tokens : List[str], brackets : List[str], char : str) -> None:
        """Adds a right bracket to tokens"""
        # If missing a left bracket, raise an error
        if len(tokens) == 0 or len(brackets) == 0:
            raise BracketsMismatchError()
        # If there is an empty bracket, raise an error
        if self.fd.is_left_bracket(tokens[-1]):
            raise EmptyBracketsError()
        # If the last operator inside the bracket is missing and operand, raise an error
        if self.fd.is_operator(tokens[-1]):
            raise MissingOperandError()
        # If the bracket does not match with the last opening bracket, raise an error
        if not self.fd.brackets_match(brackets.pop(), char):
            raise BracketsMismatchError()
        # Add to tokens
        tokens.append(char)

    def __needs_operation(self, tokens : List[str]) -> bool:
        """Checks if the previous token is an operand"""
        return len(tokens) != 0 \
            and not self.fd.is_left_bracket(tokens[-1]) \
            and not self.fd.is_operator(tokens[-1])
