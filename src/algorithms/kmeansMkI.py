#!/usr/bin/env python
#title:				kmeansMkI.py
#description:		Our personal Python K-Means++ implementation
#author:			Tillmann Brendel, Conrad Großer
#date:				26.05.2018
#version:			0.1
#usage:				python pyscript.py
#notes:
#known_issues:
#python_version:	3.x
#==============================================================================

# IMPORTS

# Importing the time for benchmarking purposes
import time
from datetime import date

# For random generation of numbers import randint and shuffle to shuffle an array
from random import randint, shuffle

# Importing libary for multi core processing
import multiprocessing

# CODE
# Main function of the algorithm
def kmeansmk1(clusters):
	print("Sorting data into " + str(clusters) + " clusters.")

# Startup function for collecting necesarry data
def startup(data):
	clusters = int(input("How many clusters are known? "))
	# cores = input("How many cores should be used? ")
	# path = input("Where is the data? ") or in this case data

	# For benchmarking starting the timer now
	start_time = time.time()

	# Firing up the engines!
	kmeansmk1(clusters, data)
	# kmeansmk1(clusters, cores, path)

	# Stopping benchmark
	seconds = time.time() - start_time
	print(str(seconds) + " seconds for execution")

# Simple generator for test data
def testgenerator():
	dataArray = []
	for i in range(1,100):
		if i <= 20:
			plz = generatePLZ("09")
		elif i > 20 and i < 50:
			plz = generatePLZ("08")
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

data = testgenerator()
startup(data)