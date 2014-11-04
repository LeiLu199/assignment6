import unittest
from interval.interval import *

class intervalConstructTests(unittest.TestCase):
    """Test the init function of class Interval. """

    def setUp(self):
        self.interval = None

    def tearDown(self):
        self.interval = None

    def test_not_an_interval(self):
        """Test non invalid interval inputs. """
        none_intervals = [12, '', 'jaisodc', '((1,, 3]]']
        for none_interval in none_intervals:
            with self.assertRaises(NotAnIntervalError):
                self.interval = Interval(none_interval)

    def test_invalid_bounds(self):
        """Test intervals that have valid forms but contain no integers. """
        intervals = ['(1, 1]', '[1, 0]', '(1, 2)']
        for interval in intervals:
            with self.assertRaises(InvalidBoundsError):
                self.interval = Interval(interval)

    def test_valid_bounds(self):
        """Test valid interval inputs. """
        intervals = ['(1, 2]', '[1, 1]', '(1, 3)']
        for interval in intervals:
            try:
                self.interval = Interval(interval)
                self.assertFalse(False)
            except:
                self.assertFalse(True)

class intervalFunctionalityTests(unittest.TestCase):
    """Test the functionality of class Interval. """

    def setUp(self):
        self.interval = Interval('(-3, 5]')
    
    def tearDown(self):
        self.interval = None

    def test_attributes(self):
        """Assert attributes are parsed correctly. """
        self.assertEqual(self.interval.lower, -3)
        self.assertEqual(self.interval.upper, 5)
        self.assertFalse(self.interval.lower_inclusive)
        self.assertTrue(self.interval.upper_inclusive)

    def test_get_val(self):
        """Test get_val() method. """
        self.assertEqual(self.interval.get_val(), range(-2, 6))
        self.interval.lower = 1
        self.assertEqual(self.interval.get_val(), range(2, 6))

    def test_repr(self):
        """Test __repr__() method. """
        self.assertEqual(self.interval.__repr__(), '(-3, 5]')
        self.interval.lower = 1
        self.assertEqual(self.interval.__repr__(), '(1, 5]')

class mergeIntervalsTests(unittest.TestCase):
    """Test mergeIntervals() function. """

    # Note that we have to assert the equality of resulting interval's string representation to the expected value because simply comparing two instances will always return false.
    def test_just_overlapping(self):
        self.assertEqual(mergeIntervals(Interval('(1, 4]'), Interval('[5, 8)')).__repr__(), '(1, 8)')

    def test_overlapping(self):
        self.assertEqual(mergeIntervals(Interval('(1, 4]'), Interval('[3, 8)')).__repr__(), '(1, 8)')

    def test_containing(self):
        self.assertEqual(mergeIntervals(Interval('(1, 4]'), Interval('(1, 8)')).__repr__(), '(1, 8)')
    
    def test_not_overlapping(self):
        with self.assertRaises(NotOverlappingError):
            mergeIntervals(Interval('(1, 4]'), Interval('(5, 8)'))

class mergeOverlappingTests(unittest.TestCase):
    """Test mergeOverlapping() function. """

    def setUp(self):
        self.intervals = [Interval('[1, 5]'), Interval('[2, 6)'), Interval('(8, 10]'), Interval('[8, 18]')]
        self.answer = ['[1, 6)', '[8, 18]']

    def tearDown(self):
        self.intervals = None
        self.answer = None

    def runTest(self):
        result = mergeOverlapping(self.intervals)
        # Assert the length and string representations are correct.
        self.assertEqual(len(result), len(self.answer))
        for i in range(len(result)):
            self.assertIn(result[i].__repr__(), self.answer)

class insertTests(unittest.TestCase):
    """Test insert() function. """
    
    def setUp(self):
        self.intervals = [Interval('[1,2]'), Interval('(3,5)'), Interval('[6,7)'), Interval('(8,10]'), Interval('[12,16]')]
        self.new_interval = Interval('[4, 9]')
        self.answer = ['[1, 2]', '(3, 10]', '[12, 16]']

    def tearDown(self):
        self.intervals = None
        self.new_interval = None
        self.answer = None

    def runTest(self):
        result = insert(self.intervals, self.new_interval)
        self.assertEqual(len(result), len(self.answer))
        for i in range(len(result)):
            self.assertEqual(result[i].__repr__(), self.answer[i])

if __name__ == '__main__':
    unittest.main()
