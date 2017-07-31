# 7/20/2017 Denise Lamb
# so i attended a 6 hour General Assembly class in Boston 
# and this is all they taught us to make. We didn't even cover python until
# after lunch. Argh! #wantToLearnMore!!

# this script runs a game of high/low using python interpreter 3.x 

# getting the random module
import random 


print("hello there, and welcome to the game of high low. try and guess the number 1-10 - so exciting!")

# my variables
num_computer_chooses = random.randint(1, 10)
prompt = 'Guess a number between 1 and 10: '
user_guess = None
responses = {'low': 'nope! too low! Try again.', 
			 'high': 'nope! too high! Try again.', 
			 'correct': 'you got it right! yay!'}

while user_guess != num_computer_chooses: 
	# user makes a guess
	user_guess = raw_input(prompt)

	try: user_guess = int(user_guess)
	except Exception:
		print('input must be a number')
		continue

	# validate user_guess is a number
	if user_guess < 1 or  user_guess > 10:
		print('invlaid number. please guess again.')
	# check user_guess against num_computer_chooses
	elif user_guess > num_computer_chooses:
		# too high
		print(responses['high'])
	elif user_guess < num_computer_chooses:
		# too low
		print(responses['low'])
	else:
		# correct 
		print(responses['correct'])

		