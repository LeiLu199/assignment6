'''
Created on Oct 28, 2014

@author: ds-ga-1007
'''
import re

def isInputIntervalValid(input_interval):
    """
    To check if the interval is valid
    
    Argument:
       input_interval(string): a string of an interval
    
    Return:
       True(boolean): If the interval is valid, return True.
       False(boolean): If the interval is invalid, return False
      
    Example:
    >>> isValidInterval('(3,9)')
    True
    >>> isValidInterval('((3,9)')
    False
    >>> isValidInterval('[3,9]]')
    False
    >>> isValidInterval('(8,9)')
    False
    >>> isValidInterval('for god sake')
    False
    
    """
    #delete the blank spaces in the input_interval
    input_interval = ''.join(input_interval.split())
    
    #check if the input_interval starts with '(' or '[' and ends with ')' or ']'
    if (input_interval[-1] == ')' or ']') and (input_interval[0] == '(' or '[') :
        try:
            #The lower and upper is the bracket or parenthesis of an interval. Check if there is a ',' in the interval.
            CommaIndex = input_interval.index(',')
            lower = input_interval[0]
            upper = input_interval[-1]
            
            #To check if the input_interval has other invalid characters.
            lower_bound = int(input_interval[1:CommaIndex])
            upper_bound = int(input_interval[CommaIndex+1:-1])
            if lower == '[':
                Real_lower_bound = lower_bound 
            else:
                Real_lower_bound = lower_bound + 1
            if upper == ']':
                Real_upper_bound = upper_bound 
            else:
                Real_upper_bound = upper_bound - 1
            
            if Real_lower_bound <= Real_upper_bound:
                return True
            else:
                return False
        except:
            return False
    else:
        return False
            
def getIntervalElements(interval_input):
    """
    Get the elements of an interval, and store them in different variables
    
    Argument:
        interval_input: the string of the input interval
    Return:
        (lower, lower_bound, Real_lower_bound, upper_bound, Real_upper_bound, upper)
    """
    lower = interval_input[0]
    upper = interval_input[-1]
    CommaIndex = interval_input.index(',')
    lower_bound = int(interval_input[1:CommaIndex])
    upper_bound = int(interval_input[CommaIndex+1:-1])
    if lower == '[':
            Real_lower_bound = lower_bound
    else:
            Real_lower_bound = lower_bound + 1
    if upper == '[':
            Real_upper_bound = upper_bound
    else:
            Real_upper_bound = upper_bound - 1
    return (lower, lower_bound, Real_lower_bound, upper_bound, Real_upper_bound, upper)
    

def isInputIntervalListValid(IntervalListString):
    """
    Check if the input of a interval list string is valid. Use re.findall to split the string into intervals.
    """
    
    #Get a new string without blank spaces   
    IntervalListString = ''.join(IntervalListString.split())
    
    #The ListofSplitedInterval will store the splited intervals of IntervalListString.
    ListofSplitedInterval = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\)\]]+', IntervalListString)
    if ListofSplitedInterval == []:
        return False
    
    for interval in ListofSplitedInterval:
    #Examine if there is any invalid interval.
        if isInputIntervalValid(interval):
            continue
        else:
            return False
    return True

def splitIntervalList(interval_list_input):
    """
    split intervals by the comma between two closed intervals.
    """
    
    SplitedListInterval = re.split('(?<=[\]\)])\s*,\s*', interval_list_input)
    return SplitedListInterval
    
    
    
    

           
          
    