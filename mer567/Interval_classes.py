"Note: the main body of this function is buggy. I'm aware of that and have tried to fix it any way i know how and somehow i just keep breaking it even more. In particular, if you imput an interval with incorrect bounds it does not alert you to it at first, but then raises the exception after you input a second interval and you can't break out of the loop. I apoligize in advance."



#include packages:

import itertools
import numpy as np
import sys

class Interval_Notation_Error(Exception):
    pass

class Interval_Bounds_Error(Exception):
    pass

class Intervals_Cannot_Merge(Exception):
    pass

class Error_in_user_input(Exception):
    pass

class User_wants_to_quit(Exception):
    pass



class Interval:
    def __init__(self, initial_input):
        #allow for minor user error
        corrected_input = initial_input.replace(" ", "")
        #try:
        self.lower_bound,self.upper_bound, self.lower_bracket, self.upper_bracket= parse_interval(corrected_input)
        ensure_correct_bounds(self.lower_bound,self.upper_bound)
        
    def __repr__(self):
        str = "Interval boundry is %d %d " % (self.lower_bound, self.upper_bound)
        return str
 
    

def parse_interval(initial):

    #parse values and brackets
    parts = initial.split(",")
    lower_bracket = initial[0]
    upper_bracket = initial[-1]

    ensure_correct_notation(parts,lower_bracket,upper_bracket)

    #find lower and upper bound
    lower_bound = int(parts[0][1:])
    upper_bound = int(parts[1][:-1])

    #turn the bounds into inclusive
    if lower_bracket == "(" :# if "("
        lower_bound = lower_bound +1

    if upper_bracket == ")" :
        upper_bound = upper_bound -1

    return lower_bound,upper_bound, lower_bracket, upper_bracket
 

def ensure_correct_notation(parts,lower_bracket,upper_bracket):
    try:
        assert len(parts) == 2
        assert lower_bracket in [ "[" , "("]
        assert upper_bracket in [ "]", ")"]
    except:
        raise Interval_Notation_Error("Interval notation is illegal. ")

def ensure_correct_bounds(lower_bound, upper_bound):
    try:
        assert( lower_bound <= upper_bound)
    except:
        raise Interval_Bounds_Error("these are not legal interval bounds. ")


def mergeIntervals(int1, int2):

    intervals_to_merge = [Interval(int1), Interval(int2)]
 
    transformed_sorted_intervals_to_merge = sorted(intervals_to_merge, key=lambda x: x.lower_bound)

    returned = check_overlap_status(transformed_sorted_intervals_to_merge)
    new_interval = actual_merging(returned, transformed_sorted_intervals_to_merge)
    return new_interval


def check_overlap_status(transformed_sorted_intervals_to_merge):
    ''' This function returns True if invertals are overlapping
    False if one is contained within the other and None if they are neither'''

    # store variables to more readable code
    int1, int2 = transformed_sorted_intervals_to_merge
    lower1, upper1 = int1.lower_bound, int1.upper_bound
    lower2 , upper2 = int2.lower_bound, int2.upper_bound
    

    if lower1<=lower2 and upper1+1 >= lower2: # note that we are adding +1 to upper to account for [1,4]+[5,6] --> [1,6]
        if upper1 <= upper2: #overlap
            return True 

        else: #contained
            return False
    else:
        raise Intervals_Cannot_Merge("Intervals cannot be merged. ")

def actual_merging(s, transformed_sorted_intervals_to_merge):

    int1, int2 = transformed_sorted_intervals_to_merge

    if s == True:  # case of overlapping
        lower = int1.lower_bound
        upper = int2.upper_bound
        lower_bracket = int1.lower_bracket
        upper_bracket = int2.upper_bracket

    else: # case of containment
        lower = int1.lower_bound
        upper = int1.upper_bound
        lower_bracket = int1.lower_bracket
        upper_bracket = int1.upper_bracket

    return format_for_printing(lower, upper, lower_bracket, upper_bracket)

def format_for_printing(lower, upper, lower_bracket, upper_bracket):
    if lower_bracket == "(":
        #subtract to adjust
        lower = lower -1
    if upper_bracket == ")":
        #add to adjust
        upper = upper+1
    return "%s%d,%d%s" % (lower_bracket, lower, upper, upper_bracket)



def mergeOverlapping(all_intervals):
    maximally_merged = []
    all_intervals_sorted = sorted(all_intervals, key=lambda x: Interval(x).lower_bound)

    while len(all_intervals_sorted)>1:
        try: 
            new_interval =  mergeIntervals(all_intervals_sorted[0], all_intervals_sorted[1])
            
            all_intervals_sorted.pop(0) #remove element we are done with
            all_intervals_sorted[0] = new_interval
        
        except (Intervals_Cannot_Merge) as e:
            #print "in the right except" + str(e)
            maximally_merged.append(all_intervals_sorted.pop(0))

    maximally_merged.append(all_intervals_sorted[0]) 
    return  maximally_merged #maximally_merged #merged range!

def insert(intlist, newint): #note that this function changes the actual alist
    intlist.append(newint)
    return mergeOverlapping(intlist)




''' This function parses the user input into a list of intervals based on bracket pairs '''
def parsing_user_input(initial_input):
    if initial_input.lower() == "quit":
        return "quit"
    else:
        parsed_intervals = []
        counter_low = []
        counter_high =[]
        for index, j in enumerate(initial_input):
            if j == "[" or j == "(":
                counter_low.append(index)

            if j == "]" or j == ")":
                counter_high.append(index)

        for x in zip(counter_low,counter_high):
            parsed_intervals.append(initial_input[x[0]:x[1]+1])

        return parsed_intervals

def check_initial_user_input(input_to_check):
    #before parsing 
    parsed_intervals = parsing_user_input(input_to_check)

    if len(parsed_intervals) >1: # if list cycle through and check entry
        if parsed_intervals == "quit":
            raise User_wants_to_quit("Goodbye now")
        else:
            for i in parsed_intervals:
                Interval(i)

    elif parsed_intervals == []:
        raise Error_in_user_input("Your input is unaccceptable, try again")

def check_user_input(input_to_check):
    if input_to_check == "quit":
        raise User_wants_to_quit("Goodbye now")
    else:
        Interval(input_to_check)


##########################
if __name__ == "__main__":

    try: 
        initial_input = raw_input("Please enter a list of intervals:   ")
        #intervaltoadd = "filler garbage"
        parsed_intervals_cum = []
        intervaltoadd = raw_input("Interval? ")

        while (initial_input.lower() != "quit") and (intervaltoadd.lower() != "quit"): # allow for flexibility in user input
            try : 
                check_initial_user_input(initial_input)
                parsed_intervals = parsing_user_input(initial_input)

                #intervaltoadd = raw_input("Interval? ")

                check_user_input(intervaltoadd)

                if parsed_intervals_cum == []:
                    parsed_intervals_cum = insert(parsed_intervals, intervaltoadd)
                else:
                    parsed_intervals_cum = insert(parsed_intervals_cum, intervaltoadd)
                print parsed_intervals_cum
                intervaltoadd = raw_input("Interval? ")

            except User_wants_to_quit as e:
                print str(e)

            except (Interval_Notation_Error, Interval_Bounds_Error) as e:
                print str(e) + "Try again please"
                intervaltoadd = raw_input("Interval? ")

            except Error_in_user_input as e:
                print str(e)
                initial_input = raw_input("Please enter a list of intervals:   ")
    except KeyboardInterrupt as k:
        print " ... Goodbye now!"
        sys.exit()

 
