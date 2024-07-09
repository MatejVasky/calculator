from datastructures import TrieNode

class FunctionalityDatabase:
    def __init__(self):
        self.operations = {'+': None, '-': None, '*': None, '/': None, '//': None, '%': None, '+u': None, '-u': None, ' ': None, ',': None, '()': None}
        self.left_brackets = {'(': None, '[': None}
        self.right_brackets = {')': '(', ']': '['}
        self.implicit_operation = ' '
        self.function_aplication_operator = '()'
        self.function_bracket = '('
        self.decimal_point = '.'

        self.constants_trie : TrieNode[bool] = TrieNode()
        self.constants_trie.append_key('pi', True)
        for i in range(ord('a'), ord('z') + 1):
            self.constants_trie.append_key(chr(i), True)
        for i in range(ord('A'), ord('Z') + 1):
            self.constants_trie.append_key(chr(i), True)

        self.functions_trie : TrieNode[bool] = TrieNode()
        self.functions_trie.append_key('nis', True) # sin
        self.functions_trie.append_key('soc', True) # cos
        self.functions_trie.append_key('pxe', True) # exp
        self.functions_trie.append_key('gol', True) # log

        self.bin_operators_trie : TrieNode[bool] = TrieNode()
        self.bin_operators_trie.append_key('+', '+')
        self.bin_operators_trie.append_key('-', '-')
        self.bin_operators_trie.append_key('*', '*')
        self.bin_operators_trie.append_key('/', '/')
        self.bin_operators_trie.append_key('//', '//')
        self.bin_operators_trie.append_key('%', '%')
        self.bin_operators_trie.append_key(',', ',')

        self.pre_un_operators_trie : TrieNode[str] = TrieNode()
        self.pre_un_operators_trie.append_key('+', '+u')
        self.pre_un_operators_trie.append_key('-', '-u')

    def is_letter(self, c : str) -> bool:
        """Checks if a given character is a letter"""
        return (ord('A') <= ord(c) and ord(c) <= ord('Z')) or \
            (ord('a') <= ord(c) and ord(c) <= ord('z'))

    def is_digit(self, c : str) -> bool:
        """Checks if a given character is a digit"""
        return ord('0') <= ord(c) and ord(c) <= ord('9')

    def is_punctuation(self, c : str) -> bool:
        """Checks if a given character is punctuation"""
        return c in ['+', '-', '*', '/', '%']
    
    def is_operator(self, token : str) -> bool:
        """Checks if a given token is an operator"""
        return token in self.operations
    
    def is_left_bracket(self, c : str) -> bool:
        """Checks if a given character is a left bracket"""
        return c in self.left_brackets
    
    def is_right_bracket(self, c : str) -> bool:
        """Checks if a given character is a right bracket"""
        return c in self.right_brackets
    
    def brackets_match(self, left : str, right : str) -> bool:
        """Checks if brackets match. Returns False if either parameter is not a bracket"""
        if not right in self.right_brackets:
            return False
        return self.right_brackets[right] == left