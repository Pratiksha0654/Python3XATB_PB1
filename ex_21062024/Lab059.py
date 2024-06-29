#coversion of list to set

my_list = ["a", "b","c",12, 34.90, True]


my_set = set(my_list)
print(my_set)    # {True, 34.9, 12, 'b', 'a', 'c'}

set1 ={89, 0,0, 67, 90,78, 3, 76, 100}
print(set1)    #{0, 3, 67, 100, 76, 78, 89, 90}
# set are A set is mutable, i.e., we can remove or add elements to it
# unordered,
# gives unique items