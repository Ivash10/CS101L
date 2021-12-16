import math

# method return average
def average(values):
# list is empty , return nan
 if len(values) == 0:
  return math.nan
  sum = 0
  for val in values:
   sum = sum + val
   return sum/len(values)