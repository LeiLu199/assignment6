'''
Created on Oct 26, 2014

@author: ds-ga-1007
'''
import re

def IsValidInterval(interval_input):
    """
    check whether the input of interval is a valid interval.
    A valid interval must have: '(' or '[', two integers separated by ',', and ')' or ']'.
    
    If interval_input is a valid interval, return True; otherwise return False.
    """
    
    #input of interval must be a string
    if isinstance(interval_input, str):
        #Check whether input of interval has a valid form
        match = re.search('^\s*[\(\[]\s*\-?\d+\s*,\s*\-?\d+\s*[\)\]]\s*$',interval_input)
        if match:
            return True
        else:
            return False
    else:
        return False

def ParseIntervals(interval_input):
    """
    Parse the input of interval to get attributes of interval
    
    Args:
        interval_input(string)
    Return:
        {
            lower(int): lower bound. The first integer of interval
            upper(int): upper bound. The second integer of interval
            lower_inclusive(bool): If the input has '[', True;
                                   if the input has '(', False.
            upper_inclusive(bool): If the input has ']', True;
                                   if the input has ')', False.
        }
    
    """
    #remove all the spaces in the interval 
    interval_nospace = interval_input.replace(" ","")
    
    #get the value of lower_inclusive and upper_inclusive
    if interval_nospace[0] == '(':
        lower_inclusive = False
    elif interval_nospace[0] == '[':
        lower_inclusive = True
    if interval_nospace[-1] == ')':
        upper_inclusive = False
    elif interval_nospace[-1] == ']':
        upper_inclusive = True
    
    #get the value of lower and upper.The first part before ',' has the lower, the second part after ',' has the upper.
    intervalparts = interval_nospace.split(',')
    lowerpart = intervalparts[0]
    upperpart = intervalparts[-1]
    lower = int(lowerpart[1:])
    upper = int(upperpart[:-1])
    
    return(lower, upper, lower_inclusive, upper_inclusive)

def IsValidBound(interval_input):
    """
    Check whether the interval exists. The interval must at least contain one integer. 
    The upperbound of interval must be more than the lowerbound of interval 
    
    If interval_input has a valid bound, return True; otherwise return False.
    """
    lower, upper, lower_inclusive, upper_inclusive = ParseIntervals(interval_input)
    
    #define the real value of bounds. real_lower represents lower bound, real_upper represents upper bound.
    #for example, (2,5]: real_lower = 3; real_upper = 5. It is a valid interval.
    #             (2,3): real_lower = 3; real_upper = 2. It is not a valid interval.
    real_lower = lower + int(not lower_inclusive)
    real_upper = upper - int(not upper_inclusive)
    
    if real_lower > real_upper:
        return False
    else:
        return True

def IsValidIntervalList(intervallist):
    """
    Check whether the list of intervals are all valid 
    
    If all items in intervallist are valid, return True; otherwise return False.
    """
    #remove all the spaces in the interval 
    intervallist_nospace = intervallist.replace(" ","")
    
    #use re.findall to split the interval list
    intervals = re.findall('\s*[\(\[]\s*-*\s*\d+\s*,\s*-*\s*\d+\s*[\)\]]\s*', intervallist_nospace)
    if intervals == []:
        return False
    
    #check whether every interval is valid
    for item in intervals:
        if IsValidInterval(item) and IsValidBound(item):
            continue
        else:
            return False
    return True
