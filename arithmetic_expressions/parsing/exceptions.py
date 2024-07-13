class ParsingError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class ImplicitMultiplicationError(ParsingError):
    def __init__(self):
        super().__init__("Cannot implicitly multiply by a number from the right")

class BracketsMismatchError(ParsingError):
    def __init__(self):
        super().__init__("Brackets do not match")

class EmptyBracketsError(ParsingError):
    def __init__(self):
        super().__init__("Brackets cannot be empty")

class MissingOperandError(ParsingError):
    def __init__(self):
        super().__init__("Operator missing right operand")

class UnknownVariableError(ParsingError):
    def __init__(self, word : str):
        super().__init__(f"Cannot parse expression '{word}'")

class UnknownOperatorError(ParsingError):
    def __init__(self, word : str):
        super().__init__(f"Cannot parse operator/sequence of operators '{word}'")

class TwoDecimalPointsError(ParsingError):
    def __init__(self):
        super().__init__("Number cannot contain two decimal points")

class IsolatedDecimalPointError(ParsingError):
    def __init__(self):
        super().__init__("A decimal point may not occur without digits surrounding it")