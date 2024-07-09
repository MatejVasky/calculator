class EvaluationError(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)

class UndefinedError(EvaluationError):
    def __init__(self):
        super().__init__("Operation undefined")

class FunctionOrOperationEvaluationException(EvaluationError):
    """An exception for an error is raised during function or operation evaluation"""
    def __init__(self, e : Exception):
        super().__init__("an error was raised during function or operation evaluation")
        self.e = e