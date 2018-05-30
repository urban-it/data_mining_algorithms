# For random generation of numbers import randint
from random import randint, shuffle

# Simple generator for test plzs (40-40-20 biased), returns 1D array of plzs
def plzGen(entries):
	dataArray = []
	plz_lenght = 5
	for i in range(0, int(entries)):
		if i < round(entries * 0.4):
			plz = generateNumber(plz_lenght, 2)
		elif i >= round(entries * 0.4) and i < round(entries * 0.8):
			plz = generateNumber(plz_lenght, 9)
		else:
			plz = generateNumber(plz_lenght, randint(0,9))
		dataArray.append(plz)
	shuffle(dataArray)
	return dataArray

# Function for generating the content of one single row randomly
def generateNumber(numberLenght, startingNumber):
	number = str(startingNumber)
	for length in range(0, numberLenght - 1):
		number = number + str(randint(0,9))
	return number

# Function for writing data into a file (content = string, nameChunkStart and namePartStart are for better naming)
# /testdata/ folder has to be created at this point
def writeFile(content, nameChunkStart, namePartStart):
	filenumber = int(nameChunkStart) + int(namePartStart)
	file = open("testdata/file" + str(filenumber) + ".txt", "w")
	for w in range(0, len(content)):
		file.write(content[w] + "\n")