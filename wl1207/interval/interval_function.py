from input_parser import *
from My_exception import *
 
class interval():
	def __init__(self, input_interval):
		"""Constructor of class interval.
		   Exam whether a input is in valid interval format and represents a non-empty interval."""
		   
		self.input_interval = input_interval
		
		if isValidFormat(self.input_interval):
			self.lower_bound, self.lower_value, self.upper_value, self.upper_bound = parse_userinput(input_interval)
			
		else:
			raise NotAValidInputFormatException('Input interval is not in a valid input format, please check again.')
		
		if not isNotEmptyInterval(self.lower_bound, self.lower_value, self.upper_value, self.upper_bound):
			raise NotAValidInputIntervalException('Input interval is an empty interval, please check again.')
			
	def __repr__(self):
		return represent_interval(self.lower_bound, self.lower_value, self.upper_value, self.upper_bound)
		
def mergeIntervals(interval_1, interval_2):
	"""First exam if interval_1, interval_2 are overlapped. If not, raise an exception.
	   Then if two intervals overlap, get the merged lower_bound, lower_value, upper_value, upper_bound.
	   Define that when encounters (i,p), [i+1,q), we use (i,*); when encounters (p,j], (q,j+1), we use (*,j+1). 
	   Finally, return the merged interval."""
	
	if (interval_1.lower_bound+interval_1.lower_value > interval_2.upper_value-interval_2.upper_bound) or (interval_2.lower_bound+interval_2.lower_value > interval_1.upper_value-interval_1.upper_bound):
		raise NotOverlappingException('The intervals do not overlap, please check again.')
		
	else:
		if interval_1.lower_value + 0.5*interval_1.lower_bound < interval_2.lower_value + 0.5*interval_2.lower_bound:
			merged_lower_value, merged_lower_bound = (interval_1.lower_value, interval_1.lower_bound)
		else:
			merged_lower_value, merged_lower_bound = (interval_2.lower_value, interval_2.lower_bound)
		
		if interval_1.upper_value - 0.5*interval_1.upper_bound > interval_2.upper_value - 0.5*interval_2.upper_bound:
			merged_upper_value,merged_upper_bound = (interval_1.upper_value, interval_1.upper_bound)
		else:
			merged_upper_value,merged_upper_bound = (interval_2.upper_value, interval_2.upper_bound)
			
	return interval(represent_interval(merged_lower_bound, merged_lower_value, merged_upper_value, merged_upper_bound))		

def mergeOverlapping(list_of_intervals):
	"""Sort the input list of intervals using intervals' lower_value as key. 
	   Substitute the original input list with the sorted list.
	   We repeatedly compare the first interval and the second:
			if they cannot merge, 
				put the first interval into the merged_list, and delete it in the input list of intervals. 
				Then we can compare the new 'first' interval and the new 'second'.
			if they can merge, 
				substitute the first interval with the merged interval, and delete the second one in the input list.
				Then again we can compare the new 'first' interval and the new 'second'.
	   Loop until there is no element left in the input list_of_intervals that can be compared with.	
	"""
	   
	list_of_intervals = sorted(list_of_intervals, key = lambda x:x.lower_value + 0.5*x.lower_bound)
	
	merged_list = []
	
	while len(list_of_intervals)>0:
		try:
			list_of_intervals[0] = mergeIntervals(list_of_intervals[0], list_of_intervals[1])
			del list_of_intervals[1]
		except:
			merged_list.append(list_of_intervals[0])
			del list_of_intervals[0]
	
	return merged_list
	
def insert(list_of_intervals, new_interval):
	#Add the new interval into the list of intervals.
	
	list_of_intervals.append(new_interval)
	return mergeOverlapping(list_of_intervals)


