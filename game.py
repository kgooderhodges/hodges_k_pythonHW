# import the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameVars, compare


while gameVars.player is False:
	print("************************************")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("************************************")
	print("Choose your weapon!\n")
	player=input("Choose Rock, Paper, Scissors: \n")
	if player == "rock":
		player=("Rock")
	if player == "paper":
		player=("Paper")	
	if player == "scissors":
		player=("Scissors")

	print("************************************")
	print("Computer - ", gameVars.computer)
	print("Player - ", player)
	print("************************************")

	compare.compare(player)

	if gameVars.player_lives is 0:
		winlose.winorlose("LOSE :(")
				
	elif gameVars.computer_lives is 0:
		winlose.winorlose("WON!")


	player = False
	gameVars.computer = gameVars.choices[randint(0,2)]
 