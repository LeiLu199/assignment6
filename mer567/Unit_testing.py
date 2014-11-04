#import bar, baz
from Interval_classes import *
import unittest


class TestMerge(unittest.TestCase):
    def setUp(self):
        self.intervalfortesting_1 = '[1,4]'
        self.intervalfortesting_2 = "(2,5]"
        self.intervalfortesting_3 = "[40,80)"
    
        # Tests for Question 1
        #self.mybar = Interval(self.intervalfortesting)

    def test_merge_constructor(self):
        temp = mergeIntervals(self.intervalfortesting_1, self.intervalfortesting_2)

        self.assertEqual(temp, "[1,5]")

        self.assertRaises(Intervals_Cannot_Merge,  mergeIntervals, self.intervalfortesting_2, self.intervalfortesting_3)
        #self.assertEqual(Interval(self.intervalfortesting_1).upper_bound, 4)

class TestMergeOverlapping(unittest.TestCase):
    def setUp(self):
        self.intervalfortesting_1 = ["[1,4]", "(2,5]"]
        self.intervalfortesting_2 = ["[1,4]", "(20,50]"]
        self.intervalfortesting_3 = ["[1,4]","(2,5]", "(20,50]"]
        # Tests for Question 1
        #self.mybar = Interval(self.intervalfortesting)

    def test_mergeoverlapping_constructor(self):
        temp = mergeOverlapping(self.intervalfortesting_1)
        self.assertEqual(temp, ["[1,5]"])

        temp2 = mergeOverlapping(self.intervalfortesting_2)
        self.assertEqual(temp2, ["[1,4]", "(20,50]"])

        temp3 = mergeOverlapping(self.intervalfortesting_3)
        self.assertEqual(temp3, ["[1,5]", "(20,50]"])


class TestMergeOverlapping(unittest.TestCase):
    def setUp(self):
        self.inserttesting_initial = ["[1,4]", "(2,5]"]
        self.inserttesting_2 = "(20,50]"
        self.inserttesting_3 = "[6,10]"

    def test_mergeoverlapping_constructor(self):
        temp = insert(self.inserttesting_initial, self.inserttesting_2)
        self.assertEqual(temp, ["[1,5]", "(20,50]"])

    
        temp2 = insert(temp, self.inserttesting_3)
        self.assertEqual(temp2, ["[1,10]", "(20,50]"])


 
if __name__ == '__main__':
    unittest.main()