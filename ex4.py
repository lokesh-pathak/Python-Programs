# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False otherwise.

vowels = ['a', 'e', 'i', 'o', 'u']

def vornot(str):
  if str in vowels:
    return True
  else:
    return False

#test
print vornot('e')
print vornot('u')
print vornot('z')
print vornot('x')