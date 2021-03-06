# In a game of Lingo, there is a hidden word, five characters long.
# The object of the game is to find this word by guessing,
# and in return receive two kinds of clues:
# 1) the characters that are fully correct, with respect to identity as well as to position, and
# 2) the characters that are indeed present in the word, but which are placed in the wrong position.
# Write a program with which one can play Lingo. Use square brackets to mark characters correct in the sense of
# 1) and ordinary parentheses to mark characters correct in the sense of
# 2) Assuming, for example, that the program conceals the word "tiger",
# you should be able to interact with it in the following way:


# snake
# Clue: snak(e)
# fiest
# Clue: f[i](e)s(t)
# times
# Clue: [t][i]m[e]s
# tiger
# Clue: [t][i][g][e][r]

def lingo():
	word='tiger'
	guess=raw_input()
	while guess!=word:
		pos=-1
		output=''
		for char in guess:
			pos+=1
			if char in word:
				if word[pos]==guess[pos]:
					output+='['+char+']'
				else:
					output+='('+char+')'
			else:
				output+=char
		print 'clue:' +output
		guess=raw_input()
	print 'Found!'

#test
lingo()
