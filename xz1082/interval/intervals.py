"""
Intervals.py
"""

import re
from .utility import *
from .exceptions import *

class interval:
    '''
    Define an interval class that represents the range of integers between a lower bound and an upper bound
    Examples: "[1,4]" represents the numbers 1 through 4
          "(2,5]" represents the numbers 3 through 5
          "[4,8)" represents the numbers 4 through 7
          "(3,9)" represents the numbers 4 through 8
    '''
    
    def __init__(self, new_string):
    #takes an user input string - new_string to construct an interval.
        if isvalid_interval(new_string):        
            self.lower_bracket, self.lower, self.upper, self.upper_bracket = parse(new_string)
        else:
            raise invalidIntervalException()
    
    def __repr__(self):
        return self.lower_bracket + str(self.lower) + ', ' + str(self.upper) + self.upper_bracket
    

def mergeIntervals(int1, int2):
    '''
    If two intervals, int1 and int2, overlap, return a merged interval; otherwise, throw an exception.
    Examples:
        >>> int1, int2 = Interval('(1, 5]'), Interval('[3, 8)')
        >>> print mergeIntervals(int1, int2)
       (1, 8)    
    
    '''
    if (int1.upper < int2.lower - 1) or (int2.upper + 1 < int1.lower):
        raise noOverlappingException()
    else:
        lower = min(int1.lower, int2.lower)
        upper = max(int1.upper, int2.upper)
        
        if lower == int1.lower:
            lower_bracket = int1.lower_bracket
        if lower == int2.lower:
            lower_bracket = int2.lower_bracket  
        if upper == int1.upper:
            upper_bracket = int1.upper_bracket
        if upper == int2.upper:
            upper_bracket = int2.upper_bracket  
        
        string = lower_bracket+ '%d,%d' %(lower, upper) + upper_bracket
        mergeInterval = interval(string)
        return mergeInterval


def mergeOverlapping(intlist):
    '''
    Takes a list of intervals and merges all overlapping intervals, returning a new list of merged intervals.

    Example:
    >>> intlist = [interval('[1,5]'), interval('[2,6)'), interval('(8,10]'), interval('[8,18]')]
    >>> mergeOverlapping(intlist)
    [[1,6), [8,18]]
    '''
    #sort the interval list according to their lower bounds. 
    intlist.sort(key = lambda x: x.lower)
    current = intlist[0]        
    merged_list = []
        
    #try to merge the current two intervals, if cannot succeed, append the new interval and continue. 
    for x in range(1,len(intlist)):
        try:
            current = mergeIntervals(current, intlist[x])
        except:
            merged_list.append(current)
            current = intlist[x]
        
    #append the last interval to the merged list
    merged_list.append(current)
    return merged_list


def insert(intlist, newint):
    '''
    Takes two arguments: a list of non-overlapping intervals; and a single interval. Insert newint into intlist and merge the results if necessry. 
    Examples:
        >>> intervals = [Interval('[1, 3]'), Interval('[6, 9]')]
        >>> new_interval = Interval('[2, 5]')
        >>> insert(intervals, new_interval)
        [[1, 9]]    
    '''
    
    intlist.append(newint)    
    newlist = mergeOverlapping(intlist)
    newlist.sort(key = lambda x: x.lower)
    return newlist 


