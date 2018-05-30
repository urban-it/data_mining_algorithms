#!/usr/bin/env python
#title:				kmeansMkI.py
#description:		Our personal Python K-Means++ implementation
#author:			Tillmann Brendel, Conrad Großer
#license:			Pending
#date:				26.05.2018
#version:			1.0
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

# Importing own libaries Datamining Libary and Datamining Test
import dmlib
import dmtest

# CODE
# Main function of the algorithm
def kmeansmk1(data, clusters, runs):
	# Defining cluster points
	for i in range(0, clusters):
		globals()["cpoint_" + str(i)] = data[randint(0, len(data))]
		print("Initial cluster " + str(i + 1) + ": " + str(globals()["cpoint_" + str(i)]))

	# Get max value in the data array
	highPoint = dmlib.findHighest(data)

	for run in range(0, runs):
		new_data = assignCluster(data, highPoint, clusters)
		calcClusters(new_data, clusters)

	return 0

# Calculates middle values for each cluster, takes 2D array (item, assigned_cluster)
def calcClusters(data, clusters):
	for cluster in range(0, clusters):
		clustersum = 0
		count = 0
		for item in range(0, len(data[0])):
			if data[1][item] == globals()["cpoint_" + str(cluster)]:
				clustersum = clustersum + int(data[0][item])
				count = count + 1
		globals()["cpoint_" + str(cluster)] = round(clustersum / count)
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

	# runs = int(input("How many runs are sufficient? "))
	runs = 500
	
	# For benchmarking starting the timer now
	start_time = time.time()

	# Firing up the engines!
	kmeansmk1(data, clusters, runs)

	# Stopping benchmark
	seconds = time.time() - start_time
	print(str(seconds) + " seconds for execution")

	# Printing final clusters
	for i in range(0, clusters):
		print("Cluster " + str(i + 1) + " found at " + str(globals()["cpoint_" + str(i)]))


# Start the algorithm and generate test data
data = dmtest.plzGen(1000)

startup(data)
