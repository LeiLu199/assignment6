class Error(Exception):
    """Base class for exceptions in this module.

    Attributes:
        msg (str): Explanation of the exception.
    
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
    
class NotAnIntervalError(Error):
    """Raised when user input string is not in valid interval form. """
    pass


class InvalidBoundsError(Error):
    """Raised when given interval bounds and bound types represent an empty interval. """
    pass

class NotOverlappingError(Error):
    """Raised when trying to merge two intervals that not overlap. """
    pass
