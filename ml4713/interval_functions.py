# -*- coding: utf-8 -*-
"""This file contains:
       interval class constructor
       isMergeable() 
       mergeInterval() 
       mergeOverlapping()
       insert()
"""
from interval_exceptions import *


class interval:
    def __repr__(self):
        return self.lrbd+str(self.lfnum)+','+str(self.rtnum)+self.upbd
        
    def __init__(self,rep):
       """define the input as an interval with 6 attributes:
       self.lfnum represents the left numerical value from the input
       self.rtnum represents the right numerical value from the input
       self.lrbd represents the left parenthesis from the input
       self.upbd represents the right parenthesis from the input 
       self.minval represents the smallest integer number in the interval
       self.maxval represents the largest integer number in the interval
       self.span represents the collection of intergers that are covered in the interval
       """
       self.rep=rep 
       self.num=self.rep[1:-1].split(",")
       self.lfnum=int(self.num[0])
       self.rtnum=int(self.num[1])
       self.lrbd=rep[0]
       self.upbd=rep[-1]
        
 #different comb of parentheses and interval constrains to determin the indication of a interval
       if (self.lrbd=='[' and self.upbd==']') and (self.lfnum<=self.rtnum):
            self.span=range(self.lfnum,self.rtnum+1)
            self.minval=self.lfnum
            self.maxval=self.rtnum
       elif (self.lrbd=='(' and self.upbd==']')  and (self.lfnum<self.rtnum):
            self.span=range(self.lfnum+1,self.rtnum+1)
            self.minval=self.lfnum+1
            self.maxval=self.rtnum
       elif (self.lrbd=='[' and self.upbd==')') and (self.lfnum<self.rtnum):
            self.span=range(self.lfnum,self.rtnum)
            self.minval=self.lfnum
            self.maxval=self.rtnum-1
       elif (self.lrbd=='(' and self.upbd==')') and (self.lfnum<self.rtnum-1):
            self.span=range(self.lfnum+1,self.rtnum)
            self.minval=self.lfnum+1
            self.maxval=self.rtnum-1
       else:
            raise Invalid_Interval_input('Invalid Input')
               
            

def isMergeable(int1,int2):
    """int1 and int2 are assumed to be ordered according to their minvals before implementing this function
       If either conditions is satisfied, then return True:
       1. if two intervals have common elements in their range
       2. if two intervals max and min values are adjacent to each other
    """
    if set(int1.span)&set(int2.span) or int1.maxval+1==int2.minval:
        return True
    else:
        return False


def mergeIntervals(int1,int2): 
    """Before merging two intervals together, sort them according to their minvals,
       return a merged interval in the end if mergeable.
    """
    newint=interval('(-1,1)')    
    if int1.minval>int2.minval or (int2.lrbd=='(' and int1.minval==int2.minval):
       int1,int2=int2,int1
             
    if  isMergeable(int1,int2):
        newrtNum=max(int1.rtnum,int2.rtnum)
        if newrtNum==int2.rtnum:
           newint=interval(int1.lrbd+str(int1.lfnum)+','+str(newrtNum)+int2.upbd)
        else:
           newint=interval(int1.lrbd+str(int1.lfnum)+','+str(newrtNum)+int1.upbd)

    else:
        raise Cant_be_merged('Can\'t be merged')
        
    return newint
        


def mergeOverlapping(intlist):
    """Merge the interval list if there is any mergeable intervals, and return 
       a new interval list. Otherwise, return the original interval list.
    """
    
    intlist.sort(key=lambda x: x.minval)
    newint=[intlist[0]]

    for elem in intlist[1:]:
        try:
            newint[-1]=mergeIntervals(elem,newint[-1])
        except:
            newint.append(elem)
        
    return newint 


 

def insert(intlist,newint):
    """insert newint into intlist, if there is any mergeable intervals, then 
       return the merged interval list. Otherwise, return the original list with new
       interval in a sorted order.
    """
    intlist.append(newint)
    return mergeOverlapping(intlist)