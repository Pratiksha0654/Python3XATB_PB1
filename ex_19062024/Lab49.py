# sum of two numbers by lamda expression

#Syntax>>>(lamda arg1 : return) (value)

def sum(a,b):
    return a+b

result= sum(10,20)
print(result)           #30


#method 1 by lambda
result1 = (lambda a, b: a+b)(10, 20)
print(result1)                 #30

#method 2 by lambda
result2 = lambda a, b: a+b
print(result2(10, 20))              #30