# *arg example>>>This function takes an arbitrary number of arguments
# and prints them out.

def print_args(*args):
    for i in args:
        print(i, end="\n")
    


print_args(1, 2.89, True, "pratiksha",-5)