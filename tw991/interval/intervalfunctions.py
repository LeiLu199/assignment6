import re
import string
from .exceptions import *

def isValidIntervalInput(interval_input):
    """
    Check whether input string has a valid interval form ( , ), [ , ), [ , ) or [ , ]
    """

    #input should be string
    if isinstance(interval_input, str):
        form = re.compile('^\s*[\(\[]\s*-*\s*\d+\s*,\s*-*\s*\d+\s*[\)\]]\s*$')
        match = form.match(interval_input)
        if match:
            return True
        else:
            return False
    else:
        return False

def isValidIntervalListInput(list_input):
    """
    Check whether input is a valid interval list string which should have at least one interval form
    """

    #input should be string
    if isinstance(list_input, str):
        form = re.compile('\s*[\(\[]\s*-*\s*\d+\s*,\s*-*\s*\d+\s*[\)\]]\s*')
        match = form.findall(list_input)
        if len(match) > 0:
            return True
        else:
            return False
    else:
        return False


def parseIntervalString(interval_input):
    """
    Parse input string to 4 outputs:
    lower bound(int), upper bound(int), lower bracket type(str) and upper bracket type(str)
    """

    if isValidIntervalInput(interval_input):
        number_form = re.compile('-*\d+')
        bracket_form = re.compile('[\(\[\)\]]')
        #deleting all spaces and find number and bracket type in input string
        interval_input_nospace = string.replace(interval_input,' ','')
        lower_bracket, upper_bracket = bracket_form.findall(interval_input_nospace)
        lower, upper = number_form.findall(interval_input)
        return int(lower), int(upper), lower_bracket, upper_bracket
    else:
        raise invalidIntervalInputException()


def getInclusiveValue(lower, upper, lower_bracket, upper_bracket):
    """
    Take in 4 arguments, including lower bound(int), upper bound(int), lower bracket type(str) and upper bracket
    type(str) and return 2 int numbers representing the inclusive lower and upper bound
    """

    if lower_bracket == '(':
        lower_bracket_rep = 1
    else:
        lower_bracket_rep = 0
    if upper_bracket == ')':
        upper_bracket_rep = -1
    else:
        upper_bracket_rep = 0
    lower_inclusive = lower + lower_bracket_rep
    upper_inclusive = upper + upper_bracket_rep
    return lower_inclusive, upper_inclusive


def isValidInterval(interval_input):
    """
    Check whether input interval is an empty set
    """

    lower, upper, lower_bracket, upper_bracket = parseIntervalString(interval_input)
    lower_inclusive, upper_inclusive = getInclusiveValue(lower, upper, lower_bracket, upper_bracket)
    if lower_inclusive > upper_inclusive:
        return False
    else:
        return True

