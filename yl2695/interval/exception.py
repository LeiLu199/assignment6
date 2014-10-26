class InvalidIntervals(Exception):
    '''
    Raise this exception when the interval that the user inputs is valid.
    '''
    pass


class IntervalsNotOverlap(Exception):
    '''
    Raise this exception when the intervals do not overlap.
    '''
    pass
