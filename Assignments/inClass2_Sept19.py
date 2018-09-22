# Prompt user to input how old they are in years.
age = int(input('How old are you (years only): '))
# User inputs integer.

# Display "Infant" if age is exactly 1 or less.
if age <= 1:
    print('You\'re an infant.')
# Display "Child" if less than 13 and older then 1.
elif age < 13 and age > 1:
    print('You\'re a child.')
# Display "Teenager" if less than 20 to exactly 13.
elif age < 20 and age >=13:
    print('You\'re a teenager.')
# Display "Adult" if greater than or equal to 20.
elif age >= 20:
    print('You\'re an adult.')
# Check if input is valid entry. Display error message if invalid.
else: # THIS IS USELESS BECAUSE IT CAN"T HAPPEN, BECAUSE INT AT LINE 2 WILL ERR.
    print('ERROR! That\'s not a valid input! Try again!')