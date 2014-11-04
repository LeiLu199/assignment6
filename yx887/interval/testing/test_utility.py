import unittest
from interval.utility import *

class isValidTests(unittest.TestCase):
    """Test isValid() function. """

    def test_non_string(self):
        """Test non-string input. """
        self.assertFalse(isValid(7))

    def test_empty_string(self):
        """Test empty string input. """
        self.assertFalse(isValid(''))

    def test_random_string(self):
        """Test random string input. """
        self.assertFalse(isValid('pangmailang'))

    def test_decimal_bounds(self):
        """Test interval input with decimal number bounds. """
        self.assertFalse(isValid('(1.1, 2.2)'))

    def test_string_bounds(self):
        """Test interval formed input with no number bounds. """
        self.assertFalse(isValid('[A, x]'))

    def test_brackets(self):
        """Test nearly interval formed input with strange () or [] positions. """
        self.assertFalse(isValid('((1, 3]]'))
        self.assertFalse(isValid(']1, 3('))
        self.assertFalse(isValid('(]1, 3'))
        
    def test_negaive_bounds(self):
        """Test interval with negative bounds. """
        self.assertTrue(isValid('(-3, 4]'))
        self.assertTrue(isValid('[-5, -1)'))

    def test_valid_interval(self):
        """Test valid interval with positive bounds. """
        intervals = ['(1, 2]', '[1, 2)', '(1, 2)', '[1, 2]']
        for interval in intervals:
            self.assertTrue(isValid(interval))

    def test_extra_spaces(self):
        """Test valid interval string with extra spaces. """
        self.assertTrue(isValid(' ( 1 , 2 ] '))

class isValidBoundsTests(unittest.TestCase):
    """Test isValidBounds() function. """

    def test_both_inclusive(self):
        self.assertFalse(isValidBounds(1, 0, True, True))
        self.assertTrue(isValidBounds(1, 1, True, True))
        self.assertTrue(isValidBounds(1, 2, True, True))

    def test_either_inclusive(self):
        self.assertFalse(isValidBounds(1, 1, True, False))
        self.assertFalse(isValidBounds(1, 1, False, True))
        self.assertTrue(isValidBounds(1, 2, False, True))

    def test_both_exclusive(self):
        self.assertFalse(isValidBounds(1, 1, False, False))
        self.assertFalse(isValidBounds(1, 2, False, False))
        self.assertTrue(isValidBounds(1, 3, False, False))

class parseTests(unittest.TestCase):
    """Test parse() function. """

    def test_valid_interval(self):
        intervals = ['(1, 2]', '[1, 2)', '(1, 2)', '[1, 2]']
        answers = [(1, 2, False, True), (1, 2, True, False), (1, 2, False, False), (1, 2, True, True)]
        for i in range(4):
            self.assertEqual(parse(intervals[i]), answers[i])

    def test_negaive_bounds(self):
        self.assertEqual(parse('(-3, 4]'), (-3, 4, False, True))
        self.assertEqual(parse('[-5, -1)'), (-5, -1, True, False))

    def test_extra_spaces(self):
        self.assertEqual(parse(' ( 1 , 2 ] '), (1, 2, False, True))

class parseIntervalsTests(unittest.TestCase):
    """Test parseIntervals() function. """
    
    def test_valid_intervals(self):
        intervals = '[-10,-7], (-4,1], [3,6), (8,12), [15,23]'
        self.assertEqual(parseIntervals(intervals), ['[-10,-7]', '(-4,1]', '[3,6)', '(8,12)', '[15,23]'])

    def test_extra_spaces(self):
        intervals = '  [-10,-7]  ,  (-4,1]  ,  [3,6) ,  (8,12)  , [15,23] '
        self.assertEqual(parseIntervals(intervals), ['[-10,-7]', '(-4,1]', '[3,6)', '(8,12)', '[15,23]'])

    def test_invalid_intervals(self):
        intervals = '[foo, bar], (huabanxie, panmalon), [3,6)'
        with self.assertRaises(NotAnIntervalError):
            parseIntervals(intervals)

class stringRepresentTests(unittest.TestCase):
    """Test stringRepresent() function. """

    def test_negative_bounds(self):
        self.assertEqual(stringRepresent(-3, -1, False, True), '(-3, -1]')

    def test_positive_bounds(self):
        self.assertEqual(stringRepresent(1, 3, True, False), '[1, 3)')

if __name__ == '__main__':
    unittest.main()
