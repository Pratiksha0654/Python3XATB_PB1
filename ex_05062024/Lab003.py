# print()
# self - Concept in OOps which points to inself - ignore.
# *args - Unlimited number of arguments * - string, int, float, boolean..
# sep=' ' - How you want to seperate the arguments
# end='\n' - in the end what you want to do>used to chane the default line ending from newline(\n) to any other character
# file=None - File IO
# **********************************
# (sep=)

print("Hellow", "World", 123, 17.8, True, sep=",")  # Hellow-World-123-17.8-True
print("Hi, Welcome to Python class ","Pratiksha", sep="-")    #2 arguments
print("Hi, Welcome to Python class ")    #1 arguments ("")

# SyntaxError: positional argument follows keyword argument
# print(sep="-" "Hellow","world")
