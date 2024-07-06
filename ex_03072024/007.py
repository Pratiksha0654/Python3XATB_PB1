# try , except  ,else and finally

try:
    a= int(input("enter num1"))
    b= int(input("enter num2"))
    c=a/b
    print("number c is",c)

except Exception as ve:
    print(ve)

except Exception as zde:
    print(zde)

else:
    print(f' Result is {c}')    # this will execute when there is no error exception , if there is excepation then execpt code will execute

finally:
    print("end of program")   # always execute
    
