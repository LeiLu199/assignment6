import unittest
from interval import *


class TestMergeInterval(unittest.TestCase):
    '''
    when testing MergeInterval function
    '''
    def test_overlapping_situation(self):
        '''
        when 2 intervals overlap
        :return:
        '''
        self.assertEqual(mergeInterval(interval('[1,4)'), interval('[3,8)')).__repr__(), '[1,8)')

    def test_containing_situation(self):
        '''
        when 1 contains the other
        :return:
        '''
        self.assertEqual(mergeInterval(interval('[2,12)'), interval('[4,9]')).__repr__(), '[2,12)')

    def test_no_overlapping_situation(self):
        '''
        when 2 do not overlap
        :return:
        '''
        with self.assertRaises(notOverlappingException):
            #raise exception
            mergeInterval(interval('[3,7)'), interval('[12,15)'))


class TestMergeOverlapping(unittest.TestCase):
    '''
    test function MergeOverlapping
    '''
    def setUp(self):
        #set up lists and intervals
        self.option1 = [interval('[6,12)'), interval('[12,15]'), interval('[8,14)')]
        self.output1 = [interval('[6,15]')]
        self.option2 = [interval('[1,7)'), interval('[8,12)')]
        self.output2 = [interval('[1,7)'), interval('[8,12)')]

    def test_overlappingsituation(self):
        mergeAnswer1 = mergeOverlapping(self.option1)
        self.assertEqual(len(mergeAnswer1), len(self.output1))
        for idx in range(len(mergeAnswer1)):
            self.assertEqual(mergeAnswer1[idx].__repr__(), self.output1[idx].__repr__())

    def test_notoverlappingsituation(self):
        mergeAnswer2 = mergeOverlapping(self.option2)
        self.assertEqual(len(mergeAnswer2), len(self.output2))
        for idx in range(len(mergeAnswer2)):
            self.assertEqual(mergeAnswer2[idx].__repr__(), self.output2[idx].__repr__())


class TestInsert(unittest.TestCase):
    '''
    test inserting function
    '''
    def setUp(self):
        self.list1 = [interval('(1,5]'), interval('(7,14]'), interval('(16,99]')]
        self.interval1 = interval('[4,18]')
        self.answer1 = [interval('(1,99]')]
        self.list2 = [interval('(3,8)'), interval('[10,13)'), interval('(77,79]'), interval('(34,36]')]
        self.interval2 = interval('(5,12]')
        self.answer2 = [interval('(3,12]'), interval('(34,36]'), interval('(77,79]')]

    def test_insert(self):
        insertAnswer1 = insert(self.list1, self.interval1)
        self.assertEqual(len(insertAnswer1), len(self.answer1))
        for idx in range(len(insertAnswer1)):
            self.assertEqual(insertAnswer1[idx].__repr__(), self.answer1[idx].__repr__())
        insertAnswer2 = insert(self.list2, self.interval2)
        self.assertEqual(len(insertAnswer2), len(self.answer2))
        for idx in range(len(insertAnswer2)):
            self.assertEqual(insertAnswer2[idx].__repr__(), self.answer2[idx].__repr__())

if __name__ == '__main__':
    unittest.main()

