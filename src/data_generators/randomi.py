# Meet randomI, a random data generator for test data generation

def main(i, a, b):
	for x in range(0, int(i)):
		generateFile(a, b)

def generateFile(rows, lenghtOfRows):
	for y in range(0, rows):
		generateRow(lenghtOfRows)

def generateRow(lenghtOfRows):
	for z in range(0, lenghtOfRows):
		line = line + generateChar()

print("Hello World")
i = input("How many datapices would you like to generate?")
a = input("How many rows should each datapiece have?")
b = input("How long should each row be?")

main(i, a, b)