"""

script for assignment 6. 

This file prompts the user to input a sequences of intervals. It will attempt to 
sort and merge the inputed intervals. File exits when the user types 'quit'

"""

from interval import interval

# Get initial list
inList = raw_input('List of intervals? ')

isCorrect = False



 
##############################################################################
# Initial Input
##############################################################################

while isCorrect == False:

    if inList == 'quit': 
        #return [] 
        exit()           

    try:
        
        if inList == '': raise Exception           
    
        splitInList = inList.split(', ')
        outList = [interval(x) for x in splitInList]
        
        isCorrect = True
        
    except KeyboardInterrupt:
        
        exit()
        
    except:
        
        isCorrect = False
        print 'Please make your input of the form [a,b], [c,d)], ,,, , [z,y]'
        inList = raw_input('List of intervals? ')
 
##############################################################################
# Subsequent Input
##############################################################################

inputInterval = raw_input('Interval? [TYPE quit TO EXIT] ')

# Check intervals
while inputInterval != 'quit':     
    
    try:
        if inputInterval == '': raise Exception
    
        outList = interval.insert(outList,interval(inputInterval))
        print outList
        
    except KeyboardInterrupt:
        
        exit()
    
    except:
    
        print 'Invalid Interval'
    
    inputInterval = raw_input('Interval? [TYPE quit TO EXIT] ')


