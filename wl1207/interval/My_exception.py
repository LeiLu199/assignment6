class NotAValidInputFormatException(Exception):
	"""Raise when the user input string is not in valid interval format."""
	pass
	
class NotAValidInputIntervalException(Exception):
	"""Raise when the user input string is actually an empty interval."""
	pass
	
class NotOverlappingException(Exception):
	"""Raise when two intervals can not overlap."""
	pass 
