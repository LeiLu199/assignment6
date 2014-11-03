import Exceptions
from Basic_Tools import *

class interval():
	def __init__(self, string):
		'''Initializing object variables.

		'''
		# Standardizing the string
		self.string = ''.join(string.split())
		# Using index of the comma as benchmark
		comma_index = string.index(',')
		self.lower_bracket = string[0]
		self.lower_bound_tmp = int(string[1:comma_index])
		if self.lower_bracket == '(':
			self.real_lower_bound = self.lower_bound_tmp + 1
		else:
			self.real_lower_bound = self.lower_bound_tmp

		self.upper_bracket = string[-1]
		self.upper_bound_tmp = int(string[comma_index+1:-1])
		if self.upper_bracket == ')':
			self.real_upper_bound = self.upper_bound_tmp - 1
		else:
			self.real_upper_bound = self.upper_bound_tmp
	
	def __repr__(self):
		return self.string



def mergeIntervals(int1, int2):
	'''This function merges two legal intervals and returns a new standardized interval.

	'''
	# Raise exception if intervals do not overlap
	if (int1.real_upper_bound < int2.real_lower_bound - 1) or  (int2.real_upper_bound < int1.real_lower_bound - 1):
		raise Exceptions.Not_Overlap('There exist intervals that do not overlap')

	# Initializing the target interval as an empty string
	merging_interval = ''


	if int1.real_lower_bound <= int2.real_lower_bound:
		merging_interval += int1.lower_bracket + str(int1.lower_bound_tmp) + ','
	else:
		merging_interval += int2.lower_bracket + str(int2.lower_bound_tmp) + ','
	if int1.real_upper_bound >= int2.real_upper_bound:
		merging_interval += str(int1.upper_bound_tmp) + int1.upper_bracket
	else:
		merging_interval += str(int2.upper_bound_tmp) + int2.upper_bracket

	# Standardizing the target interval
	merged_interval = interval(merging_interval)

	return merged_interval






def mergeOverlapping(intlist):
	'''This function takes a list of intervals as input, merges all overlaps and returns a new list of intervals. 

	'''
	def key_index(interval):
		'''This function returns the real lower bound of an interval as the index of the succeeding sort function.

		'''
		return interval.real_lower_bound

	# Sorting the interval list to an ascending order
	intlist = sorted(intlist, key = key_index)

	# Initializing the target interval list as an empty list
	merged_interval_list = []

	# Merging if overlap exists 
	n = 0
	while n < len(intlist):
		for m in range(n+1, n+2):
			try:
				intlist.insert(n, mergeIntervals(intlist[n], intlist[m]))
				intlist.remove(intlist[n+1])
				intlist.remove(intlist[n+1])
				n -= 1
				break
			except:
				merged_interval_list.append(intlist[n])
		n += 1

	# Return the merged interval list
	return merged_interval_list




def insert(intlist, newint):
	'''This function takes a interval list and a single interval as input and returns a merged interval list.

	'''
	# Appending the newly inserted interval to the interval list.
	intlist.append(newint)

	# Merging the possible overlaps and return the new interval list.
	return mergeOverlapping(intlist)


