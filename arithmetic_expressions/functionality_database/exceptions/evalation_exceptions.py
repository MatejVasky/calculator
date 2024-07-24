class EvaluationError(Exception):
    """A base class for evaluation errors"""
    def __init__(self, *args : object):
        super().__init__(*args)

class WrongNumberOfArgumentsError(EvaluationError):
    """An error for when a wrong number of arguments is provided to a function"""
    def __init__(self, *args : object):
        super().__init__(*args)

class UndefinedError(EvaluationError):
    """An error for when a function or an operation is undefined at a given input"""
    def __init__(self, *args : object):
        super().__init__(*args)

class VariableUndefinedError(EvaluationError):
    """An error for when a variable without an assigned value is accessed"""
    def __init__(self):
        super().__init__("variable is undefined")

class ParserError(EvaluationError):
    """An error for when parsing of a token fails"""
    def __init__(self, *args : object):
        super().__init__(*args)

class ParserEvaluationError(EvaluationError):
    """An error for when a parser crashes"""
    def __init__(self, e : Exception):
        super().__init__("a parser failed")
        self.e = e

class FunctionOrOperationEvaluationError(EvaluationError):
    """An error for when an error is raised during function or operation evaluation"""
    def __init__(self, e : Exception):
        super().__init__("an error was raised during function or operation evaluation")
        self.e = e

class InvalidTokensError(EvaluationError):
    """An error for when the list of tokens is invalid"""
    def __init__(self):
        super().__init__("invalid tokens")