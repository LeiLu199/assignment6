import unittest
from Assignment_required_functions import *
from Basic_Tools import *

class mergeIntervals_Test(unittest.TestCase):
    '''unittest of the function mergeIntervals
    
    '''
    def setUp(self):
        self.int1 = interval('(-100,20]')
        self.int2 = interval('[2,30]')
        self.int3 = interval('(-100,30]')
        self.int4 = interval('(10,15]')
        self.int5 = interval('[20,40]')
        self.int6 = [interval('(10,15]'),interval('[20,40]')]

    def merge_int_case1(self):
        merge_test = mergeIntervals(self.int1, self.int2)
        self.assertEqual(merge_test.__repr__(), self.int3.__repr__())

    def merge_int_case2(self):
        merge_test = mergeIntervals(self.int1, self.int4)
        self.assertEqual(merge_test.__repr__(), self.int1.__repr__())

    def merge_int_case3(self):
        merge_test = mergeIntervals(self.int4, self.int5)
        self.assertEqual(merge_test.__repr__(), self.int6.__repr__())

class mergeOverlapping_Test(unittest.TestCase):
    '''unittest of the function mergeOverlapping

    '''
    def setUp(self):
        self.intlist = [interval('(-100,9)'), interval('[3,30)'),interval('[40,45]'), interval('[60,101)')]
        self.merged = [interval('(-100,30)'),interval('[40,45]'),interval('[60,101)')]

    def testMergeoverlapping(self):
        merge_overlap_test = mergeOverlapping(self.intlist)
        self.assertEqual(len(merge_overlap_test),len(self.merged))
        for i in range(len(merge_overlap_test)):
            self.assertEqual(merge_overlap_test[i].__repr__(), self.merged[i].__repr__())



class insert_Test(unittest.TestCase):
    '''unittest of the function insert

    '''
    def setUp(self):
        self.intlist1 = [interval('[-1,90)'),interval('(15,36]')]
        self.int1 = interval('[7,110]') 
        self.merged1 = [interval('[-1,110]')] 
        self.intlist2 = [interval('[-8,0)'), interval('[3,9)'), interval('[13,20)'), interval('(15,17]')]
        self.int2 = interval('[1,11]')
        self.merged2 = [interval('[-8,0)'),interval('[1,11]'),interval('[13,20)')]  
    def testInsert(self):
        insert_test1 = insert(self.intlist1, self.int1)
        insert_test2 = insert(self.intlist2, self.int2)
        self.assertEqual(len(insert_test1), len(self.merged1))
        self.assertEqual(len(insert_test2), len(self.merged2))
        for i in range(len(insert_test1)):
            self.assertEqual(insert_test1[i].__repr__(), self.merged1[i].__repr__())
            self.assertEqual(insert_test2[i].__repr__(), self.merged2[i].__repr__())


if __name__ == '__main__':
    unittest.main()