'''
Created on Oct 28, 2014

@author: ds-ga-1007
'''

from basicFunctions import *
from Exceptions import *

class interval:
    """
    Class of integer intervals
    
    Attributes:
    lower(str): the lower bound bracket or parenthesis
    upper(str): the upper bound bracket or parenthesis
    lower_bound(int): the lower bound displayed in the interval 
    upper_bound(int): the upper bound displayed in the interval
    Real_lower_bound(int): the actual value of the lower bound in the interval
    Real_upper_bound(int): the actual value of the upper bound in the interval
    """
    def __init__(self,input_interval):
        """
        The function constructs the class of interval.
        """
        if isInputIntervalValid(input_interval):
            #Get an input_interval without blank spces
            input_interval = ''.join(input_interval.split())
            self.input_interval = input_interval
          
            #Get all the elements for an interval if it is valid.
            self.lower, self.lower_bound, self.Real_lower_bound, self.upper_bound, self.Real_upper_bound, self.upper = getIntervalElements(input_interval)          
        else:
            # raise exception when the input_interval is invalid
            raise InvalidInterval()
    
    def range_of_interval(self):
        """
        Get the range of interval.
        """
        return range(self.Real_lower_bound,self.Real_upper_bound + 1)
               
    def __repr__(self):
        """
        The repr function will return the interval in string.
        """
        return self.input_interval

def mergeIntervals(int1, int2):
    """
    Takes two intervals, and if the intervals overlap returns a merged interval. 
    If the intervals do not overlap, an exception should be thrown.
    
    Arguments:
       int1: the first interval
       int2: the second interval
   
   Returns:
       merged_interval: an interval merged by int1 and int2
    
    Examples:
    >>>int1, int2 = interval('[1,4]'), interval('(2,5)')
    >>>print mergeIntervals(int1,int2)
    [1,5)
    >>>
    >>> int1,int2 = interval('(1,4]'), interval('(2,5]')
    >>> print mergeIntervals(int1,int2)
    (1,5]
    >>>
    >>>int1, int2 = interval('(1,4]'), interval('(2,5)')
    >>>print mergeIntervals(int1,int2)
    (1,5)
    >>>
    >>>int1, int2 = interval('[1,4)'), interval('(2,5]')
    >>>print mergeIntervals(int1,int2)
    [1,5]
    >>>
    """
    
    #Get ranges of the two intervals to determine if they overlap
    range_of_the_first_interval = int1.range_of_interval()
    range_of_the_second_interval = int2.range_of_interval()
   
    #The merge is used to store the merged interval    
    merge = ''
    
    #Determine if the two intervals can merge. If not, raise exception
    if (int(range_of_the_first_interval[0])-1)>int(range_of_the_second_interval[-1]) or (int(range_of_the_second_interval[0])-1)>int(range_of_the_first_interval[-1]):   
        raise NotOverlapInterval()
    
    #Store the merged string in merge, and concatenate into a whole string   
    else:
        if int1.Real_lower_bound <= int2.Real_lower_bound:
            merge = int1.lower + str(int1.Real_lower_bound) + ','
        else:
            merge = int2.lower + str(int2.Real_lower_bound)+','
        if int1.Real_upper_bound >= int2.Real_upper_bound:
            merge = merge + str(int1.Real_upper_bound) + int1.upper
        else:
            merge = merge + str(int2.Real_upper_bound) + int2.upper
    #Use merged_interval to represent the merged interval
    merged_interval = interval(merge)
     
    return merged_interval      
            
        
    
def mergeOverlapping(intlist):
    """
    Takes a list of intervals and merges all overlappping intervals.
    
    Argument:
       intlist: List of intervals to be merged.
    
    Return:
       intervals_merged: an interval list with the merged results.   
    
    Example:
    >>>intlist = [interval('[1,5]'), interval('[2,6)'), interval('(8,10]'), interval('[8,18]')]
    >>>mergeOverlapping(intlist)
    [[1,6), [8,18]]
    
    """
    
    #Sort the list according to lower bounds
    SortedIntlist = sorted(intlist, key = lambda x: x.Real_lower_bound)              
    
    #Store the first interval of the list in current_interval
    current_interval = SortedIntlist[0]
    #Store the list of intervals that have been merged 
    intervals_merged = []
    
    for i in range(1,len(SortedIntlist)):
        #Try to merge a interval with the next interval
        try:
            #If the two intervals can merge, store the merged interval in the current_interval 
            current_interval = mergeOverlapping(current_interval,SortedIntlist[i]) 
        except:
            intervals_merged.append(current_interval)
            current_interval = intlist[i]
    
    #Append the last interval to the intervals_merged    
    intervals_merged.append(current_interval)
    
    return intervals_merged
    
    
def insert(intlist, newint):
    """
    Take two arguments: a list of non-overlapping intervals; and a single interval. 
    The function should insert newint into intlist, merging the result if necessary.
    
    """
    intlist.append(newint)
    return mergeOverlapping(intlist)
