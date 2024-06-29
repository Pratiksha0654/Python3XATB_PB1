def my_decorator(funct):

    def abc():
        print("starting")
        funct()    #decorator
        print("ending")

    return abc()

@my_decorator
def pratiksha():
    print("hello, Pratiksha here as a decorator")

