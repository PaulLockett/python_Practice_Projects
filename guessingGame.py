import random

number = random.randint(1,10)
guess = 0
while not guess == number:
	guess = int(input("\nguess a number between 1 and 10: "))
	if guess < number:
		print("Your guess is too low")
	elif guess > number:
		print("your guess is too high")
	elif guess == number:
		print("you guessed right!")
		play_More = input("\nwould you like to ply again? y/n ")
		if play_More == "y" or play_More == "Y":
			number = random.randint(1,10)
print("bye bye!")