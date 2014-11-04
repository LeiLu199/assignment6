import re
class interval:
    """
    class take string representation of the interval 
    """
    def __init__(self,input):
        self.input=input
        number_list=re.findall(r'[+-]?\d+',self.input)#extract numbers from inputed interval 
        lower_bound_num=int(number_list[0])
        upper_bound_num=int(number_list[-1])
        
        #The following conditions shows the requirement for interval bounds
        if self.input[0]=="[" and self.input[-1]==']':# both bounds are inclusive case
            if lower_bound_num > upper_bound_num: raise ValueError ("Invalid interval: lower must not be more than upper if both bounds are inclusive ")
          
        
        elif self.input[0]=="(" and self.input[-1]==')':#both bounds are exclusive case
            if lower_bound_num>=upper_bound_num-1:
                raise ValueError ("Invalid interval: lower must be less than upper - 1 if both bounds are exclusive ")
        
        else: #either bounds is exclusive or inclusive case
            if lower_bound_num>=upper_bound_num:
                raise ValueError ("Invalid interval: lower must be less than upper if either bounds is inclusive ")
    
    
    def __repr__(self):
            return "%s" %(self.input)
        



#Code testing, works!
#Example case testing
"""
a=interval("[1,4]")
b=interval('(2,5]')
c=interval("[4,8)")
d=interval("(3,9)")
print a, b, c, d
"""
#error cases testing:
#f=interval("(-1,-1)") 
#error should be expected
#print f




    