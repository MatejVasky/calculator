class ImplicitMultiplicationError(Exception):
    def __init__(self):
        super().__init__("Cannot implicitly multiply by a number from the right")

class BracketsMismatchError(Exception):
    def __init__(self):
        super().__init__("Brackets do not match")

class EmptyBracketsError(Exception):
    def __init__(self):
        super().__init__("Brackets cannot be empty")

class InvalidOperatorError(Exception):
    def __init__(self):
        super().__init__("Invalid operator")

class MissingOperandError(Exception):
    def __init__(self):
        super().__init__("Operator missing right operand")

class UnknownVariableError(Exception):
    def __init__(self, word : str):
        super().__init__(f"Cannot parse expression '{word}'")

class UnknownOperatorError(Exception):
    def __init__(self, word : str):
        super().__init__(f"Cannot parse operator/sequence of operators '{word}'")