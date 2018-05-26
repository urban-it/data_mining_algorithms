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
def kmeansmk1(data):
	clusters = 2
	data_size = len(data)

	# Defining cluster points
	for i in range(0, clusters):
		globals()["cpoint_" + str(i)] = randint(0, data_size)
		print("Cluster " + str(i) + ": " + str(data[globals()["cpoint_" + str(i)]]))

	data_assigned = []
	highPoint = findHighest(data)

	for item in range(0, data_size):
		min_cluster = highPoint
		for cluster in range(0, clusters):
			clusternumber = globals()["cpoint_" + str(cluster)]
			if min_cluster > calcdiff(item, clusternumber, data):
				min_cluster = calcdiff(item, clusternumber, data)
				assinged_cluster = clusternumber
		data_assigned.append(assinged_cluster)

	# for item in range(0, data_size):
	# 	print("Datapoint: " + str(data[item]) + " | Assigned cluster: " + str(data[data_assigned[item]]))

def findHighest(data):
	maximum = 0
	for i in range(0, len(data)):
		if int(data[i]) > maximum:
			maximum = int(data[i])
	return maximum

def calcdiff(point1, point2, data):
	if int(data[point2]) > int(data[point1]):
		difference = int(data[point2]) - int(data[point1])
	else:
		difference = int(data[point1]) - int(data[point2])
	# print("Datapoint: " + str(data[point1]) + " | Cluster: " + str(data[point2]) + " | Difference: " + str(difference))
	return betrag(difference)

def betrag(zahl):
	if zahl < 0:
		zahl = int((-2 * zahl) / 2)
	return zahl

# Startup function for collecting necesarry data
def startup(data):
	# clusters = int(input("How many clusters are known? "))
	# cores = input("How many cores should be used? ")
	# path = input("Where is the data? ") or in this case data

	# For benchmarking starting the timer now
	start_time = time.time()

	# Firing up the engines!
	kmeansmk1(data)
	# kmeansmk1(clusters, cores, path)

	# Stopping benchmark
	seconds = time.time() - start_time
	# print(str(seconds) + " seconds for execution")

# Simple generator for test data
def testgenerator():
	dataArray = []
	for i in range(0,100):
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