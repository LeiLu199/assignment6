import re

def True_Single_Interval(string):
	'''This function checks whether a single interval is valid.

	Return True if the single interval is valid
	Return False if the single interval is invalid'''

	# Reconstruct the string without blank spaces
	string = ''.join(string.split())

	# A correct interval format should start with a '(' or '['
	# Followed by a pair of ascending integers which separated by a comma
	# End with a ')' or ']'
	if (string[0] == '(' or '[') and (string[-1] == ')' or ']'):
		try:
			comma_index = string.index(',')

			lower_bracket = string[0]
			lower_bound_tmp = int(string[1:comma_index])
			if lower_bracket == '(':
				real_lower_bound = lower_bound_tmp + 1
			else:
				real_lower_bound = lower_bound_tmp

			upper_bracket = string[-1]
			upper_bound_tmp = int(string[comma_index+1:-1])
			if upper_bracket == ')':
				real_upper_bound = upper_bound_tmp - 1
			else:
				real_upper_bound = upper_bound_tmp

			if real_lower_bound <= real_upper_bound:
				return True
			else:
				return False
		except:
			return False
	else:
		return False

		
def True_Interval_List(string):
	'''This function checks whether the input interval list is in correct form.

	Return True if all are correct
	Return False if invalid pattern exists'''

	# Reconstruct the string without blank spaces
	string = ''.join(string.split())

	# Construct standard interval list from the string
	Interval_List = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\)\]]+', string)

	if Interval_List == []:
		return False
	for interval in Interval_List:
		if True_Single_Interval(interval):
			continue
		else:
			return False
	return True