# Define a function that computes the length of a given list or string.

def lenght(str):

 count = 0
 for char in str:
     count += 1
 return count
#test
print lenght('my name is lokesh')
print lenght('learning python')
