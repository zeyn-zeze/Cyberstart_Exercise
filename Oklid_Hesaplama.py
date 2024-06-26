import math


points = [(0, 0), (5,7),(3,8),(9,3),(2,6)]

def euclideanDistance(x, y):
    return math.sqrt((y[0] - x[0]) ** 2 + (y[1] - x[1]) ** 2)

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)


print("Noktalar arasındaki mesafeler: ", distances)
print("\n")
print("Minimum mesafe:", min_distance)
