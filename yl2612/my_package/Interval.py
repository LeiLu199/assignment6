from Exceptions import *
from NewIntervalFunctions import *

class interval(object):
    '''
    This class handle the range of integers between a lower bound and an upper bound
    
    '''
    def __init__(self,interval_string):
        '''
        Construct an interval object given a string representing an integer interval.
        If interval_string is not a valid interval, raise exception.
        '''
        if isValidInterval(interval_string):
            self.interval_string = interval_string
            self.left, self.right, self.lower, self.upper = splitIntervalString(interval_string)
            self.lower_inclusive, self.upper_inclusive = getTrueValue(self.left, self.right, self.lower, self.upper)
            self.left_inclusive = True if self.left == '[' else False
            self.right_inclusive = True if self.right == ']' else False
        else:
            raise invalidInterval('The interval is invalid.')
   
    def __repr__(self):
        return self.interval_string


def mergeIntervals(int1,int2):
    '''
    merge two intervals if they overlap, or an exception will be thrown
    '''
    if int1.lower_inclusive > int2.upper_inclusive +1 or int1.upper_inclusive < int2.lower_inclusive -1:
        raise notOverlappingException('Intervals do not overlap.')
    else:
        if int1.lower_inclusive < int2.lower_inclusive:
            merge_left = int1.left 
            merge_lower = int1.lower
        elif int1.lower_inclusive == int2.lower_inclusive:
            merge_left = int1.left if int1.lower==int2.lower else '('
            merge_lower=min(int1.lower, int2.lower)
        else:
            merge_left = int2.left
            merge_lower = int2.lower
        if int1.upper_inclusive < int2.upper_inclusive:
            merge_right = int2.right
            merge_upper = int2.upper
        elif int1.upper_inclusive == int2.upper_inclusive:
            merge_right = int1.right if int1.upper==int2.upper else ')'
            merge_upper = max(int1.upper, int2.upper)
        else:
            merge_right = int1.right
            merge_upper = int1.upper
        merge_string = ''
        merge_string = merge_left + str(merge_lower) + ',' + str(merge_upper) + merge_right
        new_interval = interval(merge_string)
        return new_interval

def  mergeOverlapping(intlist):
    '''
    merge all overlapping intervals
    '''
    sorted_list = sorted(intlist, key=lambda x: x.lower)
    current_interval=sorted_list[0]
    current_interval_list=[]
    for next_interval in sorted_list[1:]:
        try:
            current_interval = mergeIntervals(current_interval, next_interval)
        except:
            current_interval_list.append(current_interval)
            current_interval = next_interval
    current_interval_list.append(current_interval)
    return current_interval_list

def insert(intlist, newint):
    '''
    insert a new interval into an interval list and merge them if possible
    '''
    intlist.append(newint)
    return mergeOverlapping(intlist)