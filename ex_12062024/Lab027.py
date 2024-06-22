#Multiple conditions

a=10
b=90
c=34
d=76

r1 = (a>b)   #false
r2 = (c<d)   #True
r3 = r1 and r2   #False and True
print(r3)    #False

r3 = r1 or r2   #False or True
print(r3)    #True