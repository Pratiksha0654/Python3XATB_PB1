# SET
# collection of UNIQUE items

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = {9, 10, 11, 12, 13, 14, 15}

m_set1 = set1.union(set2)    # all items
print(m_set1)

m_set2 = set1.intersection(set2)   #common items
print(m_set2)

# m_set3=set1.difference(set2)
# print(m_set3)

m_set4 = set2.difference(set1)
print(m_set4)

m_set5 = set1.symmetric_difference(set2)
print(m_set5)

set1.update(set2)
print(set1)
set2.update(set1)
print(set2)


# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# {9, 10}
# {11, 12, 13, 14, 15}
# {1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 14, 15}
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}
