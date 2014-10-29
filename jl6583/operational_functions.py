'''
Created on Oct 27, 2014

@author: luchristopher
'''
import sys
import re
from custom_exception import *
from __builtin__ import str
from interval import *

def isLegal(arg_interval_str):
    '''Returns True if a string representation of an interval(arg_interval_str) is legal, following validations are included:
        1)Non-string representations: 4321, True are illegal
        2)Pattern not matched: '<1,2>','[1.4,2.8]','(--2,4)','anystring' are illegal, '[1,2]','(   3   ,  5 )' are acceptable representations
    '''
    #check if arg_interval_str is an instance of built-in str
    if type(arg_interval_str) != str:
        return False
    interval_format_pattern = re.compile(r'(?P<INTERVAL>^\s*[\[\(]\s*\-?\d+\s*,\s*\-?\d+\s*[\)\]]\s*$)');
    #returns true if pattern is matched, else return false
    return bool(re.search(interval_format_pattern,arg_interval_str))
    
def validateList(arg_interval_list):
    '''run isLegal validation for all intervals in the interval list, raises an IllegalInterval exception when there are illegal intervals'''
    for interval in arg_interval_list:
        if not isLegal(interval):
            raise IllegalInterval('Input sequence contains illegal intervals, please re-enter the sequence.\n')
    
def intervalParser(arg_interval_str):
    '''This function was used to parse down intervals and check if parsed intervals are in correct form:
        Intervals are separated with delimiter ',', while extra blank characters are omitted
    '''
    list_delimiter = re.compile(r'(?<=[\]\)])\s*,\s*')
    parsed_list = list_delimiter.split(arg_interval_str)
    validateList(parsed_list)
    return parsed_list
        
        
    