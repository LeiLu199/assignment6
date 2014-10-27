from interval.intervalClass import *
from interval.intervalFunctions import *
from interval.intervalExceptions import *

#Main function
if __name__ == "__main__":

	#Input the list of intervals
	while True:
		#Terminate if the the command is "quit" or keyboardInterrupt
		try:
			userInput = raw_input("List of intervals? ")
			if userInput == "quit":
				raise KeyboardInterrupt

			intervalList = set_interval_list( userInput )

			break

		#Invalid intervals appear
		except InitErr as err:
			print err
		except KeyboardInterrupt:
			print "\nProgram terminated"
			sys.exit(0)
		

	#Input the interval that is going to be inserted
	while True:
		#Terminate if the the command is "quit" or keyboardInterrupt
		try:
			userInput = raw_input("Intervals? ")
			if userInput == "quit":
				raise KeyboardInterrupt

			i = interval( userInput )

		#Invalid intervals appear
		except InitErr as err:
			print err
			continue
	
		except KeyboardInterrupt:
			print ""
			break


		#Insert the interval
		intervalList = insert(intervalList, i)

		print_interval_list( intervalList )


	print "Program terminated"

