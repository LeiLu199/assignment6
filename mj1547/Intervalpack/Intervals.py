'''

@author: jiminzi
'''

#from mj1547.intervalpack.intervalfunction import *
from Intervalpack.intervalfunction import isInputIntervalvalid,\
    formatInputlist, formatInterval
from Intervalpack.Exceptions import InvaildIntervals, NoOverLapping

class Interval():
    
    def __init__(self,intervalstring):
        if isInputIntervalvalid(intervalstring):
            #delete all the blank in strings
            intervalstring = intervalstring.replace(" ", "")
            
            self.intervalstring=intervalstring
            # make it to as the formmat of my intervals
            self.left_bound_mark,self.lowbound,self.real_left_value,self.upbound,self.real_right_value,self.right_bound_mark = formatInterval(intervalstring) 
        else:
            raise InvaildIntervals('invalid')
        # raise a exception when it is invalid
    def __repr__(self):
        return  self.intervalstring
    #self.left_bound_mark+str(self.left_string)+','+str(self.right_string)+self.right_bound_mark

def mergeIntervals(int1,int2):
    '''
    function which campare with two intervals and determine merge or not
    '''
    # firstly. to detemine there has overlap or not, by campare the real_value which I set to represent the value in interval
    while (int1.real_right_value<(int2.real_left_value-1)) or int2.real_right_value<(int1.real_left_value-1):
        raise NoOverLapping('no overlap')
     #begin wirh a     
    mergeIn=''
    #merge new intervals by campare the numbers
    if int1.real_left_value <= int2.real_left_value and int1.lowbound <= int2.lowbound:
        mergeIn=mergeIn+'{}{},'.format(int1.left_bound_mark,int1.lowbound)
    else:
        mergeIn=mergeIn+'{}{},'.format(int2.left_bound_mark,int2.lowbound)
    if int2.real_right_value< int1.real_right_value and int1.upbound < int2.upbound:
        mergeIn=mergeIn+'{}{}'.format(int1.upbound,int1.right_bound_mark)
    else:
        mergeIn=mergeIn+'{}{}'.format(int2.upbound,int2.right_bound_mark)
    #write the interval with new notation and values
    newmerge=Interval(mergeIn)
    return newmerge
    
def mergeOverLapping(intlist):
    '''
    merge the inputlist one by one 
    '''
    for interval in intlist:
        if isInputIntervalvalid(str(interval)):
            continue
        else:
            raise InvaildIntervals(' interval in the intlist is invalid!')
    def sortkey(a):#sort by the real_left value
        return a.real_left_value
    intlist =sorted(intlist,key = sortkey)
    new_list = []
    temp=intlist[0]
    x=len(intlist)-1
    '''
    use for loop to campare the intervals one by one and use the mergerInterval() function to merge
    '''
    for i in range(x):
        try:
            temp=mergeIntervals(temp, intlist[i+1])
        except:
            new_list.append(temp)
            temp=intlist[i+1]
    new_list.append(temp)
    return new_list

def insert(intlist,newinterval):
    '''
    it is the insert function
    insert the new interval and use MERGEoverlapping() function to merge them
    '''
    intlist.append(newinterval)
    return mergeOverLapping(intlist)