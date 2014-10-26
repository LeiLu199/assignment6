from interval import *

#Q5: main 
def main():
    """
    main function: 
    prompts the user for a list of intervals, reads a string from the user, 
    and creates a list containing these intervals. Once this string has 
    been read, the program should continue prompting for intervals from 
    the user, insert the interval into the list, and display the list at 
    the end of each operation, and correctly validate the input.
        
    
    """

    InputIntervalList=raw_input("List of intervals? ")
    StringIntervalList=InputIntervalList.split(', ')
    intval_list = []
    end = False
    try:    
        for i in range(len(StringIntervalList)):
            intval_list.append(interval(StringIntervalList[i]))
    except:
        print "Invalid Interval List, program end"
        end = True
    while not end:
        NewInterval=raw_input("Interval?")
        if NewInterval=="quit":
            break
        try:
            y_int=interval(NewInterval)
            intval_list=insert(intval_list,y_int)
            print intval_list
        except:
            print 'Invalid Interval'
            continue





if __name__ =="__main__":
    main()