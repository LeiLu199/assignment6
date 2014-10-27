import re
import string
from .exception import *

def validIntervalOrNot(inputString):
    '''
    input: string
    return: True or False
    tell if the input interval is a valid interval.
    First, it has to be a string.
    '''
    if isinstance(inputString, str):
        #delete all the spaces in the string
        stringNoSpace = string.replace(inputString, ' ','')
        '''
        when it is not an empty string, check whether it has brackets/parentheses(l and r), 
        comma, and integer(lbound and ubound) in between. if it has all these, 
        check if its smallest integer is no larger than biggest
        '''
        if len(stringNoSpace) > 0:
            if (stringNoSpace[0] == '(' or '[') and (stringNoSpace[-1] == ')' or ']'):
                try:
	            commaIndex = stringNoSpace.index(',')
                    lbound = int(stringNoSpace[1:commaIndex])
                    ubound = int(stringNoSpace[commaIndex + 1:-1])
                    l = stringNoSpace[0]
                    r = stringNoSpace[-1]
       
                    lrange = lbound + int(l == '(')
                    urange = ubound - int(r == ')')
                    if lrange <= urange:
                        return True
                    else:
                        return False
                except:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

def getInfo(inputString):
    '''
    return the six element of the interval if it is valid:
    l: left bracket/parentheses
    r: right bracket/parentheses
    lbound: the small number in interval
    ubound: the big number in interval
    lrange: the smallest number contained in the interval
    urange: the biggist number contained in the interval
    '''
    if validIntervalOrNot(inputString):
        stringNoSpace = string.replace(inputString, ' ','')
        commaIndex = stringNoSpace.index(',')
        lbound = int(stringNoSpace[1:commaIndex])
        ubound = int(stringNoSpace[commaIndex + 1:-1])
        l = stringNoSpace[0]
        r = stringNoSpace[-1]
        lrange = lbound + int(l == '(')
        urange = ubound - int(r == ')')
        return l, lbound, lrange, ubound, urange, r
    else:
        raise invalidIntervalInput()

def parseValidIntervalList(inputList):
    '''
    check if the input is a valid interval list which should contain at lease 1 interval
    '''
    if isinstance(inputList,str):
        listNoSpace = string.replace(inputList, ' ','')
        intervalForm = re.compile('[\(\[]-?\d+,-?\d+[\)\]]')
        intervalList = intervalForm.findall(listNoSpace)
        if len(intervalList) > 0:
            return True
        else:
            return False
    else:
        return False  
