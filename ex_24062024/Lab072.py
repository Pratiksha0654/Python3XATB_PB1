# Recursion
# Recursion is programming technique where a function call
# itself in order to solve a problem

#Key concept
#Base case
#Recusive case

#Factorial

def factorial(n):
    if n==0 or n==1:
        return 1

    else:
        return n* factorial(n-1)

print(factorial(5))    #120

