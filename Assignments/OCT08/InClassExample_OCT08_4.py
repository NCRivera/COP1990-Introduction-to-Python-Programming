data = input('Enter a number between 0 - 100: ') # If negative number, will not work, strip negative sign.

message = "\nisnumeric: You entered"

print(message, data)

print(data.isnumeric())

if data.isnumeric():
    print("Yes, Numeric")
    numericInput = True
    print(numericInput)
else:
    print("Not Numeric")
    numericInput = False
    print(numericInput)
