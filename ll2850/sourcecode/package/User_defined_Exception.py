'''
Created on Oct 25, 2014

@author: leilu
'''

#Raised when the interval is invalid: 
class InvalidIntervalException(Exception):
    pass

class IntervalFormatIssueException(Exception):
    pass

#Raised when two intervals are not overlapping
class IntervalMergeException(Exception):
    pass

#Raised when at least one interval among the list is invalid
class IntervallistsException(Exception):
    pass
