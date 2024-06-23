# Functions
# Block of Code - Which can executed or reused.
# Define
# Call

# They can return something
# The can't return -> non return
# They have parameters
# They don't parameters / arguments
# They can have return something / value
# They can't have return -> void

# def say_hello():       #no argument/no parameter/ no retun type
#     print("Hello")
# say_hello()
#
#
# def say_hello(name):       #argument/parameter/ no retun type
#     print("Hello", name)
# say_hello("addy")
# say_hello("sunny")

# def say_hello_default_arg(name="Pratiksha"):   #argument/parameter/ with default argument
#           print("Hello", name)
#
# say_hello_default_arg()    #no arg passed here, it will take default value
# say_hello_default_arg("Akash")    #arg passed here or
# say_hello_default_arg(name="Sunny")    #arg passed here

def addition_arg_with_return(a, b):
    return a + b


result = addition_arg_with_return(4, 5)
# result = addition_arg_with_return(a=67, b=56)
# result = addition_arg_with_return(a:40, b:58)
print(result)
