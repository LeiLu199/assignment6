'''
Created on Oct 26, 2014

@author: ds-ga-1007
'''
import unittest
from interval.interval import *
from interval.exceptions import *

class TestIntervals(unittest.TestCase):
    """
    Test whether the intervals are valid
    """
    
    def setUp(self):
        print 'Test the validity of intervals'
        self.interval = None
    def tearDown(self):
        print 'TestIntervals Over!'
        self.interval = None
        
    def test_invalidInterval(self):
        invalidintervallist = ['(1,6]]','((4,7)','foo','{1,2]']
        for invalidinterval in invalidintervallist:
            with self.assertRaises(IntervalInputException):
                self.interval = interval(invalidinterval)  
    
    def test_invalidBoundInterval(self):
        invalidBoundIntervallist = ['(2,3)','[4,2]','(5,5]']
        for invalidBoundInterval in invalidBoundIntervallist:
            with self.assertRaises(IntervalBoundException):
                self.interval = interval(invalidBoundInterval)                
    
    def test_validInterval(self):
        validintervallist = ['(1,4 ]','( 2 ,  5)','[8,9)']
        for validinterval in validintervallist:
            self.assertTrue(interval(validinterval)) 
            
class TestMergeIntervals(unittest.TestCase):
    """
    Test mergeIntervals(int1,int2) function
    """
    def setUp(self):
        print 'Test whether two intervals can merge'
        self.interval1 = interval('(1,4)')
        self.interval2 = interval('[1,3]')
        self.interval3 = interval('(3,8)')
        self.interval4 = interval('(-3,2]')
        self.interval = None
    
    def tearDown(self):
        print "TestMergeIntervals Over! "
    def test_intervalsCanMerge(self):
        self.assertEqual(mergeIntervals(self.interval1,self.interval2).__repr__(),interval('[1,4)').__repr__())
    def test_intervalsCannotMerge(self):
        with self.assertRaises(OverlapplingException):
            self.interval = mergeIntervals(self.interval3,self.interval4)

class TestMergeOverlapping(unittest.TestCase):
    """
    Test mergeOverlapping(intlist) function
    """
    def setUp(self):
        print 'Test whether a list of intervals can merge'
        self.intlist = [interval('[1,5]'),interval('[2,6)'),interval('(8,10]'),interval('[8,18]')]
        self.mergedlist = [interval('[1,6)'),interval('[8,18]')]
    
    def tearDown(self):
        print "TestMergeOverlapping Over! "
    def test_intlistCanMerge(self):
        mergedresult = mergeOverlapping(self.intlist)
        self.assertEqual(len(mergedresult), len(self.mergedlist))
        for i in range(len(self.mergedlist)):
            self.assertEqual(mergedresult[i].__repr__(),self.mergedlist[i].__repr__())

class TestInsert(unittest.TestCase):
    """
    Test insert(intlist, newint) function
    """
    def setUp(self):
        print 'Test inserting a new interval into a list of interval'
        self.intlist1 = [interval('[1,3]'),interval('[6,9]')]
        self.newint1 = interval('[2,5]')
        self.insertedlist1 = [interval('[1,9]')]
        self.intlist2 = [interval('[1,2]'),interval('(3,5)'),interval('[6,7)'),interval('(8,10]'),interval('[12,16]')]
        self.newint2 = interval('[4,9]')
        self.insertedlist2 = [interval('[1,2]'),interval('(3,10]'),interval('[12,16]')]
    
    def tearDown(self):
        print "TestInsert Over! "
    def test_Insert_A_Newint(self):
        insertresult1 = insert(self.intlist1,self.newint1)
        insertresult2 = insert(self.intlist2,self.newint2)
        self.assertEqual(len(insertresult1), len(self.insertedlist1))
        self.assertEqual(len(insertresult2), len(self.insertedlist2))
        for i in range(len(insertresult1)):
            self.assertEqual(insertresult1[i].__repr__(),self.insertedlist1[i].__repr__())
        for i in range(len(insertresult2)):
            self.assertEqual(insertresult2[i].__repr__(),self.insertedlist2[i].__repr__())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()