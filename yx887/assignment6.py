import sys
from interval.interval import *
from interval.utility import isValidBounds, parseIntervals

def main():
    """Main function. Take a list of intervals, and as user providing new intervals, merge them together.
    """
    # Input loop for list of intervals
    while 1==1:

        # Try to catch KeyboardInterrupt and EOFError
        try:
            intervals = raw_input('List of intervals? ')
        except (KeyboardInterrupt, EOFError):
            print 'Bye!'
            sys.exit()

        # If user input quit or exit, exit the program
        if intervals == 'quit' or intervals == 'exit':
            print 'Bye!'
            sys.exit()

        # Parse string as intervals, catch possible exceptions
        try:
            intervals = map(Interval, parseIntervals(intervals))
            break
        except (NotAnIntervalError, InvalidBoundsError) as e:
            print e
            continue

    # Input loop once user successfully input list of intervals
    while 2>1:

        # Try to catch KeyboardInterrupt and EOFError
        try:
            user_input = raw_input('Interval? ')
        except (KeyboardInterrupt, EOFError):
            print 'Bye!'
            break

        # Quit if user ask politely
        if user_input == 'quit' or user_input == 'exit':
            print 'Bye!'
            break
        else:
            # Try to construct an interval given user input, catch possible exceptions
            try:
                new_interval = Interval(user_input)
            except (NotAnIntervalError, InvalidBoundsError) as e:
                print e
                continue
            
            # Do insertion and print result
            intervals = insert(intervals, new_interval)
            print intervals

if __name__ == '__main__':
    main()
            
            
