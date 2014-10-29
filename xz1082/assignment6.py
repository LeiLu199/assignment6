"""
Assignment6.py
"""
import sys
from interval.intervals import *
from interval.utility import *

def main():
    '''
    Take a list of intervals as inputs, ask the user to input more intervals, and try to merge it into the interval list.
    '''
    #check if input interval list is correct.
    while True:
         #exit when user input 'quit' or CTRL-C.
        try:
            new_input = raw_input('List of intervals?')
            if new_input == 'quit':
                sys.exit()
        except KeyboardInterrrupt:
            sys.exit()
        
        #parse string as intervals.
        try:
            interval_list = map(interval, parseIntervals(new_input))
            break
        except (invalidIntervalException, invalidIntervalListException) as e:
            print e
            continue
    
    #take more intervals from the user
    while True:
        try:
            interval_input = raw_input('Intervals?')
            if isvalid_interval(interval_input) == False:
                raise invalidIntervalException()
            if interval_input =='quit':
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()

        #turn input string into an interval and insert it into the list
        try:
            new_interval = interval(interval_input)
        except (invalidIntervalException) as e:
            print e
            continue
    
        interval_list = insert(interval_list, new_interval)    
        print interval_list

        
if __name__ == '__main__':
    main()

