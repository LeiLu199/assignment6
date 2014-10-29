import sys
from interval import *
from interval.intervalFunctions import *
from interval.exception import *
from interval.interval import *

def main():
    '''
    First ask the costumer to input a string of interval list. Try if the list contains valid intervals.
    If yes, return a interval list; if not, catch exception.
    '''
    while True:
        try:
            inputString = raw_input('List of intervals?')
            if inputString == 'quit':
                raise KeyboardInterrupt
            intervalList = parseIntervalList(inputString)
            break

        except KeyboardInterrupt:
            print 'terminated!'
            sys.exit()
        except (nullInterval, invalidIntervalList):
            print 'Invalid list!'
            
    while True:
        '''
        Then ask the customer to input a string of interval. Try if it is a valid interval
        If yes, merge interval with interval list; if not, catch exception.
        '''
        try:
            intnew = raw_input('Interval?')
            if intnew == 'quit':
                raise KeyboardInterrupt
            newInterval = interval(intnew)
            intervalList = insert(intervalList,newInterval)
            print intervalList
            continue
        except KeyboardInterrupt:
            print 'terminated!'
            sys.exit()
        except (nullInterval, invalidIntervalInput):
            print 'Invalid interval!'
	    continue
    
if __name__ == '__main__':
    main()
