# Strings  >bunch of charachaters
# presentation can be used in 3 ways>>> '', "", """...."""

name1 = "Harry"
print(name1)
name2 = 'Potter'
print(name2)
name3 = """harry potter .This is one of my fav"""
print(name3)

# Raw String
dir = r'C:\nomedir\some dir'
print(dir)  # C:\nomedir\some dir

# Format of the String
first_name = "Harry"
last_name = "Potter"
print(first_name + " " + last_name)
print(first_name, last_name)
# f -> formatting - it will replace the values of the variables
# {} -> placeholders
print(f'Your Full name is {first_name} {last_name}')  # Your Full name is Harry Potter

#example of formating>can be used in multple operations
name="pratiksha"
num=10
print(f'{num}*1={num}')# the value of num is 10
print(f'{num}*2={num*2}')# the value of num is 10
print(f'{num/2}')# the value of num is 10
