__author__ = 'chianti'

import unittest

from Interval import *


# Test different kinds of invalid input, check if we can get the corresponding exceptions

if 1 == 0:
    class test_ValidityExamination(unittest.TestCase):
        def test_ValidityExamination(self):
            for bogus in ["qefjiasdf", "{1,1}", "]1,5]", "[2,1]", "(1,1]", "(3,4)"]:
                try:
                    interval(bogus)
                except Exception as e:
                    print(e)


# Test mergeIntervals(int1, int2)

class mergeIntervalsTests(unittest.TestCase):

    def test_overlapping_intervals(self):
        self.assertEqual(mergeIntervals(interval('[4,7)'), interval('[5,9)')).__repr__(), interval('[4,9)').__repr__())

    def test_overlapping_intervals(self):
        self.assertEqual(mergeIntervals(interval('[4,7)'), interval('(2,4]')).__repr__(), interval('(2,7)').__repr__())

    def test_overlapping_intervals(self):
        self.assertEqual(mergeIntervals(interval('[4,7)'), interval('(2,9)')).__repr__(), interval('(2,9)').__repr__())

    def test_overlapping_intervals(self):
        self.assertEqual(mergeIntervals(interval('(2,9)'), interval('[4,7)')).__repr__(), interval('(2,9)').__repr__())

    def test_not_overlapping_intervals(self):
        with self.assertRaises(CannotMergeTwoIntervalsError):
            mergeIntervals(interval('(1, 4]'), interval('(5, 8)'))

# Test mergeOverlapping(intervals)

class mergeOverlappingTests(unittest.TestCase):

    def setUp(self):
        self.interval_list = [interval('[1,5]'), interval('[2,6)'), interval('(8,10]'), interval('[8,18]')]
        self.answer = ['[1,6)', '[8,18]']

    def tearDown(self):
        self.interval_list = None
        self.answer = None

    def runTest(self):
        result = mergeOverlapping(self.interval_list)
        for i in range(len(result)):
            self.assertIn(result[i].__repr__(), self.answer)

# Test insert(intlist, newint)

class insertTests(unittest.TestCase):

    def setUp(self):
        self.intlist = \
            [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
        self.newint = interval('[4, 9]')
        self.answer = ['[1,2]', '(3,10]', '[12,16]']

    def tearDown(self):
        self.intlist = None
        self.newint = None
        self.answer = None

    def runTest(self):
        result = insert(self.intlist, self.newint)
        for i in range(len(result)):
            self.assertEqual(result[i].__repr__(), self.answer[i])


if __name__ == '__main__':
    unittest.main()