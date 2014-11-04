import re
from .exceptions import NotAnIntervalError

def isValid(interval_rep):
    """Check if the interval has valid form: ( or [ followed by two integers separated by , and a ) or ].

    Args:
      interval_rep (str): User input string representation of interval.

    Returns:
      bool: True if valid pattern is found, False otherwise.

    Examples:
      >>> print isValid('(7, 73]')
      True
      >>> print isValid('  ( 7 ,  73 ]  ')
      True
      >>> print isValid('[7.7, 73.3)')
      False
      >>> print isValid('huabanxie')
      False
    
    """
    # Must be a string
    if not isinstance(interval_rep, str):
        return False

    # Find valid pattern in interval_rep
    match = re.search('^\s*[\(\[]\s*\-?\d+\s*,\s*\-?\d+\s*[\)\]]\s*$', interval_rep)
    if match:
        return True
    else:
        return False

def isValidBounds(lower, upper, lower_inclusive, upper_inclusive):
    """Check if the interval contain at least one element.
    
    Args:
        lower (int): First element in the interval, presumably lower bound.
        upper (int): Second element in the interval, presumably upper bound.
        lower_inclusive (bool): True if lower bound is inclusive, False otherwise.
        upper_inclusive (bool): True if upper bound is inclusive, False otherwise.

    Returns:
        bool: True if the interval contain at lease one element, False otherwise.

    Examples:
        >>> print isValidBounds(1, 2, True, False)
        True
        >>> print isValidBounds(1, 2, False, False)
        False

    """

    if lower_inclusive and upper_inclusive:
        return lower <= upper
    elif lower_inclusive or upper_inclusive:
        return lower < upper
    else:
        return lower < upper - 1

def parse(interval_rep):
    """Parse user input string to get detailed interval info.

    Args:
        interval_rep (str): User input string representation of interval.

    Returns:
        (
            lower (int): First element in the interval, presumably lower bound.
            upper (int): Second element in the interval, presumably upper bound.
            lower_inclusive (bool): True if [ is the first character, False if ( is the first character.
            upper_inclusive (bool): True if ] is the last character, False if ] is the last character.
        )

    Examples:
        >>> print parse('(7, 73]')
        (7, 73, False, True)

    """
    rep = interval_rep.strip()

    # Get bound types
    if rep[0] == '(':
        lower_inclusive = False
    elif rep[0] == '[':
        lower_inclusive = True
    if rep[-1] == ')':
        upper_inclusive = False
    elif rep[-1] == ']':
        upper_inclusive = True

    # Get bounds
    lower, upper = map(int, re.split('\s*,\s*', rep.strip(' ()[]')))

    return (lower, upper, lower_inclusive, upper_inclusive)

def parseIntervals(intervals_rep):
    """Parse user input string representation of a list of intervals.

    Args:
        intervals_rep (str): User input string representation of a list of intervals.

    Returns:
        list: A list of string representations of each individual interval.

    Examples:
        >>> intervals_rep = ' [-10,-7], (-4,1], [3,6), (8,12), [15,23]'
        >>> parseIntervals(intervals_rep)
        ['[-10,-7]', '(-4,1]', '[3,6)', '(8,12)', '[15,23]']
        >>>
        >>> intervals_rep = '[huabanxie, panmalon), [2, 3]'
        >>> parseIntervals(intervals_rep)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
          File "interval/utility.py", line 115, in parseIntervals
            raise NotAnIntervalError('At least one interval in the list is not in the correct form. Please check again.')
        interval.exceptions.NotAnIntervalError: At least one interval in the list is not in the correct form. Please check again.

    """
    intervals = re.split('(?<=[\]\)])\s*,\s*', intervals_rep.strip())
    for interval in intervals:
        if not isValid(interval):
            raise NotAnIntervalError('At least one interval in the list is not in the correct form. Please check again.')

    return intervals


def stringRepresent(lower, upper, lower_inclusive, upper_inclusive):
    """Given complete interval information, construct a string representation of the interval.

    Args:
        lower (int): First element in the interval, presumably lower bound.
        upper (int): Second element in the interval, presumably upper bound.
        lower_inclusive (bool): True if lower bound is inclusive, False otherwise.
        upper_inclusive (bool): True if upper bound is inclusive, False otherwise.
    
    Returns:
        str: String representation of the interval.

    Examples:
        >>> print stringRepresent(7, 73, False, True)
        '(7, 73]'

    """

    return lower_inclusive * '[' + (1-lower_inclusive) * '(' + str(lower) + ', ' + str(upper) + upper_inclusive * ']' + (1-upper_inclusive) * ')'

