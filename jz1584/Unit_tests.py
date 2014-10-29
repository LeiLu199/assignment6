import unittest
from Q2 import mergeIntervals as me
from Q3 import mergeOverlapping as mo
from Q4 import insert 


class Testing(unittest.TestCase):
    """Provide unit tests for the mergeIntervals, mergeOverlapping,
       and insert functions using the Python unittest module
    """
    def setUp(self):
        pass
    
    def test_mergeInterval(self):
        self.assertEqual(me("(-10,-7]" , "[-8,1]"), "[-9,1]","not able to merge")
    
    def test_mergeOverlapping(self):
        self.assertEqual(mo("[1,5], [2,6), (8,10], [8,18]"), [[1,5],[8,18]])
    
    def test_insert(self):
        self.assertEqual(insert("[1,2], (3,5), [6,7), (8,10],[12,16]","[4,9]"),[[1,2], [4,10], [12,16]])
        
        
if __name__ == '__main__':
    unittest.main()
                         

