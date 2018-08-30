# According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
# ("Semordnilap" is itself "palindromes" spelled backwards.)
# Write a semordnilap recogniser that accepts a file name
# (pointing to a list of words) from the user and finds and prints
# all pairs of words that are semordnilaps to the screen.
# For example, if "stressed" and "desserts" is part of the word list,
# the the output should include the pair "stressed desserts".
# Note, by the way, that each pair by itself forms a palindrome!
import re
def Semordnilap():

	f=open('file_path','r+')
	file=f.readlines()
	for line in file:
		line = line.strip()
		z=list(line.split())
		for word in z:
			p=word[::-1]
			for x in z:
				if x==p:
					print [word,x]
	print ("the line is not semordnilap")
	f.close()

#test

# Semordnilap('stressed','desserts')
# Semordnilap('stressed','dessert')

Semordnilap()
