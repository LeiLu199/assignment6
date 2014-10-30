'''

@author: jiminzi
'''
# some input from my own package
import sys
from Intervalpack.intervalfunction import isInputIntervalvalid,formatInterval, isInputIntervalListVaild,\
    formatInputlist
from Intervalpack.Exceptions import InvaildIntervals
#from mj1547 import Interval
from Intervalpack.Intervals import mergeOverLapping, insert, Interval


def main():
 #main function  
    while True:
        try:
            input_list = raw_input("List of intervals? ")
            # to determine the inputlist is valid or not
            if isInputIntervalListVaild(input_list):
                break
            else:
                raise InvaildIntervals('there will have invalid')
        except KeyboardInterrupt:
            sys.exit()
    #start with a new empty ;ost
    int_list = []
    target_stringList = formatInputlist(input_list)
    for x in target_stringList:
        int_list.append(Interval(x))
    int_list = mergeOverLapping(int_list)

    while True:
        try:        
            input_string = raw_input("Interval? ")
            if input_string != 'quit':
          #quit when input quit
                try:
                    interval_list = insert(int_list, Interval(input_string))
                    print '... result ..'
                except:
                    print 'Invalid '
            else:
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()

        print interval_list
    
if __name__ == '__main__':
    main() 