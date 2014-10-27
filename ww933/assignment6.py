__author__ = 'chianti'

'''
The main function prompts the user for a list of intervals, reads a string from the user, and creates a list containing
these intervals.Once this string has been read, the main function continues prompting for intervals from the user,
insert the interval into the list, and display the list at the end of each operation.
The main function can also correctly validate the input from the user.
'''
import sys

from Interval import *
from PreHandle import *


def main():
# The first loop examines certain kinds of interrupts
# If receive  StopIteration, or GeneratorExit, or KeyboardInterrupt, or SystemExit, check then quit or continue
# If receive quit or quit() or exit or exit(), check then quit or continue

    while 1 == 1:
        try:
            intervals = raw_input('List of intervals? ')

        except (StopIteration, GeneratorExit, KeyboardInterrupt, SystemExit):
            MakingSureMessage = raw_input('Do you want to quit? (Type YES to confirm) ')

            if MakingSureMessage == 'Yes' or MakingSureMessage == 'yes'  or MakingSureMessage == 'YES':
                sys.exit()

            else:
                continue

        if intervals == 'quit' or intervals == 'quit()' or intervals == 'exit' or intervals == 'exit()':
            MakingSureMessage = raw_input('Do you want to quit? (Type YES to confirm) ')

            if MakingSureMessage == 'Yes' or MakingSureMessage == 'yes' or MakingSureMessage == 'YES':
                sys.exit()

            else:
                continue

        # Then split the input into single intervals and check validity, raise exceptions if the intervals are not
        # valid intervals
        try:
            intervals = map(interval, SplitIntoSingleInterval(intervals))
            break

        except (IsValidPatternError, IsValidIntervalError) as e:
            print e
            continue


# Once we checked the validity of the input, the following loop helps to continue prompting for intervals from the
# user, insert the interval into the list, and display the list at the end of each operation.
    while 2 == 2:

        # If receive StopIteration, GeneratorExit, KeyboardInterrupt, or SystemExit, raise exceptions
        # Otherwise, try to get new interval and insert it into interval lists, then merge the whole interval lists
        try:
            new_int = raw_input('Interval ? ')

        except (StopIteration, GeneratorExit, KeyboardInterrupt, SystemExit):
            MakingSureMessage = raw_input('Do you want to quit? (Type YES to confirm) ')

            if MakingSureMessage == 'Yes' or MakingSureMessage == 'yes'  or MakingSureMessage == 'YES':
                sys.exit()

            else:
                continue

        if new_int == 'quit' or new_int == 'quit()' or new_int == 'exit' or new_int == 'exit()':
            MakingSureMessage = raw_input('Do you want to quit? (Type YES to confirm) ')

            if MakingSureMessage == 'Yes' or MakingSureMessage == 'yes'  or MakingSureMessage == 'YES':
                sys.exit()

            else:
                continue

        try:
            new_interval = interval(new_int)

        except (IsValidPatternError, IsValidIntervalError) as e:
            print e
            continue

        intervals = insert(intervals, new_interval)

        print intervals


if __name__ == '__main__' and True:
    main()
