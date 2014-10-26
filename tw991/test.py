import unittest
from interval import *
from interval.intervalfunctions import *


class TestMergeIntervals(unittest.TestCase):
    """Test mergeIntervals(interval1, interval2) function"""

    def test_overlapping(self):
        self.assertEqual(mergeIntervals(interval('(1,5]'),interval('[2,6]')).__repr__(), '(1, 6]')

    def test_containing(self):
        self.assertEqual(mergeIntervals(interval('(1,8)'),interval('[3,6]')).__repr__(), '(1, 8)')

    def test_notoverlapping(self):
        with self.assertRaises(noOverlappingException):
            mergeIntervals(interval('(1,5)'),interval('[7,10)'))

class TestMergeOverlapping(unittest.TestCase):
    """Test mergeOverlapping(interval_list) function"""

    def setUp(self):
        self.list = [interval('[1,5)'),interval('[2,6)'),interval('(8,10]'),interval('[8,18]')]
        self.answer = [interval('[1,6)'),interval('[8,18]')]
        self.list2 = [interval('(1,5)'),interval('[7,10)')]
        self.answer2 = [interval('(1,5)'),interval('[7,10)')]

    def test_merge_overlapping(self):
        mergeAnswer = mergeOverlapping(self.list)
        self.assertEqual(len(mergeAnswer),len(self.answer))
        for index in range(0,len(mergeAnswer)):
            self.assertEqual(mergeAnswer[index].__repr__(), self.answer[index].__repr__())

    def test_merge_nooverlapping(self):
        mergeAnswer2 = mergeOverlapping(self.list2)
        for index in range(0,len(mergeAnswer2)):
            self.assertEqual(mergeAnswer2[index].__repr__(), self.answer2[index].__repr__())


class TestInsert(unittest.TestCase):
    """Test insert(interval_list, new_interval) function"""

    def setUp(self):
        self.list1 = [interval('[1,3]'), interval('[6,9]')]
        self.newinterval1 = interval('[2,5]')
        self.answer1 = [interval('[1,9]')]
        self.list2 = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
        self.newinterval2 = interval('[4,9]')
        self.answer2 = [interval('[1,2]'), interval('(3,10]'), interval('[12,16]')]

    def test_insert(self):
        insertAnswer1 = insert(self.list1, self.newinterval1)
        insertAnswer2 = insert(self.list2, self.newinterval2)
        self.assertEqual(len(insertAnswer1),len(self.answer1))
        self.assertEqual(len(insertAnswer2),len(self.answer2))
        for index in range(0,len(insertAnswer1)):
            self.assertEqual(insertAnswer1[index].__repr__(), self.answer1[index].__repr__())
            self.assertEqual(insertAnswer2[index].__repr__(), self.answer2[index].__repr__())


if __name__ == '__main__':
    unittest.main()