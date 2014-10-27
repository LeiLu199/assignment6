import unittest
from interval.interval import *
from interval.exceptions import *

#Test for mergeInterval function

class mergeIntervalTests(unittest.TestCase):
    def test_Overlap(self):
        self.assertEqual(str(mergeIntervals(interval('[3,7)'),interval('(2,4)'))),'(2,7)')
        self.assertEqual(str(mergeIntervals(interval('[3,7)'),interval('[-2,3)'))),'[-2,7)')
        self.assertEqual(str(mergeIntervals(interval('[3,7)'),interval('(4,6)'))),'[3,7)')
    
    def test_notOverlap(self):
        with self.assertRaises(NotOverlappingError):
            mergeIntervals(interval('[3,7)'),interval('(7,10)'))

#Test for mergeOverlapping function
class mergeOverlappingTests(unittest.TestCase):
    
    def test_MergeOverlapping(self):
        int1 = interval('[1,5]')
        int2 = interval('[2,6)')
        int3 = interval('(8,10]')
        int4 = interval('[8,18]')
        intlist = [int1, int2, int3, int4]
        self.assertEqual(str(mergeOverlapping(intlist)),'[[1,6), [8,18]]')

#Test for Insert function
class InsertTests(unittest.TestCase):

    def test_InsertExample1(self):
        int1 = interval('[1,3]')
        int2 = interval('[6,9]')
        newint = interval('[2,5]')
        intlist = [int1, int2]
        self.assertEqual(str(insert(intlist,newint)),'[[1,9]]')

    def test_InsertExample2(self):
        int1 = interval('[1,2]')
        int2 = interval('(3,5)')
        int3 = interval('[6,7)')
        int4 = interval('(8,10]')
        int5 = interval('[12,16]')
        newint = interval('[4,9]')
        intlist = [int1, int2, int3, int4, int5]
        self.assertEqual(str(insert(intlist,newint)),'[[1,2], (3,10], [12,16]]')
            
if __name__ == '__main__':
    unittest.main()


