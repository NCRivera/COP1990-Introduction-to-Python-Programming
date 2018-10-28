infile = open('numbers.txt', 'r')

num1 = int(infile.readline())
num2 = int(infile.readline())
num3 = int(infile.readline())

infile.close()

total = num1 + num2 + num3

print('The numbers are:', num1, num2, num3)
print('Their total is:', total)

i = 1
for number in [num1, num2, num3]:
    print("Number", i, "is:", number)
    i += 1

#Professors Solution
infile = open('numbers.txt', 'r')
for line in range(3):
    print(infile.readline())
infile.close()