class Error(Exception):
    """create a class that has features of Exception base class"""
    def __init__(self, msg):  # constructor that takes in a string as error message
        self.msg = msg

    def __str__(self):
        return self.msg

class invalid_interval_form(Error):
    """Raised when input string is not in interval form. """
    pass


class invalid_interval(Error):
    """Raised when given interval is not a valid interval.. """
    pass

class non_overlapping(Error):
    """Raised when trying to merge two intervals are not overlapping. """
    pass