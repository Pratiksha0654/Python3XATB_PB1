#args>  any number of arguments
def sum_three(a=1, b=2,c=3):
    return a+b+c

result1 = sum_three(10, 20, 30)   #60
result2 = sum_three(a=10, b=80, c=30)      #120
result3 = sum_three()   #take def values    #6
result5 = sum_three(10)   #take 2 def values    #50
result4 = sum_three(18, 29)   #take 1 def values   #15

print(result1,result2, result3, result4, result5)


