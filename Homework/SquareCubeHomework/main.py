"""
Program: cube.py
Project 2.2

Compute the surface area of a cube.

The input is the cube's edge. 
The output is the surface area of the cube.
"""
# Nicholas Rivera
# September 19, 2018

# Request the input. Here I am requesting the input from the user (edge).
# It must be converted to integer.
edge = int(input("Enter the cube's edge: "))

# Compute the surface area. I compute this by combining the formula '6a**2',
# where 'a' will be replaced by the variable 'edge' to create a new variable 'surfaceArea'
surfaceArea = 6 * (edge ** 2)

# Display the surface area. The variable 'surfaceArea' that was computed with the 'edge'  will now be displayed
# to show the calculation made.
print("The surface area is", surfaceArea, "square units.")
