data = input('Enter a number between 0 and 100: ')

print("isdigit: You entered:", data)

if data.lstrip('-').isdigit():
    print('Yes, Digit.')
    digitInput = True
    print(digitInput)
else:
    print('Not a digit.')
    digitInput = False
    print(digitInput)

if int(data) >= 0 and int(data) <= 100:
    print('In range!')
else:
    print('Out of range!')