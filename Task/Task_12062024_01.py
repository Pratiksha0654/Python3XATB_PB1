# Leap Year program

year = int(input("Enter the year: "))
if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
    print("This is leap year")
else:
    print("This is not a leap year")
