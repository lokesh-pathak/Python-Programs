# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.

def max(num1, num2,num3):

	if (num1 > num2) and (num1 > num3):
	   largest = num1
	elif (num2 > num1) and (num2 > num3):
	   largest = num2
	else:
	   largest = num3
	return largest
#test
print max(3, 5 ,4)
print max(10, 6 , 78)
