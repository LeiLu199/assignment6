from Q3 import mergeOverlapping 
"""
Q3 is the from question 3 function that I created, for simplicity, I just used it for creating new function
"""
def insert(intlist,newint):
    """
    inserts single interval (newint) into a list of non-overlapping intervals (intlist), and 
    merges the overlapping intervals. Returns a single merged interval or a list of merged intervals
    """
    combineList=intlist+','+newint#combines a list of intervals and a new intervals
    MergeIntervalList=mergeOverlapping(combineList) 
    return MergeIntervalList



#testing code, work ! under definition of strictly overlapping
"""
a=insert("[1,3], [6,9]", '[2,5]')
print a
"""
#We know (3,5) is the same as [2,4]

