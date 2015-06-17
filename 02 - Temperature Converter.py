print "Temperature Converter - Bonfire"  # Name of the program, and it's creator.
print "Thanks to AllMeasures.com for the conversion table."  # http://www.allmeasures.com/temperature.html

ConvertF = str.lower(raw_input("Convert Temperature From (Accepts F, C, or K) : "))  # Accepts F, C, or K.
ConvertT = str.lower(raw_input("Convert Temperature To (Accepts F, C, or K) : "))  # Accepts F, C, or K.
InTemp = str.lower(raw_input("Input Temperature: "))  # Temperature, pretty straightforward
Temp = int(InTemp)  # Turn our temperature into an integer

if ConvertF == ConvertT:  # If you're converting something to itself, it should equal itself
	print "Final temperature equals" + Temp  # Output

if (ConvertF == "f") & (ConvertT == "c"):  # F to C
	Output = ((Temp - 32) * 5/9)
	print Output

elif (ConvertF == "f") & (ConvertT == "k"):  # F to K
	Output = ((Temp - 32) * 5/9 + 273.15)
	print Output

if (ConvertF == "c") & (ConvertT == "f"):  # C to F
	Output = ((Temp * 9/5) + 32)
	print Output

elif (ConvertF == "c") & (ConvertT == "k"):  # C to K
	Output = (Temp + 273.15)
	print Output

if (ConvertF == "k") & (ConvertT == "f"):  # K to F
	Output = ((Temp - 273.15) * 9/5 + 32)
	print Output

elif (ConvertF == "k") & (ConvertT == "c"):  # K to C
	Output = (Temp - 273.15)
	print Output
