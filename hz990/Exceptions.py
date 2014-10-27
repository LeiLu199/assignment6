class Invalid_Interval_List(Exception):
	'''This exception would be raised if the list of intervals is invalid.

	''' 
	def __str__(self):
		return 'Your list of intervals is an invalid format.\n' + \
		'Intervals in your list should be separated by a single comma.\n' + \
		'Besides, each interval should start with a ( or [\n' + \
		'Followed by a pair of ascending integers which separated by a comma.\n' + \
		'End with a ) or ].\nPlease try again.\n'


class Invalid_Interval_Format(Exception):
	'''This exception would be raised if the input of interval is invalid.

	''' 
	def __str__(self):
		return 'Your input is an invalid interval form.\n' + \
		'Interval should start with a ( or [\n' + \
		'Followed by a pair of ascending integers which separated by a comma.\n' + \
		'End with a ) or ].\nPlease try again or type \'quit\' to exit.\n'


class Not_Overlap(Exception):
	'''This exception would be raised if intervals do not overlap.

	'''