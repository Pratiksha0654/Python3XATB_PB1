# #Multiple for loop condition
# #match

Username= "Pratiksha"
password= "pass123"

match Username:
    case "pratiksha":
        print("Username matched succesfully")
    case _:
        print("Incorrect username")
match password:
    case "pass123":
        print("password matched succesfully")
    case _:
        print("Incorrect password")


# browser = "firefox"
# # 3.10
# match browser:
#     case "chrome":
#         print("execute the code of the chrome browser")
#     case "firefox":
#         print("execute the code of the firefox browser")
#     case _:
#         print("No idea")
