# Write a version of a palindrome recognizer that also accepts phrase palindromes
# such as "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?",
# "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil",
# "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude
# Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!".
# Note that punctuation, capitalization, and spacing are usually ignored

# import re

# def palindrome():
# 	string=raw_input("enter the string")
# 	z=re.sub( r'[^a-zA-Z]+','',string)
# 	z=''.join((x for x in st if x not in string.punctuation))
# 	reverse=z[::-1]

# 	if z.lower() == reverse.lower():
# 		return True

# 	return False	



# #test
# # print palindrome("Go hang a salami I'm a lasagna hog.")
# # print palindrome("Was it a rat I saw?")
# # print palindrome("Step on no pets")
# # print palindrome("Sit on a potato pan, Otis!")
# # print palindrome("Lisa Bonet ate no basil")
# # print palindrome("Satan, oscillate my metallic sonatas")
# # print palindrome("I roamed under it as a tired nude Maori")
# # print palindrome("Rise to vote sir")
# # print palindrome("Dammit, I'm mad!")
# # print palindrome("This is not a palindrome")

# print palindrome()

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

def is_palindrome(str):
	
	no_punct=''
	for c in str:
		if c not in punctuations:
			no_punct=no_punct+c
	#print type(no_punct)
	s1=no_punct.lower()
	s2=s1[::-1]
	#print s1
	#print s2
	if s1==s2:
		print True
	else:
		print False	

#test
is_palindrome("Go hang a salami I'm a lasagna hog.")