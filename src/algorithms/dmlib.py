# Calculate the difference between two points giving the indexes of these xdata entries
import math
def calcdiff(point1, point2, data):
    if int(point2) > int(point1):
        difference = int(point2) - int(point1)
    else:
        difference = int(point1) - int(point2)
    # print("Datapoint: " + str(xdata[point1]) + " | Cluster: " + str(xdata[point2]) + " | Difference: " + str(difference))
    return betrag(difference)

def calcdiff2d(point1, point2):
    point1 = [int(i) for i in point1]
    point2 = [int(i) for i in point2]
    difference = math.sqrt(((point2[0])-(point1[0]))**2+((point2[0])-(point1[0]))**2)
    return betrag(difference)


# Get the absolute value of a number and returns it as int
def betrag(number):
    if number < 0:
        number = int((-2 * number) / 2)
    return number


# Determine the highest int value in an array and returns is as an int
def findHighest(data):
    maximum = 0
    for i in range(0, len(data)):
        if int(data[i]) > maximum:
            maximum = int(data[i])
    return maximum

def pp_calcdiff(data, clusterpoint):
	max_diff = 0
	new_cluster = 0
	for item in range(0,len(data)):
		if calcdiff(data[item], clusterpoint) > max_diff:
			max_diff = calcdiff(data[item], clusterpoint)
			new_cluster = data[item]
	return new_cluster

def pp_calcdiff_2(data, clusterpoint, clusterpoint_2):
	max_diff = 0
	new_cluster = 0
	for item in range(0,len(data)):
		if calcdiff(data[item], clusterpoint) + calcdiff(data[item], clusterpoint_2) > max_diff:
			max_diff = calcdiff(data[item], clusterpoint)
			new_cluster = data[item]
	return new_cluster
