import unittest
from interval import *
from interval.interval_functions import *


class mergeIntervals_test(unittest.TestCase):
    """Test mergeIntervals"""

    def overlapping(self):
        self.assertEqual(mergeIntervals('(1,5]', '[2,6]').__repr__(), '[2, 6]')  # check the result

    def within(self):
        self.assertEqual(mergeIntervals('(1,8)', '[4,6]').__repr__(), '[2, 7]')  # check the result

    def non_overlapping(self):
        with self.assertRaises('No Overlapping'):
            mergeIntervals('(0,3)', '[9,15)')  # check the result

class mergeOverlapping_test(unittest.TestCase):
    """Test mergeOverlapping"""

    def basic(self):  # check if the function is working
        self.string1 = '[1,5), [2,6), (8,10], [8,18]'
        self.result1 = ['[1,5]', '[8,18]']
        self.string2 = '(0,4), [6,15)'
        self.result2 = ['[1,3]', '[6,14]']

    def overlapping_test(self):  # check the overlapping case
        result = mergeOverlapping(self.string1)
        self.assertEqual(len(result),len(self.result1))  # check if the lengths of two list equal
        for i in range(0,len(result)):
            self.assertEqual(result[i].__repr__(), self.result1[i].__repr__())  # check if elements with same indexes
                                                                                # are the same

    def non_overlapping_test(self):  # check the non_overlapping_case
        result_non_overlapping = mergeOverlapping(self.string2)
        for i in range(0,len(result_non_overlapping)):
            self.assertEqual(result_non_overlapping[i].__repr__(), self.result2[i].__repr__())
            # check if elements with same indexes are the same


class insert_test(unittest.TestCase):
    """Test insert"""

    def basic(self):  # check if the function is working
        self.string1 = '[1,3], [6,9]'
        self.inserted_interval1 = '[2,5]'
        self.result1 = ['[1,9]']
        self.string2 = '[1,2], (3,5), [6,7), (8,10], [12,16]'
        self.inserted_interval2 = '[4,9]'
        self.result2 = ['[1,2]', '[4,10]', '[12,16]']

    def test_insert(self):  # check the function in deeper environment
        insert_output1 = insert(self.string1, self.inserted_interval1)
        insert_output2 = insert(self.string2, self.inserted_interval2)
        self.assertEqual(len(insert_output1),len(self.result1))  # check if the lengths of two list equal
        self.assertEqual(len(insert_output2),len(self.result2))
        for i in range(0,len(insert_output1)):
            self.assertEqual(insert_output1[i].__repr__(), self.result1[i].__repr__())
            self.assertEqual(insert_output2[i].__repr__(), self.result2[i].__repr__())
            # check if elements with same indexes are the same

if __name__ == '__main__':
    unittest.main()
