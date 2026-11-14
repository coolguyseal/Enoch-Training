import math


try:
    radius = float(input("Enter the radius of the circle: "))
    if radius < 0:
        raise ValueError("radius cannot be negative")
except ValueError as error:
    print(f"Invalid radius: {error}")
else:
    area = math.pi * radius**2
    print(f"Area of the circle: {area}")