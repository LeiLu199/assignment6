from exception import *
from basicFunctions import *


class interval():
    def __init__(self, string):
        '''
        The init function constructs the self-elements in the class.
        '''
        if isValidInterval(string):
            # delete all the blank spaces in the string
            string = "".join(string.split())

            # self.string stores the original string of the interval.
            self.string = string

            self.lower_notation, self.lowerBound, self.real_lowerBound, self.upperBound, self.real_upperBound, self.upper_notation = splitInterval(string)
        else:
            # raise exception when the interval that the user inputs is invalid.
            raise InvalidIntervals('This is an invalid interval!')
        
    def __repr__(self):
        '''
        The repr function just returns the string of the interval.
        '''
        return self.string


def mergeIntervals(int1, int2):
    '''
    Takes two intervals, and if the intervals overlap returns a merged interval. If the intervals do not overlap, an IntervalsNotOverlap Exception will be thrown.

    Arguments:
        int1: the first interval.
        int2: the second interval.
    Return:
        merged_interval: a merged interval.

    Example:
    >>> int1 = interval('(3,6)')
    >>> int2 = interval('[3,5]')
    >>> mergeIntervals(int1, int2)
    [3,6)
    >>>
    >>> int1 = interval('(3,5)')
    >>> int2 = interval('(2,5]')
    >>> mergeIntervals(int1, int2)
    (2,5]
    >>>
    >>> int1 = interval('(3,5]')
    >>> int2 = interval('[4,6)')
    >>> mergeIntervals(int1, int2)
    (3,6)
    >>> int1 = interval('(3,5]')
    >>> int2 = interval('(6,8]')
    >>> mergeIntervals(int1, int2)
    Traceback (most recent call last):
    File "<pyshell#49>", line 1, in <module>
        mergeIntervals(int1, int2)
    File "/Users/lyc/Desktop/Untitled", line 81, in mergeIntervals
        raise IntervalsNotOverlap('The two intervals cannot overlap!')
    IntervalsNotOverlap
    '''
    # The target_string is used to store the final string of the merged interval.
    target_string = ''

    # Judge whether the two intervals can merge. If they cannot merge, raise exception
    if int1.real_upperBound < int2.real_lowerBound - 1 or int2.real_upperBound < int1.real_lowerBound -1:
        raise IntervalsNotOverlap('The two intervals cannot overlap!')

    # Use target_string to store the first half of the merged string.
    if int1.real_lowerBound <= int2.real_lowerBound and int1.lowerBound <= int2.lowerBound:
        target_string += int1.lower_notation + str(int1.lowerBound) + ','
    else:
        target_string += int2.lower_notation + str(int2.lowerBound) + ','

    # Use target_string to store the second half of the merged string
    if int1.real_upperBound >= int2.real_upperBound and int1.upperBound >= int2.upperBound:
        target_string += str(int1.upperBound) + int1.upper_notation
    else:
        target_string += str(int2.upperBound) + int2.upper_notation

    # Use merged_interval to store the final merged intervals
    merged_interval = interval(target_string)

    return merged_interval


def mergeOverlapping(intlist):
    '''
    Takes a list of intervals and merges all overlapping intervals.

    Argument:
        intlist: a list that contains some intervals.

    Return:
        target_list: a list that has merges these intervals in the intlist.

    Example:
    >>> intlist = [interval('[1,5]'), interval('[2,6)'), interval('(8,10]'), interval('[8,18]')]
    >>> mergeOverlapping(intlist)
    [[1,6), [8,18]]
    '''
    # check first whether all the intervals in the intlist is valid, if there is a invalid one, raise an exception!
    for interval in intlist:
        if isValidInterval(str(interval)):
            continue
        else:
            raise InvalidIntervals('At leat one interval in the intlist is invalid!')

    # Define a key function getkey which takes an interval as input and returns its real lower bound as a key.
    def getkey(interval):
        return interval.real_lowerBound

    # sorted the inlist which uses the intervals' real lower bound as a key in the process of sorting.
    intlist = sorted(intlist, key=getkey)

    # initialize target_list and it is used to store the merged interval list.
    target_list = []

    i = 0
    while i < len(intlist):
        for j in range(i+1, i+2):
            # Try to merge the interval with the next interval.
            try:
                # If these two intervals can merge, put the merged interval in the first place.
                intlist.insert(i, mergeIntervals(intlist[i], intlist[j]))

                # delete the two intervals which can merge
                intlist.remove(intlist[i+1])
                intlist.remove(intlist[i+1])
                i -= 1
                break
            except:
                # append the interval which cannot merges with the followings intervals to the target-list.
                target_list.append(intlist[i])
                pass
        i += 1
    return target_list


def insert(intlist, newint):
    '''
    Takes two arguments: a list of non-overlapping intervals; and a single interval. The function WILL insert newint into intlist, merging the result if necessary.

    Arguments:
        intlist: a list which contains some intervals.
        newint: an interval that needs to be inserted into the list.

    Returns:
        mergeOverlapping(intlist): a list that contains the insert interval and has merged over lapping.

    Example:
    >>> intlist = [interval('[1,3]'), interval('[6,9]')]
    >>> newint = interval('[2,5]')
    >>> insert(intlist, newint)
    [[1,9]]
    >>>
    >>> intlist = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
    >>> newint = interval('[4,9]')
    >>> insert(intlist, newint)
    [[1,2], (3,10], [12,16]]
    '''
    intlist.append(newint)
    return mergeOverlapping(intlist)
