# Real time example for decorators
# in running program > capture the time taken by calling decorators
import time


def my_decorator(funct):
    def abc():
        start_time = time.time()
        funct()
        end_time = time.time()
        print("Time Taken - " + str(end_time - start_time))

    return abc()


@my_decorator
def xyz():
    time. sleep(5)
    print("record the time taken")

@my_decorator   #one decorator can be used with multiple functions
def xyz2():
    time.sleep(2)
    print("record the reporting time")

@my_decorator
def xyz3():
    time. sleep(6)
    print("record the time taken")

