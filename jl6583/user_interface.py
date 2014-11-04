'''
Created on Oct 27, 2014
user_interface.py contains user interfaces that receives user input
@author: luchristopher
'''

from custom_exception import *
from operational_functions import *
from interval import *

def getInputList():
    '''Taking in a string and parse the string down as the initial list of intervals'''
    while True:
        try:
            input_list = raw_input('List of intervals? ')
        except (KeyboardInterrupt, EOFError):
            print >> sys.stderr, 'Program Terminated by unexpected operation from keyboard or file'
            return None
            sys.exit()
        
        if input_list == 'quit':
            return None
            sys.exit()
        
        #Parse down the input sequence, will flush the input_list when illegal intervals are detected
        try:
            interval_list = map(interval,intervalParser(input_list))
            break
        except (IllegalInterval):
            continue
    return interval_list