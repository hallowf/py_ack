

class FunctionNotFound(Exception):
    """Exception to raise when function is not found"""

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
