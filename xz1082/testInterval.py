# -*- coding: utf-8 -*-
"""
testInterval.py
"""
import unittest
from interval.intervals import *
from interval.exceptions import *


class classIntervalTestCase(unittest.TestCase):
    '''
    test class interval
    '''
    def setUp(self):
        self.interval = None
        self.invalidIntervalList = ['(3, 5])', '(5, 6)', '[(2, 4)]', 'interval']
        self.validIntervalList = ['(2,8)', '[1,6]', '[3 ,4)']

    def tearDown(self):
        self.interval = None

    def testExceptionRaisesTests(self):
        '''
        check when the intervals are invalid, whether the program can raise InvalidIntervals exception.
        '''
        for bad_interval in self.invalidIntervalList:
            with self.assertRaises(invalidIntervalException):
                self.interval = interval(bad_interval)

    def testValidIntervalsTests(self):
        '''
        check when the intervals are all valid, whether the program can go well.
        '''
        for good_interval in self.validIntervalList:
            self.assertTrue(interval(good_interval))


class mergeIntervalsTestCase(unittest.TestCase):
    '''
    test mergeIntervals()
    '''
    def setUp(self):
        self.int1 = interval('(1,3)')
        self.int2 = interval('[2,5]')
        self.int3 = interval('(2,8]')
        self.int4 = interval('(6,8]')

    def tearDown(self):
        self.interval = None

    def testOverlapping(self):
        self.assertEqual(mergeIntervals(self.int1, self.int2).__repr__(), interval('[5,7)').__repr__())

    def testNotOverlapping(self):
        with self.assertRaises(IntervalsNotOverlap):
            self.interval = mergeIntervals(self.int3, self.int4)


class mergeOverlappingTestCase(unittest.TestCase):
    '''
    test mergeOverlapping()
    '''
    def setUp(self):
        self.intlist = [interval('[1,5]'), interval('[2,6)'), interval('(8,10]'), interval('[8,18]')]
        self.mergedintlist = [interval('[1,6)'), interval('[8,18]')]
    
    def tearDown(self):
        self.intlist = None
        self.mergedintlist = None

    def testMerged(self):
        result = mergeOverlapping(self.intlist)
        for i in range(len(result)):
            self.assertIn(result[i].__repr__(), self.mergedintlist)


class insertTestCase(unittest.TestCase):
    '''
    test insert()
    '''
    def setUp(self):
        self.list = [Interval('[1,2]'), Interval('(3,5)'), Interval('[6,7)'), Interval('(8,10]'), Interval('[12,16]')]
        self.new_interval = Interval('[4, 9]')
        self.new_list = ['[1, 2]', '(3, 10]', '[12, 16]']

    def tearDown(self):
        self.intervals = None
        self.new_interval = None
        self.new_list = None

    def testInsert(self):
        result = insert(self.list, self.new_interval)
        self.assertEqual(len(result), len(self.new_list))
        for i in range(len(result)):
            self.assertEqual(result[i].__repr__(), self.new_list[i])

if __name__ == '__main__':
    unittest.main()