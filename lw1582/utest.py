import unittest
from interval import *
import customExceptions

class TestMergeIntervals(unittest.TestCase):
    '''tests mergeIntervals function'''
    def setUp(self):
        self.interval1 = interval('(1,4]')
        self.interval2 = interval('[2,3]')
        self.interval3 = interval('(4,9]')
        self.interval4 = interval('(1,9]')

    def testOverlap(self):
        merge = mergeIntervals(self.interval1,self.interval3)
        self.assertEqual(merge.__repr__(),self.interval4.__repr__())

    def testInclude(self):
        merge = mergeIntervals(self.interval1,self.interval2)
        self.assertEqual(merge.__repr__(),self.interval1.__repr__())

class TestMergeOverlapping(unittest.TestCase):
    '''test mergeOverlapping function'''
    def setUp(self):
        self.newlist = [interval('(1,4)'),interval('(-5,1]'),interval('[10,18)'),interval('[3,7)')]
        self.mergelist = [interval('(-5,7)'),interval('[10,18)')]
    
    def testMergeOverlapping(self):
        mergedIntervals = mergeOverlapping(self.newlist)
        self.assertEqual(len(mergedIntervals),len(self.mergelist))
        print mergedIntervals
        for i in range(len(mergedIntervals)):
            self.assertEqual(mergedIntervals[i].__repr__(),self.mergelist[i].__repr__())

class TestInsert(unittest.TestCase):
    '''test insert function'''
    def setUp(self):
        self.list1 = [interval('(1,9)'),interval('(12,15]')]
        self.newint1 = interval('[9,12]')
        self.newlist1 = [interval('(1,15]')]
        self.list2 = [interval('(1,3)'),interval('(-5,0]'),interval('[9,18)'),interval('[3,7)')]
        self.newint2 = interval('(-3,1]')
        self.newlist2 = [interval('(-5,7)'),interval('[9,18)')]

    def testInsertSorted(self):
        insertAnswer1 = insert(self.list1,self.newint1)
        self.assertEqual(len(insertAnswer1),len(self.newlist1))
        for i in range(len(insertAnswer1)):
            self.assertEqual(insertAnswer1[i].__repr__(),self.newlist1[i].__repr__())

    def testInsertUnsorted(self):
        insertAnswer2 = insert(self.list2,self.newint2)
        self.assertEqual(len(insertAnswer2),len(self.newlist2))
        for i in range(len(insertAnswer2)):
            self.assertEqual(insertAnswer2[i].__repr__(),self.newlist2[i].__repr__())

if __name__ == '__main__':
    unittest.main()
