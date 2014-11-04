import sys
from interval.interval_function import *
from interval.input_parser import *
from interval.My_exception import NotAValidInputFormatException, NotAValidInputIntervalException

def main():
	while True:
		try:
			list_of_intervals = raw_input('List of intervals? ')
		except(KeyboardInterrupt, EOFError):
			print 'Process exit. '
			sys.exit()
			
		if list_of_intervals == 'quit':
			print 'Process exit. '
			sys.exit()
		
		try:
			list_of_intervals = map(interval, parse_ListofInterval(list_of_intervals))
			break
		except(NotAValidInputFormatException, NotAValidInputIntervalException) as exception:
			print exception
			continue
			
	while True:
		try:
			new_interval = raw_input("Interval? If want to exit, please input 'quit'.")
		except(KeyboardInterrupt,EOFError):
			print 'Process exit. '
			sys.exit()
			
		if new_interval == 'quit':
			print 'Process exit. '
			sys.exit()
		else:
			try:
				new_interval = interval(new_interval)
			except(NotAValidInputFormatException, NotAValidInputIntervalException) as exception:
				print exception
				continue
			list_of_intervals = insert(list_of_intervals, new_interval)
			print list_of_intervals

if __name__ =='__main__':
	main()
