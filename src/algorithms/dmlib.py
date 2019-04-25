# Imports for dmlib
import math


# Calculate the difference between two points giving the indexes of these xdata entries
def calcdiff(point1, point2):
    if int(point2) > int(point1):
        difference = int(point2) - int(point1)
    else:
        difference = int(point1) - int(point2)
    return difference


# Calculate the difference between two points in 2D space
def calcdiff2d(point1, point2):
    point1 = [int(i) for i in point1]
    point2 = [int(i) for i in point2]
    difference = math.sqrt(((point2[0]) - (point1[0])) ** 2 + ((point2[1]) - (point1[1])) ** 2)
    return abs(difference)
