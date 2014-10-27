from intervalExceptions import *
import re

#The class of interval
class interval:
        def __init__(self, intervalString):
                #Remove the spaces, and record the string
                self.expr = intervalString.replace(" ", "")

                #If the interval is invalid, raise exception
                if re.match(r"^[\[\(]\s*-?\d+\s*\,\s*-?\d+\s*[\)\]]$", self.expr) == None:
                        raise InitErr("Invalid interval")

                        self.valid = False
                        return

                #Extract the lower and upper bound
                self.lBound = self.expr[0]
                self.uBound = self.expr[-1]

                #Extract the numbers of bound
                boundNum = self.expr.strip("()[]").split(",")
                self.boundNum = [int(i) for i in boundNum]

                #Calculate the actual first number in the interval
                self.firstNum = self.boundNum[0]
                if self.lBound == "(":
                        self.firstNum = self.boundNum[0] + 1

                #Calculate the actual last number in the interval
                self.lastNum = self.boundNum[1]
                if self.uBound == ")":
                        self.lastNum = self.boundNum[1] - 1

                #Check the interval is reasonable or not
                if self.firstNum > self.lastNum:
                        raise InitErr("Invalid interval")

                        self.valid = False
                        return

                #Everything is fine, so validity of the interval is ensured
                self.valid = True

        def __repr__(self):
                #Print the content of the interval in the given format
                return self.expr + " represents the number " + str(self.firstNum) + " through " + str(self.lastNum)


