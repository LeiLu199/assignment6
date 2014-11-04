import unittest
from interval.interval import *
from interval.intervalFunctions import *

class TestMergeIntervals(unittest.TestCase):
    '''
    test the function mergeIntervals
    '''
    def setUp(self):
        self.interval1 = interval('(-1,3]')
        self.interval2 = interval('[2,9]')
        self.interval3 = interval('(-1,9]')
        self.interval4 = interval('(10,15]')
    def testOverlap(self):
        merge = mergeIntervals(self.interval1, self.interval2)
        self.assertEqual(merge.__repr__(), self.interval3.__repr__())

    def testContain(self):
        merge = mergeIntervals(self.interval2, self.interval3)
        self.assertEqual(merge.__repr__(), self.interval3.__repr__())

class TestMergeOverlapping(unittest.TestCase):
    '''
    test the function mergeOverlapping
    '''
    def setUp(self):
        self.list = [interval('(2,9)'), interval('[3,10)'),interval('[12,15)'), interval('[-6,3)')]
        self.merged = [interval('[-6,10)'),interval('[12,15)')]

    def testMergeoverlapping(self):
        mergeAnswer = mergeOverlapping(self.list)
        self.assertEqual(len(mergeAnswer),len(self.merged))
        for i in range(len(mergeAnswer)):
            self.assertEqual(mergeAnswer[i].__repr__(), self.merged[i].__repr__())

class TestInsert(unittest.TestCase):
    '''
    test the function insert
    '''
    def setUp(self):
        self.list1 = [interval('[1,9)'),interval('(10,12]')]
        self.newint1 = interval('[5,11]') 
        self.answer1 = [interval('[1,12]')] 
        self.list2 = [interval('[1,3)'), interval('[2,5)'), interval('[6,9)'), interval('(8,15]'), interval('[17,20)')]
        self.newint2 = interval('(5,10)')
        self.answer2 = [interval('[1,5)'),interval('(5,15]'),interval('[17,20)')]  
    def testInsert(self):
        insertAnswer1 = insert(self.list1, self.newint1)
        insertAnswer2 = insert(self.list2, self.newint2)
        self.assertEqual(len(insertAnswer1), len(self.answer1))
        self.assertEqual(len(insertAnswer2), len(self.answer2))
        for i in range(len(insertAnswer1)):
            self.assertEqual(insertAnswer1[i].__repr__(), self.answer1[i].__repr__())
            self.assertEqual(insertAnswer2[i].__repr__(), self.answer2[i].__repr__())
if __name__ == '__main__':
    unittest.main()
