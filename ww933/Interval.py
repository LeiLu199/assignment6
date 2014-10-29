__author__ = 'chianti'

from PreHandle import *
from Exceptions import *

'''
The interval class represents the range of an interval.
It may throw two exceptions, IsValidIntervalError or IsValidPatternError, if the interval is not valid.
It basically divide an interval into four parts: lower bound, upper bound,
whether the lower bound is inclusive, whether the upper bound is inclusive.
For example: [4,9) becomes (4, 9, True, False)
It also consists a string representation of the interval.
'''

class interval:

    def __init__(self, SingleInterval):

        if IsValidPattern(SingleInterval):
        #IsValidPatter checks that whether the pattern matches :
        #( or [, followed by decimal digits, then a ",", then decimal digits, then  ) or ]
            self.lower, self.upper, self.lower_inclusive, self.upper_inclusive = parse(SingleInterval)

            if IsValidInterval(self.lower, self.upper, self.lower_inclusive, self.upper_inclusive):
            #use IsValidInterval to test whether the inclusive lower bound of the interval is less than or equal
            #to the inclusive upper bound
                pass

            else:
                raise IsValidIntervalError('The Interval is not valid !')

        else:
            raise IsValidPatternError('Not Interval at all !')

    def __repr__(self):
        # __repr__ returns the string representation of the interval

        return output_format(self.lower, self.upper, self.lower_inclusive, self.upper_inclusive)


# mergeIntervals(int1, int2) takes two intervals and decide whether the intervals overlap
# if they overlap, return a merged interval.
# if not, an exception is thrown.

def mergeIntervals(int1, int2):
    #Note: here we assume int1 and int2 are two valid intervals

    rewritten_int1 = RewriteValidInterval\
        (int1.lower, int1.upper, int1.lower_inclusive, int1.upper_inclusive)
    rewritten_int2 = RewriteValidInterval\
        (int2.lower, int2.upper, int2.lower_inclusive, int2.upper_inclusive)
#Use RewriteValidInterval to update lower and upper
#Let the new lower be an inclusive lower bound, new upper be an inclusive upper bound

    if rewritten_int1[0] <= rewritten_int2[0]:
    # if the inclusive lower bound of int1 is no larger than the inclusive lower bound of int2

        if rewritten_int1[1] >= rewritten_int2[0] - 1: # if the two intervals overlap

            if rewritten_int1[1] > rewritten_int2[1]:
                merged_interval = (int1.lower, int1.upper, int1.lower_inclusive, int1.upper_inclusive)

            else:
                merged_interval = \
                (int1.lower, int2.upper, int1.lower_inclusive, int2.upper_inclusive)

            return interval(output_format(merged_interval[0], merged_interval[1], merged_interval[2], merged_interval[3]))

        else:  # if the two intervals do not overlap
            raise CannotMergeTwoIntervalsError('Two intervals do not overlap')

    else: # if the inclusive lower bound of int1 is larger than the inclusive lower bound of int2

        if rewritten_int2[1] >= rewritten_int1[0] - 1:

            if rewritten_int1[1] <= rewritten_int2[1]:
                merged_interval = (int2.lower, int2.upper, int2.lower_inclusive, int2.upper_inclusive)

            else:
                merged_interval = (int2.lower, int1.upper, int2.lower_inclusive, int1.upper_inclusive)

            return interval(output_format(merged_interval[0], merged_interval[1],
                                          merged_interval[2], merged_interval[3]))

        else:  # if the two intervals do not overlap

            raise CannotMergeTwoIntervalsError('Two intervals do not overlap')


#function mergeOverlapping takes a list of intervals and merges all overlapping intervals.!
def mergeOverlapping(intervals):

    num_int = len(intervals)
    intlist = sorted(intervals, key = lambda t: t.lower)  #sort intervals by their lower bound

    for i in xrange(0, num_int-1):
        j = i+1
        try:
            intlist[j]=mergeIntervals(intlist[i], intlist[j])
            intlist[i] = ''
        except:
            pass

    return [intlist[i] for i in range(len(intlist)) if intlist[i] != '']

'''
The function insert(intlist, newint) takes two arguments: a list of non- overlapping intervals; and a single interval.
The function can insert newint into intlist, then merge the result if necessary.
'''
def insert(intlist, newint):

    intlist.append(newint)

    return mergeOverlapping(intlist)

