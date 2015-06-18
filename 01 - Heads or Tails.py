from random import randint  # Necessary packages

print "Head or Tails - Bonfire"  # Name of the program, and it's creator.
Flips = raw_input("Number of coins to flip? ") # Question
NumFlips = int(Flips)  # Convert input to integer.

while NumFlips > 0:	 # While there are still coins to flip, work!
	Number = randint(1,10000)  # Generate a random integer, 1 to 10,000.

	if Number > 5000:  # If the number is greater than 5,000, then...
		Outcome = "Heads"  # The outcome is heads.
	elif Number <= 5000:  # If the number is less than or equal to 5,000, then...
		Outcome = "Tails"  # The outcome is tails.

	print Outcome + " with a number of " + str(Number)  # Print the outcome, and it's cooresponding number.
	NumFlips -= 1  # Reduce the number of needed flips by one.
