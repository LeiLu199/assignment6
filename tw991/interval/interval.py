from .intervalfunctions import *
from .exceptions import *


class interval:

    def __init__(self, interval_input):
        """
        Integer interval class . Having 6 attributes:
        lower(int): Lower bound
        upper(int): Upper bound
        lower_inclusive(int): Lower inclusive bound
        upper_inclusive(int): Upper inclusive bound
        lower_bracket(str): Lower bound bracket ('(' or '[')
        upper_bracket(str): Upper bound bracket (')' or ']')
        """
        if isValidInterval(interval_input):
            self.lower, self.upper, self.lower_bracket, self.upper_bracket = parseIntervalString(interval_input)
            self.lower_inclusive, self.upper_inclusive = getInclusiveValue(self.lower, self.upper, self.lower_bracket, self.upper_bracket)
        else:
            raise invalidIntervalException()

    def __repr__(self):
        return self.lower_bracket + str(self.lower) + ', ' + str(self.upper) + self.upper_bracket


def parseIntervalListString(list_input):
    """
    Parse the input interval list string to a list of interval instances
    """
    if isValidIntervalListInput(list_input):
        form = re.compile('\s*[\(\[]\s*-*\s*\d+\s*,\s*-*\s*\d+\s*[\)\]]\s*')
        interval_list_string = form.findall(list_input)
        interval_list = []
        for interval_string in interval_list_string:
            try:
                #Check each interval in the list if it's valid
                interval_list.append(interval(interval_string))
            except invalidIntervalException:
                print "There is invalid interval in the list"
                raise invalidIntervalException
        return interval_list
    else:
        raise invalidIntervalListInputException()



def mergeIntervals(interval1, interval2):
    """
    Merge two interval instances. If the intersection of two intervals is not null, merged interval instance is returned.
    Otherwise, noOverlappingException will be raised.
    """
    if interval1.upper_inclusive + 1 < interval2.lower_inclusive or interval2.upper_inclusive + 1 < interval1.lower_inclusive:
        raise noOverlappingException()
    else:
        if interval1.lower_inclusive <= interval2.lower_inclusive:
            lower = interval1.lower
            lower_bracket = interval1.lower_bracket
        else:
            lower = interval2.lower
            lower_bracket = interval2.lower_bracket
        if interval1.upper_inclusive >= interval2.upper_inclusive:
            upper = interval1.upper
            upper_bracket = interval1.upper_bracket
        else:
            upper = interval2.upper
            upper_bracket = interval2.upper_bracket
        merged_interval_string = lower_bracket + str(lower) + ', ' + str(upper) + upper_bracket
        return interval(merged_interval_string)


def interval_sort(interval1,interval2):
    """Define the comparing of two intervals"""
    if interval1.lower > interval2.lower:
        return 1
    if interval2.lower > interval1.lower:
        return -1
    return 0


def mergeOverlapping(input_list):
    """
    Merge the input_list until the intersection of any two intervals is null.
    input_list will not be changed and a new list will be returned
    """
    interval_list = input_list[:]
    #sort the interval list according to the lower bound
    interval_list.sort(interval_sort)
    #Initialize the list of unmerged and merged intervals
    unmerged_list=[]
    merged_list=[]
    while len(interval_list)>0:
        #merge start from the interval with the smallest lower bound
        merging_interval=interval_list[0]
        for interval in interval_list:
            try:
                merging_interval=mergeIntervals(merging_interval,interval)
            except noOverlappingException:
                #If interval can't merge with merging_interval, interval will be stored to unmerged_list
                unmerged_list.append(interval)
        merged_list.append(merging_interval)
        interval_list = unmerged_list[:]
        unmerged_list = []
    return merged_list


def insert(interval_list, new_interval):
    """
    Insert new_interval into an interval list and merge the result if possible
    """
    input_list = interval_list[:]
    input_list.append(new_interval)
    merged_list = mergeOverlapping(input_list)
    return merged_list
