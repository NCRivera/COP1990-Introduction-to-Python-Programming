# Programming Exercises Shipping Charge

# Named constants
PACKAGEPRICE = 99

# Local variables
fullPrice = 0
amountPurchased = 0
discount = 0
discountTotal = 0
purchaseTotal = 0

# Get number
 #use the text in your code: 'Enter the number of packages purchased: :
amountPurchased = int(input("Enter the number of packages purchased: "))

# Calculate the discount rate
if amountPurchased >= 10 and amountPurchased <= 20:
    discount = 0.1
elif amountPurchased >= 20 and amountPurchased <= 49:
    discount = 0.2
elif amountPurchased >= 50 and amountPurchased <= 99:
    discount = 0.3
elif amountPurchased >= 100:
    discount = 0.4
else:
    discount = 0.0

# Calculate the full price
fullPrice = PACKAGEPRICE * amountPurchased

# Calculate the discount amount
discountTotal = fullPrice * discount

# Calculate the total amount
purchaseTotal = fullPrice - discountTotal

# Print results

#use this to display out put
#Discount Amount: $'and format discount amount to .2f
#Total Amount: $ and format total amount to .2f

print('Discount Amount: $ %0.2f' % discountTotal)
print('Total Amount: $ %0.2f' % purchaseTotal)
