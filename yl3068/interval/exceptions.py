
class Error(Exception):
    pass

#Define InvalidIntervalError, raise it when the input interval is invalid
class InvalidIntervalError(Error):
    
    def __init__(self,msg):
        self.msg = msg

#Define NotOverlappingError, raise it when the two intervals to be merged are not overlapping

class NotOverlappingError(Error):

    def __init__(self,msg):
        self.msg = msg


