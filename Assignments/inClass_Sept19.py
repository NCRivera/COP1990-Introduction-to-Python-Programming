# Prompt user to input a number. Must be a number between 1 and 7.
number = int(input('Give me a number between 1 and 7 and I\'ll give you the day of the week: '))
# User inputs number in range.
# Check if input is valid. If invalid input (outside range), display error message. I DONT KNOW HOW TO DO THIS. USE ELSE?

# If user input integer 1 then display 'Monday'
if number == 1:
    print('Monday')
# If user input integer 2 then display 'Tuesday'.
elif number == 2:
    print('Tuesday')
# If user input integer 3 then display 'Wednesday'.
elif number == 3:
    print('Wednesday')
# If user input integer 4 then display 'Thursday'.
elif number == 4:
    print('Thursday')
# If user input integer 5 then display 'Friday'.
elif number == 5:
    print('Friday')
# If user input integer 6 then display 'Saturday'.
elif number == 6:
    print('Saturday')
# If user input integer 7 then display 'Sunday'.
elif number == 7:
    print('Sunday')
else: # THIS IS USELESS BECAUSE IT CAN"T HAPPEN, BECAUSE INT AT LINE 2 WILL ERR.
    print('ERROR! That\'s not a valid input! Try again!')