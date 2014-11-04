from .exceptions import *

#define a function to check if the input interval is valid

def isValidInterval(string):

    """
    Target: Test if a input interval is valid or not
        if it is valid, return interval features, (lower_num, lower_sym, lower_sym_exclusive, upper_num, upper_sym, upper_sym_exclusive);
        if it is invalid, return False

    Example:
    >>> isValidInterval('(3,7))')
    False
    >>> isValidInterval('(3,7(')
    False
    >>> isValidInterval('(3,3)')
    False
    >>> isValidInterval('hello')
    False
    >>> isValidInterval('(3,7)')
    (3, '(', 1, 7, ')', 1)
    >>> isValidInterval('[3,7]')
    (3, '[', 0, 7, ']', 0)

    """
    
    #Test if the input is a string or not

    if isinstance(string, str):
        
        #Delete all blank spaces in the string

        string = string.replace(' ', '')
        
        #Try to check if this input string has valid features to convert to a interval. If it does, return these interval features; if it doesn't, return False
 
        try:
            lower_sym = string[0]
            upper_sym = string[-1]
            separate = string.index(',')
            lower_num = int(string[1:separate])
            upper_num = int(string[separate+1:-1])
            
            if lower_sym == '[':
                lower_sym_exclusive = 0
            elif lower_sym == '(':
                lower_sym_exclusive = 1
            if upper_sym == ']':
                upper_sym_exclusive = 0
            elif upper_sym == ')':
                upper_sym_exclusive = 1

            #Check if input interval satisfies the bounding requirement
            if lower_num + lower_sym_exclusive + upper_sym_exclusive <= upper_num:
                return (lower_num, lower_sym, lower_sym_exclusive, upper_num, upper_sym, upper_sym_exclusive)
            else:
                return False
        except:
            return False
    else:
        return False

#define a class to change a string to a interval
class interval:

    """
    Target: change the input string to a interval

    First,test if the input string is valid to be converted to a interval. If it is,change it to a valid interval; if it isn't, raise InvalidIntervalError.

    Example:
    >>> interval ('(3,7)')
    (3,7)
    >>> interval ('(3,   7  )')
    (3,7)
    >>> interval ('(3,4)')
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "interval/interval.py", line 43, in __init__
         raise InvalidIntervalError('invalid intervals')
    interval.exceptions.InvalidIntervalError

    """

    def __init__(self, string = ''):
        
        
        if isValidInterval(string):
            self.string = string
            self.lower_num, self.lower_sym, self.lower_sym_exclusive, self.upper_num, self.upper_sym, self.upper_sym_exclusive = isValidInterval(string)
        else:
            raise InvalidIntervalError('invalid intervals')
        
                    
    def __repr__(self):
        return self.lower_sym + str(self.lower_num) + "," + str(self.upper_num) + self.upper_sym

#function to merge two intervals
def mergeIntervals(int1, int2):

    """
    Target:Take two intervals, and if the intervals overlap returns a merged interval; if not, raise a NotOverlappingError

    Arguments:
    int1, int2: two interval instances to merge.

    Returns:
    int_merged: merged interval from int1, int2.

    Examples:

    >>> int1, int2 = interval('(-2, 3)'), interval('[3, 7)')
    >>> print mergeIntervals(int1, int2)
    (-2,7)
    >>> int1, int2 = interval('(-2, 2)'), interval('[3, 7)')
    >>> print mergeIntervals(int1, int2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "interval/interval.py", line 53, in mergeIntervals
        raise NotOverlappingError('No overlapping intervals')
    interval.exceptions.NotOverlappingError

    """
    #If not overlapping, raise a exception
    if int1.upper_num - int1.upper_sym_exclusive < int2.lower_num + int2.lower_sym_exclusive - 1 or int2.upper_num - int2.upper_sym_exclusive < int1.lower_num + int1.lower_sym_exclusive - 1:
        raise NotOverlappingError('No overlapping intervals')
    
    #if it is overlapping, merge two intervals    
    else:
        
        merged = ''
        
        if int1.upper_num - 0.5*int1.upper_sym_exclusive >= int2.upper_num - 0.5*int2.upper_sym_exclusive:
            upper_num = int1.upper_num
            upper_sym = int1.upper_sym
        else:
            upper_num = int2.upper_num
            upper_sym = int2.upper_sym
            
        if int1.lower_num + 0.5*int1.lower_sym_exclusive <= int2.lower_num + 0.5*int2.lower_sym_exclusive:
            lower_num = int1.lower_num
            lower_sym = int1.lower_sym
        else:
            lower_num = int2.lower_num
            lower_sym = int2.lower_sym
            
        merged = merged + lower_sym + str(lower_num) + ',' + str(upper_num) + upper_sym
        
        int_merged = interval(merged)
        
    return int_merged

#function to merge all overlapping intervals
def mergeOverlapping(intlist):

    """
    Target: Take a list of intervals and merge all overlapping intervals, the original list of interval won't change after mergging.

    Arguments:
    intlist: list of intervals to be merged

    Returns:
    merged_all: a new list after mergging all overlapping intervals

    Examples:
    >>> intlist = [interval('[1, 5]'), interval('[2, 6)'), interval('(8, 10]'), interval('[8, 18]')]
    >>> mergeOverlapping(intlist)
    [[1,6), [8,18]]
    >>> intlist
    [[1,5], [2,6), (8,10], [8,18]]

    """

    #Sort these intervals in the list of intervals
    def getkey(itv):
        return itv.lower_num + 0.5*itv.lower_sym_exclusive
    p = sorted(intlist, key=getkey)
    
    merged_init = p[0]
    merged_all = []
    
    #Merge intervals
    for i in range(1, len(p)):
        #Try to merge current two intervals, if they are not overlapping, create a new one and continue
        try:
            merged_init = mergeIntervals(merged_init, p[i])
            
        except NotOverlappingError:
            merged_all.append(merged_init)
            merged_init = p[i]
    #Append the last merged interval to the new list of intervals
    merged_all.append(merged_init)
    
    return merged_all

#function to insert a new interval to a existing interval list
def insert(intlist, newint):

    """
    Target: 
    insert a single interval to a existing list of non-overlapping intervals

    Arguments:
    intlist: a list of non-overlapping intervals
    newint: a new single interval

    Returns:
    mergeOverlapping(intlist): the merged list of intervals that contains both the intlist and newint

    Example:
    >>> intlist = [interval('[1, 5]'), interval('[2, 6)'), interval('(8, 10]'), interval('[8, 18]')]
    >>> newint = interval('[4,9)')
    >>> insert(intlist, newint)
    [[1,18]]

    *Attention: the result will change the original list of intervals!!!

    """

    intlist.append(newint)
    return mergeOverlapping(intlist)


