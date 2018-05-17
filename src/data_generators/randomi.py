# Meet randomI, a random data generator for test data generation
from random import randint

import time
from datetime import date

def main(i, a, b):
	for x in range(0, i):
		writeFile(generateFile(a, b), x)

def generateFile(rows, lenghtOfRows):
	content = []
	for y in range(0, rows):
		content.append(generateRow(lenghtOfRows))
	return content

def generateRow(lenghtOfRows):
	row = ""
	for z in range(0, lenghtOfRows):
		row = row + str(randint(0, 9))
	return row

def writeFile(content, x):
	file = open("testdata/file" + str(x) + ".txt", "w")
	for w in range(0, len(content)):
		file.write(content[w] + "\n")

print("Hello World")
i = int(input("How many datapices would you like to generate? "))
a = int(input("How many rows should each datapiece have? "))
b = int(input("How long should each row be? "))

start_time = time.time()

main(i, a, b)

print("Data is generated. Have fun!")
sec = time.time() - start_time
minutes = sec / 60
print("randomI took " + str(sec) + " seconds (" + str(minutes) + " minutes) for execution.")