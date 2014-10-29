'''
Created on Oct 28, 2014

@author: luchristopher
'''
import unittest

from interval import *

class TestMergeInterval(unittest.TestCase):
    '''provide unit test for mergeIntervals():
        >>>
        In class TestMergeOverlapping:
                
            User Defined Methods:
                test_overlap(self) : test if function generates correct merged result for overlapped intervals
                test_next_overlap(self) : test if function generates correct merged result for adjacent intervals
                test_contain(self) : test if function generates correct merged result when one interval is contained in the other
                test_not_overlap(self) : test if function successfully raises an NotOverlapping exception when two intervals are not overlapped
                test_priority(self) : test if function successfully deals with the priority setting (exclusive > inclusive)
    '''    

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_overlap(self):
        self.assertEqual(mergeIntervals(interval('[1,3]'),interval('[2,4]')).__repr__(),'[1,4]')

    def test_next_overlap(self):
        self.assertEqual(mergeIntervals(interval('[-3,0]'), interval('[1,3]')).__repr__(),'[-3,3]')
        self.assertEqual(mergeIntervals(interval('(-3,0)'), interval('(-2,3)')).__repr__(),'(-3,3)')
    
    def test_contain(self):
        self.assertEqual(mergeIntervals(interval('[-1,3]'),interval('(-3,5)')).__repr__(),'(-3,5)')
    
    def test_not_overlap(self):
        with self.assertRaises(NotOverlapping):
            mergeIntervals(interval('[1,2]'),interval('[4,5]'))
    
    def test_priority(self):
        self.assertEqual(mergeIntervals(interval('[1,4]'), interval('(0,5)')).__repr__(),'(0,5)')


class TestMergeOverlapping(unittest.TestCase):
    '''provide unit test for mergeOverlapping():
        >>>
        In class TestMergeOverlapping:
            Attributes:
                intervals(list(interval)) : the interval list used as the test input 
                merged_result(list(str)) : expected string representation of the outputs
                
            User Defined Methods:
                runTest(self) : test if mergeOverlapping generates correct output, by comparing the length of two results 
                                and then compare the content of each element in the list
    '''
    def setUp(self):
        self.intervals = [interval('[1,5]'),interval('[2,6)'),interval('(8,10]'),interval('[8,18]')]
        self.merged_result = ['[1,6)','[8,18]']
    
    def tearDown(self):
        self.intervals = None
        self.merged_result = None

    def runTest(self):
        merged_list = mergeOverlapping(self.intervals)
        #compare the length of two results and then compare the content of each element in the list
        self.assertEqual(len(merged_list),len(self.merged_result))
        for i in range(len(merged_list)):
            self.assertEqual(merged_list[i].__repr__(),self.merged_result[i])
        
class TestInsert(unittest.TestCase):
    '''provide unit test for mergeOverlapping():
        >>>
        In class TestMergeOverlapping:
            Attributes:
                intervals(list(interval)) : the interval list used as the test input 
                insert_result(list(str)) : expected string representation of the outputs
                insert_interval(interval) : interval to be inserted to the 'intervals'
                
            User Defined Methods:
                runTest(self) : test if insert() generates correct output, by comparing the length of two results 
                                and then compare the content of each element in the list
    '''
    
    def setUp(self):
        self.intervals = [interval('[1,2]'), interval('(3,5)'), interval('[6,7)'), interval('(8,10]'), interval('[12,16]')]
        self.insert_interval = interval('[4,9]')
        self.insert_result = ['[1,2]', '(3,10]', '[12,16]']
        
    def tearDown(self):
        self.intervals = None
        self.insert_interval = None
        self.insert_result = None
        
    def runTest(self):
        #compare the length of two results and then compare the content of each element in the list
        inserted_list = insert(self.intervals,self.insert_interval)
        self.assertEqual(len(self.insert_result),len(inserted_list))
        for i in range(len(inserted_list)):
            self.assertEqual(self.insert_result[i], inserted_list[i].__repr__())       
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()