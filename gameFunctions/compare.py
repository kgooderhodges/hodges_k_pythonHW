from gameFunctions import gameVars

def compare(player):
	
	if player == gameVars.computer:
		print("----- TIE, no one wins! Try again -----")

	elif player =="quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "Rock": 
		if gameVars.computer == "Paper":
			print("------------------------------------")
			print("BOO! You lose!", gameVars.computer, "covers", player)
			print("------------------------------------")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("************************************")
			print("YAY! Winning!", player, "smashes", gameVars.computer)
			print("************************************")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "Paper": 
		if gameVars.computer == "Scissors":
			print("------------------------------------")
			print("BOO! You lose!", gameVars.computer, "cuts", player)
			print("------------------------------------")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("************************************")
			print("YAY! Winning!", player, "covers", gameVars.computer)
			print("************************************")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "Scissors": 
		if gameVars.computer == "Rock":
			print("------------------------------------")
			print("BOO! You lose!", gameVars.computer, "smashes", player)
			print("------------------------------------")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("************************************")
			print("YAY! Winning!", player, "cuts", gameVars.computer)
			print("************************************")
			gameVars.computer_lives = gameVars.computer_lives -1 