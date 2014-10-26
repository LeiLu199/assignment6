import Intervals
from exception import *
import unittest


class classIntervalTestCase(unittest.TestCase):
    '''
    test class interval
    '''
    def setUp(self):
        '''
        set up data used in the tests.
        '''
        print 'Test starts!'
        self.interval = None
        self.invalidIntervalList = ['(2, 5])', '(2, 3)', '[( 2, 5)]', 'python']
        self.validIntervalList = ['(2,4)', '[2,5]', '[ 3 ,4)']

    def tearDown(self):
        print 'Test stops!'

    def test_exceptionRaisesTests(self):
        '''
        check when the intervals are invalid, whether the program can raise InvalidIntervals exception.
        '''
        for item in self.invalidIntervalList:
            with self.assertRaises(InvalidIntervals):
                self.interval = interval(item)

    def test_validIntervalsTests(self):
        '''
        check when the intervals are all valid, whether the program can go well.
        '''
        for item in self.validIntervalList:
            self.assertTrue(interval(item))


class mergeIntervalsTestCase(unittest.TestCase):
    '''
    test mergeIntervals()
    '''
    def setUp(self):
        '''
        set up data in the test
        '''
        print 'Test Starts!'
        self.int1 = interval('(3,6)')
        self.int2 = interval('[3,5]')
        self.int3 = interval('(3,5]')
        self.int4 = interval('(6,8]')

    def tearDown(self):
        print 'Test stops!'

    def testTwoIntervalsCanMerge(self):
        self.assertEqual(mergeIntervals(self.int1, self.int2).__repr__(), interval('[3,6)').__repr__())

    def testTwoIntervalsCannotMerge(self):
        with self.assertRaises(IntervalsNotOverlap):
            self.interval = mergeIntervals(self.int3, self.int4)


class mergeOverlappingTestCase(unittest.TestCase):
    '''
    test mergeOverlapping()
    '''
    def setUp(self):
        '''
        set up data for the test.
        '''
        print 'Test Starts!'
        self.intlist = [interval('[1,5]'), interval('[2,6)'), interval('(8,10]'), interval('[8,18]')]
        self.mergedintlist = [interval('[1,6)'), interval('[8,18]')]
    
    def tearDown(self):
        print 'Test stops!'

    def testIntlistCanMerge(self):
        for i in range(len(self.mergedintlist)):
            self.assertEqual(self.mergedintlist[i].__repr__(), mergeOverlapping(self.intlist)[i].__repr__())


class insertTestCase(unittest.TestCase):
    '''
    test insert()
    '''
    def setUp(self):
        '''
        set up testing data for the test.
        '''
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
