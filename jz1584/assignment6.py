from Q1 import *
from Q2 import *
from Q3 import *
from Q4 import *
"""
Note: In this assignment, I use definition of Strictly overlapping as overlapping definition, where the bounds of one interval fall on 
or within the bounds of another interval
"""
print "Q1 testing results:"
a=interval("[1,4]")
b=interval('(2,5]')
c=interval("[4,8)")
d=interval("(-3,9)")
print a, b, c, d
#f=interval("(-2,-1)") #error should be expected
#print f

print "\nNote: Unit-Test for Q2, Q3, Q4 is done in a separated file called Unit_tests.py \n"


from Q5 import *# running program in question 5
