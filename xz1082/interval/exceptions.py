"""
exceptions.py
"""
class invalidIntervalException(Exception):
    '''
    raise when input string is not in an interval form
    '''
    def __str__(self):
        return "Input string is not in an interval form!"
    pass


class noOverlappingException(Exception):
    '''
    raise when two intervals are not overlapping.
    '''
    def __str__(self):
        return "Intervals are not overlapping!"
    pass

class invalidIntervalListException(Exception):
    '''
    raise when input interval list is not in a list of intervals form.
    '''
    def __str__(self):
        return "Input string is not a valid interval list!"
    pass


    


