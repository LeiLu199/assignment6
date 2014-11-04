'''
Created on Nov 2, 2014

@author: leilu
'''
from lib2to3.fixer_util import String
import re
from User_defined_Exception import *

#Formalize an given string by getting rid of spaces.
def formalize(interval):
    space_free_interval=interval.replace(" ", "")
    return space_free_interval

#Check the format of the string to see if it is of the format of an interval
def check_format(interval):   
    effective_interval=re.findall(r'[\(\[]{1,1}-*[0-9]+,{1,1}-*[0-9]+[\)\]]{1,1}',interval)
    return effective_interval

#Given a string, removing the spaces and check if it is valid: lower bound should be smaller than the upper bound"
def check_interval(String_interval):
    interval=formalize(String_interval)
    if check_format(interval)==[]:# the interval is of the wrong format
        raise IntervalFormatIssueException("The format of the interval is incorrect")
    
    else:
        try:
            lower = int(interval[1:-1].split(",")[0])
            upper = int(interval[1:-1].split(",")[1])
            if(interval[0] == "[" and interval[-1] == ']'):
                if lower <= upper:
                    return True
                else:
                    return False

            if(interval[0] == "[" and interval[-1] == ")"):
                if lower < upper:
                    return True
                else:
                    return False

            if(interval[0] == "(" and interval[-1] == "]"):
                if lower < upper:
                    return True
                else:
                    return False

            if(interval[0] == "(" and interval[-1] == ")"):
                if lower < upper - 1:
                    return True
                else:
                    return False
        except:
            return False