from intervalClass import *
from intervalExceptions import *
import os
import sys
import re
import numpy as np

#Return true if it matches the regular expression of interval
def validOrNot(intervalString):
        if re.match(r"^[\[\(]\s*-?\d+\s*\,\s*-?\d+\s*[\)\]]$", intervalString) == None:
                return False
        return True

#Determine that two intervals are overlapped or not
def overlappedOrNot(int1, int2):

        #Sort it by the order of boundNum[i], firstNum, lastNum, and boundNum[1]
        intlist = sorted([int1, int2], key = lambda i: (i.boundNum[0], i.firstNum, i.lastNum, i.boundNum[1]))

        #If the two intervals are not overlapped, return False
        if intlist[0].lastNum + 1 < intlist[1].firstNum:
                return False
        return True

#Merge two intervals, and return the result
def mergeIntervals(int1, int2):

        #Check the two intervals are overlapped or not
        if not overlappedOrNot(int1, int2):
                raise MergeErr

        #Find the new lower and upper bound by comparing the two intervals
        forLower = sorted([int1, int2], key = lambda i: (i.boundNum[0], i.firstNum))
	forUpper = sorted([int1, int2], key = lambda i: (i.boundNum[1], i.lastNum), reverse=True)

        #Return the merged interval
        return  interval( forLower[0].lBound + str(forLower[0].boundNum[0]) + "," + str(forUpper[0].boundNum[1]) + forUpper[0].uBound )


#Sort the given list of intervals and merge any two of overlapped intervals
def mergeOverlapping(intervalList):

        #Sort the list by the order of boundNum[i], firstNum, lastNum, and boundNum[1]
        intervalList =  sorted(intervalList, key = lambda i: (i.boundNum[0], i.firstNum, i.lastNum, i.boundNum[1]))

        #Create a stack for merge algorithm, and move the first item to it from intervalList
        stack = [intervalList[0]]
        intervalList.pop(0)

        #Loop until intervalList is empty
        while len(intervalList) != 0:

                #Merge the top in the stack and the first in intervalList if they are overlapped
                if overlappedOrNot(stack[-1], intervalList[0]):
                        stack[-1] = mergeIntervals(stack[-1], intervalList[0])
                #If they are not overlapped, push the first in intervalList to the stack
                else:
                        stack.append(intervalList[0])
                #Pop up the the first in the intervalList
                intervalList.pop(0)

        return stack


#Append the given interval on a list of intervals, and merge if neccessary
def insert(intervalList, newint):
        return mergeOverlapping(intervalList+[newint])


#Initailize the an list of intervals by the given string
def set_interval_list(intervalListString):
        #Split the string into strings of intervals
	intervalRegularExpression = re.compile(r"[\[\(]\s*-?\d+\s*\,\s*-?\d+\s*[\)\]]")
	intervalListString = intervalRegularExpression.findall( intervalListString )

	#If the intervals list is empty, raise initialization exception
	if len(intervalListString) == 0:
		raise InitErr("Invalid intervals")

        #Remove spaces
        intervalListString = [i.replace(" ", "") for i in intervalListString]



        #For each interval, initialize it
        intervalList = []
        for i in intervalListString:
                tmpint = interval(i)
                if not tmpint.valid:
                        return []
                intervalList.append( tmpint )

        #Return the list of intervals
        return intervalList


#Print the content in the list of intervals
def print_interval_list(intervalList):
        for i in range(len(intervalList)-1):
                print intervalList[i].expr + ", ",

	print intervalList[-1].expr
