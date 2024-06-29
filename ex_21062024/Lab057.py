# adding tuple1 ,tuple 2
#search in tuple   :in we can use for finding the item in tuple

t1 = ("a","b","c")
t2 = ("x","y","z")

new_tuple= (t1, t2)
print(new_tuple)      #(('a', 'b', 'c'), ('x', 'y', 'z'))

print(new_tuple[0])   #('a', 'b', 'c')
print(new_tuple[0][0])   #a
print(new_tuple[0][1])    #b
print(new_tuple[1])   #('x', 'y', 'z')

#tuple are immutable , we cannot append t2 in t1 instaed we can go for +

new_tuple1= (t1 + t2)

print(new_tuple1)       #('a', 'b', 'c', 'x', 'y', 'z')
print('a' in new_tuple1)   #true
print('z' in new_tuple1)    #True
print('k' in new_tuple1)    #False

#Unpacking of the tuple
a,b,c =(10,20,30)
# so Unpacking or tuple assignment is the process
# that assigns the values on the right-hand side to the left-hand side variables.
