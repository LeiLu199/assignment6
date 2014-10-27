"""
utility.py
this file has utility functions for implementing interval class in intervals.py.
"""
import re
from .exceptions import *

def isvalid_interval(user_input):
    '''
    tests if the user's input is in a valid interval form.
    Examples:
      >>> print isvalid_interval('(1, 10]')
      True
      >>> print isvalid_interval('(1, 10]')
      True
      >>> print isvalid_interval('[1, 10')
      False
      >>> print isvalid_interval('interval')
      False
      '''
    #check if input is a string.
    if not isinstance(user_input, str):
        return False
    
    #check if input pattern is valid.
    match = re.search('^\s*[\(\[]\s*\-?\d+\s*,\s*\-?\d+\s*[\)\]]\s*$', user_input)
    if match:
       return True
    else:
       return False
    
    index = ','
    lower = int(user_input[1:index])           
    upper = int(user_input[index+1:-1])
    if lower <= upper:
        return True
    else:
        return False

def parse(string):
    '''
    parse user input string into detailed interval parts.
    return: 
        (lower_bracket, real_lowerBound, real_upperBound, upper_bracket)
    '''

    lower_bracket = string[0]
    upper_bracket = string[-1]

    index = string.index(',')
    
    #split the string by index into lowerbound and upperbound.
    lowerBound = int(string[1:index])
    upperBound = int(string[index+1:-1])

    if lower_bracket == '(':
        real_lowerBound = lowerBound + 1
    else:
        real_lowerBound = lowerBound
    
    if upper_bracket == ')':
        real_upperBound = upperBound - 1
    else:
        real_upperBound = upperBound
        
    return (lower_bracket, real_lowerBound, real_upperBound, upper_bracket)


def isvalid_intervalList(list_input):
    '''
    split the interval list string to different intervals and check if they are all valid.
    '''
    
    if not isinstance(list_input, str):
        return False
        
    form = re.compile('\s*[\(\[]\s*-*\s*\d+\s*,\s*-*\s*\d+\s*[\)\]]\s*')
    match = form.findall(list_input)
    if len(match) > 0:
        return True
    else:
        return False

def parseIntervals(intervals_string):
    '''
    parse user input string of a list of intervals, and return a list of string representations of each interval.
    Examples:
        >>> intervals_rep = ' [-10,-7], (-4,1], [3,6), (8,12), [15,23]'
        >>> parseIntervals(intervals_rep)
        ['[-10,-7]', '(-4,1]', '[3,6)', '(8,12)', '[15,23]']
    '''
    intervals = re.split('(?<=[\]\)])\s*,\s*', intervals_string.strip())
    for interval in intervals:
        if not isvalid_interval(interval):
            raise invalidIntervalException()
    
    return intervals
    
    
    
    
    
    
    
    