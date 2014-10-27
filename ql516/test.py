# -*- coding: utf-8 -*-

import unittest 
from intervalClass import *
from IntervalFunctions import *


class TestMergeIntervalsFunction(unittest.TestCase):

    def test_not_overlapping(self):
        with self.assertRaises(Exception):
            mergeIntervals(interval("[1,4]"),interval("[7,10]"))
    
    def test_overlapping1(self):
        self.assertEqual(mergeIntervals(interval("[1,7]"),interval("[7,10]")).str,"[1,10]")

    def test_overlapping2(self):
        self.assertEqual(mergeIntervals(interval("[5,7]"),interval("[3,10]")).str,"[3,10]") 

    def test_overlapping3(self):
        self.assertEqual(mergeIntervals(interval("[10,12)"),interval("[7,10]")).str,"[7,12)")




class TestMergeOverlappingFunction(unittest.TestCase):
    
    def setUp(self):
        self.interval_list = [interval("[1,5]"), interval("[2,6)"), interval("(8,10]"), interval("[8,18]")]
        self.answer = "[[1,6), (8,18]]"
    
    def test_function(self):
        self.result = mergeOverlapping(self.interval_list)
        self.assertEqual(str(self.result),self.answer)






class TestInsertFunction(unittest.TestCase):
    
    def setUp(self):
        self.intervalList_1 = [interval("[1,3]"), interval("[6,9]")]
        self.insertInterval_1 = interval("[2,5]")
        self.answer_1 = "[[1,9]]"
        self.intervalList_2 = [interval("[1,2]"), interval("(3,5)"), interval("[6,7)"),interval("(8,10]"), interval("[12,16]")]
        self.insertInterval_2 = interval("[4,9]")
        self.answer_2 = "[[1,2], (3,10], [12,16]]"
    
    def test_insert_1(self):
        result_1 = insert(self.intervalList_1,self.insertInterval_1)
        self.assertEqual(str(result_1),self.answer_1)
    
    def test_insert_2(self):
        result_2 = insert(self.intervalList_2,self.insertInterval_2)
        self.assertEqual(str(result_2),self.answer_2)
    
    
if __name__ == "__main__":
    unittest.main()
    
    
    