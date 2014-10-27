import re

def convert_interval(interval_list):
    """takes a list of string-type intervals 
        returns a list of 'inclusive' tuples for further use
    """
    content=re.findall(r'[+-]?\d+', interval_list)#gets content from all intervals 
    num_list=[int(i) for i in content]#collects the content of all intervals to a list of integers 
    symbol_list=re.findall(r'[()[\]]', interval_list)#lists all the corresponding symbols( eg. (,],).[) from intervals 
       
    for i in range(len(symbol_list)):#convert a string list of interval to  equivalent inclusive range
        if symbol_list[i]== ")":
            num_list[i]=num_list[i]- 1
        if symbol_list[i]== "(":
            num_list[i]=num_list[i]+ 1
    #print num_list 
    tuple_list=[]#create an empty list that will contain the corresponding tuple of each interval
    for i in range(0 ,len(num_list)-1,2):#for example, in integers case, tuple (3,5) represents [2,4]
        tuple_list.append((num_list[i],num_list[i+ 1]))
    return tuple_list 

def merging(tuples):
    """returns a list of or a single 'tuple' after merging
    """
    tuples.sort()#sorts the list of tuples
    def slim(tuples,diff):
        """checks each tuple once upon a time 
            merges any tuples that have common elements
        """
        init=len(tuples)-diff-1
        if init<1: 
            return tuples
        if tuples[init][0]>tuples[init-1][1]:
            return slim(tuples,diff+1)
        else:
            tuples[init-1]=((tuples[init][0],tuples[init-1][0])[tuples[init-1][0]<tuples[init][0]],(tuples[init][1],tuples[init-1][1])[tuples[init-1][1]>tuples[init][1]])
            del tuples[init]
            return slim(tuples,0)
    return slim(tuples,0)

def mergeOverlapping(intlist):
    """return a list of merged intervals or a single interval in inclusive-interval form
    """
    list_tuple=convert_interval(intlist)
    mergeTuple=merging(list_tuple)

    output_interval=[]
    for i in mergeTuple:
        output_interval.append(list(i))#converts tuple form back to interval form
    return output_interval
    



"""
#testing codes, works!
#print "Note:Merged all intervals into equivalent inclusive-interval form:"
intlist='[1,5], [2,7), (8,10], [8,18]'
a=mergeOverlapping(intlist)
print a 
"""


