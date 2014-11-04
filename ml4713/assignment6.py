# -*- coding: utf-8 -*-
"""
This is Programming for Data Science Homework6 script file.
Mengfei Li (ml4713)
"""
import sys
import re
from interval_functions import *


def main():
    """In the main function, the user is asked to input a series of intervals which are automatically
       coverted to a list. After the initial input, the user is asked to input a new interval and the program
       will merge the interval to the list that is created before if mergeable. Otherwise, the program will update
       the list with new input interval. The program keeps going until the user hit "quit".
    """
    
    while True: 
        try:
          listofint=raw_input('List of intervals? ')
          if listofint!='quit':
              try:
                 listofint=[interval(x) for x in re.split('(?<=[\]\)])\s*,\s*', listofint)]
                 break
              except (Invalid_Interval_list_input, ValueError):
                 print "invalid interval list"
          elif listofint=='quit':  
               sys.exit()
        except KeyboardInterrupt:
               sys.exit()
        
        
    while True:    
        try:
           newinput=raw_input('Interval? ')
           if newinput=='quit':
              sys.exit()
        
           else:
             try:
                listofint=insert(listofint,interval(newinput))
                print listofint
             except (Invalid_Interval_input,ValueError):
                print 'Invalid Interval'
                continue
        
        except KeyboardInterrupt:
               sys.exit()

if __name__=='__main__':
    main()
    

    
    
    

