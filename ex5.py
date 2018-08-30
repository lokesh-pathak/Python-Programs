# Write a function translate() that will translate a text into "rovarspraket" (Swedish for "robber's language"). 
# That is, double every consonant and place an occurrence of "o" in between. 
# For example, translate("this is fun") should return the string "tothohisos isos fofunon".


import string

#The concatenation of the ascii_lowercase and ascii_uppercase constants described below. This value is not locale-dependent.

#letters = string.ascii_letters								

vowels = ['a','e', 'i', 'o', 'u']

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

def translate(str):
  result = ""
  for c in str:
    if c in consonants:
      result += c+'o'+c
    else:
      result += c
  return result

#test
print translate("python is fun")
print translate("you should try this")