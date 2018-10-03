# Request a number input from the user.
numberEntered = 0

# If number is positive, add to sum variable.
numberSum = 0

# if number is negative, terminate program

while numberEntered >= 0:
    numberSum += numberEntered
    numberEntered = int(input('Enter a number to be added: '))

message = "The sum of all the numbers entered is:\t"
print(message, numberSum)