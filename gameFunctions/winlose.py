from random import randint
from gameFunctions import gameVars, compare

def winorlose(status):
	print(status, "\n")
	print("You", status)
	print("Computer wants to play again, do YOU? \n")
	choice = input("Y / N?")

	if choice == "Y" or choice =="y":
		# reset the game and start all over again
		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		gameVars.player = False
		gameVars.computer = gameVars.choices [randint(0, 2)]
		
	elif choice == "N" or choice == "n":
		print("You choose to quit? Alright then, quitter!")
		exit()
	else:
		print("Come on! You know the drill. Yes or no!")
		# recursion function -> calling a function from inside itself
		winorlose(status)
