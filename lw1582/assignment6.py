'''main codes'''

from interval import *
from customExceptions import *

def main():
  

  while True:
    try:
      intlist = raw_input("Enter the list of intervals: ")
      if intlist == "quit":
        break
      intlist = convertStrList(intlist)
      intlist = mergeOverlapping(intlist)
      break
    except(invalidForm,invalidRange,invalidList) as e:
      print(str(e))
      continue

  while True:

    try:
      newint = raw_input("Enter the interval to insert: ")
      if newint == "quit":
        break
      newint = interval(newint)
      newlist = insert(intlist,newint)
      print newlist
      continue
    except(invalidForm,invalidRange) as e:
      print(str(e))
      continue
    
    
  print "bye bye!"


if __name__ == "__main__":
  try:
    main()
  except KeyboardInterrupt:
    pass