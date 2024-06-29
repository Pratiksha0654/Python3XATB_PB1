#double the element in the list

# my_list = [1, 2, 3, 4, 5]

#Method1
# temp_list = []
# for i in my_list:
#     temp_list.append(i*2)
#
# print(temp_list)

#Method2
# new_list = [i*2 for i in my_list]
# print(new_list)

#Method3

# map()
#1. Takes ech item from list
# 2. execute the function on each item
# 3. return the result of each item

# def double(x):
#     return x*2
# new_list = list(map(double, my_list))    #map()
# print(new_list)

#Method 4 by labda

# lambda x: x*2
# new_list = list(map(lambda x: x*2, my_list))
# print(new_list)

#in single line
print(list(map(lambda x: x*2, [1, 2, 3, 4, 5])))