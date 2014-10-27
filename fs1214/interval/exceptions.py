'''
Created on Oct 26, 2014

@author: ds-ga-1007
'''
class IntervalInputException(Exception):
    """
    Raise when the input of interval is a invalid form
    """
    def __str__(self):
        return "The input is not an interval! An interval must have: '(' or '[', two integers separated by ',', and ')' or ']'!"
    
class IntervalBoundException(Exception):
    """
    Raise when the real bound of interval is not valid
    """
    def __str__(self):
        return "The interval is invalid! An interval must at least contain one integer!"
    
class IntervalListInputException(Exception):
    """
    Raise when the input of list of intervals is a invalid form
    """
    def __str__(self):
        return "The input is not a valid interval list!"
    
class OverlapplingException(Exception):
    """
    Raise when two intervals are not overlapping
    """
    def __str__(self):
        return "The intervals are not overlapping!"
    
