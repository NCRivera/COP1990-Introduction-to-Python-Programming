# Calculate houraly wage along with overtime pay, if applicable.
wage = float(input("Enter the wage: "))
hours = int(input("Enter the regular hours: "))
overtimeHours = int(input("Enter the overtime hours: "))

OVERTIME_PAY = (wage * 1.5) * overtimeHours
PAY = wage * hours + OVERTIME_PAY

print("The total weekly pay is", "$" + str(PAY))
