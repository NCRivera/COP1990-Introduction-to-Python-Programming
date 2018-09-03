# Math calcs for a sphere
from math import pi
radius = float(input("What is the radius of your sphere? "))

diameter = 2 * radius
circumference = diameter * pi
surfaceArea = 4 * pi * radius * radius
volume = (4/3) * pi * radius * radius * radius

print("Diameter     :", diameter)
print("Circumference:", circumference)
print("Surface Area :", surfaceArea)
print("Volume       :", volume)
