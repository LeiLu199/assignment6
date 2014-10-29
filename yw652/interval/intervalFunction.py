from .interval import *
import string
import re
from Exceptions import *


def isValidForm(interval_string):
    '''
    check whether a given interval input is a valid form or not
    :param interval_string:
    :return: boolean value
    '''

    if isinstance(interval_string,str):

        #delete all the spaces
        itv_no_space = string.replace(interval_string," ","")

        #compile a form of standard interval
        form = re.compile('^[\(\[]-?\d+,-?\d+[\)\]]$')

        #match the interval input to the standard form
        matchPath = form.match(itv_no_space)

        if matchPath:
            return True
        else:
            return False
    else:
        return False

def isValidInterval(interval_string):
    '''
    check whether an interval input with standard form is a valid interval
    :param interval_string:
    :return: boolean value
    '''

    if isinstance(interval_string,str):
        if isValidForm(interval_string):
            itv_no_space = string.replace(interval_string," ","")

            #Get the index of the comma and initialize other parameters (2 bounds, and the min, max of the range)
            comma = itv_no_space.index(',')
            LBound = int(itv_no_space[1:comma])
            UBound = int(itv_no_space[comma+1:-1])
            min = LBound + int(itv_no_space[0] == '(')
            max = UBound - int(itv_no_space[-1] == ')')

            #if min <= max, then it's a valid interval, otherwise it's all invalid
            if min <= max:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def getIntervalInfo(interval_string):

    '''
    return a list of 6 variables that represents the lower and upper inclusive types, lower bounds and upper bounds, as well as the min and max of the interval
    '''

    infoList = []
    if isValidInterval(interval_string):
        itv_no_space = string.replace(interval_string," ","")
        comma = itv_no_space.index(',')
        LBound = int(itv_no_space[1:comma])
        UBound = int(itv_no_space[comma+1:-1])
        min = LBound + int(itv_no_space[0] == '(')
        max = UBound - int(itv_no_space[-1] == ')')

        #Grab the brackets/parenthesis
        leftSide = itv_no_space[0]
        rightSide = itv_no_space[-1]

        #append everything into the list

        infoList.append(leftSide)
        infoList.append(LBound)
        infoList.append(min)
        infoList.append(UBound)
        infoList.append(max)
        infoList.append(rightSide)

    else:
        raise invalidIntervalException

    return infoList


def isListValid(list_string):
    '''
    check whether there's at least one valid interval
    :param list_string:
    :return: boolean
    '''

    if isinstance(list_string,str):
        #check whether the input list contains at least one interval form (may not be valid)

        #Delete all the spaces in the list string
        list_string_compact = string.replace(list_string," ","")

        #compile the list into the correct form
        form = re.compile('[\[\(]-?\d+,-?\d+[\)\]]')

        #match the input list to the correct list form
        matchPath = form.findall(list_string_compact)

        if len(matchPath) > 0:
            return True
        else:
            return False
    else:
        return False


