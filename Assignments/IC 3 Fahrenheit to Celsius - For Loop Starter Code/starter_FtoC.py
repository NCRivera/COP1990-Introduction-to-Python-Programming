# Fahrenheit to Celsius

# Declare a variable to hold the temperature
# in degrees Fahrenheit.
fahrenheit = 0.0

# Calculate and print value for each temperature.
print ('Celsius\t\tFahrenheit')
print ('------------------------------------------')

'use a for loop'
for celsiusDegree in range(21):
    fahrenheit = ((9 / 5) * celsiusDegree) + 32
    print (celsiusDegree, '\t\t', format(fahrenheit, '.1f') )