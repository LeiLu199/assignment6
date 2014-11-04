import sys
from interval import *
from interval.intervalfunctions import *


def main():
    """
    User provide a list of intervals, and merge new interval to this list
    """

    #make sure input interval list is correct
    while True:
        try:
            input_list = raw_input('List of intervals?')
            if input_list == 'quit':
                sys.exit()

        #exit when user input 'quit' or CTRL-C
        except KeyboardInterrupt:
            sys.exit()
        try:
            interval_list = parseIntervalListString(input_list)
            break
        except (invalidIntervalListInputException, invalidIntervalException) as e:
            print e

    #start to take interval from user
    while True:
        try:
            input_interval = raw_input('Intervals?')
            if input_interval=='quit':
                sys.exit()
        #exit when user input 'quit' or CTRL-C
        except KeyboardInterrupt:
            sys.exit()

        #try to make input string as interval and insert it into the list
        try:
            interval_list = insert(interval_list, interval(input_interval))

        #when input string is not interval form, invalidIntervalInputException will be raised
        #when input string is a null interval, invalidIntervalException will be raised
        except (invalidIntervalException, invalidIntervalInputException):
            print "Invalid Interval"
            continue
        print interval_list

if __name__ == '__main__':
    main()