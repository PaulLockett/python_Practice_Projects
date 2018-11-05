# module for random number functions
import random

'''
Draws the hangman depending on the fails and gives the hint
'''
def visualize(try_word, word, fails, letters_used, hint):
	head = " "
	body = ' '
	left_arm = ' '
	right_arm = ' '
	left_foot = ' '
	right_foot = ' '

	if fails[0] > 6:
		head = 0
		body = '|'
		left_arm = '/'
		right_arm = '\\'
		left_foot = '/'
		right_foot = '\\'
	elif fails[0] > 5:
		head = 0
		body = '|'
		left_arm = '/'
		right_arm = '\\'
		left_foot = '/'
	elif fails[0] > 4:
		head = 0
		body = '|'
		left_arm = '/'
		right_arm = '\\'
	elif fails[0] > 3:
		head = 0
		body = '|'
		left_arm = '/'
	elif fails[0] > 2:
		head = 0
		body = '|'
	elif fails[0] > 1:
		head = 0

	print(" _____ ")
	print("|     |")
	print(f"|     {head}")
	print(f"|    {left_arm}{body}{right_arm}")
	print(f"_    {left_foot} {right_foot}")

	str_letters_used = " ".join(letters_used)
	str_try_word = " ".join(try_word)
	print(f"\nfails: {fails[0]} \n letters_used: {str_letters_used} ")
	if fails[0] > 3:
		print(f"\nhint: {hint}")

	print(f"\n{str_try_word}")

'''
Takes input and places it on either the used letters list or the list of blanks
'''
def inputParsing(word_set_list, fails, letters_used, word_set):
	word = word_set_list[word_set][0]
	try_word = word_set_list[word_set][1]

	inputValid = False
	while not inputValid:
		try_letter = input()
		if try_letter.isalpha() and len(try_letter) == 1 and not try_letter in letters_used:
			inputValid = True
			try_letter.lower()
		elif try_letter in letters_used:
			print("You already used that letter please pick another:")
		else:
			print("Sorry, please only give me one letter:")


	if try_letter in word:
		try_word = [word[i] if try_letter == word[i] else try_word[i] for i in range(len(try_word))]
		word_set_list[word_set].pop()
		word_set_list[word_set].append(try_word)
	else:
		temp = fails.pop()
		temp += 1
		fails.append(temp)
		letters_used.append(try_letter)
'''
Checks for wins and loss and signals retry or game over
'''
def reset_or_quit(word_set_list, word_set, fails, gameover, retry_game, num_wins):
	word = word_set_list[word_set][0]
	try_word = word_set_list[word_set][1]
	str_try_word = "".join(try_word)
	retry = ""
	inputValid = False

	if fails[0] > 6:
		print("you lost")

		while not inputValid:
			retry = input("would you like to play again? y/n")
			if retry[0] == "y" or retry[0] == "Y":
				retry_game.pop()
				retry_game.append(True)
				inputValid = True
			elif retry[0] == "n" or retry[0] == "N":
				gameover.pop()
				gameover.append(True)
				inputValid = True
			else:
				print("inputValid please retry")
	elif word == str_try_word:
		print("you win")
		temp = num_wins[0]
		num_wins.pop()
		temp += 1
		num_wins.append(temp)

		while not inputValid:
			retry = input("would you like to play again? y/n: ")
			if retry[0] == "y" or retry[0] == "Y":
				retry_game.pop()
				retry_game.append(True)
				inputValid = True
			elif retry[0] == "n" or retry[0] == "N":
				gameover.pop()
				gameover.append(True)
				inputValid = True
			else:
				print("inputValid please retry")

#declare variables
fails = [0]
letters_used = [' ']
chosen_set = ["easy_words"]
chosen_word_num = [0]
chosen_word = ["lag"]
gameover = [False]
retry = [False]
inputValid = False
num_wins = [0]

# dict of words and thier solves
word_sets = {
	"easy_words": [
		["lag", "---"], 
		["download","--------"], 
		["respawn","-------"], 
		["tank","----"] 
	],
	"med_words": [
		["quickscope","----------"], 
		["speedrun","--------"], 
		["strafing","--------"], 
		["platformer","----------"]
	],
	"hard_words": [
		["first person shooter","----- ------ -------"], 
		["real time strategy","---- ---- --------"], 
		["driving simulator","------- ---------"], 
		["anti aliasing","---- --------"]
	]
}

# dict of hints
hint_sets = {
	"easy_words": {
		'lag': 'This will happen if you are playing on a slow console or computer',
		'download': 'You do this to get a game or file from the internet', 
		'respawn': 'This is how you "come back to life" in a game', 
		'tank': 'This is a psudo class of player that are the main attacker in a group'
	},

	"med_words": {
		'quickscope': '360 no "this word" ', 
		'speedrun': 'the playing of a game to completion very quickly', 
		'strafing': 'moving side to side qickly as to not get sniped easily', 
		'platformer': 'super mario 3 is in this genre of games'
	},

	"hard_words": {
		'first Person Shooter': 'call of duty is in this genre of games', 
		'real time strategy': 'starcraft is in this genre of games', 
		'driving simulator': 'fordza can be considered to be in this genre of games', 
		'anti aliasing': 'option that can be toggled on or off that smooths the edges of videogame graphics'
	}
}

#introduction and setup of word
print("\nHey! Welcome to Hangman_v1 (the early alpha build)")
print("\nTo play the game:")
print("1. select your difficulty")
print("2. chose a letter to guess")
print("3. repeat step 2 till you win (or lose)")
print("4. chose to play again if you want (start back at step one)\n")
print("Hint: the Words all have to do with gaming in some way\n")
while not inputValid:
	level_choice = input("what level word do you want to play with?\n easy, medium, or hard: ")
	if level_choice.isalpha():
		level_choice.lower()

	if level_choice.isalpha() and (level_choice == "easy" or level_choice == "medium" or level_choice == "hard"):
		if level_choice == "easy":
			chosen_set[0] = "easy_words"
		if level_choice == "medium":
			chosen_set[0] = "med_words"
		if level_choice == "hard":
			chosen_set[0] = "hard_words"
		inputValid = True
	else:
		print("Input invalid, please type the name of one of the three option")
inputValid = False
chosen_word_num[0] = random.randint(0,3)
chosen_word[0] = word_sets[chosen_set[0]][chosen_word_num[0]][0]
fails[0] = 0
letters_used.clear()
letters_used.append(" ")

#intial draw of hangman
visualize(word_sets[chosen_set[0]][chosen_word_num[0]][1], word_sets[chosen_set[0]][chosen_word_num[0]][0], fails, letters_used, hint_sets[chosen_set[0]][chosen_word[0]])

while not gameover[0]:
	# resets the board to a new word
	if retry[0]:
		while not inputValid:
			level_choice = input("what level word do you want to play with?\n easy, medium, or hard: ")
			if level_choice.isalpha():
				level_choice.lower()

			if level_choice.isalpha() and (level_choice == "easy" or level_choice == "medium" or level_choice == "hard"):
				if level_choice == "easy":
					chosen_set[0] = "easy_words"
				if level_choice == "medium":
					chosen_set[0] = "med_words"
				if level_choice == "hard":
					chosen_set[0] = "hard_words"
				inputValid = True
			else:
				print("Input invalid, please type the name of one of the three option")
		inputValid = False
		chosen_word_num[0] = random.randint(0,3)
		chosen_word[0] = word_sets[chosen_set[0]][chosen_word_num[0]][0]
		fails[0] = 0
		letters_used.clear()
		letters_used.append(" ")
		visualize(word_sets[chosen_set[0]][chosen_word_num[0]][1], word_sets[chosen_set[0]][chosen_word_num[0]][0], fails, letters_used, hint_sets[chosen_set[0]][chosen_word[0]])
	retry[0] = False
	
	# takes input and puts it in the right place
	inputParsing(word_sets[chosen_set[0]], fails, letters_used, chosen_word_num[0])

	# draws the hangman
	visualize(word_sets[chosen_set[0]][chosen_word_num[0]][1], word_sets[chosen_set[0]][chosen_word_num[0]][0], fails, letters_used, hint_sets[chosen_set[0]][chosen_word[0]])
	
	#checks for loss or win
	reset_or_quit(word_sets[chosen_set[0]], chosen_word_num[0], fails, gameover, retry, num_wins)

# Report wins and goodbye
print("Thanks for Playing!")
print("You won:",num_wins[0],"times")
