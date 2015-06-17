import requests
# Import every package we need.

print "Name Generator - Bonfire"  # Name of the program, and it's creator.
print "Credits to RandomUser.Me for the endless name list!"  # http://randomuser.me (Lets hope that they stay up!)

Gender = str.lower(raw_input("Male, Female, or Random? "))  # Question
Amount = raw_input("Number of names to generate? ")  # Question
Number = int(Amount)  # Couldn't do int(raw_input) here, as it would break for some reason. Redundant, I know.

def generate(Gender, Number):

	if Gender == "random":  # Random
		while Number > 0:  # While there are still names left to generate, work!
			req = requests.get("http://api.randomuser.me")  # Fetch JSon output from an API.
			rjson = req.json()  # Let the program know that we're working  with JSon.
			First = rjson['results'][0]['user']['name']['first']  # Fetch the first name.
			Last = rjson['results'][0]['user']['name']['last']  # Fetch the last name.
			print First.capitalize() + " " + Last.capitalize()  # Lets capitalize the first and last name, because the JSon doesn't do this defaultly.
			Number -= 1  # Generate one less name (Minus one)

	else:  # OR for Male and Female
		while Number > 0:
			req = requests.get("http://api.randomuser.me/?gender=" + Gender)
			rjson = req.json()
			First = rjson['results'][0]['user']['name']['first']
			Last = rjson['results'][0]['user']['name']['last']
			print First.capitalize() + " " + Last.capitalize()
			Number -= 1

generate(Gender, Number)  # Call the Generate function.
