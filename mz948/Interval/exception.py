'''
exception.py
This file contains different exceptions. 
'''
class invalidIntervalException(Exception):
    """Raise exception when the input string is not a valid interval."""
    
    def __str__(self):
        return "Input string is not a valid interval"
    pass

class notOverlappingException(Exception):
    """Raise exception when two intervals are not overlapping."""
    
    def __str__(self):
        return "Intervals are not overlapping"
    pass

class invalidIntervalListException(Exception):
    """Raise exception when the input string does not contain any valid interval"""
    def __str__(self):
        return "Input is not a valid interval list"
    pass