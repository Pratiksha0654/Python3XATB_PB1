# Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than,
# or equal to the second number.

num1 = int(input("first number is :"))
num2 = int(input("second number is :"))

if (num1 > num2):
    print("num 1 is greater than num2")
else:
    print("num2 is greater than num1")

if (num1 == num2):
    print("num 1 is equals to num2")
else:
    print("num1 is not equals to num2")


# num1 = float(input("Enter the first number: "))
#
# num2 = float(input("Enter the second number: "))
#
# result = compare_numbers(num1, num2)
#
# print(result)