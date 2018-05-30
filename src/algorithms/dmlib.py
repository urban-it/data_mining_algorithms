# Calculate the difference between two points giving the indexes of these data entries
def calcdiff(point1, point2, data):
	if int(point2) > int(point1):
		difference = int(point2) - int(point1)
	else:
		difference = int(point1) - int(point2)
	# print("Datapoint: " + str(data[point1]) + " | Cluster: " + str(data[point2]) + " | Difference: " + str(difference))
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