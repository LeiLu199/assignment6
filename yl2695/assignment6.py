import sys
from interval.exception import InvalidIntervals
from interval.Intervals import *
from interval.basicFunctions import *


def main():
    '''
    The main function takes a list of intervals as inputs and asks the user to input interval and try to merge it into the interval-list.
    '''

    # let user inputs the interval list string and make sure all the intervals in it are all satisfactory.
    while True:
        try:
            start_string = raw_input("List of intervals? ")
            if isInputIntervalListValid(start_string):
                break
            else:
                raise InvalidIntervals('At least one interval is invalid!')
        except KeyboardInterrupt:
            sys.exit()

    # split the satisfactory string into intervals and merge them into a list called interval_list 
    interval_list = []
    target_stringList = splitInputIntervalString(start_string)
    for item in target_stringList:
        interval_list.append(interval(item))
    interval_list = mergeOverlapping(interval_list)

    while True:
        try:

            # let the user input intervals
            input_string = raw_input("Interval? ")
            if input_string != 'quit':

                # try to insert the input string into the interval list.
                try:
                    interval_list = insert(interval_list, interval(input_string))
                    print '... result of inserting into list...'
                except:
                    print 'Invalid interval'

            # if the user inputs 'quit', exit!
            else:
                sys.exit()

        except KeyboardInterrupt:
            sys.exit()

        print interval_list

if __name__ == '__main__':
    main()
