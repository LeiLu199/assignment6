import unittest
from Interval import *
from Exceptions import *
from NewIntervalFunctions import *

class testInterval(unittest.TestCase):
    '''
    test class interval
    '''
    def testInterval(self):
        i = interval("[1,4]")
        self.assertTrue(i.left_inclusive and i.right_inclusive and i.lower==1 and i.upper==4)
        i = interval("(2,5]")
        self.assertTrue(not i.left_inclusive and i.right_inclusive and i.lower==2 and i.upper==5)
        i = interval("[4,8)")
        self.assertTrue(i.left_inclusive and not i.right_inclusive and i.lower==4 and i.upper==8)
        i = interval("(3,9)")
        self.assertTrue(not i.left_inclusive and not i.right_inclusive and i.lower==3 and i.upper==9)
        #Try some bogus and wrong bounds
        for bogus in ["qefjiasdf", "{1,1}", "]1,5]", "[2,1]", "(1,1]", "(3,4)", "[[4,9)","(5,9))"]:
            self.assertRaises(Exception, interval, bogus)
            
class testMergeIntervals(unittest.TestCase):
    '''
    test mergeIntervals
    '''
    def testMergeIntervals(self):
        # working test
        self.assertEqual(str(mergeIntervals(interval('[1,4]'), interval('[3,8]'))), '[1,8]')
        self.assertEqual(str(mergeIntervals(interval('(1,4)'), interval('[3,8]'))), '(1,8]')
        self.assertEqual(str(mergeIntervals(interval('[1,9]'), interval('(3,8)'))), '[1,9]')
        self.assertEqual(str(mergeIntervals(interval('[1,9]'), interval('(3,10]'))), '[1,10]')
        self.assertEqual(str(mergeIntervals(interval('(3,10]'), interval('[1,9]'))), '[1,10]')
        self.assertEqual(str(mergeIntervals(interval('(1,5)'), interval('(4,10]'))), '(1,10]')
        self.assertEqual(str(mergeIntervals(interval('[1,5]'), interval('[2,6)'))), '[1,6)')
        # exception test
        self.assertRaises(notOverlappingException, mergeIntervals, interval('[-100, 0]'), interval('[100,200]'))
        self.assertRaises(notOverlappingException, mergeIntervals, interval('[1, 4)'), interval('[5,8]'))


class testMergeOverlapping(unittest.TestCase):
    '''
    test mergeoverlapping
    '''
    def testMergeOverlapping(self):
        intervals = ('[1,5]', '[2,6)', '(8,10]', '[8,18]')
        intList = [interval(item) for item in intervals]
        self.assertEqual([str(item) for item in mergeOverlapping(intList)], ['[1,6)', '[8,18]'])

        intervals = ('[1,2]', '[3,4)', '(5,7]', '[8,18]')
        intList = [interval(item) for item in intervals]
        self.assertEqual([str(item) for item in mergeOverlapping(intList)], ['[1,4)', '(5,18]'])

class testInsert(unittest.TestCase):
    '''
    test insert
    '''
    def testInsert(self):
        intervals = ('[1,3]', '[6,9]')
        intList = [interval(item) for item in intervals]
        newint = interval('[2,5]')
        self.assertEqual([str(item) for item in insert(intList, newint)], ['[1,9]'])

        intervals = ('[1,2]', '(3,5)', '[6,7)', '(8,10]', '[12,16]')
        intList = [interval(item) for item in intervals]
        newint = interval('[4,9]')
        self.assertEqual([str(item) for item in insert(intList, newint)], ['[1,2]', '(3,10]', '[12,16]'])

        intervals = ["[1,5]", "[2,7)", "(8,10]", "[8,18]"]
        intList = [interval(item) for item in intervals]
        newint = interval("[6,9)")
        self.assertEqual([str(item) for item in insert(intList, newint)], ['[1,18]'])

if __name__ == '__main__':
    unittest.main()
