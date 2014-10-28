'''
Created on Oct 27, 2014
'exceptions.py' contains all customized exceptions.
@author: luchristopher
'''
class CustomException(Exception):
    '''Base class for customized exceptions'''
    def __init__(self,arg_prompt_message):
        self.prompt_message = arg_prompt_message
        
    def __str__(self):
        return self.prompt_message

class IllegalInterval(CustomException):
    '''Class inherited from CustomException, raised when the string expression of intervals are not in valid forms'''

class EmptySet(CustomException):
    '''Class inherited from CustomException, raised when the string expression of intervals represents a empty interval'''
    
class UnexpectedType(CustomException):
    '''Unexpected type for the interval()''' 

class NotOverlapping(CustomException):
    '''Intervals not overlapped'''