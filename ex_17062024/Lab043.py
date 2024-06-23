def f1(a, b, c):
    # return a+b+c
    print(a, b, c)
    return a * b * c  # we can pass only single retun


result = f1(10, 20, 30)
result1 = f1(b=90, a=1, c=3)  # any order u can give
print(result)
print(result1)
