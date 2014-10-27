'''
unittest.py
'''
import unittest
from Interval.Interval import *
from Interval.utility import *
class intervalClassTest(unittest.TestCase):
    '''
    test class interval
    '''
    def setUp(self):
 
        print 'Test begins!'
        self.interval = None
        self.invalidIntervalList = ['((100, 101])', 'bye']
        self.validIntervalList = ['(1,7)', '[11,20]', '[5,7)', '[20,23]']

    def tearDown(self):
        print 'Test stops!'

    def test_exceptionRaiseTest(self):
        '''
        test whether the program can raise an exception or not when there is 
        at least one invalid interval in the string.
        '''
        for item in self.invalidIntervalList:
            with self.assertRaises(invalidIntervalException):
                self.interval = interval(item)

    def test_validIntervalsTests(self):
        '''
        test the interval class for a list of valid intervals.
        '''
        for item in self.validIntervalList:
            self.assertTrue(interval(item))


class mergeIntervalsTest(unittest.TestCase):
    '''
    test mergeIntervals()
    '''
    def setUp(self):

        print 'Test begins!'
        self.int1 = interval('(10,16)')
        self.int2 = interval('[5,10]')
        self.int3 = interval('(3,12]')
        self.int4 = interval('(6,8]')

    def tearDown(self):
        print 'Test Stops!'

    def test_just_Merge(self):
        self.assertEqual(mergeIntervals(self.int1, self.int2).__repr__(), interval('[5,16)').__repr__())
   
    def test_merge(self):
        self.assertEqual(mergeIntervals(self.int1, self.int3).__repr__(), interval('(3,16)').__repr__())
    
    def test_notOverLapping(self):
        with self.assertRaises(notOverlappingException):
            self.interval = mergeIntervals(self.int1, self.int4)


class mergeOverlappingTest(unittest.TestCase):
    '''
    test mergeOverlapping()
    '''
    def setUp(self):

        print 'Test begins!'
        self.intlist = [interval('[1,3]'), interval('[2,9)'), interval('(10,13]'), interval('[5,7]')]
        self.mergedintlist = [interval('[1,9)'), interval('[10,13]')]
    
    def tearDown(self):
        print 'Test stops!'

    def test_IntListOverlapping(self):
        for i in range(len(self.mergedintlist)):
            self.assertEqual(self.mergedintlist[i].__repr__(), mergeOverlapping(self.intlist)[i].__repr__())


class insertTest(unittest.TestCase):
    '''
    test the function insert()
    '''
    def setUp(self):

        print 'Test starts!'
        self.intlist1 = [interval('[1,3]'), interval('[6,9]')]
        self.newint1 = interval('[2,5]')
        self.result1 = interval('[1,9]')
        self.intlist2 = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
        self.newint2 = interval('[4,9]')
        self.result2 = [interval('[1,2]'), interval('(3,10]'), interval('[12,16]')]

    def tearDown(self):
        print 'Test stops!'

    def testInsertNewint(self):
        for item in insert(self.intlist1, self.newint1):
            self.assertEqual(item.__repr__(), self.result1.__repr__())
        for i in range(len(self.result2)):
            self.assertEqual(insert(self.intlist2, self.newint2)[i].__repr__(), self.result2[i].__repr__())

if __name__ == '__main__':
    unittest.main()