print "FizzBuzz - Bonfire"  # Name of the program, and it's creator.
Input = int(raw_input("Max Range: "))  # How high should we count to?

for Input in range(1,Input):  # While there are still numbers to work with (1, Max Range), work!
    if (Input % 5 == 0) & (Input % 3 == 0):  # If the input is divisible by 5 and 3, FizzBuzz. (Double remainder of 0)
        print str(Input) + " FizzBuzz"
    elif Input % 3 == 0:  # If the input is ONLY divisble by 3, Fizz. (Modulus remainder of 0)
        print str(Input) + " Fizz"
    elif Input % 5 == 0:  # If the input is ONLY divisble by 5, Buzz. (Modulus remainder of 0)
        print str(Input) + " Buzz"

  # We check to see if the number can be divisible by 5 or 3, and see if it's remainder is a 0. If it is, mark it.
