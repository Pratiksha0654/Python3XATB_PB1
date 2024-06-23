# program to match username and password using match

username = input("Enter username: ")
password = input("Enter password: ")

match username, password:
    case "admin", "pass@123":
        print("Login successfull")
    case _:
        print("Login failed")
