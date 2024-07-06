try:
    a = int(input("enter num1"))  # ValueError: invalid literal for int() with base 10: 'prati'
    b = int(input("enter num2"))
    c = a / b  # 10/0   ZeroDivisionError: division by zero
    print("C number is :", c)

except Exception as e:
    print(e)    #for 10/0 #division by zero
                #invalid literal for int() with base 10: 'proh'

    print("Please enter integer")   # we can mention user frindly msg



