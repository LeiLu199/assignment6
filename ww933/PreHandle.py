__author__ = 'chianti'

import re

#IsValidPattern tests that whether the input matches the pattern:
#                             ( or [, followed by decimal digits, then a ",", then decimal digits, then  ) or ]
#If it is a match, return True
#If it is not a match, return False
def IsValidPattern(InputContents):

    if re.search('^\s*[\(\[]\s*\-?\d+\s*,\s*\-?\d+\s*[\)\]]\s*$', InputContents):
        return True

    else:
        return False

'''
use parse function to divide an interval into four parts: lower, upper, lower_inclusive, upper_inclusive
use lower and upper to get the lower bound and upper bound of the Interval
use lower_inclusive and upper_inclusive to suggest that whether the two bounds are inclusive
'''
def parse(input_interval):

    ParsedInterval = input_interval.strip()
    lower, upper = map(int, re.split('\s*,\s*', ParsedInterval.strip(' ()[]')))

    if ParsedInterval[0] == '(':
        lower_inclusive = False

    elif ParsedInterval[0] == '[':
        lower_inclusive = True

    if ParsedInterval[-1] == ')':
        upper_inclusive = False

    elif ParsedInterval[-1] == ']':
        upper_inclusive = True

    return (lower, upper, lower_inclusive, upper_inclusive)

'''
use IsValidInterval to test whether the inclusive lower bound of the interval is less than or equal to the
inclusive upper bound
'''
def IsValidInterval(lower, upper, lower_inclusive, upper_inclusive):

    if lower_inclusive and upper_inclusive:
        return lower <= upper

    elif lower_inclusive or upper_inclusive:
        return lower <= upper - 1

    else:
        return lower <= upper - 2

#Rewrite (lower, upper, lower_inclusive, upper_inclusive)
#Update lower and upper, let the new lower be an inclusive lower bound, new upper be an inclusive upper bound
#Return the updated lower and upper bound
def RewriteValidInterval(lower, upper, lower_inclusive, upper_inclusive):

    if lower_inclusive:
        inclusive_lower = lower

    else:
        inclusive_lower = lower + 1
        lower_inclusive = True

    if upper_inclusive:
        inclusive_upper = upper

    else:
        inclusive_upper = upper - 1
        upper_inclusive = True

    return (inclusive_lower, inclusive_upper, lower_inclusive, upper_inclusive)

'''
we use CompareRewrittenInterval to achieve two goals:
            1. Change each interval's lower and upper into inclusive lower and inclusive upper
            2. Compare two intervals' inclusive bound and change their positions,
               let the interval with the smaller inclusive lower bound be the first interval
'''
def CompareRewrittenInterval(int1, int2):

    RewriteValidInterval(int1)
    RewriteValidInterval(int2)

    if int1.inclusive_lower <= int2.inclusive_lower:
        return(int1, int2)

    else:
        return(int2, int1)

'''
change (lower, upper, lower_inclusive, upper_inclusive) into interval format
for example:
    >> print output_format(4, 7, True, False)
    >> [4,7)
'''
def output_format(lower, upper, lower_inclusive, upper_inclusive):

    output_interval = []

    if lower_inclusive:
        output_interval.append('[')

    else:
        output_interval.append('(')

    output_interval.append(str(lower))
    output_interval.append(',')
    output_interval.append(str(upper))

    if upper_inclusive:
        output_interval.append(']')

    else:
        output_interval.append(')')

    interval_format = output_interval[0]+output_interval[1]+output_interval[2]+output_interval[3]+output_interval[4]


    return interval_format



#SplitInterval Splits the input of multiple intervals into intervals
def SplitIntoSingleInterval(InputContents):

    return re.split('(?<=[\]\)])\s*,\s*', InputContents)






