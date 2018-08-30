# Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. 
# For example, histogram([4, 9, 7]) should print the following:

# ****
# *********
# *******

# from ex11 import generate_n_chars

# def histogram(l):

# 	for x in l:
# 		char=generate_n_chars(x,'*')
# 	print char

# #test

# histogram([1,2,3])
# histogram([4,9,7])
# histogram([2,5,8])


def histogram(l):
    for x in l:
        output = ''
        times = x
        while( times > 0 ):
          output += '*'
          times = times - 1
        print(output)
    print('\n')

#test

histogram([4, 9, 7])

histogram([2, 3, 6, 5])

histogram([1, 2, 3, 4])

histogram([5, 9, 7, 2])