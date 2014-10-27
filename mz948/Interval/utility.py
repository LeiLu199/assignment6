'''
utility.py
This file contains functions for the class interval

'''

import re 

def isValidInterval(interval_string):
    '''
    Check whether the input string has a valid interval form:( , ), ( , ], [ , ), or [ , ]
    '''
    
    # Must be a string
    if isinstance (interval_string, str):
    # Input must have valid form 
        match = re.search('^\s*[\(\[]\s*\-?\d+\s*,\s*\-?\d+\s*[\)\]]\s*$', interval_string)
        if match:
            return True
        else:
            return False
    else:
        return False 

def parse(interval_string):
    '''
    split user input string into six parts:
        1. lower bound type (str) 
        2. upper bound type (str)
        3. lower bound (int)
        4. upper bound (int)
        5. real lower bound (int)
        6. real upper bound (int)
    '''
    
    lower_boundType = interval_string[0]
    upper_boundType = interval_string[-1]
    
    index = interval_string.index(',')

    lowerBound = int(interval_string[1:index])
    upperBound = int(interval_string[index+1:-1])

    if lower_boundType == '(':
        real_lowerBound = lowerBound + 1
    else:
        real_lowerBound = lowerBound
    if upper_boundType == ')':
        real_upperBound = upperBound - 1
    else:
        real_upperBound = upperBound
    return (lower_boundType, lowerBound, real_lowerBound, upperBound, real_upperBound, upper_boundType)
             
    
def isValidIntervalList(input_list):
    """
    Check whether the input string is a valid list of intervals or not. 
    """

    # IMust be a string
    if isinstance(input_list, str):
        form = re.compile('\s*[\(\[]\s*-*\s*\d+\s*,\s*-*\s*\d+\s*[\)\]]\s*')
        match = form.findall(input_list)
        if len(match) > 0:
            return True
        else:
            return False
    else:
        return False

def parseIntervalList(input_list):
    '''
    This function takes a string as argument and parses the string into a list 
    of intervals if the string contains any interval.
    '''
    intervals = re.split('(?<=[\]\)])\s*,\s*', input_list.strip())
    for interval in intervals:
        if not isValidInterval(interval):
            raise Exception('At least one interval in the list is not in the correct form.')

    return intervals