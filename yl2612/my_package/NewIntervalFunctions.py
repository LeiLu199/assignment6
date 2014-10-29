import re

def isValidInterval(interval_string):
    '''
    check if a single interval is valid
    
    An interval is valid if and only if:
        it has a correct form of ( , ), [ , ), [ , ], ( , ] with only integers inside
        its lower bound is smaller than its upper bound
    '''
    
    #remove whitespace
    interval_string = interval_string.strip()
    
    #store the brackets/parentheses of the interval
    left = interval_string[0]
    right = interval_string[-1]
    
    #check if the interval has a corrent form of ( , ), [ , ), [ , ], ( , ] with integers inside.
    if (left == '(' or left =='[') and (right == ')' or right == ']'):
        try:
            comma = interval_string.find(',')
            
            # item between the comma must be intergers, otherwise the interval is invalid
            lower = int(interval_string[1:comma])
            upper = int(interval_string[comma+1:-1])
            
            # check if the lower bound is small than the upper bound
            if left == '(':
                lower_inclusive = lower + 1
            elif left == '[':
                lower_inclusive = lower             
            if right == ')':
                upper_inclusive = upper - 1
            elif right == ']':
                upper_inclusive = upper
                
            if lower_inclusive <= upper_inclusive:
                return True
            else:
                return False                  
        except:
            return False
    else:
        return False

def splitIntervalString(interval_string):
    '''
    split the interval string
    ''' 
    
    #get the lower and upper bound brackets/parentheses
    interval_string = interval_string.strip()
    left = interval_string[0]
    right = interval_string[-1]
   
    #parse the lower and upper bound numbers
    int_string=interval_string.strip('()[]').split(',')
    
    #get the lower and upper bound numbers
    lower = int(int_string[0].strip())
    upper = int(int_string[-1].strip())

    return (left,right,lower,upper)
    

def getTrueValue(left, right, lower, upper):
    '''
    get the true value of lower and upper bound
    '''
    
    if left == '(':
        lower_inclusive = lower + 1
    elif left == '[':
        lower_inclusive = lower
    if right == ')':
        upper_inclusive = upper - 1
    elif right == ']':
        upper_inclusive = upper
    else:
        return False
    return (lower_inclusive, upper_inclusive)


def isValidIntervalList(interval_list_input):
    '''
    check if a list of interval input is valid
    '''
    
    #remove the whitespace
    interval_list_input = interval_list_input.strip()
    
    #find all intervals with bracket/parenthesis + at least one number(inclding negative number and 0) + comma + at least one number(inclding negative number and 0) + bracket/parenthesis
    store_list_input = re.findall (r'[\[\(\)\]]+-*[0-9]+\,+-*[0-9]+[\)\]\(\[]+', interval_list_input)
    
    if store_list_input == []:
        return False
    
    #check the form of intervals
    for item in store_list_input:
        if isValidInterval(item):
            continue
        else:
            return False
    return True


def splitIntervalList(interval_list_input):
    '''
    split intervals by locating the comma between two closed intervals 
    '''
    
    split_list_interval = re.split('(?<=[\]\)])\s*,\s*', interval_list_input)
    return split_list_interval
