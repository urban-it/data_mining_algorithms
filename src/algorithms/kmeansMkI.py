#!/usr/bin/env python
#title:				kmeansMkI.py
#description:		Our personal Python K-Means++ implementation
#author:			Tillmann Brendel, Conrad Großer
#date:				26.05.2018
#version:			0.2
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
	# Using two clusters for testing
	clusters = 2

	# Create a new data array for working
	new_data = []
	new_data.append(data)

	# Get the size of the data array
	data_size = len(new_data[0])

	# Defining cluster points
	for i in range(0, clusters):
		globals()["cpoint_" + str(i)] = randint(0, data_size)
		print("Cluster " + str(i) + ": " + str(new_data[0][globals()["cpoint_" + str(i)]]))

	# Create new array for assigned clusters of each value
	data_assigned = []

	# Get max value in the data array
	highPoint = findHighest(new_data[0])

	# For each item in data find the minimal difference to a cluster and write it in the new data array in the second place (new_data[item][cluster_index])
	for item in range(0, data_size):
		# Set the minimal cluster difference to the highest difference in the list to ease comparision
		min_cluster = highPoint

		# Check the difference between the point (item) and each cluster and set min_cluster to the smallest difference 
		for cluster in range(0, clusters):
			clusternumber = globals()["cpoint_" + str(cluster)]
			if min_cluster > calcdiff(item, clusternumber, new_data[0]):
				min_cluster = calcdiff(item, clusternumber, new_data[0])
				assinged_cluster = clusternumber
		# Assign the minimal difference cluster to the data
		data_assigned.append(assinged_cluster)
	# Add the assigned values list to the new_data array
	new_data.append(data_assigned)

	# Print out the list of datapoints and assigned clusters
	for item in range(0, len(new_data[0])):
		print("Datapoint: " + str(new_data[0][item]) + " | Assigned cluster: " + str(new_data[0][new_data[1][item]]))

	return new_data

# Determine the highest int value in an array
def findHighest(data):
	maximum = 0
	for i in range(0, len(data)):
		if int(data[i]) > maximum:
			maximum = int(data[i])
	return maximum

# Calculate the difference between two points giving the indexes of these data entries
def calcdiff(point1, point2, data):
	if int(data[point2]) > int(data[point1]):
		difference = int(data[point2]) - int(data[point1])
	else:
		difference = int(data[point1]) - int(data[point2])
	# print("Datapoint: " + str(data[point1]) + " | Cluster: " + str(data[point2]) + " | Difference: " + str(difference))
	return betrag(difference)

# Get the absolute value of a number
def betrag(number):
	if number < 0:
		number = int((-2 * number) / 2)
	return number

# Startup function for collecting necesarry data
def startup(data):
	# clusters = int(input("How many clusters are known? "))
	# cores = input("How many cores should be used? ")
	# path = input("Where is the data? ") or in this case data

	# For benchmarking starting the timer now
	start_time = time.time()

	# Firing up the engines!
	kmeansmk1(data)
	# kmeansmk1(clusters, cores, data)

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

# Start the algorithm and generate test data
data = testgenerator()
startup(data)