'''
Created on Oct 25, 2014

@author: leilu
'''
import unittest
from Class_Intervals import *
from package.basic_functions import *
from package.Class_Intervals import *
from package.User_defined_Exception import *
from package.Assignment6 import *

'''
Test and make sure that the IntervalFormatIssueException is properly raised if there is a format issue.
'''
class FormatTest(unittest.TestCase):
    def test_format(self):
        with self.assertRaises(IntervalFormatIssueException):
            print interval("sh29").range
'''
Test mergeIntervals(interval1, interval2) function: make sure that it returns the correct merged interval and correct exception should raise 
'''
class Interval_Test(unittest.TestCase):
    def test_overlap_Interval(self):
        self.assertEqual(mergeIntervals(interval('(3,9]'),interval('[2,6]')).__repr__(), '[2,9]')
    
    def test_overlapping(self):
        self.assertEqual(mergeIntervals(interval('(5,10]'),interval('[1,6]')).__repr__(), '[1,10]')

    def test_notoverlapping(self):
        with self.assertRaises(IntervalMergeException):
            mergeIntervals(interval('(1,5)'),interval('[5,19)'))
    
    def test_InvalidInterval(self):
        with self.assertRaises(InvalidIntervalException):
            mergeIntervals(interval('(3,1)'),interval('[5,19)'))
    
           
'''
Test MergOverlapping lists Function
'''
class TestMergeOverlapping(unittest.TestCase):
    def setUp(self):
        self.list1 = [interval('[1,5)'),interval('[2,6)'),interval('(8,10]'),interval('[8,18]')]
        self.merged1 = [interval('[1,6)'),interval('[8,18]')]

    def test_merge_overlapping(self):
        mergeAnswer1 = mergeOverlapping(self.list1)
        self.assertEqual(len(mergeAnswer1),len(self.merged1))
        for i in range(0,len(mergeAnswer1)):
            self.assertEqual(mergeAnswer1[i].__repr__(), self.merged1[i].__repr__())
 
'''
Test insert(interval_list, new_interval) function    
'''
class Test_Insert(unittest.TestCase):
    def setUp(self):
        self.list = [interval('[1,6]'), interval('[10,19]')]
        self.interval = interval('[5,11]')
        self.newmerged = [interval('[1,19]')]        
        self.list2 = [interval('[1,3]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
        self.interval2 = interval('[4,9]')
        self.newmerged2 = [interval('[1,3]'), interval('(3,10]'), interval('[12,16]')]

    def test_InsertFunction(self):
        MergedInterval = insert(self.list, self.interval)
        MergedInterval2 = insert(self.list2, self.interval2)
        self.assertEqual(len(MergedInterval),len(self.newmerged))
        self.assertEqual(len(MergedInterval2),len(self.newmerged2))
        for i in range(0,len(MergedInterval)):
            self.assertEqual(MergedInterval[i].__repr__(), self.newmerged[i].__repr__())
        for i in range(0,len(MergedInterval2)):
            self.assertEqual(MergedInterval2[i].__repr__(), self.newmerged2[i].__repr__())
    
    
if __name__ == '__main__':
    unittest.main()
