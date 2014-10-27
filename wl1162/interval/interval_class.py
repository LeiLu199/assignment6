import re
from exceptions import *

class interval:
    def __init__(self, string):
        """
        Constructor that takes a string of an interval with upper and lower bounds in integer.
        """
        digits = re.findall('[+-]?\d+', string)  # find all the digits in the string regardless of positive or negative
        list1 = map(int, digits)  # create a list contains the upper and lower bounds of the interval with lower first
        if len(list1) != 2:  # if the list has more than two elements, this is not an interval
            raise invalid_interval_form('Not an interval.')  # raise exception if it is not an interval
        self.lower_bound = list1[0]  # Given the first element of the list as lower bound
        self.upper_bound = list1[-1]  # Given the last element of the list as upper bound
        if self.lower_bound > self.upper_bound:  # if lower bound is greater than upper bound, this interval is invalid
            raise invalid_interval('Not a valid interval.')  # raise exception if it is not valid
        else:  # if the interval is valid, divide into four cases with inclusive and exclusive bounds
            if string[0] == '[' and string[-1] == ']':  # both inclusive
                self.actual_interval = range(self.lower_bound, self.upper_bound + 1)  # get digits within the interval
            elif string[0] == '(' and string[-1] == ']':  # half inclusive, half exclusive
                self.actual_interval = range(self.lower_bound + 1, self.upper_bound + 1)  # get digits within the interval
            elif string[0] == '[' and string[-1] == ')':  # half inclusive, half exclusive
                self.actual_interval = range(self.lower_bound, self.upper_bound)  # get digits within the interval
            elif string[0] == '(' and string[-1] == ')':  # both exclusive
                if self.lower_bound + 1 == self.upper_bound:  # if lower bound = upper bound +1 in both exclusive
                                                              # interval will be null
                    raise invalid_interval('Not a valid interval.')  # raise exception if this happens
                else:
                    self.actual_interval = range(self.lower_bound + 1, self.upper_bound)  # otherwise, get the digits

    
        
        
            
        
