from interval import interval
import intervalExceptions
import unittest

class TestIntervalClass(unittest.TestCase):

    def setUp(self):
        self.interval1 = interval('[1,2]')
        self.interval2 = interval('[3,4]')
        self.interval3 = interval('[1,4]')
        self.interval4 = interval('(5,10]')
        
        self.list = [self.interval1, self.interval2, self.interval4]                

    def test_intervalJunk(self):

        # test for non-Interval Input, should raise an exception for invalid interval
        self.assertRaises(intervalExceptions.invalidIntervalError, interval, 'asdfasf')
                
    def test_intervalBackwards(self):

        # test for backwards interval, should raise an exception for invalid interval

        self.assertRaises(intervalExceptions.invalidIntervalError, interval, '[5,1]')

    def test_merge(self):
        
        # test for merge
        
        self.assertTrue(interval.mergeIntervals(self.interval1,self.interval2) == self.interval3)

    def test_mergeDisjoint(self):
        
        # test for disjoint intervals, should raise an exception for disjoint intervals        
        
        self.assertRaises(intervalExceptions.disjointIntervalsError, interval.mergeIntervals,self.interval1,self.interval4)

    def test_mergeOverlapping(self):

        # test to merge a list of intervals
        
        self.assertEquals(interval.mergeOverlapping(self.list),[self.interval3, self.interval4])
        
    def test_insert(self):

        # test to insert an interval into a list        
        
        self.assertEquals(interval.insert([self.interval1, self.interval4], self.interval2),[self.interval3, self.interval4])


if __name__ == '__main__':
    unittest.main()