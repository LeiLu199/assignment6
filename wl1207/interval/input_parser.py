import re
import My_exception

def isValidFormat(input_interval): 
	""" An input interval(type: string) should be in one of the following format:
		[A,B], [A,B), (A,B],(A,B), where both A and B should be integers. 
		If not, return False."""
	
	if not isinstance(input_interval, str):
		return False
	
	valid_format = re.search('^\s*[\(\[]\s*\-?\d+\s*,\s*\-?\d+\s*[\)\]]\s*$', input_interval)
	if valid_format:
		return True
	else:
		return False

def parse_userinput(input_interval):
	"""For each user input, we will get four attributes - 
	   where lower_value and upper_value are integers, 
	   lower_bound: =1 if the lower bound is '('; =0 if the lower bound is '['; 
	   upper_bound: =-1 if the upper bound is ')', =0 if the upper bound is ']'."""
	   
	
	input_interval_strip = input_interval.strip()
	
	lower_value, upper_value = map(int,re.split('\s*,\s*', input_interval_strip.strip(' ()[]')))
	
	if input_interval_strip[0] == '(':
		lower_bound = 1
	elif input_interval_strip[0] == '[':
		lower_bound = 0
	if input_interval_strip[-1] == ')':
		upper_bound = 1
	elif input_interval_strip[-1] == ']':
		upper_bound = 0
			
	return (lower_bound, lower_value, upper_value, upper_bound)
			
def isNotEmptyInterval(lower_bound, lower_value, upper_value, upper_bound):
	"""Only consider the intervals that at least have one integer as return True, otherwise false.
	   [i,j] contains integer from i to j, both are inclusive;
	   [i,j) contains integer from i to actually j-1;
	   (i,j] contains integer from actually i+1 to j;
	   (i,j) contains integer from actually i+1 to j-1."""
	   
	if lower_value + lower_bound > upper_value - upper_bound:
		return False
	else:
		return True
	
			
def represent_interval(lower_bound, lower_value, upper_value, upper_bound):
	if lower_bound == 1:
		lower_bracket = '('
	elif lower_bound == 0:
		lower_bracket = '['
	if upper_bound == 1:
		upper_bracket = ')'
	elif upper_bound == 0:
		upper_bracket = ']'
	return lower_bracket + str(lower_value) + ',' + str(upper_value) + upper_bracket
		
def parse_ListofInterval(input_listofintervals):
	"""For user input list of intervals, exam its valid format. If invalid, raise exception. 
	   Return a list of intervals."""
	
	list_of_intervals = re.split('(?<=[\]\)])\s*,\s*', input_listofintervals.strip())
	for interval in list_of_intervals:
		if not isValidFormat(interval):
			raise NotAValidInputFormatException('There are some invalid interval in the input list of intervals. ')
	return  list_of_intervals
