'''

Classes for custom excpetions for interval class

'''



class invalidIntervalError(Exception):
    # error for invalid intervals, gets raised when the interval does not make sense
    pass

class disjointIntervalsError(Exception):
    # raised by mergeInterval() for disjoint intervals, caught in merge list
    pass

class intervalError(Exception):
    pass