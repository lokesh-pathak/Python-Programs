# Represent a small bilingual lexicon as a Python dictionary in the following fashion
#  {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"} 
#  and use it to translate your Christmas cards from English into Swedish. 
#  Use the higher order function map() to write a function translate() 
#  that takes a list of English words and returns a list of Swedish words.


d = {"merry":"god", "christmas":"jul", "and":"och","happy":"gott", "new":"nytt", "year":"ar"}

def translate(l):
	return map(lambda x: d[x], l.split())

#test
print translate('merry christmas and happy new year')
print translate('happy new year')
