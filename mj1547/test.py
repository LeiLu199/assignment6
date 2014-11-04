'''


@author: jiminzi
'''
import unittest


from Intervalpack.Intervals import mergeIntervals, Interval, mergeOverLapping,\
    insert
from Intervalpack.Exceptions import NoOverLapping, InvaildIntervals


'''
test mergeIntervals() function
'''
class mergeIntervalsTestCase(unittest.TestCase):
    
    def setUp(self):            
        self.intervala = Interval('[3,4)')
        self.intervalb = Interval('[3,5]')
        self.intervalc= Interval('(3,4]')
        self.intervald = Interval('(6,8]')
  # set some intervals

    def testTwoIntervalsMerge(self):
        self.assertEqual(mergeIntervals(self.intervala, self.intervalb).__repr__(), Interval('[3,5]').__repr__())
# to campare with the answer and the result by the mergeInterval function
    def testTwoIntervalsnotMerge(self):
        with self.assertRaises(NoOverLapping):
            self.intervald = mergeIntervals(self.intervalc, self.intervald)
''''
failure here since they cannot merge
'''
class mergeOverLappingTestCase(unittest.TestCase):
    '''
    test mergeOverLapping() function
    '''
    def setUp(self):
        print 'test of the mergeoverlap'
        self.intlist=[Interval('(1,3)'),Interval('[6,7)'),Interval('[3,5)'),Interval('(6,9]')]
        self.mergelist=[Interval('(1,5)'),Interval('[6,9]')]
    # to campare with the true answer    
    def testIntlistmergeable(self):
        for i in range(len(self.mergelist)):
            self.assertEqual(self.mergelist[i].__repr__(),mergeOverLapping(self.intlist)[i].__repr__())


class insertTestCase(unittest.TestCase):
    '''
    test insert
    '''
    #set some datas
    def setUp(self):
        print 'begin the insert test'
        self.intervallist1 = [Interval('(1,5]'),Interval('[3,8]')]
        self.insertint1=Interval('[12,18]')
        self.templist=[Interval('(1,8]'),Interval('[12,18]')]
        self.intervallist2 = [Interval('(2,4)'),Interval('(1,6  ]')]
        self.insertint2=Interval('(3,5]')
        self.templist2=Interval('(1,6]')
    # to campare with my answer and results
    def testInsertint(self):
        for x in range(len(self.templist)):        
            self.assertEqual(insert(self.intervallist1,self.insertint1)[x].__repr__(),self.templist[x].__repr__())
        for i in range(len(self.templist2)):
            self.assertEqual(insert(self.intervallist2,self.insertint2)[i].__repr__(),self.templist2[i].__repr__())
           
if __name__ == '__main__':
    unittest.main()