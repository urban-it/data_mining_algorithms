# For random generation of numbers import randint
from random import randint, shuffle

# Simple generator for test data (100 plzs, 20-30-50 biased), returns 1D array of plzs 
def testgenerator():
	dataArray = []
	for i in range(0,100):
		if i <= 40:
			plz = generatePLZ("05")
		elif i > 40 and i < 80:
			plz = generatePLZ("50")
		else:
			plz = generatePLZ("")
		dataArray.append(plz)
	shuffle(dataArray)
	return dataArray

# Generates a PLZ from a certain start point
def generatePLZ(start):
	if len(start) == 0:
		plz = ""
		for j in range(1,6):
			plz = plz + str(randint(0,9))
	else:
		plz = start
		for j in range(1,4):
			plz = plz + str(randint(0,9))
	return plz
