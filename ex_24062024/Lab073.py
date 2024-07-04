#hacker ring progra
# m:leetcode>>>sun of digits

number = 12345
#sum of digit?

r1=number //10  #1234
q1=number %10   #5
print(r1, q1)

r2=r1 //10   #123
q2=r1 %10   #4
print(r2, q2)

r3=r2 //10
q3=r2 %10
print(r3, q3)

r4=r3 //10
q4=r3 %10
print(r4, q4)

r5=r4 //10
q5=r4 %10
print(r5, q5)


sum = q1+q2+q3+q4+q5
print("sum of digits: ", sum)   #15


#by recursion method

def sum_of_digit (n):
    #base case
    if n<10:
        return n
    else:
        return n%10 + sum_of_digit(n//10)

print(sum_of_digit(12345))   #15

#method3>>>>by while
def sum_of_digit(n):
    sum = 0
    while n>0:
        sum = sum+ n%10
        n= n//10

    return sum

print(sum_of_digit(12345))   #15


# / >div
# //> quotient
# % >>> reminder







