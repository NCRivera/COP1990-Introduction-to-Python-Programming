# FIXME (1): Prompt for four weights. Add all weights to a list. Output list.
weights = []
people = 4
for person in range(people):
    score = float(input("Enter weight %d:\n" % (person + 1)))
    weights.append(score)

print('Weights:', weights)

# FIXME (2): Output average of weights.
averageWeight = sum(weights)/people
print('\nAverage weight: %0.2f' % averageWeight)

# FIXME (3): Output max weight from list.
maxWeight = max(weights)
print('Max weight: %0.2f\n' % maxWeight)

# FIXME (4): Prompt the user for a list index and output that weight in pounds and kilograms.
index = int(input('Enter a list index (1 - 4):\n'))

print("Weight in pounds: %0.2f" % weights[index - 1])
print('Weight in kilograms: %0.2f\n' % ((weights[index - 1])/2.2))

# FIXME (5): Sort the list and output it.
weights.sort()
print('Sorted list:', weights)
