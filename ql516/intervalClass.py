# -*- coding: utf-8 -*-

# Q1: Class  
class interval(object):
    """
    represent a integer interval from a string like: "[x,y]"
    and show whether it is a valid interval
    
    Attribute
    =========
    u : upper bound: True is inclusive 
    l : lower bound: True is inclusive 
    x : lower bound value
    y : upper bound value
    data : a list contain all the integer belong to the interval
    str : the input intrval string
    
    Example
    ========
    >>> a = interval("[3,15)")
    >>> a
    [3,15)
    >>> a.data
    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    >>> b = interval("{1,5}")
    interval bound not found
    Exception
    
    """
    def __init__(self,strr):
        """
        initialize the interval, take a string, return an interval object
        """
        
        # split the string to interval elements
        if strr[0]=='[':
            self.l=True
        elif strr[0]=='(':
            self.l=False
        else :
            raise Exception("interval bound not found")
        if strr[-1]==']':
            self.u=True
        elif strr[-1]==')':
            self.u=False
        else:
            raise Exception("interval bound not found")
        coma_i=strr.index(',')
        self.x=int(strr[1:coma_i])
        self.y=int(strr[coma_i+1:-1])
        self.str = strr
        
        # Verify the interval. 
        #If it is valid , use 'data' denote the list of all the intergers belong to the interval
        self.data=[]
        if self.x>self.y: 
            raise Exception("Error: lower bound > upper bound")
        else:
            if self.u and self.l:                   # closed interval [x,y] 
                self.data=range(self.x,self.y+1)               
            
            if (self.u and (not self.l)) :          # half open interval (x,y]
                if self.x!=self.y: 
                    self.data = range(self.x+1,self.y+1)       
                else : 
                    #print "error:!!1"
                    raise Exception 
            
            if ((not self.u) and self.l) :          # half open interval [x,y)
                if self.x!=self.y: 
                    self.data = range(self.x,self.y)
                else :
                   # print "error:!!2"
                    raise Exception
            
            if ((not self.u)and (not self.l)) :     # open interval (x,y)
                if self.x<self.y-1:
                    self.data = range(self.x+1,self.y)
                else :
                    #print "error:!!!3"
                    raise Exception

    
    def __repr__(self):
        """
        print the inputted String
        """
        return self.str
    
    



