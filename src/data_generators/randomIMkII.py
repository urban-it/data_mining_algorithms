from random import randint

def generatePLZ():
	plz = ""
	for i in range(0,5):
		plz = plz + str(randint(0,9))
	return plz

def generateTel():
	telephone = ""
	for i in range(0, 11):
		telephone = telephone + str(randint(0,9))
	return telephone
