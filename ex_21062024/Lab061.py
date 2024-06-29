#Decorators

# Definition: A decorator is a callable (usually a function) that takes another function as input and returns a modified version of that function.
# Syntax: Decorators use the "@" symbol followed by the decorator name, placed on the line immediately before the function or class definition.


def my_decorator(func):

    def abc():
        print("starting")
        print("*****************")
        func()             #decorator
        print("ending")
        print("*****************")

    return abc()


@my_decorator
def call_decorator_func():
    print("hello ,I am decorator function")



