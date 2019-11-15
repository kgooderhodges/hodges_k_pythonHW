from gameFunctions import gameVars

# need a function to run to compare the choices
# # figure out wat to pass into the function - hint => what are you comparing?
def compare(player):
	
	if player == gameVars.computer:
		#we have a tie, no point going any further
		print("tie, no one wins! try again")

	elif player =="quit":
		print("you chose to quit, quitter.")
		exit()

	elif player == "Rock": 
		if gameVars.computer == "Paper":
			print("************************************")
			print("BOO! You lose!", gameVars.computer, "covers", player)
			print("************************************")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("************************************")
			print("YAY! Winning!", player, "smashes", gameVars.computer)
			print("************************************")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "Paper": 
		if gameVars.computer == "Scissors":
			print("************************************")
			print("BOO! You lose!", gameVars.computer, "cuts", player)
			print("************************************")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("************************************")
			print("YAY! Winning!", player, "covers", gameVars.computer)
			print("************************************")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "Scissors": 
		if gameVars.computer == "Rock":
			print("************************************")
			print("BOO! You lose!", gameVars.computer, "smashes", player)
			print("************************************")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("************************************")
			print("YAY! !", player, "cuts", gameVars.computer)
			print("************************************")
			gameVars.computer_lives = gameVars.computer_lives -1 