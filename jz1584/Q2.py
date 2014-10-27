import re

def extract_value(inputed_interval):  
        """returns the lower bound &upper bound numbers from interval"""
        number_list=re.findall(r'[+-]?\d+',inputed_interval)#create a list contains numbers from inputed interval
        lower_number=int(number_list[0]) 
        upper_number=int(number_list[-1])
        return lower_number, upper_number
    

def list_intervalValue(inputed_interval):
    """returns a list that contains all the elements of the inputed interval  
    """
    int_lower,int_upper=extract_value(inputed_interval)#extract lower & and upper bound numbers from interval
    elements_list=[]#creates a empty list that will contain all possible elements from interval
    if inputed_interval[0]=='[' and inputed_interval[-1]==']': elements_list=range(int_lower,int_upper+1)
    elif inputed_interval[0]=='(' and inputed_interval[-1]==')': elements_list=range(int_lower+1,int_upper)
    elif inputed_interval[0]=='(' and inputed_interval[-1]==']': elements_list=range(int_lower+1,int_upper+1)
    else: elements_list=range(int_lower,int_upper) 
    # the above put elements to the list, which depends on inclusive/exclusive case of interval
    return elements_list


def mergeIntervals(int1,int2):
    """returns two overlap string-typed intervals, 
        inputed intervals should be strings, for example int1="[-2,3]"
    """
    int1_list=list_intervalValue(int1)
    int2_list=list_intervalValue(int2)
    
    if len(set(int1_list).intersection(int2_list)) > 0: # merged If there is at least one common element in both lists
        merge_list=range(min(int1_list[0],int2_list[0]),max(int1_list[-1],int2_list[-1])+1)
        return "[%s,%s]"%(merge_list[0],merge_list[-1])
            
    else:# if there is not common element, then raise exception
        raise Exception("Intervals do not overlap")
        


#testing, works!
#note [-1,7] is the same as (-2,7]
"""
a=mergeIntervals("(-2,3)" ,"(1,7]")
print a 
"""
#non-overlap case:
#c=('[2,20)')
#d=('[21,33]')
#mergeIntervals(c,d)
