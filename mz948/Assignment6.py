'''
'''
import sys
from Interval.exception import *
from Interval.utility import *
from Interval.Interval import *
def main():
    '''
    This function takes a list of intervals as input and then asks the user to 
    input another interval and try to merge those intervals. 
    '''
    while True:
        try:
            #catch keyboard interruption and EOFerror
            input_string = raw_input('List of intervals?')
        except (KeyboardInterrupt, EOFError):
            sys.exit()
            
            
        # If the user inputs quit or exit, exit the program
        if input_string == 'quit' or input_string == 'exit':
                sys.exit()
        
        try:
            intervals = map(interval,parseIntervalList(input_string))
            break
        except (invalidIntervalListException, invalidIntervalException) as e:
            print e
            continue
                
    #let user input the interval   
    while True:
        try: 
            user_input = raw_input('Interval?')
        except(KeyboardInterrupt, EOFError):
            break
        
        if user_input =='quit' or user_input == 'exit':
            break 
        
        else:
            # Try to merge all the intervals given by user and through exceptions if necessary 
            try:
                new_interval = interval(user_input)
            except (invalidIntervalException) as e:
                print e 
                continue
        
            intervals = insert(intervals,new_interval)
            print intervals
            
if __name__ == '__main__':
    main()