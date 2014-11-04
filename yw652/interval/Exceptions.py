class invalidListException(Exception):
    '''
    raised when the list does not follow standard form
    '''
    def __str__(self):
        return "Input string is in an invalid form"
    pass


class invalidIntervalException(Exception):
    '''
    raised when interval is invalid
    '''
    def __str__(self):
        return "Input string contains invalid interval"

    pass


class notOverlappingException(Exception):
    '''
    when not overlapping
    '''
    def __str__(self):
        return "Not overlapping"
    pass


