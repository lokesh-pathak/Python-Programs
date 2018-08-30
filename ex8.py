# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

from ex7 import reverse

def is_palindrome(str):
	reverse(str)
	return str == str[::-1]

#test
print is_palindrome("radar")
# print is_palindrome("Anna")
# print is_palindrome("Definitely not a palindrome :)")
# print is_palindrome("Rotator")
# print is_palindrome("what is palindrom")
