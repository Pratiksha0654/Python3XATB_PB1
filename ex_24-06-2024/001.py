#Recursion
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
#     num = 5
#     print(f"The factorial of {num} is {factorial(num)}")
#

def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        sum_digits = sum_digits + n % 10
        n = n // 10  # Quotient
        # /  - div
        # // Quotient
        # % - Reminder
    return sum_digits
print(sum_of_digits(12345))