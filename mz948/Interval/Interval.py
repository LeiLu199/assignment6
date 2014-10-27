import re
from .exception import *
from .utility import *

class interval:
    '''
    Class of interval that represents the range of integers between a lower bound and an upper bound 
    
    Examples: 
    [1,4] represents the numbers 1 through 4 
    (2,5] represents the numbers 3 through 5 
    [4,8) represents the numbers 4 through 7 
    (3,9) represents the numbers 4 through 8
  
    '''
    def __init__(self, interval_string):
        '''
        Constructor of the class interval
        '''
        if isValidInterval(interval_string):            
            self.string = interval_string
            self.lower, self.upper = map(int, interval_string.strip('[] ()').split(','))  
            self.lower_boundType, self.lowerBound, self.real_lowerBound, self.upperBound, self.real_upperBound, self.upper_boundType = parse(interval_string)
        else:
            raise invalidIntervalException()
        
    def __repr__(self):
        return self.string


def mergeIntervals(int1, int2):
    '''
    This function takes two intervals as arguments. If the intervals overlap, it returns a merged interval. 
    If the intervals do not overlap, an exception should be thrown"
    
    Examples: 
    >>> int1 = interval('(5,12)')
    >>> int2 = interval('[2,7]')
    >>> mergeIntervals(int1, int2)
    [2,12)
    '''
    # Establish local variable merged_string
    merged_string = ''

    # Determine whether these two intervals are overlapping ot not. If they are not overlapping, raise exception
    if (int1.real_upperBound < int2.real_lowerBound - 1) or (int2.real_upperBound < int1.real_lowerBound -1):
        raise notOverlappingException()
    else:
        if (int1.real_lowerBound <= int2.real_lowerBound) and (int1.lowerBound <= int2.lowerBound):
            merged_string += int1.lower_boundType + str(int1.lowerBound) + ','
        else:
            merged_string += int2.lower_boundType + str(int2.lowerBound) + ','

        if (int1.real_upperBound >= int2.real_upperBound) and (int1.upperBound >= int2.upperBound):
            merged_string += str(int1.upperBound) + int1.upper_boundType
        else:
            merged_string += str(int2.upperBound) + int2.upper_boundType

    merged_interval = interval(merged_string)

    return merged_interval


def interval_sort(int1,int2):
    '''sort two intervals by their lowerbound'''
    if int1.real_lowerBound > int2.real_lowerBound:
        return 1
    if int2.real_lowerBound > int1.real_lowerBound:
        return -1
    return 0
    
def mergeOverlapping(intlist):
    '''
    This function takes a list of intervals and merges all overlapping intervals.
    
    Example: Given the interval list [1,5], [2,6), (8,10], [8,18], returns [1,6), [8,18].
    '''
#    if not isValidIntervalList(intlist):
 #       raise invalidIntervalListException()
#    else:
    n = len(intlist)
    # sort the intervals
    intlist.sort(key= lambda x: x.lower)

    for i in xrange(0, n - 1): 
        j = i + 1
        try:
            intlist[j] = mergeIntervals(intlist[i], intlist[j])
            intlist[i] = ''
        except:
            pass
    new_intlist = [intlist[i] for i in range(len(intlist)) if intlist[i] != '']
    return new_intlist

def insert(intlist, newint):
    '''
    This function takes two arguments: a list of non- overlapping intervals; and a single interval. 
    The function inserts newint into the intlist and merges the intervals if they are overlapping.
    
    Examples: 
    1. Given intervals [1,3] and [6,9], insert and merge [2,5]. The result will be [1,9].
    2. Given [1,2], (3,5), [6,7), (8,10], [12,16], insert and merge [4,9]. 
       The result will be [1,2], (3,10], [12,16].
    '''
    
    intlist.append(newint)
    return mergeOverlapping(intlist)

