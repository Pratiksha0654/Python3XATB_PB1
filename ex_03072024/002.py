# exmaple for possibilities of error

a= int(input("enter num1"))   #ValueError: invalid literal for int() with base 10: 'prati'
b= int(input("enter num2"))
c=a/b      #10/0   ZeroDivisionError: division by zero
print("Sum of two number is :", c)   # if gave space then intendation error


#now how to handle this errors:
#1. try # code......except Exception as e:

# try:
#     a = int(input("enter num1"))  # ValueError: invalid literal for int() with base 10: 'prati'
#     b = int(input("enter num2"))
#     c = a / b  # 10/0   ZeroDivisionError: division by zero
#     print("Sum of two number is :", c)
#
# except Exception as e:
#     print(e)



