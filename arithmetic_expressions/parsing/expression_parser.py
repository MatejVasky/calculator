from typing import List
from arithmetic_expressions.functionality_database import FunctionalityDatabase
from arithmetic_expressions.functionality_database.exceptions import ImplicitMultiplicationError, BracketsMismatchError, EmptyBracketsError, MissingOperandError, UnknownVariableError, UnknownOperatorError, TwoDecimalPointsError, IsolatedDecimalPointError

NONE = 0
INT = 1
FLOAT = 2
TEXT = 3
OPERATOR = 4

class ExpressionParser:
    def __init__(self, fd : FunctionalityDatabase):
        self.fd = fd

    def parse_expression(self, expression : str) -> List[str]:
        """Splits a given arithmetic expression into tokens"""
        state = NONE
        word = ''
        prev_word = None
        tokens : List[str] = []
        brackets : List[str] = []

        for c in expression:
            if state == NONE:
                if c == ' ':
                    pass
                elif self.fd.is_letter(c):
                    if prev_word != None:
                        self.process_text(tokens, prev_word, c)
                        prev_word = None
                    word += c
                    state = TEXT
                elif self.fd.is_digit(c):
                    if prev_word != None:
                        self.process_text(tokens, prev_word, c)
                        prev_word = None
                    word += c
                    state = INT
                elif c == self.fd.decimal_point:
                    if prev_word != None:
                        self.process_text(tokens, prev_word, c)
                        prev_word = None
                    word += c
                    state = FLOAT
                elif self.fd.is_punctuation(c):
                    if prev_word != None:
                        self.process_text(tokens, prev_word, c)
                        prev_word = None
                    word += c
                    state = OPERATOR
                elif self.fd.is_left_bracket(c):
                    if prev_word != None:
                        self.process_text(tokens, prev_word, c)
                        prev_word = None
                    self.process_left_bracket(tokens, brackets, c)
                elif self.fd.is_right_bracket(c):
                    if prev_word != None:
                        self.process_text(tokens, prev_word, c)
                        prev_word = None
                    self.process_right_bracket(tokens, brackets, c)
            elif state == INT:
                if c == ' ':
                    pass
                elif self.fd.is_letter(c):
                    self.process_number(tokens, word)
                    word = c
                    state = TEXT
                elif self.fd.is_digit(c):
                    word += c
                elif c == self.fd.decimal_point:
                    word += c
                    state = FLOAT
                elif self.fd.is_punctuation(c):
                    self.process_number(tokens, word)
                    word = c
                    state = OPERATOR
                elif self.fd.is_left_bracket(c):
                    self.process_number(tokens, word)
                    word = ''
                    self.process_left_bracket(tokens, brackets, c)
                    state = NONE
                elif self.fd.is_right_bracket(c):
                    self.process_number(tokens, word)
                    word = ''
                    self.process_right_bracket(tokens, brackets, c)
                    state = NONE
            elif state == FLOAT:
                if c == ' ':
                    pass
                elif self.fd.is_letter(c):
                    self.process_number(tokens, word)
                    word = c
                    state = TEXT
                elif self.fd.is_digit(c):
                    word += c
                elif c == self.fd.decimal_point:
                    raise TwoDecimalPointsError()
                elif self.fd.is_punctuation(c):
                    self.process_number(tokens, word)
                    word = c
                    state = OPERATOR
                elif self.fd.is_left_bracket(c):
                    self.process_number(tokens, word)
                    word = ''
                    self.process_left_bracket(tokens, brackets, c)
                    state = NONE
                elif self.fd.is_right_bracket(c):
                    self.process_number(tokens, word)
                    word = ''
                    self.process_right_bracket(tokens, brackets, c)
                    state = NONE
            elif state == TEXT:
                if c == ' ':
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
                    self.process_text(tokens, word, c)
                    word = c
                    state = OPERATOR
                elif self.fd.is_left_bracket(c):
                    self.process_text(tokens, word, c)
                    word = ''
                    self.process_left_bracket(tokens, brackets, c)
                    state = NONE
                elif self.fd.is_right_bracket(c):
                    self.process_text(tokens, word, c)
                    word = ''
                    self.process_right_bracket(tokens, brackets, c)
                    state = NONE
            elif state == OPERATOR:
                if c == ' ':
                    self.process_operator(tokens, word)
                    word = ''
                    state = NONE
                elif self.fd.is_letter(c):
                    self.process_operator(tokens, word)
                    word = c
                    state = TEXT
                elif self.fd.is_digit(c):
                    self.process_operator(tokens, word)
                    word = c
                    state = INT
                elif c == self.fd.decimal_point:
                    self.process_operator(tokens, word)
                    word = c
                    state = FLOAT
                elif self.fd.is_punctuation(c):
                    word += c
                elif self.fd.is_left_bracket(c):
                    self.process_operator(tokens, word)
                    word = ''
                    self.process_left_bracket(tokens, brackets, c)
                    state = NONE
                elif self.fd.is_right_bracket(c):
                    self.process_operator(tokens, word)
                    word = ''
                    self.process_right_bracket(tokens, brackets, c)
                    state = NONE

        if state == NONE:
            if prev_word != None:
                self.process_text(tokens, prev_word, ' ')
        elif state == INT:
            self.process_number(tokens, word)
        elif state == FLOAT:
            self.process_number(tokens, word)
        elif state == TEXT:
            self.process_text(tokens, word, ' ')
        elif state == OPERATOR:
            raise MissingOperandError()
        
        if len(tokens) != 0 and self.fd.is_operator(tokens[-1]):
            raise MissingOperandError()
        if len(brackets) != 0:
            raise BracketsMismatchError()
        
        return tokens
    
    def process_number(self, tokens : List[str], word : str) -> None:
        """Adds a number (int or float) to tokens"""
        if self.needs_operation(tokens):
            raise ImplicitMultiplicationError()
        if word == self.fd.decimal_point:
            raise IsolatedDecimalPointError()
        tokens.append(word)

    def process_text(self, tokens : List[str], word : str, next_char : str) -> None:
        """Splits sequence of letters into individual tokens and adds them to tokens"""
        # Add implicit multiplication before, if necessary
        if self.needs_operation(tokens):
            tokens.append(self.fd.implicit_operation)

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
                tokens.append(self.fd.implicit_operation)
            token_start = token_end
        
        # Add the function from the end, if necessary
        if func_name != None:
            tokens.append(func_name)
            tokens.append(self.fd.function_application_operator)

    def process_operator(self, tokens : List[str], word : str) -> None:
        """Splits sequence of punctuation into individual operator tokens and adds them to tokens"""
        token_start = 0
        while token_start < len(word):
            if self.needs_operation(tokens): # Look for a binary operator
                token_end, operator = self.fd.bin_operators_trie.find_longest_match(word, start=token_start)
            else: # Look for a prefix unary operator
                token_end, operator = self.fd.pre_un_operators_trie.find_longest_match(word, start=token_start)
            # If operator not found
            if token_start == token_end:
                raise UnknownOperatorError(word)
            # Add operator to tokens
            tokens.append(operator)
            token_start = token_end

    def process_left_bracket(self, tokens : List[str], brackets : List[str], char : str) -> None:
        """Adds a left bracket to tokens"""
        if self.needs_operation(tokens):
            tokens.append(self.fd.implicit_operation)
        tokens.append(char)
        brackets.append(char)

    def process_right_bracket(self, tokens : List[str], brackets : List[str], char : str) -> None:
        """Adds a right bracket to tokens"""
        if len(tokens) == 0 or len(brackets) == 0:
            raise BracketsMismatchError()
        if self.fd.is_left_bracket(tokens[-1]):
            raise EmptyBracketsError()
        if self.fd.is_operator(tokens[-1]):
            raise MissingOperandError()
        if not self.fd.brackets_match(brackets.pop(), char):
            raise BracketsMismatchError()
        tokens.append(char)

    def needs_operation(self, tokens : List[str]) -> bool:
        """Checks if the previous oper"""
        return len(tokens) != 0 \
            and not self.fd.is_left_bracket(tokens[-1]) \
            and not self.fd.is_operator(tokens[-1])
