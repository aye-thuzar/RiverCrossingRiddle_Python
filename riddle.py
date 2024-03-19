'''
River Crossing Riddle Simulation
Aye Thuzar
'''


def river_crossing_simulation():

	'''we will use booleans to model each character
	   False means on bank0
	   True means on bank1
	   the goal is to move all characters to bank1
	'''

	# using a list so that we can pass in as one parameter
	# to all needed functions
	# [Human, Wolf, Goat, Cabbage]
	characters = [False,False,False,False]

	display_description()

	# keep playing the game until you each the final state
	# or a fail state
	while(has_reach_end_state(characters) < 1):
		show_game_state(characters)
		choice = get_input()
		change_state(characters, choice)
	show_game_state(characters)

def get_input():
	# getting input from the user
	char = input("Please enter h, w, g or c to move the characters: ")
	# error_handing
	while char.lower() not in ['h', 'w', 'g', 'c']:
		print("Your input is not valid.")
		char = input("Please reenter h, w, g or c to move the characters: ")
	return char

def display_description():
	'''This funciton displays the game rules.'''

	s = "-------------------------------------------------------------------------------\n"
	s += "River Crossing Riddle Simulation\n"
	s += "-------------------------------------------------------------------------------\n"
	s += "The farmer wants to move the wolf, the goat and the cabbage across the river,\n"
	s += "but he can only carry one thing at a time on his boat. if you leave the goat \n" 
	s += "alone with the cabbage the goat will eat the cabbage and the wolf will eat \n"
	s += "the goat if it gets the chance alone with it. \n"
	s += "The farmer always moves move other characters or by himself. Each character \n" 
	s += "can only move to the other bank if they are on the same bank as the farmer."
	print(s)


def show_game_state(actors):
	'''This function display which charcaters are on which bank.'''
	bank0 = "";
	bank1 = "";
	line="\n----------------------------------------\n"
	if actors[0]:
		bank1=bank1+"        H"
	else:
		bank0=bank0+"        H"
	if actors[1]:
		bank1=bank1+"        W"
	else:
		bank0=bank0+"        W"
	if actors[2]:
		bank1=bank1+"        G"
	else:
		bank0=bank0+"        G"
	if actors[3]:
		bank1=bank1+"        C"
	else:
		bank0=bank0+"        C"
	river = "\n ~~~~       ~~~~~~~\n       ~~~~    ~~~\n"
	print("\nGAME STATE:")
	print(bank0 + line + river + line + bank1 + "\n");
	

def change_state(actors, char):
	'''This function change move the characters based on the user input
	by simply toggling the booleans in the actor list.
	The farmer always moves move other characters or by himself. Each 
	character can only move to the other bank if they are on the same bank 
	as the farmer'''
	if char.lower() == 'c' and actors[3] ==  actors[0]:
		actors[3] = not actors[3]
		actors[0] = not actors[0]
	elif char.lower() == 'g' and actors[2] ==  actors[0]:
		actors[2] = not actors[2]
		actors[0] = not actors[0]
	elif char.lower() == 'w' and actors[1] ==  actors[0]:
		actors[1] = not actors[1]
		actors[0] = not actors[0]
	elif char.lower() == 'h':
		actors[0] = not actors[0]
	else:
		print("The farmer needs to be on the same bank as the character you want to move.")


def has_reach_end_state(actors):
	'''The end state could be the final state or a fail state'''
	if (actors[1] and actors[2]) and actors[3]: # all on bank1
		print("\nYou have sccessfully moved all characters!")
		return 1
	if (actors[1] == actors[2]) and (actors[0] == actors[3]) and (actors[1] != actors[0]):
		print("\nThe wolf ate the goat! =( ")
		return 1
	if (actors[2] == actors[3]) and (actors[0] == actors[1]) and (actors[2] != actors[0]):
		print("\nThe goat ate the cabbage! =( ")
		return 1
	return 0


# call the main simuliation function which calls other helper functions
river_crossing_simulation()