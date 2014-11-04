'''
Created on Oct 28, 2014

@author: ds-ga-1007
'''
import unittest
from interval.Interval import *
from interval.Exceptions import *
from interval.basicFunctions import *

class MergeIntervalsTest(unittest.TestCase):
    """ Test mergeIntervals(int1, int2) function"""
    
    def setUp(self):
        self.interval1 = interval('(2,5]')
        self.interval2 = interval('[3,8]')
        self.interval3 = interval('(2,8)')
        self.interval4 = interval('[9,11)')
    
    def tearDown(self):
        print 'Test stops!'
        
    def OverlappingTest(self):
        merge = mergeIntervals(self.interval1, self.interval2)
        self.assertEqual(merge.__repr__(), self.interval3.__repr__())
     
    def ContainingTest(self):
        merge = mergeIntervals(self.interval2,self.iinterval3)
        self.assertEqual(merge.__repr__(), self.interval3.__repr__())

    def NotOverlappingTest(self):
        with self.assertRaises(NotOverlapInterval):
            mergeIntervals(self.interval3,self.interval4)
            
class MergeOverlappingTest(unittest.TestCase):
    """ Test mergeOverlapping(intlist) function"""
    
    def setUp(self):
        self.list1 = [interval('(2,5]'), interval('[3,8]'), interval('[9,11)')]
        self.result1 = [interval('[3,8]'), interval('[9,11)')]
        self.list2 = [interval('(5,11)'), interval('[13,16]')]
        self.result2 = [interval('(5,11)')], interval('[13,16]')
    
    def tearDown(self):
        print 'Test stops!'
        
    def mergeoverlappingtest(self):
        merge_result1 = mergeOverlapping(self.list1)
        self.assertEqual(len(merge_result1),len(self.result1))
        for i in range(len(merge_result1)):
            self.assertEqual(merge_result1[i].__repr__(), self.result1[i].__repr__())
        
        merge_result2 = mergeOverlapping(self.list2)
        self.assertEqual(len(merge_result2),len(self.result2))
        for i in range(len(merge_result2)):
            self.assertEqual(merge_result2[i].__repr__(), self.result2[i].__repr__())
    
class InsertTest(unittest.TestCase):
    """ Test inset(intlist, newint) function"""
    
    def setUp(self):
        self.intlist1 = [interval('[7,11)'),interval('(12,16]')]
        self.newint1 =interval('[9,13]')
        self.insertion1 = [interval('[7,16]')]
        self.intlist2 = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'),interval('(8,10]'),interval('[12,16]')]
        self.newint2 = interval('[4,9]')
        self.insertion2 = [interval('[1,2]'), interval('(3,10]'), interval('[12,16]')]
        
    def tearDown(self):
        print 'Test stops!'
        
    def insert_test(self):
        for i in range(len(self.result1)):
            self.assertEqual(insert(self.intlist1, self.newint2)[i].__repr__(), self.result1[i].__repr__())
        for i in range(len(self.result2)):
            self.assertEqual(insert(self.intlist2, self.newint2)[i].__repr__(), self.result2[i].__repr__())
        
if __name__ == '__main__':
    unittest.main()       

