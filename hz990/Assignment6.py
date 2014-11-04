import sys
import Exceptions
from Basic_Tools import *
from Assignment_required_functions import *

def main():
	'''The main function merges the given interval list and then merges the succeeding inserted intervals.

	Step 1. Checking the format of the interval list that user entered
	Step 2. Transforming the legal raw_input into a standard interval list
	Step 3. Merging the standardized interval list
	Step 4. Check the format of the newly inserted interval then merge with the previous result.'''

	# Step 1	
	# Prompting user for a list of intervals
	# If input format is illegal, exceptions would be raised
	while True:
		try:
			raw_string = raw_input('Enter a list of intervals or type \'quit\' to exit : \n')
			if raw_string == 'quit':
				sys.exit()
			elif True_Interval_List(raw_string):
				break
			else:
				raise Exceptions.Invalid_Interval_List
		except Exceptions.Invalid_Interval_List as ex:
			print ex
		except KeyboardInterrupt:
			sys.exit()

	# Step 2
	# Transforming the legal raw_input string into a standard interval list
	Interval_List = []
	standard_string = ''.join(raw_string.split())
	Interval_List_Cache = re.findall(r'[\[\(]+-*[0-9]+\,+-*[0-9]+[\)\]]+', standard_string)
	for i in Interval_List_Cache:
		Interval_List.append(interval(i))




	# Step 3
	# Merge the interval list

	Merged_Interval_List = mergeOverlapping(Interval_List)
	print 'The interval list you entered is now merged as: \n{}'.format(Merged_Interval_List)





	# Step 4
	# Prompting user for a new interval
	# If the newly inserted interval, exceptions would be raised
	# Then merge the inserted interval and continue

	while True:
		try:
			Inserted_String = raw_input('Please enter a new interval to be inserted : ')
			if Inserted_String == 'quit':
				sys.exit()
			elif True_Single_Interval(Inserted_String):
				Merged_Interval_List = insert(Merged_Interval_List, interval(Inserted_String))
				print 'The inserted interval has been merged, the result is: \n{}'.format(Merged_Interval_List)
			
			else:
				raise Exceptions.Invalid_Interval_Format
		except Exceptions.Invalid_Interval_Format as e:
			print e
		except KeyboardInterrupt:
			sys.exit()


if __name__ == '__main__':
	main()



