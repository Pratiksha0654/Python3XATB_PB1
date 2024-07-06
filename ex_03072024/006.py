# try , except  and finally

try:
    a= int(input("enter num1"))
    b= int(input("enter num2"))
    c=a/b
    print("number c is",c)

except Exception as ve:
    print(ve)

except Exception as zde:
    print(zde)

finally:
    print("end of program")
