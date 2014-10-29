from Q1 import * #import class from question 1
from Q3 import mergeOverlapping #import mergeOverlapping function from question 3


print "The following program will insert and merge intervals from user's inputed interval strings, \nand print out the list of merged interval"
print "If you want to quit the program, please enter: quit\n" #print out program notification
temp="" #saved all user-input string interval
a=1
while a>0:#using while loop for continuing prompting for intervals from user
    initial=raw_input('please enter an interval :')
    if initial == "quit":
        break
    try:
        
        check=interval(initial)#checks if it's valid interval by using class from question 1
        temp=temp+","+initial #adds the valid interval to existing string intervals
        cumulative_interval=mergeOverlapping(temp)
        print cumulative_interval
        
    except:
        print" Invalid interval"
        
