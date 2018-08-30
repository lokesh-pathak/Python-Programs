# Define a simple "spelling correction" function correct() 
# that takes a string and sees to it that 
# 1) two or more occurrences of the space character is compressed into one, 
# and 
# 2) inserts an extra space after a period if the period is directly followed by a letter. 
# E.g. correct("This   is  very funny  and    cool.Indeed!") 
# should return "This is very funny and cool. Indeed!" Tip: Use regular expressions! 

import re

def correct(str):

	# for multiple space

	str=re.sub(' +',' ',str)
		
	#for space after period
	# (?<=[.,]) looks behind for dots or commas
	#(?=[^\s]) look ahead that matches anything that isn't a space
	# str=re.sub(r'(?<=[.,])(?=[^\s])',' ',str)
	
	str=re.sub(r'\.','. ',str)
	return str
#test
print correct("This is       very        funny and cool.Indeed!")
print correct("This   is  very funny  and    cool.Indeed!")