import unittest
from interval.interval_function import *
from interval.My_exception import *

class TestmergeIntervals(unittest.TestCase):
	#Test mergeIntervals(interval_1, interval_2)
	
	def setUp(self):
		self.interval_1 = interval('[3,6)')
		self.interval_2 = interval('(4,9]')
		self.interval_3 = interval('(6,8]')
		
	def tearDown(self):
		pass
		
	def test_overlapping(self):
		#Intervals [3,6) and (4,9] should overlap and return [3,9]
		self.assertEqual(mergeIntervals(self.interval_1,self.interval_2).__repr__(), '[3,9]')
		
	def test_not_overlapping(self):
		#Intervals [3,6) and (6,8] should not overlap and raise exception.
		with self.assertRaises(NotOverlappingException):
			mergeIntervals(self.interval_1,self.interval_3)
	
	def test_containing(self):
		#Intervals (4,9] contains (6,8] and thus should return (4,9] 
		self.assertEqual(mergeIntervals(self.interval_2,self.interval_3).__repr__(), '(4,9]')
		
		
class TestmergeOverlapping(unittest.TestCase):
	#Test mergeOverlapping(list_of_intervals)
	
	def setUp(self):
		self.list_1 = [interval('[-10,-7]'), interval('(-8,0]'), interval('(1,4)'), interval('[2,5)')] 
		self.list_2 = [interval('[-10,-7]'), interval('[1,3)')] 
		self.list_1_answer = [interval('[-10,0]'), interval('(1,5)')]
		self.list_2_answer = [interval('[-10,-7]'),interval('[1,3)')]
		
	def tearDown(self):
		pass
		
	def test_merge_overlapping(self):
		#Intervals [-10,-7],(-8,0],(1,4) and [2,5) are overlapped and should return [-10,0], (1,5)
		mergeresult = mergeOverlapping(self.list_1)	
		self.assertEqual(len(mergeresult),len(self.list_1_answer))
		for i in range(len(mergeresult)):
			self.assertEqual(mergeresult[i].__repr__(), self.list_1_answer[i].__repr__())
			
	def test_merge_notoverlapping(self):
		#Intervals [-10,-7] and [1,3) are not overlapped.
		mergeresult = mergeOverlapping(self.list_2)
		self.assertEqual(len(mergeresult),len(self.list_2_answer))
		for i in range(len(mergeresult)):
			self.assertEqual(mergeresult[i].__repr__(), self.list_2_answer[i].__repr__())

			
class Testinsert(unittest.TestCase):
	def setUp(self):
		self.list_1 = [interval('[-10,-7]'), interval('(-8,0]'), interval('[1,4)'), interval('(2,5)')] #Merging this list should return [-10,0] and [1,5)
		self.insert_interval_1 = interval('[-5,1]') #should merge with list_1
		self.insert_interval_2 = interval('(6,9)') #should not merge with list_1
		self.list_1_and_interval_1 = interval('[-10,5)')
		self.list_1_and_interval_2 = [interval('[-10,0]'), interval('[1,5)'), interval('(6,9)')]
		
	def tearDown(self):
		pass
	
	def Test_insert_merged(self):
		#The inserted interval should be merged into the list.
		mergeresult = insert(self.list_1, self.insert_interval_1)
		self.assertEqual(len(mergeresult),len(self.list_1_and_interval_1))
		for i in range(len(mergeresult)): 
			self.assertEqual(mergeresult[i].__repr__(), self.list_1_and_interval_1[i].__repr__())
	
	def Test_insert_notmerged(self):
		#The inserted interval should not be merged into the list.
		mergeresult = insert(self.list_1, self.insert_interval_2)
		self.assertEqual(len(mergeresult),len(self.list_1_and_interval_2))
		for i in range(len(mergeresult)):
			self.assertEqual(mergeresult[i].__repr__(), self.list_1_and_interval_2[i].__repr__())
		
if __name__ == '__main__':
	unittest.main()

