'''import custom exceptions modules'''
from customExceptions import *



class interval(object):
  '''class interval takes string representation of the range of integers between a lower bound and an upper bound. The lower and upper bounds can be either "inclusive" or "exclusive" and can be positive or negative'''
  def __init__(self,integerRange):
    if isValidInterval(integerRange):
      if isValidRange(integerRange):
        self.intervalRange = intervalRangeTuple(integerRange)
        self.lowerBracket, self.lowerbound, self.upperbound, self.upperBracket = parseInterval(integerRange)
      else:
        raise invalidRange("invalid interval range. first value must be less than or equal to last value")
    else:
      raise invalidForm("interval must be in the form: '(/[ digit,digit ]/)' ")
  def __repr__(self):
    return self.lowerBracket + str(self.lowerbound) + "," + str(self.upperbound) + self.upperBracket 

'''
the following four functions are used for the interval class:
    1. isValidInterval
    2. parseInterval
    3. intervalRangeTuple
    4. isValidRange

    isValidInterval
    checks whether the interval input fits the form of an interval: '(/[ digit,digit ]/)'
    
    parseInterval
    splits the interval input into lowerBracket, lowerBound, upperBound, and upperBracket
   
    intervalRangeTuple
    returns four number values: lowerbound, firstvalue, lastvalue, upperbound
    for example:
    for the interval [1,5), the intervalRangeTuple would be (1,1,4,5)
   
    isValidRange
    checks if the last value of the interval is smaller than the first value of the interval 
'''

def isValidInterval(IntervalString):
  '''checks whether the interval has a valid form'''
  IntervalNoSpace = IntervalString.replace(" ","")
  IntervalisValid = False
  
  '''checks if the brackets are correct'''
  if (IntervalNoSpace[0] == "(" or "[") and (IntervalNoSpace[-1] == ")" or "]"):
    IntervalisValid = True
  else:
    return False 

  IntervalBound = IntervalNoSpace[1:-1].split(",")
  '''checks if without the brackets, the string can be split into two parts'''
  if len(IntervalBound) != 2:
    return False
  '''checks if the two elements of the bounds are numbers'''
  if IntervalBound[0][0] in ('-'):
    if IntervalBound[0][1:].isdigit():
      IntervalisValid = True
    else:
      return False
  else:
    if IntervalBound[0].isdigit():
      IntervalisValid = True
    else:
      return False
  
  if IntervalBound[1][0] in ('-'):
    if IntervalBound[1][1:].isdigit():
      IntervalisValid = True
    else:
      return False
  else:
    if IntervalBound[1].isdigit():
      IntervalisValid = True
    else:
      return False
  
  return IntervalisValid

def parseInterval(IntervalString):
  '''takes the string apart into interval components''' 
  if isValidInterval(IntervalString):
    IntervalNoSpace = IntervalString.replace(" ","")
    lowerBracket = IntervalNoSpace[0]    
    upperBracket = IntervalNoSpace[-1]    
    lowerBound = IntervalNoSpace[1:-1].split(",")[0]
    upperBound = IntervalNoSpace[1:-1].split(",")[1]
    
    return lowerBracket, int(lowerBound), int(upperBound), upperBracket
  
  else:
    raise invalidIntervalInput("invalid interval entered")
  
def intervalRangeTuple(IntervalString):
  '''puts the interval into a tuple consisting of lowerbound,firstvalue,lastvalue,upperbound'''
  try:
    ParsedInterval = parseInterval(IntervalString)
  
    '''determine lowerbound of interval'''
    if ParsedInterval[0] == "[":
      lowInclusive = 0
    elif ParsedInterval[0] == "(":
      lowInclusive = 1
    
    '''determine upperbounds of interval range'''
    if ParsedInterval[-1] == "]":
      upInclusive = 0
    elif ParsedInterval[-1] == ")":
      upInclusive = 1
  
    '''determine the 4 values of the tuple'''
    firstvalue = lowInclusive + ParsedInterval[1]
    lastvalue = ParsedInterval[2] - upInclusive
    lowerbound = ParsedInterval[1]
    upperbound = ParsedInterval[2]
    IntervalRange = (lowerbound, firstvalue, lastvalue, upperbound)

    return IntervalRange
  except (invalidIntervalInput, invalidForm, invalidRange) as e:
    print(str(e))

def isValidRange(IntervalString):
  '''checks if the range of the interval is valid'''
  IntervalisValid = False
  if isValidInterval(IntervalString):
    intervalRange = intervalRangeTuple(IntervalString)
  else:
    return False

  if intervalRange[1] > intervalRange[2]:
    IntervalisValid = False 
  else:
    IntervalisValid = True

  return IntervalisValid

def mergeIntervals(int1, int2):
  ''' function called mergeIntervals that takes two intervals. if the intervals overlap, returns a merged interval. if the intervals do not overlap, exception is thrown.

for example:

  [3,5],[6,8] will return [3,8]
  [3,5),[6,8] will trigger exception'''

  firstRange = int1.intervalRange
  secondRange = int2.intervalRange
  mergeLBound = mergeUBound = ""
  mergeLValue = mergeUValue = 0

  '''sort the two interval to determine the one with a lower bound and starting value'''
  if (firstRange[0] + firstRange[1] < secondRange[0] + secondRange[1]):
    lowerInterval = firstRange
    higherInterval = secondRange
    lowerIntervalObject = int1
  else:
    lowerIntervalObject = int2
    lowerInterval = secondRange
    higherInterval = firstRange
  
  '''check if the two intervals overlap'''
  if(lowerInterval[2] + 1 < higherInterval[1]):
    raise invalidMerge("these two intervals do not overlap")
  
  '''overlapping intervals can be either:
    1)the intervals completely overlap. i.e. [1,5] and [2,3]
    2)the interval includes some overlapping elements, i.e. [1,5]and [3,7] or [1,6) and [5,8]'''
  if lowerInterval[2] + lowerInterval[3] > higherInterval[2] + higherInterval[3]:
    newInterval = lowerIntervalObject
  else:
    mergeLValue = lowerInterval[0]
    mergeUValue = higherInterval[3]
    if lowerInterval[1] == lowerInterval[0]:
      mergeLBound = "["
    else:
      mergeLBound = "("
    if higherInterval[3] == higherInterval[2]:
      mergeUBound = "]"
    else:
      mergeUBound = ")"
    
    newInterval = interval(mergeLBound+str(mergeLValue)+","+str(mergeUValue)+mergeUBound)

  return newInterval

def convertStrList(strlist):
  '''ConvertStrList takes in a list of intervals in string form and converts them to a list of intervals'''
  intervalList = []
  stringList = strlist.replace(" ","").replace('],',']#').replace('),',')#')
  stringList = stringList.split("#")
  
  for i in stringList:
    try:
      intervalList.append(interval(i))
    except(invalidForm, invalidRange, invalidIntervalInput) as e:
      raise invalidList("Invalid interval list entered")
  return intervalList

def mergeOverlapping(intlist):
  '''mergeOverlapping takes a list of intervals and merges all overlapping intervals'''


  '''sort intervals from lowest to highest based on 1) lower bound 2)range starting value 3)range ending value and 4) upper bound'''
  intervalList = []
  intervalList = sorted(intlist, key = lambda i : (i.intervalRange[0],i.intervalRange[1],i.intervalRange[2],i.intervalRange[3]))

  mergeList = []
  mergeList.append(intervalList[0])
  del intervalList[0]

  '''go through each interval and merge if overlapping, add to new merged list if not overlapping'''
  while len(intervalList) != 0:
    endingvalue = mergeList[-1].intervalRange[2] + 1
    startingvalue = intervalList[0].intervalRange[1]
    if endingvalue < startingvalue:
      mergeList.append(intervalList[0])
      del intervalList[0]
    else:
      newInterval = mergeIntervals(mergeList[-1],intervalList[0])
      mergeList.append(newInterval)
      del mergeList[-2]
      del intervalList[0]

  return mergeList

def insert(intlist,newint):
  '''insert takes two arguments: a list of non-overlapping intervals and a single interval. The function inserts the new interval into the overlappinging interval, merging the result if necessary'''

  intlist.append(newint)
  newList = mergeOverlapping(intlist)

  return newList

