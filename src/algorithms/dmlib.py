# Calculate the difference between two points giving the indexes of these data entries
def calcdiff(point1, point2):
    if int(point2) > int(point1):
        difference = int(point2) - int(point1)
    else:
        difference = int(point1) - int(point2)
    return abs(difference)


def pp_calcdiff(data, clusterpoint):
    max_diff = 0
    new_cluster = 0
    for item in range(0, len(data)):
        if calcdiff(data[item], clusterpoint) > max_diff:
            max_diff = calcdiff(data[item], clusterpoint)
            new_cluster = data[item]
    return new_cluster


def pp_calcdiff_2(data, clusterpoint, clusterpoint_2):
    max_diff = 0
    new_cluster = 0
    for item in range(0, len(data)):
        if calcdiff(data[item], clusterpoint) + calcdiff(data[item], clusterpoint_2) > max_diff:
            max_diff = calcdiff(data[item], clusterpoint)
            new_cluster = data[item]
    return new_cluster
