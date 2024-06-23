# factorial
import math

n = 8
factorial = 1

# #method1
# for i in range(1, n + 1):
#     factorial = factorial * i
# print(factorial)
#
# # method 2
# factorial = math.factorial(5)
# print(factorial)

#method3
while n>0:
    factorial = factorial * n
    n = n-1
print(factorial)
