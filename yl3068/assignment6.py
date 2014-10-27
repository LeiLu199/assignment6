
import sys
from interval.interval import *

#final program. Take a list of intercals, and when new intervals provided, merge them together.

def main():
        
    while True:
        
        #Ask user to input interval list, if user input ^c, exit game.

        try:
            initial = raw_input('List of intervals?')
        except KeyboardInterrupt:
            print 'bye!'
            sys.exit()
        #If user input 'quit', then quit the game
        if initial == 'quit':
            print 'bye!'
            sys.exit()
        #Check if the input list is valid
        else:

            init_list = initial.split(', ')
            intlist = []
            try:
                for i in init_list:
                    intlist.append(interval(i))
                break
            except InvalidIntervalError:
                print "at least one invalid interval in the interval list, please input again~"
    
    #When user inputs a valid interval list, ask him to input a single interval
    while True:
        try:
 
            addint = raw_input('Interval?')
    
        except KeyboardInterrupt:
            print 'bye!'
            sys.exit()
        
        if addint == 'quit':
            print 'bye!'
            break
        #Merge the original interval list and the new single interval together
        else:
            try:
                newint = interval(addint)
            except InvalidIntervalError:
                print "invalid interval! please input again!"
                continue
            intlist = insert(intlist, newint)
            print intlist

if __name__ == '__main__':
    main()

