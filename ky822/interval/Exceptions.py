'''
Created on Oct 28, 2014

@author: ds-ga-1007
'''

class InvalidInterval(Exception):
    """Raised when input is not an interval"""
    def __str__(self):
        return 'The input string is not valid!'
    pass
        
class InvalidList(Exception):
    """If the interval list string has an invalid one"""
    def __str__(self):
        return 'The input string has at least one interval that is invalid'
    pass

class NotOverlapInterval(Exception):
    """Raised when intervals do not overlap."""
    def __str__(self):
        return 'The intervals do not overlap!'
    pass
        