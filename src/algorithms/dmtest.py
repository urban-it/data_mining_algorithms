# For random generation of numbers import randint
from random import randint, shuffle

# Simple generator for test nums (40-40-20 biased), returns 1D array of nums
def numGenLight(entries, shuffle, num_lenght):
	dataArray = []
	for i in range(0, int(entries)):
		if i < round(entries * 0.4):
			num = generateNumber(num_lenght, 2)
		elif i >= round(entries * 0.4) and i < round(entries * 0.6):
			num = generateNumber(num_lenght, 9)
		elif i >= round(entries * 0.6) and i < round(entries * 0.9):
			num = generateNumber(num_lenght, 4)
		else:
			num = generateNumber(num_lenght, randint(0,9))
		dataArray.append(num)
	if shuffle:
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

# Function for generating 'entries'x int_lenght'-long numbers in 'clusters' clusters
def numGen(entries, cluster, int_lenght, suffle_value):
	dataArray = []
	clusterArray = []

	for cluster_num in range(0, cluster):
		clusterArray.append(randint(10,99))

	for item in range(0, entries):
		decider = randint(0, 2)
		if decider == 2:
			dataArray.append(generateNumber(int_lenght, randint(1,9)))
		else:
			cluster_decider = randint(0, cluster - 1)
			dataArray.append(generateNumber(int_lenght - 1, clusterArray[cluster_decider]))

	if suffle_value:
		shuffle(dataArray)

	return dataArray
