n = int(input("Number of points: "))
farthest = (0,0)
for i in range(n):
    x = int(input(f"Enter the x coordinate of point number {i+1}: "))
    y = int(input(f"Enter the y coordinate of point number {i+1}: "))
    if not x > 0 or y < 0:
        continue
    distance = farthest[0]**2 + farthest[1]**2
    if x**2 + y**2 > distance:
        farthest = (x,y)
print(f"The point in the second quadrant that is the farthest from origin is ({x}, {y})")
