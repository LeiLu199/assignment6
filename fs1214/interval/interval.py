'''
Created on Oct 26, 2014

@author: ds-ga-1007
'''
from exceptions import *
from intervalfunctions import *

class interval:
    def __init__(self, interval_input=''):
        """
        use intervalfunctions to construct the interval class.
        Interval Class has 4 class variables:
        {
            lower(int): lower bound. The first integer of interval
            upper(int): upper bound. The second integer of interval
            lower_inclusive(bool): If the input has '[', True;
                                   if the input has '(', False.
            upper_inclusive(bool): If the input has ']', True;
                                   if the input has ')', False.
        }
        
        interval instance can be null.
        If the interval is not valid, raise the exception,IntervalBoundException or IntervalInputException.
        """
        if interval_input != '':
            if IsValidInterval(interval_input):
                self.lower, self.upper, self.lower_inclusive, self.upper_inclusive = ParseIntervals(interval_input) 
                if not IsValidBound(interval_input):
                    raise IntervalBoundException()
            else:
                raise IntervalInputException()
            
            
    def GetIntegers(self):
        """
        Get the range of the integers, return a list of the exact values of the interval.
        """ 
        integers = range(self.lower + int(not self.lower_inclusive),self.upper + int(self.upper_inclusive))
        return integers
    def __repr__(self):
        interval_rep = self.lower_inclusive*'['+(not self.lower_inclusive)*'('+str(self.lower)+','+str(self.upper)+self.upper_inclusive*']'+(not self.upper_inclusive)*')'
        return interval_rep

def ParseIntervalList(intervallist):
    """
    Parse the input to a list of intervals, return a list of interval class instance. 
    If any interval in the intervallist is invalid, 
    raise the exception, IntervalInputException, or IntervalBoundException, or IntervalListInputException.
    """
    if IsValidIntervalList(intervallist):
        #remove all the spaces in the interval 
        intervallist_nospace = intervallist.replace(" ","")
        #use re.findall to split the interval list, return a list string of intervals 
        interval_strings = re.findall('\s*[\(\[]\s*-*\s*\d+\s*,\s*-*\s*\d+\s*[\)\]]\s*', intervallist_nospace)
        intervallist = []
        for item in interval_strings:
            try:
                intervallist.append(interval(item))
            except (IntervalInputException,IntervalBoundException) as error:
                raise error
        return intervallist
    else:
        raise IntervalListInputException()

def mergeIntervals(int1, int2):
    """
    Merge two intervals, int1 and int2 are interval instances of Interval Class.
    If the intervals are not overlapped, OverlapplingException will be raised. Otherwise return merged interval.
    """
    
    #use GetIntegers function to get the real range of intervals.
    Integers1 = int1.GetIntegers()
    Integers2 = int2.GetIntegers()
    if Integers1[-1] < Integers2[0]-1 or Integers1[0] > Integers2[-1]+1:
        raise OverlapplingException()
    else:
        lower = min(Integers1 + Integers2)
        upper = max(Integers1 + Integers2)
        # we assume that (a,...) has smaller lower bound than [a+1,...). So when they merge, the merged interval shoulb be (n,...). 
        # the upper bound is similiarly treated.
        if lower in Integers1:
            if lower in Integers2 and int1.lower > int2.lower:
                lower,lower_inclusive = int2.lower,int2.lower_inclusive
            else:
                lower,lower_inclusive = int1.lower,int1.lower_inclusive                    
        elif lower in Integers2:
            lower,lower_inclusive = int2.lower,int2.lower_inclusive 
        
        if upper in Integers1:
            if upper in Integers2 and int1.upper < int2.upper:
                upper,upper_inclusive = int2.upper,int2.upper_inclusive
            else:
                upper,upper_inclusive = int1.upper,int1.upper_inclusive            
        elif upper in Integers2:
            upper,upper_inclusive = int2.upper,int2.upper_inclusive
    mergedInterval = interval()
    mergedInterval.lower,mergedInterval.upper,mergedInterval.lower_inclusive,mergedInterval.upper_inclusive = lower,upper,lower_inclusive,upper_inclusive
    return mergedInterval

def SortIntervallist(intervallist):
    """
    The input is a list of intervals. Sort this list according to the lower bound of intervals
    In this way, we don't change the original intervallist, return another list sortedIntervallist.
    """
    sortedIntervallist = sorted(intervallist, key=lambda x:x.lower - x.lower_inclusive)
    return sortedIntervallist

def mergeOverlapping(intlist):
    """
    Merge the intervals in the list. If there are no intervals that could be merged, stop merging.
    In this way, we don't change the original intlist, return another list mergeintervallist.
    """
    
    #first sort the intlist.
    sortedIntervallist = SortIntervallist(intlist)
    
    #store the first interval into temp
    temp = sortedIntervallist[0]
    #store the final merged list
    mergeintervallist = []
    
    for i in range(len(sortedIntervallist)-1):
        #try to merge temp and one interval in the list. 
        #if cannot merge, store this interval into temp and continue.
        try:
            temp = mergeIntervals(temp, sortedIntervallist[i+1])
        except OverlapplingException:
            mergeintervallist.append(temp)
            temp = sortedIntervallist[i+1]
    
    #append the last interval.
    mergeintervallist.append(temp)   
    return mergeintervallist

def insert(intlist, newint): 
    """
    Insert the new interval(newint) into the interval list(intlist). If they can merge, then merge the intervals.
    In this way, original list(intlist) is not changed
    """
    insertlist = mergeOverlapping(intlist + [newint])
    return insertlist
