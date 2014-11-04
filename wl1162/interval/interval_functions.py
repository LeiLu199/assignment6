from interval_class import *
from exceptions import *

def mergeIntervals(int1, int2):
    """merge two intervals, which takes in two strings in the interval form"""
    interval1=interval(int1)  # initialize the first string to have interval features
    interval2=interval(int2)  # initialize the second string to have interval features
    range1 = interval1.actual_interval  # get the actual digits in first interval
    range2 = interval2.actual_interval  # get the actual digits in second interval
    range3 = [i for i in range2 if i not in range1]  # create a list with digits in second but not in first interval
    
    if len(range3) == len(range2):  # compare lengths of list of second interval and digits in second but not in first
        raise non_overlapping('No overlapping between two intervals.')  # if they are equal, then no overlapping
    else:                                                                      # raise an exception of this case
        range4 = range1 + range3  # if overlapping, create a new list that add first interval the digits it is missing
        range4.sort()  # sort the resulting list
        return '[%d, %d]' %(range4[0], range4[-1])  # return a interval string with both inclusive with the first and
                                                       # last digits of the resulting list
        

def mergeOverlapping(intlist):
    """function that merge a list of intervals, which takes in a string that is separated by ', ' """
    interval_list=intlist.split(', ')  # split the string into a list with each element a string of an interval
    interval_sorted = sorted(interval_list, key=lambda x: interval(x).lower_bound)
    # sort the interval list by the lower bound of each interval in ascending order

    current = interval_sorted[0]  # Store the first interval in sorted list
    result = []  # Store merged intervals

    for i in range(1, len(interval_sorted)):
    # merge current and subsequent intervals in the list,, if non-overlapping, create a new one and add to the list
        try:
            current = mergeIntervals(current, interval_sorted[i])
        except non_overlapping:
            result.append(current)
            current = interval_sorted[i]

    result.append(current)  # Append merged intervals to the result
    return result

def insert(intlist, new_int):
    """function that takes in a string of intervals separated by ', ' and a string of a single interval
       trying to merge the single interval into the list of intervals"""
    new_list = intlist + ', ' + new_int  # Concatenate single interval into the list string to make a new string
    return mergeOverlapping(new_list)  # use the mergerOverlapping function to merge existing intervals in the string