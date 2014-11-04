class invalidIntervalInputException(Exception):
    """Raised when input string is not interval form"""
    def __str__(self):
        return "Input string is not an interval form!"
    pass


class invalidIntervalException(Exception):
    """Raised when input string represents a null set"""
    def __str__(self):
        return "Input string is not a valid interval"
    pass


class invalidIntervalListInputException(Exception):
    """Raised when input interval list string doesn't have any interval"""
    def __str__(self):
        return "Input string is not a valid interval list"
    pass


class noOverlappingException(Exception):
    """Raised when two intervals are not overlapping"""
    def __str__(self):
        return "Intervals are not overlapping"
    pass
