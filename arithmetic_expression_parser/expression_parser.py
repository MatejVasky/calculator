from typing import List
from functionality_database import FunctionalityDatabase
from .exceptions import ImplicitMultiplicationError, BracketsMismatchError, EmptyBracketsError, MissingOperandError, UnknownVariableError, UnknownOperatorError

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
                pass
            elif state == INT:
                pass
            elif state == FLOAT:
                pass
            elif state == TEXT:
                pass
            elif state == OPERATOR:
                pass
    
    def process_number(self, tokens : List[str], word : str) -> None:
        """Adds a number (int or float) to tokens"""
        if self.needs_operation(tokens):
            raise ImplicitMultiplicationError()
        tokens.append(word)

    def process_text(self, tokens : List[str], word : str, next_char : str) -> None:
        """Splits sequence of letters into individual tokens and adds them to tokens"""
        # Add implicit multiplication before, if necessary
        if self.needs_operation(tokens):
            tokens.append(self.fd.implicit_operation)

        # Find function name, if applicable
        if next_char == self.fd.function_bracket:
            func_name_start = self.fd.functions_trie.find_longest_match(word, start=len(word) - 1, end=-1, step=-1)[0] + 1
            func_name = word[func_name_start:] if (func_name_start < len(word)) else None
        else:
            func_name_start = len(word)
            func_name = None
        
        # Parse the rest of the expression
        token_start = 0
        while token_start < func_name_start:
            # Find variable name
            token_end, _ = self.fd.constants_trie.find_longest_match(word, start=token_start, end=func_name_start)
            # If variable not found
            if token_start == token_end:
                raise UnknownVariableError(word)
            # Add variable and implicit multiplication operator, if needed
            tokens.append(word[token_start:token_end])
            if token_end < len(word):
                tokens.append(self.fd.implicit_operation)
            token_start = token_end
        
        # Add the function from the end, if necessary
        if func_name != None:
            tokens.append(func_name)
            tokens.append(self.fd.function_aplication_operator)

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
