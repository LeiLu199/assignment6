from interval.intervalClass import *
from interval.intervalFunctions import *
from interval.intervalExceptions import *
import unittest

#Unittest for MergeIntervals()
class TestMergeIntervalsFunction(unittest.TestCase):
	def setUp(self):
		self.interval_1 = interval("[-2,8]")
		self.interval_2 = interval("(6,15)")
		self.interval_3 = interval("(8, 15)")
		self.interval_4 = interval("[-2,15)")
		self.interval_5 = interval("(9, 15)")

	#Case of obvious overlapping
	def test_hard_overlapping(self):
		merged = mergeIntervals(self.interval_1,  self.interval_2)
		self.assertEqual(merged.expr, self.interval_4.expr)
	
	#Case of potential overlapping
	def test_soft_overlapping(self):
		merged = mergeIntervals(self.interval_1,  self.interval_3)
		self.assertEqual(merged.expr, self.interval_4.expr)

	#If no overlapping, raise MergeErr exception
	def test_none_overlapping(self):
		self.assertRaises(MergeErr, mergeIntervals, self.interval_1, self.interval_5)


#Unittest for MergeOverlapping()
class TestMergeOverlappingFunction(unittest.TestCase):
	def setUp(self):
		self.intervalList_0 = set_interval_list("    [   -10,   -7],       (    -4,1],     [3    ,  6  )    ")
		self.intervalList_1 = set_interval_list("[-10,-7], (-4,1], [3,6)")
		self.intervalList_2 = set_interval_list("[-10,-7], [3,6), (-4,1]")
		self.intervalList_3 = set_interval_list("[-10,-7], [3,6), (-4,1], (-7,-4)")
		self.intervalList_4 = set_interval_list("[-10,-4), (-4,1], [3,6)")

	#Test that if spaces are removed
	def test_removing_spaces(self):
		mergedList = mergeOverlapping(self.intervalList_0)
		self.assertEqual(len(mergedList), len(self.intervalList_1))

		for i in range(len(mergedList)):
			self.assertEqual(mergedList[i].expr, self.intervalList_1[i].expr)

	#Test that if the sorted and merged list stays the same
	def test_self_not_changed(self):
		mergedList = mergeOverlapping(self.intervalList_1)
		self.assertEqual(len(mergedList), len(self.intervalList_1))

		for i in range(len(mergedList)):
			self.assertEqual(mergedList[i].expr, self.intervalList_1[i].expr)

	#Test that sorting works or not
	def test_sorting(self):
		mergedList = mergeOverlapping(self.intervalList_2)
		self.assertEqual(len(mergedList), len(self.intervalList_1))

		for i in range(len(mergedList)):
			self.assertEqual(mergedList[i].expr, self.intervalList_1[i].expr)

	#Test that merging works or not
	def test_merging(self):
		mergedList = mergeOverlapping(self.intervalList_3)
		self.assertEqual(len(mergedList), len(self.intervalList_4))

		for i in range(len(mergedList)):
			self.assertEqual(mergedList[i].expr, self.intervalList_4[i].expr)
	
#Unittest for insert()
class TestinsertFunction(unittest.TestCase):
	def setUp(self):
		self.intervalList_1 = set_interval_list("[-10,-7], (-4,1], [3,6)")
		self.intervalList_2 = set_interval_list("[-10,-7], (-4,1], [3,6), [10,33)")
		self.intervalList_3 = set_interval_list("[-10,-7], (-6,-5], (-4,1], [3,6)")
		self.intervalList_4 = set_interval_list("[-10,-7], (-4,6)")
		self.interval_1 = interval("[10, 33)")
		self.interval_2 = interval("(-6, -5]")
		self.interval_3 = interval("(1, 4)")	

	#Test if appending works or not
	def test_appending(self):
		insertedList = insert(self.intervalList_1, self.interval_1)
		self.assertEqual(len(insertedList), len(self.intervalList_2))

		for i in range(len(insertedList)):
			self.assertEqual(insertedList[i].expr, self.intervalList_2[i].expr)

	#Test if sorting works or not
	def test_sorting(self):
		insertedList = insert(self.intervalList_1, self.interval_2)
		self.assertEqual(len(insertedList), len(self.intervalList_3))

		for i in range(len(insertedList)):
			self.assertEqual(insertedList[i].expr, self.intervalList_3[i].expr)

	#Test if appending, sorting, and then merging work or not
	def test_merging(self):
		insertedList = insert(self.intervalList_1, self.interval_3)
		self.assertEqual(len(insertedList), len(self.intervalList_4))

		for i in range(len(insertedList)):
			self.assertEqual(insertedList[i].expr, self.intervalList_4[i].expr)
		
#Main function
if __name__ == "__main__":

	unittest.main()

