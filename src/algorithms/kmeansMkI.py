#!/usr/bin/env python
#title:				kmeansMkI.py
#description:		Our personal Python K-Means++ implementation
#author:			Tillmann Brendel, Conrad Großer
#license:			Pending
#date:				26.05.2018
#version:			1.1
#usage:				python pyscript.py
#notes:
#known_issues:
#python_version:	3.x
#==============================================================================

# IMPORTS

# Importing the time for benchmarking purposes
import time
from datetime import date

# For random generation of numbers import randint
from random import randint

# Importing libary for multi core processing
import multiprocessing

# Importing libaries for easy plotting
import numpy as np
import matplotlib.pyplot as plt

# Importing own libaries Datamining Libary and Datamining Test
import dmlib
import dmtest

# CODE
# Main function of the algorithm
def kmeansmk1(data, clusters):
	# Defining cluster points
	for i in range(0, clusters):
		globals()["cpoint_" + str(i)] = data[randint(0, len(data))]
		print("Initial cluster " + str(i + 1) + ": " + str(globals()["cpoint_" + str(i)]))

	# Get max value in the data array
	highPoint = dmlib.findHighest(data)
	done = 0
	runs = 0
	while done == 0:
		runs = runs + 1
		new_data = assignCluster(data, highPoint, clusters)
		calcClusters(new_data, clusters)
		for cluster in range(0, clusters):

			#keeps the algorithm going until the central clusterpoint doesnt change anymore
			if globals()["cpointchanged_" + str(cluster)] == 1:
				done = 1

	# Printing final clusters

	for i in range(0, clusters):
		print("Endcluster " + str(i + 1) + " is calculated to be at  " + str(globals()["cpoint_" + str(i)]) + " after " + str(runs) + " runs")


	# plotting the random data and the found clusters
	anew = []
	inew = 0
	while inew < 1000:
		anew.append(inew)
		inew = inew + 1
	floatdata = [int(x) for x in data]
	for i in range(0, clusters):
		plt.axvline(x=int(globals()["cpoint_" + str(i)]), color='r')
	plt.scatter(floatdata, anew, marker='x', s=7, color='k')
	plt.show()
	return 0

# Calculates middle values for each cluster, takes 2D array (item, assigned_cluster)
def calcClusters(data, clusters):
	for cluster in range(0, clusters):
		globals()["cpointchanged_" + str(cluster)] = 0
		globals()["oldcpoint_" + str(cluster)] = globals()["cpoint_" + str(cluster)]
		clustersum = 0
		count = 0
		for item in range(0, len(data[0])):
			if data[1][item] == globals()["cpoint_" + str(cluster)]:
				clustersum = clustersum + int(data[0][item])
				count = count + 1
		globals()["cpoint_" + str(cluster)] = round(clustersum / count)

		#checking if old clusterpoint is equal to the one just calculated
		if globals()["oldcpoint_" + str(cluster)] == globals()["cpoint_" + str(cluster)]:
			globals()["cpointchanged_" + str(cluster)] = 1
	return 0

def assignCluster(data, highPoint, clusters):
	# Create a new data array for working
	new_data = []
	new_data.append(data)

	# Create new array for assigned clusters of each value
	data_assigned = []

	# For each item in data find the minimal difference to a cluster and write it in the new data array in the second place (new_data[item][cluster_index])
	for item in range(0, len(new_data[0])):
		# Set the minimal cluster difference to the highest difference in the list to ease comparision
		min_cluster = highPoint

		# Check the difference between the point (item) and each cluster and set min_cluster to the smallest difference 
		for cluster in range(0, clusters):
			if min_cluster > dmlib.calcdiff(data[item], globals()["cpoint_" + str(cluster)], new_data[0]):
				min_cluster = dmlib.calcdiff(data[item], globals()["cpoint_" + str(cluster)], new_data[0])
				assinged_cluster = globals()["cpoint_" + str(cluster)]
		# Assign the minimal difference cluster to the data
		data_assigned.append(assinged_cluster)
	# Add the assigned values list to the new_data array
	new_data.append(data_assigned)

	return new_data

# Startup function for collecting necesarry data
def startup(data):
	# Using two clusters for testing
	clusters = int(input("How many clusters are known? "))
	# cores = input("How many cores should be used? ")
	# path = input("Where is the data? ") or in this case data
	
	# For benchmarking starting the timer now
	start_time = time.time()

	# Firing up the engines!
	kmeansmk1(data, clusters)

	# Stopping benchmark
	seconds = time.time() - start_time
	print(str(seconds) + " seconds for execution")

# Start the algorithm and generate test data
data = dmtest.plzGen(1000)

startup(data)
