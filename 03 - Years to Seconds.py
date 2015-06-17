print "Age to Seconds - Bonfire"  # Name of the program, and it's creator.
Age = raw_input("Current age in years: ")  # Ask for the age.
Years = int(Age)  # Turn the age into an integer.

Seconds = (Years * 365.2425 * 24 * 60 * 60)  # Calculate the seconds using 1 Gregorian year.

print str(Age) + " years is equal to " + str(Seconds) + " seconds."  # Print our age in years, to seconds.
