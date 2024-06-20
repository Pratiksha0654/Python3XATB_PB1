# Program to find max/min number

#max() function returns the largest item in an iterable.
# It can also be used to find the largest item between 2 or more parameters.

print(max(10, 20, 78, 90, 56, 9))
print(max(10, 20, 78, 99.99, 56, 9, 45.89, 34.90, 67.08))

#min()
print(min(10, 20, 78, 90, 56, 9, 0, -89, -56, -23478))

# TypeError: '>' not supported between instances of 'str' and 'int'
# print(max(10, 20, 78, 90, 56, 9,"Hi"))
