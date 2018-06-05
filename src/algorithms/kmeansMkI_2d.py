#!/usr/bin/env python
# title:				kmeansMkI.py
# description:		Our personal Python K-Means++ implementation
# author:			Tillmann Brendel, Conrad Großer
# license:			Pending
# date:				04.06.2018
# version:			1.5
# usage:				python pyscript.py
# notes:
# known_issues:
# python_version:	3.x
# ==============================================================================

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
def kmeansmk1(xdata, ydata, clusters):
    # Defining cluster points
    for i in range(0, clusters):
        globals()["cpoint_" + str(i)] = [xdata[randint(0, len(xdata))], ydata[randint(0, len(ydata))]]
        print("Initial cluster " + str(i + 1) + ": " + str(globals()["cpoint_" + str(i)]))
    #get max data in the data arrays
    highpointx = dmlib.findHighest(xdata)
    highpointy = dmlib.findHighest(ydata)
    #print('highpoinx: ' + str(highpointx))
    #print('highpointy: ' + str(highpointy))

    # Define variables for running the algorithm (runs is just as important as every other variable)
    done = 0
    runs = 0

    # As long as calcClusters returns done it will rearrange the clusters and assign the data to the clusters
    while done == 0:
        runs = runs + 1
        assigned_points = assignCluster(xdata, ydata, clusters, highpointx, highpointy)
        #assigned_points consists of the clusternumbers
        done = calcClusters(xdata, ydata, assigned_points, clusters)

    for i in range(0, clusters):
        print("Endcluster " + str(i + 1) + " is calculated to be at  " + str(globals()["cpoint_" + str(i)]) + " after " + str(runs) + " runs")
    for i in range(0, clusters):
        plt.plot(globals()["cpoint_" + str(i)][0], globals()["cpoint_" + str(i)][1], 'ro')
    plt.scatter([int(x) for x in xdata], [int(y) for y in ydata], marker='x', s=7, color='k')
    plt.show()

# Calculates middle values for each cluster, takes 2D array (item, assigned_cluster)
def calcClusters(xdata, ydata, assigned_points, clusters):
    for cluster in range(0, clusters):
        cpointunchanged = 1
        globals()["oldcpoint_" + str(cluster)] = globals()["cpoint_" + str(cluster)]
        clustersumx = 0
        clustersumy = 0
        count = 0
        #print('calcclusters running')
        for item in range(0, len(xdata)):
            if assigned_points[item] == cluster:
                clustersumx = clustersumx + int(xdata[item])
                clustersumy = clustersumy + int(ydata[item])
                count = count + 1
           # print('item ' + str(item) +'done')
        globals()["cpoint_" + str(cluster)] = [round(clustersumx / count), round(clustersumy / count)]
        #print('cluster ' + str(cluster) + 'done')
        # checking if old clusterpoint is equal to the one just calculated
        if globals()["oldcpoint_" + str(cluster)] != globals()["cpoint_" + str(cluster)]:
            cpointunchanged = 0

    return cpointunchanged

def assignCluster(xdata, ydata, clusters, highpointx, highpointy):
    data_assigned = []
    assigned_cluster = 0
    resetdist = dmlib.calcdiff2d([0,0],[highpointx, highpointy])
    #print('resetdist =' + str(resetdist))
    for item in range(0, len(xdata)):
        olddistance = resetdist
        for cluster in range(0, clusters):
            distance = dmlib.calcdiff2d(globals()["cpoint_" + str(cluster)], [xdata[item], ydata[item]])
           # print('distance from point ' + str(item) + ' to cluster ' + str(cluster) + ': ' + str(distance))
            if distance < olddistance:
                olddistance = distance
                assigned_cluster = cluster
       # print('cluster number ' + str(cluster) + ' assigned')
        data_assigned.append(assigned_cluster)
    # Add the assigned values list to the new_data array
    # new_data.append(data_assigned)
    return data_assigned

# Startup function for collecting necesarry xdata
def startup(xdata, ydata):
    # Using two clusters for testing
    clusters = int(input("How many clusters are known? "))
    # cores = input("How many cores should be used? ")
    # path = input("Where is the xdata? ") or in this case xdata

    # For benchmarking starting the timer now
    start_time = time.time()

    # Firing up the engines!
    kmeansmk1(xdata, ydata, clusters)

    # Stopping benchmark
    seconds = time.time() - start_time
    print(str(seconds) + " seconds for execution")

# Start the algorithm and generate test xdata
xdata = dmtest.numGenLight(10000, False, 5)
ydata = dmtest.numGenLight(10000, False, 2)

startup(xdata, ydata)
