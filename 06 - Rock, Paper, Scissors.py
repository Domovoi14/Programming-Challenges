from random import randint  # Necessary packages

print "Rock, Paper, Scissors - Bonfire"  # Name of the program, and it's creator.
Choice = raw_input("Rock, Paper, or Scissors? ")  # Fetch our desired hand-choice

Random = randint(1,10000)  # Generate a random integer, 1 to 10,000

if Random <= 3333:  # Define which integer correlates to which choice
    Outcome = "Rock"
elif 3333 < Random <= 6666:
    Outcome = "Paper"
elif 6666 < Random <= 10000:
    Outcome = "Scissors"

if (Choice == "Rock") & (Outcome == "Rock"):  # R v R | Tie
    print "Opponent picked Rock. Tie."
elif (Choice == "Rock") & (Outcome == "Paper"):  # R v P | Lose
    print "Opponent picked Paper. You lose."
elif (Choice == "Rock") & (Outcome == "Scissors"):  # R v S | Win
    print "Opponent picked Scissors. You win."
elif (Choice == "Paper") & (Outcome == "Rock"):  # P v R | Win
    print "Opponent picked Rock. You win."
elif (Choice == "Paper") & (Outcome == "Paper"):  # P v P | Tie
    print "Opponent picked Paper. Tie."
elif (Choice == "Paper") & (Outcome == "Scissors"):  # P v S | Lose
    print "Opponent picked Scissors. You lose."
elif (Choice == "Scissors") & (Outcome == "Rock"):  # S v R | Lose
    print "Opponent picked Rock. You lose."
elif (Choice == "Scissors") & (Outcome == "Paper"):  # S v P | Win
    print "Opponent picked Paper. You win."
elif (Choice == "Scissors") & (Outcome == "Scissors"):  # S v S | Tie
    print "Opponent picked Scissors. Tie."
else:
    print "Something went wrong. Oops!"  # Everything else