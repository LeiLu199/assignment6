import sys
from Interval import *
from NewIntervalFunctions import *
from Exceptions import *

def main():
    '''
    demostrate how to use the interval class and APIs.
    '''
    
    while True:
        try:
            
            # prompt user for a list of interval
            new_input = raw_input('List of intervals? ')
            
            # exit the program if the users type 'quit'
            if new_input == 'quit':
                sys.exit()
                
            # if the list is valid, split the list into intervals and store them.
            elif isValidIntervalList(new_input):           
                list_input = []
                store_list_input = splitIntervalList(new_input)
                for item in store_list_input:
                    list_input.append(interval(item))
                break
            
            #raise exception if the list is invalid
            else:
                raise invalidIntervalList('At least one interval is invalid.')
            
        except KeyboardInterrupt:
            sys.exit()
            
    while True:
        try:
            
            # continue prompting for intervals
            add_input = raw_input('Intervals? ')
            
            # exit the program if user types 'quit'
            if add_input == 'quit':
                sys.exit()
                
        except KeyboardInterrupt:
            sys.exit()
            
        try:
            
            #insert the new interval into the list
            add_input = interval(add_input)
            list_input = insert(list_input,add_input)
            print list_input
            
        except:
            print "Invalid Interval"
            continue
            
                  
    print list_input

if __name__ == '__main__':
        main()