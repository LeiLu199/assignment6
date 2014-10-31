# -*- coding: utf-8 -*-

from intervalClass import *
from IntervalExceptions import *

def isOverlaping(int1,int2):
     """
     Given two intervals int1 and int2, return whether they are overlapping
     """
     Set1 = set(int1.data)
     Set2 = set(int2.data)
     if (Set1-Set2) == Set1:                
        return False
     else:
        return True





#Q2: mergeIntervals()        
def mergeIntervals(int1, int2):
    """
    this function used to merge two interval together
    
    Arguments
    =========
    int1, int2 : interval object
    
    Return
    ======
    interval object contain all the integers in int1 and int2
    
    Example
    =======
    >>> a = interval('[2,8)')
    >>> b = interval("[5,10]")
    >>> print mergeIntervals(a,b)
    [2,10]
    >>> b = interval("[8,10]")
    >>> print mergeIntervals(a,b)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 19, in mergeIntervals
    Exception: Not Overlap !
    
    """
    if not isOverlaping(int1,int2):                 #raise exception 
        raise NotOverlap()               
    
    else:
        if int1.x<int2.x:
            MergedInterval_x=str(int1.x)
            if int1.l: MergedInterval_low='['
            else: MergedInterval_low='('
        else:
            MergedInterval_x=str(int2.x)
            if int2.l: MergedInterval_low='['
            else: MergedInterval_low='('
        
        if int1.y>int2.y:
            MergedInterval_y=str(int1.y)
            if int1.u :
                MergedInterval_up=']'
            else:
                MergedInterval_up=')'
        else:
            MergedInterval_y=str(int2.y)
            if int2.u :
                MergedInterval_up=']'
            else:
                MergedInterval_up=')'
        MergedInterval= MergedInterval_low+MergedInterval_x+','+MergedInterval_y+MergedInterval_up
        return interval(MergedInterval)
        





def mergable(int1,int2):
    """
    Check whether intervals int1 can be merged with int2.
    
    Arguments
    =========
    int1, int2 : interval objects
    
    Return
    ======
    Boolean: True: can merge
    
    Example
    =======
    >>> a = interval("[1,6)")
    >>> b = interval("[6,10]")
    >>> mergable(a,b)
    True
    >>> c = interval("[10,16)")
    >>> d = interval("(0,3)")
    >>> mergable(c,d)
    False
    
    """
    
    if int1.data[0]<=int2.data[0]:
        FirstInterval=int1
        SecondInterval=int2
    else:
        SecondInterval=int1
        FirstInterval=int2
        
    # return true if l1's last integer is not less than l2's first integer minus 1
    return (FirstInterval.data[-1]>=SecondInterval.data[0]-1)




    
def merge(int1,int2):
    """
    Given two interval int1, int2, merge them together when they are mergable,
    Different from function mergeIntervals when int1 and int2 are mergable and not overlaping
    
    Notice: only used when int1 can be merged with int2
    
    Arguments
    =========
    int1, int2 : interval object
    
    Return
    ======
    interval object contain all the integers in int1 and int2
    
    Example
    =======
    >>> a = interval('[2,8)')
    >>> b = interval("[5,10]")
    >>> print merge(a,b)
    [2,10]
    >>> b = interval("[8,10]")
    >>> print merge(a,b)  
    [2,10]
    
    
    """
    if mergable(int1,int2):
        if int1.x<int2.x:
            MergedInterval_x=str(int1.x)
            MergedInterval_low = '[' if int1.l else '('
        else:
            MergedInterval_x=str(int2.x)
            MergedInterval_low = '[' if int2.l else '('
        
        if int1.y>int2.y:
            MergedInterval_y=str(int1.y)
            MergedInterval_up = ']' if int1.u else ')'
        else:
            MergedInterval_y=str(int2.y)
            MergedInterval_up = ']' if int2.u else ')'
            
        MergedInterval= MergedInterval_low+MergedInterval_x+','+MergedInterval_y+MergedInterval_up
        return interval(MergedInterval)   






#Q3: mergeOverlapping function
def mergeOverlapping(IntervalList):
    """
    take a list of intervals and merges all overlapping intervals
    
    Arguments
    =========
    IntervalList: a list of interval objects
    
    Return
    ======
    a list of intervals after merging all the overlapping intervals
    
    Example
    =======
    >>> a =[interval("[1,5]"), interval("[2,6)"), interval("(8,10]"), interval("[8,18]")]
    >>> mergeOverlapping(a)
    [[1,6), (8,18]]
    
    
    """
    
    #Sort the interval list by their first integer
    SortedList = sorted(IntervalList,key=lambda intva: intva.data[0])
    ListLength=len(SortedList)
    head =SortedList[0]                             #head pointer   
    newList = []
    for i in range(1,ListLength):
        if mergable(head,SortedList[i]):
            head=merge(head,SortedList[i])
        else:
            newList.append(head)
            head=SortedList[i]
    newList.append(head)
    return newList







#Q4: insert()
def insert(intlist,newint):
    """
    The function insert interval "newint" into interval list "intlist", 
    merging the result if necessary
    
    Arguments
    =========
    intlist: a list of interval objects 
    newint : interval 
    
    Return
    ======
    a list of intervals
    
    Example 
    =======
    >>> a =[interval("[1,2]"), interval("(3,5)"), interval("[6,7)"),interval("(8,10]"), interval("[12,16]")]
    >>> b = interval("[4,9]")
    >>> print insert(a,b)
    [[1,2], (3,10], [12,16]]
    
    """
    
    intlist.append(newint)
    return mergeOverlapping(intlist)

