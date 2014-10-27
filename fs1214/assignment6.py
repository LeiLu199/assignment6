'''
Created on Oct 26, 2014

@author: ds-ga-1007
'''
import sys
from interval.exceptions import *
from interval.interval import *
from interval.intervalfunctions import *

def main():
    """
    Parse the input to list of intervals. Insert the interval to the list.
    If they can merge, merge the intervals. Raise the exceptions if the intervals are invalid.
    """

    originallist = raw_input('List of intervals? ')
    if originallist == 'quit':
        sys.exit()
    
    while True:
        try:
            # Parse the input to a list of intervals.
            intervallist = ParseIntervalList(originallist)
            break
        except (IntervalInputException,IntervalBoundException,IntervalListInputException) as error:
            print error
    
    newintervalstring = raw_input('Interval? ')
    
    while newintervalstring != 'quit':
        try:
            newinterval = interval(newintervalstring)
            intervallist = insert(intervallist,newinterval)
            for it in intervallist[:-1]:
                print str(it)+',',
            print intervallist[-1]           
        except KeyboardInterrupt:
            sys.exit()
        except (IntervalInputException, IntervalBoundException) as error:
            print error
        newintervalstring = raw_input('Interval? ')
def test():
    int1=interval(22)
    print int1
if __name__ == '__main__':
    main()
    #test()