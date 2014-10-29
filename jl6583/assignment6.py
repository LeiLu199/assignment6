'''
Created on Oct 9, 2014

@author: jiayi lu(jl6583)
'''
import sys
import math as mt
import re

from custom_exception import *
from operational_functions import *
from interval import *
from user_interface import *

def main():     
    #get the input list
    interval_list = getInputList()
        
    #Starting to receive separate intervals to be inserted
    #new_interval = getNewInterval()
    while True:
        #Fetching the external input errors including EOF and Keyboard interruptions
        try:
            insert_input = raw_input('Interval? ')
        except (KeyboardInterrupt, EOFError):
            print >> sys.stderr, '\nProgram Terminated by unexpected operation from keyboard or file\n'
            break
        
        #Disposal of the user sponsored termination
        if insert_input == 'quit':
            break
        
        #initialzing the interval with a string
        try:
            new_interval = interval(insert_input)  
            interval_list = insert(interval_list,new_interval)  #this would possibly raise an custom_exception
            print interval_list    
        except (IllegalInterval,EmptySet):
            print >> sys.stderr, 'Invalid interval\n'
            continue
              
if __name__ == '__main__':
    main()
        
    
    
        
        
            