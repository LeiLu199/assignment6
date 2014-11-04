import re


def isValidInterval(string):
    '''
    check whether the interval is valid.

    Argument:
        string: the string of a interval.
    Return:
        True: if the interval is valid.
        False: if the interval is invalid.

    Example:
    >>> isValidInterval('  (2, 4)  ')
    True
    >>> isValidInterval('  ((2, 4)  ')
    False
    >>> isValidInterval('  (2, 4) ]  ')
    False
    >>> isValidInterval('(2, 3)')
    False
    >>> isValidInterval('python')
    False
    '''
    # delete all the blank spaces in the string.
    string = ''.join(string.split())

    # check whether the string's first and last character is '(' or '[' and ']' or ')'
    if (string[0] == '(' or '[') and (string[-1] == ')' or ']'):
        # try to find whether this is a valid interval.
        try:
            # check whether the string has ','
            index = string.index(',')
            lower_notation = string[0]
            upper_notation = string[-1]

            # try to check whether the string has some other characters except the '(' or '[' in the first place and ')' or ']' in the last place.
            lowerBound = int(string[1:index])
            upperBound = int(string[index+1:-1])
            if lower_notation == '(':
                real_lowerBound = lowerBound + 1
            else:
                real_lowerBound = lowerBound
            if upper_notation == ')':
                real_upperBound = upperBound - 1
            else:
                real_upperBound = upperBound

            # if the real_lowerBound is less than the real_upperBound, it is not a valid interval.
            if real_lowerBound <= real_upperBound:
                return True
            else:
                return False
        except:
            return False


def splitInterval(string):
    '''
    split the interval string into six parts and use different variables to store them.

    Argument:
        string: the string of the interval.
    Return:
        (lower_notation, lowerBound, real_lowerBound, upperBound, real_upperBound, upper_notation): the six parts of the interval which stores different information.
    '''
    #  lower_notation stores the interval's left notation.
    lower_notation = string[0]

    # upper_notation stores the interval's right notation.
    upper_notation = string[-1]

    index = string.index(',')

    # lowerBound stores the interval's literal lower bound.
    lowerBound = int(string[1:index])

    # upperBound stores the interval's literal upper bound.
    upperBound = int(string[index+1:-1])

    # real_lowerBound stores the interval's real lower bound.
    # real_upperBound stores the interval's real upper bound.
    if lower_notation == '(':
        real_lowerBound = lowerBound + 1
    else:
        real_lowerBound = lowerBound
    if upper_notation == ')':
        real_upperBound = upperBound - 1
    else:
        real_upperBound = upperBound
    return (lower_notation, lowerBound, real_lowerBound, upperBound, real_upperBound, upper_notation)


def isInputIntervalListValid(intervalString):
    '''
    use re.findall to split the input interval list string into different intervals and check whether they are all satisfactory.

    Argument:
        intervalString: the string that the user inputs
    Return:
        True: if all the intervals in the string are satisfactory
        False: as long as there is one invalid interval.

    Example:
    >>> isInputIntervalListValid('(2,   4),   [4,6  )')
    True
    >>> isInputIntervalListValid('((2, 4), (  4, 7]')
    False
    >>> isInputIntervalListValid('(2, 3), (  4, 7]')
    False
    >>> isInputIntervalListValid('(2, 4), (  4, 7]]')
    False
    '''
    # delete all the blank spaces in the string first.
    intervalString = ''.join(intervalString.split())

    # target_stringList is used to store all the intervals that are splited.
    target_stringList = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\)\]]+', intervalString)

    if target_stringList == []:
        return False

    # check whether all the intervals are satisfactory. As long as there is an incorrect interval, return False!
    for item in target_stringList:
        if isValidInterval(item):
            continue
        else:
            return False
    return True


def splitInputIntervalString(intervalString):
    '''
    Assume the interval list string the user inputs is satisfactory. Then split them into intervals.
    '''
    # delete all the blank spaces in the string first.
    intervalString = ''.join(intervalString.split())

    # use re.findall to split the intervalString into all the satisfactory interval strings.
    target_stringList = re.findall(r'[\[\(]{1,1}-{0,1}[0-9]+\,+-{0,1}[0-9]+[\)\]]{1,1}', intervalString)

    return target_stringList
