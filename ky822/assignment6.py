'''
Created on Oct 28, 2014

@author: ds-ga-1007
'''
import sys
from interval.Interval import *
from interval.basicFunctions import *
from interval.Exceptions import *

def main():
    """
    Main function takes a list of intervals as input and asks the user to input intervals
    and merge them together. 
    """
    # The input interval should be correct
    while True:
        try:    
            # Request to input a list of interval
            new_input = raw_input('List of intervals?')
            #User can use 'quit' or 'exit' to terminate the program            
            if new_input == 'quit' or 'exit':
                print 'exit program'
                sys.exit()     
                 
        except KeyboardInterrupt:
            sys.exit()
        try:    
            if isInputIntervalListValid(new_input):
                break
            else:
                raise InvalidList()
        except KeyboardInterrupt:
            sys.exit()
      
    #Split the list string into intervals.
    #And then merge them into intlist which is a list of intervals.  
    splited_new_input = splitIntervalList(new_input)
    interval_list = []
    for interval in splited_new_input:
        interval_list.append(interval)
    interval_list = mergeOverlapping(interval_list)
    
    while True:
        # Request to get intervals input
        try:
            interval_added = raw_input('Intervals?')
            #User can use 'quit' or 'exit' to terminate the program            
            if new_input == 'quit' or 'exit':
                print 'exit program'
                sys.exit() 
        except KeyboardInterrupt:
            sys.exit()
        try:
            #insert the new interval into the interval_list
            interval_list = insert(interval_list, interval(interval_added))
            print interval_list
        except (InvalidInterval):
            print 'Invalid Interval'
            continue
        
        print interval_list

if __name__ == '__main__':
    main()


        
            
            
        
        