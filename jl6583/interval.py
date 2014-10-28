'''
Created on Oct 27, 2014
interval.py contains the 'interval' class and related operations
>>>>
In class interval:
    Attributes:
        lower_bound(float) : the lower bound of the interval, when the bound is inclusive at x, the value is x, 
                            however, when the bound is exclusive at x, the value of lower_bound is x-0.9
        upper_bound(float) : the upper bound of the interval, when the bound is inclusive at x, the value is x, 
                            however, when the bound is exclusive at x, the value of lower_bound is x+0.9
    
    Methods:
        __init__(self,initial_string = '') : The constructor of class interval, taking a string as parameter, 
                                            constructs an instance of interval if string are in the correct form(e.g. [1,3], (5,9))
        __repr__(self) : The overloaded string conversion function for interval instances, returns a string [a,b) as the representation 
                        of interval [a,b), exclusive bounds has higher priority in displayed form
>>>>
External Methods:
    mergeIntevals(interval_1,interval_2) : Merge 2 intervals if overlapped, throws an exception when intervals not overlapped, 
                                            returns the merged interval or raises an exception
    mergeOverlapping(interval_list = []) : Merge 2 intervals, create a new interval if intervals do not overlap, returns the
                                            merged list
    insert(interval_list,new_interval) : Append a new interval(new_interval) to the existing interval_list and merge the interval with the list, 
                                        thus creates a new interval list
@author: luchristopher
'''
import sys
import math as mt
import re
import operational_functions

from custom_exception import *
#from operational_functions import *

class interval:
    def __init__(self,initial_string = ''):
        #if the input string is in valid form, compile the string to an interval instance
        if type(initial_string) == str:
            if operational_functions.isLegal(initial_string):
                bound_list = initial_string.strip(' []()').split(',')
                self.lower_bound = int(bound_list[0])
                self.upper_bound = int(bound_list[-1])
                #a 0.9 shift was added to represent exclusive bounds
                if initial_string.strip(' ')[0] == '(':
                    self.lower_bound = self.lower_bound+0.9
                if initial_string.strip(' ')[-1] == ')':
                    self.upper_bound = self.upper_bound-0.9
                if self.lower_bound > self.upper_bound:
                    raise EmptySet('The input interval is an empty set\n')    
            else:
                raise IllegalInterval('Input strings are not in valid form\n')
        #using list to initialize a interval object, will be used in mergeIntervals
        elif type(initial_string) == list:
            self.lower_bound = initial_string[0]
            self.upper_bound = initial_string[-1]
        else:
            raise UnexpectedType("Unexpected type for initializing 'interval' instance")
    
    def __repr__(self):
        l = mt.floor(float(self.lower_bound))
        u = mt.ceil(float(self.upper_bound))
        if self.lower_bound - l != 0.0:
            lower_bracket = '('
        else:
            lower_bracket = '['
        if self.upper_bound - u != 0.0:
            upper_bracket = ')'
        else:
            upper_bracket = ']'
        output_str = '%s%d,%d%s'%(lower_bracket,l,u,upper_bracket)
        return output_str
    
def mergeIntervals(interval_1,interval_2):
    '''Merge 2 intervals if overlapped, throws an exception when intervals not overlapped'''
    if round(interval_1.lower_bound) > round(interval_2.upper_bound)+1 or round(interval_1.upper_bound)+1 < round(interval_2.lower_bound):
        raise NotOverlapping('Intervals not overlapping')
    else:
        new_lower_bound = min(interval_1.lower_bound,interval_2.lower_bound)
        new_upper_bound = max(interval_1.upper_bound,interval_2.upper_bound)
        merged_interval = interval([new_lower_bound,new_upper_bound])
        return merged_interval;
    
def mergeOverlapping(interval_list = []):
    '''Merge 2 intervals, create a new interval if intervals do not overlap'''
    #sort the interval list by the lower bound
    interval_list.sort(key = lambda x : x.lower_bound)
    temp_interval = interval_list[0]
    output_list = list()
    for i in range(1,len(interval_list)):
        try: 
            temp_interval = mergeIntervals(temp_interval,interval_list[i])
        except:
            #if unable to merge create a new interval
            output_list.append(temp_interval)
            temp_interval = interval_list[i]
    output_list.append(temp_interval)
    return output_list

def insert(interval_list,new_interval):
    '''Append a new interval(new_interval) to the existing interval_list and merge the interval with the list, thus creates a new interval list'''
    interval_list.append(new_interval)
    return mergeOverlapping(interval_list)

