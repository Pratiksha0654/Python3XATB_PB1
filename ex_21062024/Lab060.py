# how to print each item in set

set1 = {"A", "Dell", "Rose", "Shell"}
# set1= list(set)
# print(set1)
# print(set1[0])   # this will applicable for list

# how to print set item separately
# for i in set:
#     print(i)  # print all items but in unordered way

set2 = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2.remove(7)
set2.add(1000)  # {1, 2, 3, 4, 5, 6, 8, 9, 10, 1000}
print(set2)  # {1, 2, 3, 4, 5, 6, 8, 9, 10,1000}

set3 = set2.union(set1)
print(set3)  # {1, 2, 3, 4, 5, 6, 'Rose', 8, 9, 10, '1000''A', 'Shell', 'Dell'}
print(len(set3))  # 14
