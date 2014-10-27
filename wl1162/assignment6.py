import sys
from interval import *
from interval.exceptions import *
from interval.interval_functions import *
from interval.interval_class import *

def main():
    """
    create a main program that reads in user input of a permanent list and single intervals.
    try to merge single intervals into permanent list.
    """
    initial_list_input = raw_input('List of intervals?')  # read in a permanent list of intervals as string

    while True:  # start to take interval from user
        try:
            interval_input = raw_input('Intervals?')
            if interval_input == 'quit':  # if user type in 'quit' or press Ctrl-C, the program will terminated
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()

        try:  # validate the string to check if it is a valid interval
            interval(interval_input)

        except (invalid_interval, invalid_interval_form):  # if string is neither a valid interval nor in interval form
            print "Invalid Interval"                    # "Invalid Interval" will be printed
            continue

        final_list = insert(initial_list_input, interval_input)  # merge the input interval with the permanent list
        print final_list  # print out the final list

if __name__=='__main__':
    main()