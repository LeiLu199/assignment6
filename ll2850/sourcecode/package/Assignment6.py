'''
Created on Oct 25, 2014

@author: leilu
'''
from package.Class_Intervals import *
from basic_functions import *
from User_defined_Exception import *
import re

'''
main function:
It will generate an original list of intervals based on user's input
First check whether the original list if valid
if it is: Pop questions asking for new interval from user
merge user's interval into the original list
'''
def main():
    s=raw_input('List of intervals?').replace(" ", "")
    regular=re.findall(r'[\(\[]{1,1}-*[0-9]+,{1,1}-*[0-9]+[\)\]]{1,1}',s)#use regular expression to identify valid intervals in users' input
    stringlist=[]
    if regular==[]:
        raise IntervallistsException("At Least One of Intervals in The Starting Lists Is Invalid.")
    else:         
        for i in range(len(regular)):
            stringlist.append(interval(regular[i]))
  
    while True:
        user=raw_input("Intervals?")
        if user=="quit":
            break
        else:
            stringlist = insert(stringlist, interval(user))
            
        print "The Current Merged Interval Is ", stringlist
    
    
if __name__=="__main__":
    main()


    