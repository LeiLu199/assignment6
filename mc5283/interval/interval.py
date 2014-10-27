from .intervalFunctions import *
from .exception import *

class interval:
    def __init__(self, interval):
        '''
        define the elements of an interval:
        lbound:(lower bound) the smaller number in the interval
        ubound:(upper bound) the larger number in the interval
        l: the left bracket/parentheses of the interval
        r: the right bracket/parentheses of the interval
        lrange: the smallest integer in the interval range
        urange: the largets integer in the interval range
        '''       
        if  validIntervalOrNot(interval):
            self.l, self.lbound, self.lrange, self.ubound, self.urange, self.r = getInfo(interval)
        else:
            raise invalidIntervalInput() 

    def __repr__(self):
        return self.l + str(self.lbound) + ', ' + str(self.ubound) + self.r

def parseIntervalList(inputList):
    '''
    check if the input string contains valid intervals, and split the string into a list of intervals 
    input: customer's input string
    return: a list of intervals or raise exception
    '''
    if isinstance(inputList,str):
        listNoSpace = string.replace(inputList, ' ','')
        intervalForm = re.compile('[\(\[]-?\d+,-?\d+[\)\]]')
        intervalList = intervalForm.findall(listNoSpace)

        if len(intervalList) == 0:
            raise nullInterval()
        else:
            validIntervalList = []
            for i in intervalList:
                if validIntervalOrNot(i):
                    validIntervalList.append(interval(i))
                else:
                    print 'Invalid interval in the list!'
                    raise invalidIntervalList()
            return validIntervalList
    else:
        raise invalidIntervalList()

def intOverlap(int1, int2):
    '''
    check if two intervals are overlapping
    return True or False
    '''
    intlist = [int1, int2]

    sorted_list = sorted(intlist, key = lambda i: (i.lbound, i.lrange, i.urange, i.ubound))
    merge1 = sorted_list[0].urange
    merge2 = sorted_list[1].lrange
    
    if merge1 +1  >= merge2:
        return True
    else:
        return False

def mergeIntervals(int1, int2):
    '''
    input: 2 intervals
    return: if overlap, merged interval;if not, raise exception
    '''
    if not intOverlap(int1, int2):
        raise noOverlapping()
    '''
    if overlap, construct the merged interval by assigning the lower bound/range
    of the first interval to merged lower bound/range(lowerBound/lowerRange),
    and then compare the the lower bound/range of 2 intervals, substitute if 
    the lbound of 2nd interval is smaller. Similar work to find upper bound/range
    '''
    L = int1.l
    lowerRange = int1.lrange
    lowerBound = int1.lbound
    if lowerRange > int2.lrange or lowerBound > int2.lbound:
        lowerRange = int2.lrange
        lowerBound = int2.lbound
        L = int2.l

    R = int2.r
    upperRange = int2.urange
    upperBound = int2.ubound
    if upperBound < int1.ubound or upperRange < int1.urange:
        upperBound = int1.ubound
        upperRange = int1.urange
        R = int1.r
    return interval(L + str(lowerBound) + ',' + str(upperBound) + R)

def mergeOverlapping(intlist):
    '''
    merge a list of interval. if overlap, merge; if not, append.
    input: a list of intervals
    return: a list of merged intervals
    '''
    sortIntlist = sorted(intlist, key = lambda i: (i.lbound, i.lrange, i.urange, i.ubound))
    temp = [sortIntlist[0]]
    merging = sortIntlist[0]
    
    for i in range(1, len(sortIntlist)):
        if intOverlap(merging, sortIntlist[i]):
            merging = mergeIntervals(merging,sortIntlist[i])
            temp[-1] = merging
        else:
            merging = sortIntlist[i]
            temp.append(merging) 
    return temp

def insert(intlist, newint):
    return mergeOverlapping(intlist+[newint])

