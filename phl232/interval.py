"""

This module implements a class that represents an integer inverval. The interval 
is stored as upper and lower bounds and bound type i.e. open or closed.

It also contains methods for operations for lists of intervals

Example:

  interval1 = interval('(-1,100]')
  interval2 = interval('(2,5)')  
  
  interval.mergeInterval(interval1,interval 2)  

Attributes:

    inStr:  input string
    upper:  upper bound
    lower:  lower bound
    upperType:  bound type i.e. ( or [
    lowerType:  bound type i.e. ) or ]
    max:    maximum element in the set
    min:    minimum element in the set
  
Methods:

    __setRange:   sets attributes by parsing self.inStr
    __setStr:     set inStr from attributes
    
Static Methods:

    mergeInterval:  method to merge to intervals
    mergeOverlapping:     merge a list of intervals. !!! Will sort original input !!!
    insert:   inserts an interval into a list of interals and sorts on lower

"""

import intervalExceptions

class interval(object):

    boundDef = {'(': 'exclusive', ')': 'exclusive', '[': 'inclusive', ']': 'inclusive'}
    
    # Constructor

    def __init__(self,inStr):
        
        self.inStr = inStr  
        
        if len(inStr)>0:
            self.__setRange()

##############################################################################        
# Methods
##############################################################################
    
    def __setRange(self):
        
        try:        
        
            intervalRange = [int(x) for x in self.inStr[1:-1].split(',')]
            
            # Upper and lower bounds of set
            self.upper = intervalRange[1]
            self.lower = intervalRange[0]
                
            self.upperType = self.inStr[-1]
            self.lowerType = self.inStr[0]
                    
            # Max and min of set elements
            self.max = self.upper if interval.boundDef[self.upperType] == 'inclusive' else self.upper - 1 
            self.min = self.lower if interval.boundDef[self.lowerType] == 'inclusive' else self.lower + 1
            
            if self.max < self.min: raise intervalExceptions.invalidIntervalError
        
        except:
            
            raise intervalExceptions.invalidIntervalError           
            
    def __setStr(self):
        
        self.inStr = self.lowerType + str(self.lower) + ',' + str(self.upper) + self.upperType
    
    def __repr__(self):
        
        return self.inStr
        
    def __eq__(self, other): 
        return self.inStr == other.inStr

##############################################################################        
# Static Methods
##############################################################################
    
    @staticmethod
    def mergeIntervals(interval1,interval2):
    
        interval1.__setRange()
        interval2.__setRange()
        
        if interval1.min < interval2.min:
            lowerInterval = interval1
            upperInterval = interval2 
        else:
            lowerInterval = interval2
            upperInterval = interval1
    
        out = interval('')
            
        # Merge intervals by case
            
        # if disjoint
        if lowerInterval.max < upperInterval.min - 1:
            
            raise intervalExceptions.disjointIntervalsError
        
        # non-trivial intersection 
        elif lowerInterval.max <= upperInterval.max:
            
            out.lowerType = lowerInterval.lowerType 
            out.lower = lowerInterval.lower
            out.upper = upperInterval.upper
            out.upperType = upperInterval.upperType 
            
        # if upper is contained in lower
        else:
            
            out.lowerType = lowerInterval.lowerType 
            out.lower = lowerInterval.lower
            out.upper = lowerInterval.upper
            out.upperType = lowerInterval.upperType 
            
        out.__setStr()
        
        return out
    
    @staticmethod    
    def mergeOverlapping(intervalList):
        
        map(lambda x: x.__setRange(),intervalList)
        
        # Sort intervals on lower bound
        intervalList.sort(key = lambda x: x.min)
        
        outList = []
        merged = intervalList[0] 
        
        # try to merge, if disjoint then move on down the list...this is OK since
        # we already sorted
        for idxList in range(len(intervalList)):
        
            try:
                merged = interval.mergeIntervals(merged,intervalList[idxList])
            except intervalExceptions.disjointIntervalsError: 
                outList.append(merged)
                merged = intervalList[idxList]
                
        outList.append(merged)
         
        return outList           
    
    
    @staticmethod
    def insert(intervalList, newInterval):
               
        intervalList.append(newInterval)
           
        outList = interval.mergeOverlapping(intervalList)
        outList.sort(key = lambda x: x.lower)
        
        return outList