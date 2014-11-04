from .utility import *
from .exceptions import *

class Interval:
    """Class of interval with integer bounds
    
    Attributes:
        lower (int): Lower bound of the interval.
        upper (int): Upper bound of the interval.
        lower_inclusive (bool): Whether or not the lower bound is inclusive.
        upper_inclusive (bool): Whether or not the upper bound is inclusive.

    """

    def __init__(self, interval_rep):
        """
        
        Constructor of class Interval.

        Args:
            interval_rep (str): User input string representation of interval.

        """
        
        if isValid(interval_rep):
            self.lower, self.upper, self.lower_inclusive, self.upper_inclusive = parse(interval_rep)
        else:
            raise NotAnIntervalError('Not an interval! An interval consists of a ( or [ followed by integer lower bound, upper bound and a ) or ].')

        if not isValidBounds(self.lower, self.upper, self.lower_inclusive, self.upper_inclusive):
            raise InvalidBoundsError('Invalid bounds! Interval must contain at least one integer.')
            
    def get_val(self):
        """Get the range the interval is represented.
        
        Returns:
            list: A range that is equivalent to the interval representation.

        Examples:
            >>> interval1 = Interval('[1, 4)')
            >>> interval1.get_val()
            [1, 2, 3]
        
        """
        return range(self.lower + int(not self.lower_inclusive), self.upper + int(self.upper_inclusive))

    def __repr__(self):
        return stringRepresent(self.lower, self.upper, self.lower_inclusive, self.upper_inclusive)

def mergeIntervals(int1, int2):
    """Given two intervals, merge them if possible. Raise a NotOverlappingError otherwise.

    Args:
        int1, int2 (Interval): Two Interval instances to merge.

    Returns:
        Interval: An Interval instance that contains the result after merging.

    Examples:
        >>> int1, int2 = Interval('(1, 4]'), Interval('[3, 8)')
        >>> print mergeIntervals(int1, int2)
        (1, 8)
        >>>
        >>> int1, int2 = Interval('(1, 4]'), Interval('(5, 8)')
        >>> print mergeIntervals(int1, int2)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "interval/interval.py", line 77, in mergeIntervals
            raise NotOverlappingError('Two intervals not overlapping')
        interval.exceptions.NotOverlappingError: Two intervals not overlapping

    """
    # Get ranges represented by the two intervals to determine whether two intervals overlap
    range1 = int1.get_val()
    range2 = int2.get_val()
    if range1[-1] < range2[0] - 1 or range1[0] > range2[-1] + 1: 
        raise NotOverlappingError('Two intervals not overlapping')
    else:
        # Here we treat '(n, ...' as a lower lower bound than '[n+1, ...', and '..., n)' as an upper upper bound than '..., n-1]'. The presence of 0.5 below ensures that.
        lower, lower_inclusive = (int1.lower, int1.lower_inclusive) if int1.lower - 0.5 * int1.lower_inclusive <= int2.lower - 0.5 * int2.lower_inclusive else (int2.lower, int2.lower_inclusive)
        upper, upper_inclusive = (int1.upper, int1.upper_inclusive) if int1.upper + 0.5 * int1.upper_inclusive >= int2.upper + 0.5 * int2.upper_inclusive else (int2.upper, int2.upper_inclusive)

        int_merged = Interval(stringRepresent(lower, upper, lower_inclusive, upper_inclusive))

    return int_merged

def mergeOverlapping(intervals):
    """Merge all intervals in a list of intervals until any two intervals cannot be further merged.

    Args:
        intervals (list): List of intervals to be merged. Not changed after using this function.

    Returns:
        list: A new interval list containing the merge results.

    Examples:
        >>> intervals = [Interval('[1, 5]'), Interval('[2, 6)'), Interval('(8, 10]'), Interval('[8, 18]')]
        >>> mergeOverlapping(intervals)
        [[1, 6), [8, 18]]

    """
    # First sort the list according to lower bounds
    intlist = sorted(intervals, key = lambda x: x.lower - 0.5 * x.lower_inclusive)
    
    current = intlist[0] # Store current interval
    res = [] # Store already merged intervals

    for i in xrange(1, len(intlist)):
        # Try to merge current two intervals, if cannot merge create a new one and continue
        try:
            current = mergeIntervals(current, intlist[i])
        except NotOverlappingError:
            res.append(current)
            current = intlist[i]
    
    # Append the last interval to the result
    res.append(current)
    
    return res

def insert(intervals, new_interval):
    """Insert new_interval into intervals and merge the results if possible. Original intervals are not modified afterwards.

    Args:
        intervals (list): A list of intervals to be inserted.
        new_intervals (Interval): New interval to insert.

    Returns:
        list: Resulting list of intervals sorted by their lower bounds.

    Examples:
        >>> intervals = [Interval('[1, 3]'), Interval('[6, 9]')]
        >>> new_interval = Interval('[2, 5]')
        >>> insert(intervals, new_interval)
        [[1, 9]]
        >>>
        >>> intervals = [Interval('[1,2]'), Interval('(3,5)'), Interval('[6,7)'), Interval('(8,10]'), Interval('[12,16]')]
        >>> new_interval = Interval('[4, 9]')
        >>> insert(intervals, new_interval)
        [[1, 2], (3, 10], [12, 16]]
    
    """

    return mergeOverlapping(intervals + [new_interval])
