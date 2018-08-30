# Write a program able to play the "Guess the number"-game, 
# where the number to be guessed is randomly chosen between 1 and 20. 
# (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

# >>> import guess_number
# Hello! What is your name?
# Torbjorn
# Well, Torbjorn, I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too low.
# Take a guess.
# 15
# Your guess is too low.
# Take a guess.
# 18
# Good job, Torbjorn! You guessed my number in 3 guesses!

def guess_the_number():
	number=10
	guesses=0

	user_name=raw_input('Hello! What is your name?')
	print 'well, %s, I am thinking of a number between 1 and 20.' % (user_name)
	print 'Take a guess.'

	guess=input()

	while guess!=number:
		# if guess<=0 or guess>=21:
		# 	print 'the guess number should not be less than 0 or greater then 20'
		# 	print 'Take a guess.'
		# 	guess=input()

		if guess<number:
			print 'Your guess is too low.'
			print 'Take a guess.'
			guesses+=1
			guess=input()
		else:
			print 'Your guess is too high.'
			print 'Take a guess.'
			guesses+=1
			guess=input()

	if guess == number:
		print 'Good job, %s! You guessed my number in %d guesses!' % (user_name,guesses)
	

#test
guess_the_number()