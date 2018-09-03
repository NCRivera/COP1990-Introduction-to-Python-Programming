# Movie fees
ROMANCE_MOVIES = 6.00
COMEDY_MOVIES= 4.00

romance = int(input("Enter the number of romance movies: "))
comedy = int(input("Enter the number of comedies: "))

totalCost = (ROMANCE_MOVIES * romance) + (COMEDY_MOVIES * comedy)

print("The total cost is", "$" + str(totalCost))
