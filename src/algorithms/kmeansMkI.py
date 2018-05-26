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

# Importing libary for multi core processing
import multiprocessing

# CODE
# Main function of the algorithm
def kmeansmk1(clusters):
	print("Sorting data into " + str(clusters) + " clusters.")

# Startup function for collecting necesarry data
def startup():
	clusters = int(input("How many clusters are known? "))
	# cores = input("How many cores should be used? ")
	# path = input("Where is the data? ")

	# For benchmarking starting the timer now
	start_time = time.time()

	# Firing up the engines!
	kmeansmk1(clusters)
	# kmeansmk1(clusters, cores, path)

	# Stopping benchmark
	seconds = time.time() - start_time
	print(str(seconds) + " seconds for execution")

startup()