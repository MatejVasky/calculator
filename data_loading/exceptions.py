class FunctionalityLoadingException(Exception):
    """An exception for when functionality fails to load"""
    def __init__(self, *args):
        super().__init__(*args)