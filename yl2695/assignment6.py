import re
from interval.exception import InvalidIntervals
from interval.Intervals import *
from interval.basicFunctions import *


def main():
    '''
    The main function takes a list of intervals as inputs and asks the user to input interval and try to merge it into the interval-list.
    '''
    start_string = raw_input("List of intervals? ")
    while True:
        if isInputIntervalListValid(start_string):
            break
        else:
            raise InvalidIntervals('At least one interval is invalid!')
    intervalString = ''.join(start_string.split())

    # use re.findall to split the intervalString into all the satisfactory interval strings.
    target_stringList = re.findall(r'[\[\(]{1,1}-{0,1}[0-9]+\,+-{0,1}[0-9]+[\)\]]{1,1}', intervalString)

    # check whether the list input is a valid interval list.
    for item in target_stringList:
        if isValidInterval(item):
            continue
        else:
            raise InvalidIntervals('At least one interval in the list that you input is invalid!')

    # use interval_list to store the merged list.
    interval_list = []
    for item in target_stringList:
        # print interval(item)
        interval_list.append(interval(item))
    interval_list = mergeOverlapping(interval_list)

    while True:
        input_string = raw_input("Interval? ")
        if input_string != 'quit':
            try:
                print insert(interval_list, interval(input_string))
                print '... result of inserting into list...'
            except:
                print 'Invalid interval'
        else:
            break


if __name__ == '__main__':
    main()
