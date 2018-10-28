def main():
    # local variables
    num1 = 0.0
    num2 = 0.0
    sum = 0.0

    # get num1
    num1 = float(input("Enter a number: "))

    # print number
    showNumber(num1)

    # get num2
    num2 = float(input("Enter a number: "))

    # print number
    showNumber(num2)

    sum = calculate_the_sum_show(num1, num2)

    print("The sum of the numbers", num1,"+",num2, "is", sum)

# showNumber function displays the number.
def showNumber(num1):
    print("The number is", num1)

def calculate_the_sum_show(number_1, number_2):
    sum_t = number_1 + number_2
    return sum_t

main()