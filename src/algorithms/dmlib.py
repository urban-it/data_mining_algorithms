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
