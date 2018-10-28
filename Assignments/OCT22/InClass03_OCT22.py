# Ask the user for a distance.

# distance = float(input("What is the kilometer distance to convert: "))

# Convert the distance.

# miles = distance * 0.6214

# Display the conversion
# print("The conversion is", distance, "kilometers", "equals", miles, "miles.")

KILOMETERS_TO_MILES = 06.214

def main():

    Y = get_kilometers()
    X = kilo_to_miles(Y)

    print(X)
    from IncClass02 import showNumber as SN
    SN(X)

def kilo_to_miles(kilometers):
    miles = kilometers * KILOMETERS_TO_MILES
    return miles

def get_kilometers():
    kilometers = float(input("What is the distance in kilometers: "))
    return kilometers

main()

import showNumber as SN
