# import the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameVars, compare


while gameVars.player is False:
	print("====================================")
	print("Computer Lives:", gameVars.computer_lives, "/", gameVars.total_lives)
	print("Player Lives:", gameVars.player_lives, "/", gameVars.total_lives)
	print("====================================")
	print("Choose your weapon!\n")
	player=input("choose rock, paper, scissors: \n")

	# start doing some logic and condition checking
	# print("computer:", computer, "player:", player)

	# -- this is where you would do the compare stuff
	compare.compare(player)
	# -- end compare stuff

	if gameVars.player_lives is 0:
		winlose.winorlose("lose")
				
	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")


	player = False
	gameVars.computer = gameVars.choices[randint(0,2)]
