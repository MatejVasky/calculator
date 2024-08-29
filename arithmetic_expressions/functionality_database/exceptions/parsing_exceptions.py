class ParsingError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

class InvalidCharacterError(ParsingError):
    def __init__(self):
        super().__init__("an invalid character has been encountered")

class ImplicitMultiplicationError(ParsingError):
    def __init__(self):
        super().__init__("cannot implicitly multiply by a number from the right")

class BracketsMismatchError(ParsingError):
    def __init__(self):
        super().__init__("brackets do not match")

class EmptyBracketsError(ParsingError):
    def __init__(self):
        super().__init__("brackets cannot be empty")

class MissingOperandError(ParsingError):
    def __init__(self):
        super().__init__("operator missing right operand")

class UnknownVariableError(ParsingError):
    def __init__(self, word : str):
        super().__init__(f"cannot parse expression '{word}'")

class UnknownOperatorError(ParsingError):
    def __init__(self, word : str):
        super().__init__(f"cannot parse operator/sequence of operators '{word}'")

class TwoDecimalPointsError(ParsingError):
    def __init__(self):
        super().__init__("number cannot contain two decimal points")

class IsolatedDecimalPointError(ParsingError):
    def __init__(self):
        super().__init__("a decimal point may not occur without digits surrounding it")