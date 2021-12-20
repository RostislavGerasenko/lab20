import math
import itertools

def perimiter(point1, point2, point3):
    return math.sqrt((point1[0] - point2[0])**2+(point1[1] - point2[1])**2) +\
           math.sqrt((point1[0] - point3[0])**2+(point1[1] - point3[1])**2) +\
           math.sqrt((point3[0] - point2[0])**2+(point3[1] - point2[1])**2)

n = int(input("Number of points: "))
all_points = [(int(input(f"Enter the x coordinate of point number {i+1}: ")),
           int(input(f"Enter the y coordinate of point number {i+1}: ")))
          for i in range(n)]
max_points = None
max_perimeter = 0
for points in itertools.combinations(all_points, 3):
    if perimiter(*points) > max_perimeter:
        max_perimeter = perimiter(*points)
        max_points = points
max_points = ", ".join(str(point) for point in max_points)
print(f"The triangle with the beggest perimeter ({max_perimeter}) is fromed with the points: {max_points}")
