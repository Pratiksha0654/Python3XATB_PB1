# Program to find between max numbers
# a=10
# b=78
# c=89
#
# print(max(a,b,c))
# print(min(a, b, c))

# by if elif and else condition

a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))

if a > b and a > c:
    print("a is greater")
elif b > a and b > c:
    print("b is greater")
else:
    print("c is greater")

#ternary opertotrs are only used for if else

