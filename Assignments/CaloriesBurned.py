# Calories Burned
caloriesBurned = 0.0
CALORIESMINUTE = 4.2
minutes = 10

# Declare and initialize a variable
# for the calories burned per minute.


# Declare variables for the number of calories burned,
# and the number of minutes.


print ('Minutes\t\tCalories Burned')
print ('-------------------------------')

# Execute a loop to display calories burned.
while minutes <= 30:
    caloriesBurned = CALORIESMINUTE * minutes
    print (minutes, "\t\t", caloriesBurned)
    minutes += 5
