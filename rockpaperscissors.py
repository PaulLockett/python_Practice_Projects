import random
import time



print("\n                   welcome to RPS!\n          *also know as rock paper sissors")
print("\nIn this game you play against me (a stylish computer) in a game of RPS.")
print("\nRPS is played by two players each choising rock, paper, or sissors.")
print("                   rock beats sissors")
print("                   paper beats rock")
print("                   sissors beats paper")


intitialinput = False

while not intitialinput:
	play = input("\nWould you like to play? ")
	if play[0] == "y" or play[0] == "Y":
		num_of_games = int(input("How many games should we play?"))
		intitialinput = True
intitialinput = False

player_wins = 0
robot_wins = 0
for x in range(num_of_games):
	print("this is game",x + 1)
	inputvalid = False
	print("\nok my turn")
	print("what should my move be?")
	time.sleep(2)
	print("...")
	time.sleep(2)
	print("ok I got it!")

	robot_choice = random.randint(0,2)

	print("\n*robo has made a choice*")
	print("now it's your turn")


	while not inputvalid:
		player_choice = input("\nDo you pick rock, paper, or sissors?\n*pick by typing your choice:  ")
		if player_choice == "Rock":
			player_choice = "rock"
			inputvalid = True
		elif player_choice == "Paper":
			player_choice = "paper"
			inputvalid = True
		elif player_choice == "Sissors":
			player_choice = "sissors"
			inputvalid = True
		elif player_choice == "rock" or player_choice == "paper" or player_choice == "sissors":
			inputvalid = True
		else:
			print("\nI did't understand that please type either rock, paper, or sissors.")

	#print(player_choice," ",robot_choice)

	if player_choice == "rock":
		if robot_choice == 0:
			print("\nit's a tie")
		elif robot_choice == 1:
			print("\nrobo wins")
			robot_wins += 1
		elif robot_choice == 2:
			print("\nplayer wins")
			player_wins += 1
	elif player_choice == "paper":
		if robot_choice == 1:
			print("\nit's a tie")
		elif robot_choice == 2:
			print("\nrobo wins")
			robot_wins += 1
		elif robot_choice == 0:
			print("\nplayer wins")
			player_wins += 1
	elif player_choice == "sissors":
		if robot_choice == 2:
			print("\nit's a tie")
		elif robot_choice == 0:
			print("\nrobo wins")
			robot_wins += 1
		elif robot_choice == 1:
			print("\nplayer wins")
			player_wins += 1
if player_wins > robot_wins:
	print("\nThe Player wins overall")
elif player_wins < robot_wins:
	print("\nThe Robot wins overall")
elif player_wins == robot_wins:
	print("\nThere is an overall tie")
