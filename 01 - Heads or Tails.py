from random import randint # Necessary packages

print "Head or Tails - Bonfire" # Name of the program, and it's creator.
Flips = raw_input("Number of coins to flip? ") # Question
NumFlips = int(Flips) # Convert input to integer.

while NumFlips > 0:	# While there are still coins to flip, work!
	Number = randint(0,100) # Generate a random integer, 0 to 100.

	if Number >= 50: # If the number is greater or equal to 50, then...
		Outcome = "Heads" # The outcome is heads.
	elif Number <= 49: # If the number is less than or equal to 49, then...
		Outcome = "Tails" # The outcome is tails.

	print Outcome + " with a number of " + str(Number) # Print the outcome, and it's cooresponding number.
	NumFlips -= 1 # Reduce the number of needed flips by one.