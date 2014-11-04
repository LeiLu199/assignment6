from interval import *
import sys

def main():

    while True:

        #parsing the input and catch exception when necesary
        try:
            #prompting for input
            inputList = raw_input("Please enter a list of intervals:")

            if inputList == 'quit':
                raise KeyboardInterrupt

            itv_list = splitInputList(inputList)
            break

        except KeyboardInterrupt as err:
            print err
            sys.exit()

        except invalidListException as err:
            print err

    while True:
        try:
            #take interval input and exit when typed "quit"
            inputInterval = raw_input("Interval?")

            if inputInterval == 'quit':
                raise KeyboardInterrupt
    
        #catch keyboardinterrupt (ctrl c)
        except KeyboardInterrupt as err:
            print err
            sys.exit()

        try:
            #inserting
            itv_list = insert(itv_list, interval(inputInterval))

        except (invalidIntervalException, invalidListException) as err:
            #catch exception
            print err
            continue

        print itv_list

if __name__ == '__main__':
    main()





