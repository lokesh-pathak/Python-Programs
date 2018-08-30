# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. 
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

def sum(l):
  result = 0
  for i in l:
    result += i
  return result

def multiply(l):
  result = 1
  for i in l:
    result *= i
  return result

#test
print sum([1,2,3,4])
print multiply([1,2,3,4])