# Represent a small bilingual lexicon as a Python dictionary in the following
# fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"} 
# and use it to translate your Christmas cards from English into Swedish. 
# That is, write a function translate() that takes a list of English words and returns a list of Swedish words.


dictionary = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}

def translate(string):
	tstr = ""
	for i in string.split(" "):

		#The get() method returns the value for the given key, if present in the dictionary. If not, then it will return None 

		if (str(dictionary.get(i))) != "None":
			tstr= tstr+str(dictionary.get(i))+" "
		else:
			tstr= ""
			print("Please check your sentances")
	print tstr
             
#test
translate('happy new year')
translate('merry christmas and happy new year')