# -*- coding: utf-8 -*-
"""
unittest file for assignment6.py

@author: mengfeili
"""

from interval_functions import *
import unittest


class TestClassInterval(unittest.TestCase):
    """This was intended for testing the interval class.
       It concludes two parts:
       1. Interval representation testing
       2. Interval attributes testing
       3. Exception testing (invalid interval input)
    """
    def setUp(self):
        self.testInterval=interval('[8,12)')
    def tearDown(self):
        del self.testInterval    
    def test_intervalRepr(self):
        self.failUnlessEqual(self.testInterval.__repr__(),'[8,12)')
    def test_intervalAttributes(self):
        self.failUnlessEqual(self.testInterval.lrbd,'[')
        self.failUnlessEqual(self.testInterval.lfnum,8)
        self.failUnlessEqual(self.testInterval.rtnum,12)
        self.failUnlessEqual(self.testInterval.upbd,')')
        self.failUnlessEqual(self.testInterval.minval,8)
        self.failUnlessEqual(self.testInterval.maxval,11)
        self.failUnlessEqual(self.testInterval.span,range(8,12))
    def test_intervalException(self):
        self.assertRaises(Exception,interval,'foo')
        self.assertRaises(Exception,interval,'56,$$]')
        self.assertRaises(Exception,interval,'((4],5#]')
        
    
        
        
class TestisMergeable(unittest.TestCase):
    """Three conditions were tested:
        1. Two intervals with common elements
        2. Two intervals with maxval and minval adjacent
        3. Two intervals that are not mergeable
    """
    def test_intervalWithCommonElements(self):
        self.assertTrue(isMergeable(interval('[3,8]'),interval('(6,10]'))==True)
        self.assertTrue(isMergeable(interval('[3,6]'),interval('(6,10]'))==True)
        self.assertTrue(isMergeable(interval('[-1,0]'),interval('(4,8)'))==False)
        


class TestmergeIntervals(unittest.TestCase):
    """In this class, we designed 
       1. Two intervals are not mergeable will raise an error
       2. Two intervals are mergeable:
         (1). Maxval and minval are adjacent
         (2). have common elements
    """
    
    def test_mergeIntervals(self):
        self.assertRaises(Cant_be_merged,mergeIntervals,interval('[-9,7]'),interval('(12,15)'))
        self.failUnlessEqual(mergeIntervals(interval('[9,12]'),interval('(12,20]')).__repr__(),'[9,20]')
        self.failUnlessEqual(mergeIntervals(interval('(6,15)'),interval('[1,52)')).__repr__(),'[1,52)')
        



class TestmergeOverlapping(unittest.TestCase):
    """To test mergeOverlapping function under these circumstances:
       1. Given interval list is not mergeable and return the original sorted list
       2. Given interval list is mergeable:
         (1)the list contains only one interval
         (2)the list contains at least two intervals, and some of them are mergeable
    """
    def test_mergeOverlapping(self):
        self.failUnlessEqual(str(mergeOverlapping([interval('[5,7)'),interval('[-3,-1]'),interval('(23,52]')])),'[[-3,-1], [5,7), (23,52]]')
        self.failUnlessEqual(str(mergeOverlapping([interval('[1,52]')])),'[[1,52]]')
        self.failUnlessEqual(str(mergeOverlapping([interval('(7,12]'),interval('(-5,9]'),interval('[41,100)')])),'[(-5,12], [41,100)]')
        
  
class Testinsert(unittest.TestCase):
    """To test insert function under these circumstances:
       1.After insertion, new input interval cannot be merged into the given list of intervals, while the given list of intervals has mergeable intervals
       2.After insertion, new input interval cannot be merged into the given list of intervals, while the given list of intervals cannot be merged as well
       3.After insertion, new input interval is merged into the given list of intervals
    """
    def test_insert(self):
        self.failUnlessEqual(str(insert([interval('(12,23]'),interval('[0,9)'),interval('[10,17)')],interval('[-10,-5]'))),'[[-10,-5], [0,9), [10,23]]')
        self.failUnlessEqual(str(insert([interval('[-7,0)'),interval('[3,7]')],interval('(52,78]'))),'[[-7,0), [3,7], (52,78]]')
        self.failUnlessEqual(str(insert([interval('(34,72]'),interval('(1,38]')],interval('[42,65]'))),'[(1,72]]')
        





if __name__=='__main__':
  unittest.main()
    