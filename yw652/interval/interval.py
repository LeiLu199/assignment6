from .intervalFunction import *
from .Exceptions import *


class interval:

    '''
    construct an interval object
    '''

    def __init__(self, interval_string):

        if isValidInterval(interval_string):

            # if an interval is valid, then initialize all the parameters based on the info list
            infoList = getIntervalInfo(interval_string)

            self.leftSide = str(infoList[0])
            self.LBound = int(infoList[1])
            self.min = int(infoList[2])
            self.UBound = int(infoList[3])
            self.max = int(infoList[4])
            self.rightSide = str(infoList[5])

        else:
            #otherwise raises exception
            raise invalidIntervalException()


    def __repr__(self):
        return self.leftSide + str(self.LBound) + ',' + str(self.UBound) + self.rightSide

def overlapped(interval1, interval2):
    '''
    testing whether 2 given intervals overlapped or not
    :param interval1:
    :param interval2:
    :return: boolean
    '''

    intList = [interval1, interval2]

    #Sort the list based on the priority of lower bound, min, max and then upper bound
    intList = sorted(intList, key=lambda num:(num.LBound, num.min, num.max, num.UBound))

    #return false if not overlapping, otherwise true
    if intList[0].max + 1 < intList[1].min:
        return False
    return True

def mergeInterval(interval1, interval2):
    '''
    Merge 2 given intervals into 1
    :param interval1:
    :param interval2:
    :return: a merged interval or the original one
    '''
    if not overlapped(interval1, interval2):

        #if 2 interval does not overlap, raise exception
        raise notOverlappingException()

    else:
        intList = [interval1, interval2]
        intList = sorted(intList, key=lambda num: (num.LBound, num.min, num.max, num.UBound))
        if intList[0].max < intList[1].max:
            #concatenate the interval and size up/down the range
            return interval(int(intList[0].leftSide == '(') * '(' + (1-int(intList[0].leftSide=='('))*'[' + str(intList[0].LBound) + ',' + str(intList[1].UBound) + int(intList[1].rightSide==']')*']' + (1-int(intList[1].rightSide==']'))*')')
    return intList[0]

def mergeOverlapping(intList):
    '''
    merge all the overlapping intervals in a list
    :param intList:
    :return:list
    '''

    intList = sorted(intList, key = lambda num: (num.LBound, num.min, num.max, num.UBound))
    newList = []

    #append the first interval on the list to the new list and pops it off the old list
    newList.append(intList[0])
    intList.pop(0)

    #while there's more interval to examine
    while len(intList) != 0:

        #if the first interval in the old list and last interval in the new list overlap, then merge
        if overlapped(intList[0], newList[-1]) == True :
            newList[-1] = (mergeInterval(intList[0],newList[-1]))
        #otherwise just append to the end of the new list
        else:
            newList.append(intList[0])
        intList.pop(0)
    return newList

def insert(intList,interv):
    newList = []
    for itv in intList:
        newList.append(itv)
    newList.append(interv)
    #return the list after merging all the overlapped intervals within
    return mergeOverlapping(newList)

def printList(itvList):
    for item in itvList:
        print item

def splitInputList(list_string):
    '''
    parsing the input list into intervals
    :param list_string:
    :return: list of intervals
    '''

    itv_list = []

    #if the input list is a valid list input (which means that containing
    # AT LEAST 1 interval with standard form(MAY NOT BE VALID))
    if isListValid(list_string):
        list_no_space = string.replace(list_string," ","")
        form = re.compile('[\[\(]-?\d+,-?\d+[\)\]]')
        itv_list_string = form.findall(list_no_space)

        # Create a new list of INTERVAL OBJECT and raise exception when necessary
        try:
            for itv_str in itv_list_string:
                itv_list.append(interval(itv_str))
        except invalidIntervalException as err:
            print err
    else:
        raise invalidListException

    return itv_list

