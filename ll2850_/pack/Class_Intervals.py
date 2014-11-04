'''
Created on Nov 2, 2014

@author: leilu
'''
'''
Created on Nov 2, 2014

@author: leilu
'''
from basic_functions import *
from User_defined_Exception import *


class interval():
   
#function that print the interval itself.

    def __repr__(self):
        if self.low_inclusive==True:
            if self.up_inclusive==True:
                return "["+str(self.lo)+"," + str(self.up)+ "]"
            elif self.up_inclusive==False:
                return "["+str(self.lo)+"," + str(self.up)+ ")"
        else:
            if self.up_inclusive==True:
                return "("+str(self.lo)+"," + str(self.up)+ "]"
            elif self.up_inclusive==False:
                return "("+str(self.lo)+"," + str(self.up)+ ")"       


#Define Class Attributes
#self.lo =lower bound of an interval
#self.up = upper bound of an interval
#self.low_inclusive, Boolean, True if "["
#self.up_inclusive, Boolean, True if "]"

    def __init__(self,a):
        if check_interval(a):
            b=a[1:-1].split(",")
            self.lo=int(b[0])
            self.up=int(b[-1])
   
            if a[0]=="[" :#
                self.low_inclusive=True
            else:
                self.low_inclusive=False
            if a[-1]=="]":
                self.up_inclusive=True
            else: 
                self.up_inclusive=False

#This attribute return a real range of numbers given a string: for example, return "[3,4,5]" for [3,5] 
            if self.low_inclusive and self.up_inclusive and self.lo<=self.up:
                self.range = range(self.lo,self.up+1)
            elif self.low_inclusive and not self.up_inclusive and self.lo<self.up:
                self.range = range(self.lo,self.up) 
            elif not self.low_inclusive and self.up_inclusive and self.lo<self.up:
                self.range = range(self.lo+1,self.up+1) 
            elif not self.low_inclusive and not self.up_inclusive and self.lo<self.up-1:
                self.range = range(self.lo+1,self.up)
        
        else:
            raise InvalidIntervalException("Interval given is not valid. Please type in a valid one")
        
            
#This function will merge two intervals,arguments are two strings of interval, such as "[5,6]" and "(4,9)"
#Three possible Exceptions can be raised:1) if one or more intervals is invalid 2)if one or more intervals are of the wrong format 3) the two intervals are not overlapped

def mergeIntervals(int1,int2):
    newinterval=interval('[0,0]')
    ls1=int1.range
    ls2=int2.range
    newls= list (set(ls1)&set(ls2))
   
    if not newls :
        raise IntervalMergeException('These Two intervals are not overlapped.')
    else:
        if int1.lo<=int2.lo:
            newinterval.lo=int1.lo
            newinterval.low_inclusive=int1.low_inclusive
            
            if int1.up<=int2.up:
                newinterval.up=int2.up
                newinterval.up_inclusive=int2.up_inclusive
            else:
                newinterval.up=int1.up
                newinterval.up_inclusive=int1.up_inclusive
        elif int1.lo>=int2.lo:
            newinterval.lo=int2.lo
            newinterval.lo_inclusive=int2.low_inclusive
            if int1.up<=int2.up:
                newinterval.up=int2.up
                newinterval.up_inclusive=int2.up_inclusive
            else:
                newinterval.up=int1.up
                newinterval.up_inclusive=int1.up_inclusive 
      
               
    if newinterval.low_inclusive and newinterval.up_inclusive and newinterval.lo<=newinterval.up:
        newinterval.range = range(newinterval.lo,newinterval.up+1)
    elif newinterval.low_inclusive and not newinterval.up_inclusive and newinterval.lo<newinterval.up:
        newinterval.range = range(newinterval.lo,newinterval.up) 
    elif not newinterval.low_inclusive and newinterval.up_inclusive and newinterval.lo<newinterval.up:
        newinterval.range = range(newinterval.lo+1,newinterval.up+1) 
    elif not newinterval.low_inclusive and not newinterval.up_inclusive and newinterval.lo<newinterval.up-1:
        newinterval.range = range(newinterval.lo+1,newinterval.up)
    
    return newinterval 
  

#Merge a list of intervals
def mergeOverlapping(intlist):
    intlist.sort(key=lambda x:x.lo-0.5*x.low_inclusive)   
    current=intlist[0]
    total=[]
    for i in range(1, len(intlist)):
        try:
            
            current=mergeIntervals(current, intlist[i])
        except:
            total.append(current) 
            current= intlist[i]
        
    total.append(current)
    return total
    

#insert a new interval and merge
def insert(intlist, newint):
    intlist.append(newint)
    return mergeOverlapping(intlist)