# Break: based on condition,it will kick u out of the loop loop
# continue: based on condition,it will skip that iteration
# pass: do nothing/skip
#
for i in range (10):   #if npot mentioned initials then it will consider from 0
    print(i)

for i in range(1, 10):
    if i==5:
        pass
    else:
        print(i)  #1,2,3,4,6,7,8,9

for i in range(1, 10):
    if i==5 or i==3:
        break
    print(i)      #1,2,3,4