'''

@author: jiminzi
'''
import re
def isInputIntervalvalid(inputintervalstring):
    '''a function to check the inputstring is obey the format of interval or not'''
    #delete all the blank spaces
    inputintervalstring=inputintervalstring.replace(" ", "")
    # firstly,check the interval in a format begin with'('or'['and end with')'and "]"
    if (inputintervalstring[0]=='('or inputintervalstring[0]=='[')and (inputintervalstring[-1]==')'or']'):
        try:
            #now just split interval two parts by the comma ,
            split_string = re.split('[,:]',inputintervalstring)
            #
            left_string = split_string[0]
            right_string = split_string[-1]
              # and now make the left part string as like a integer
            lowbound = int(left_string[1:])
            upbound = int(right_string[0:-1])
            #and mention the left and right markers
            left_bound_mark=str(left_string[0])
            right_bound_mark=str(right_string[-1])
            #and now find the real value of the input interval by different marker [ ]or()
            if left_bound_mark =='(':
                real_left_value=lowbound+1
            else:
                real_left_value=lowbound
            if right_bound_mark == ']':
                real_right_value=upbound
            else:
                real_right_value=upbound-1
            if real_left_value <= real_right_value:
                return True
            else:
                return False
        except:
            return False
        
def formatInterval(inputintervalstring):
    ''' a function which a try to make the interval be my interval format'''
    split_string = re.split('[,:]',inputintervalstring)
     
    left_string = split_string[0]
    right_string = split_string[-1]
     #and now make the left part string as like a integer
    lowbound = int(left_string[1:])
    upbound = int(right_string[0:-1])
            #and mention the left and right markers
    left_bound_mark=str(left_string[0])
    right_bound_mark=str(right_string[-1])
    if left_bound_mark =='(':
        real_left_value=lowbound+1
    else:
        real_left_value=lowbound
    if right_bound_mark == ']':
        real_right_value=upbound
    else:
        real_right_value=upbound-1
    return (left_bound_mark,lowbound,real_left_value,upbound,real_right_value,right_bound_mark)
        
def isInputIntervalListVaild(listinputstring):
    '''
    a function the list is valid or not
    make the list became several intervals 
    and then use the isInputIntervalvalid() function to determine
    '''
    listinputstring=listinputstring.replace(" ", "")
    stringlist = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\)\]]+', listinputstring)

    for x in stringlist:
        if isInputIntervalvalid(x):
            continue
        else:
            return False
    return True
'''
a function which I used to make the list be my Interval list format
'''
def formatInputlist(listinputstring):
    #delete blanks
    listinputstring= listinputstring.replace(" ", "")
    #split the list to servaral intervals
    stringlist=re.findall(r'[\[\(]{1,1}-{0,1}[0-9]+\,+-{0,1}[0-9]+[\)\]]{1,1}',listinputstring)
    return stringlist