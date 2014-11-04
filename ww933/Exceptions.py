__author__ = 'chianti'


'''
If the pattern doesn't match:
                  ( or [, followed by decimal digits, then a ",", then decimal digits, then  ) or ]
IsValidPatternError raises
'''
class IsValidPatternError(Exception):
    pass


'''
If the inclusive lower bound of an interval is bigger than the inclusive upper bound, IsValidIntervalError raises
'''
class IsValidIntervalError(Exception):
    pass



'''
If two intervals can not be merged, CannotMergeTwoIntervalsError raises
'''
class CannotMergeTwoIntervalsError(Exception):
    pass