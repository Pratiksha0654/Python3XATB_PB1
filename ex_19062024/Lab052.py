my_list = [1, 2, 3, 4, 5]

my_list.append(12)
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(2)
print(my_list)

my_list.insert(1, 12)
print(my_list)

my_list.remove(12)
print(my_list)

my_list.reverse()
print(my_list)

my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)

my_list.clear()
print(my_list)

#
# [1, 2, 3, 4, 5, 12]
# [1, 2, 3, 4, 5]
# [1, 2, 4, 5]
# [1, 12, 2, 4, 5]
# [1, 2, 4, 5]
# [5, 4, 2, 1]
# [1, 2, 4, 5]
# [5, 4, 2, 1]
# []

# squared_list = list(map(lambda x: x**2, my_list))
# print(squared_list)

