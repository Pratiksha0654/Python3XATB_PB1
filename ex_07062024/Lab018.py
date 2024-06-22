# List data type
#List is muttable > u can change/replace any of the value in existing

my_list = [1, 2, -90, True, 78.99, "hello"]
print(my_list)
print(type(my_list))
print(len(my_list))
print(my_list[0])
print(my_list[-1])
print(my_list[-3])
print(my_list[2:5])    #[-90, True, 78.99]
print(my_list[2:-2])   #[-90, True]
print(my_list[-2:2])   #[]
print(my_list.__add__([100, 200, 300]))   #[1, 2, -90, True, 78.99, 'hello', 100, 200, 300]
print(my_list.append("milk"))  #add item at end of list
print(my_list)
print(my_list.pop()) #
print(my_list)
print(my_list.insert(2, "water"))   #add item at index 2
print(my_list)
print(my_list.remove("water"))   #remove item from list
print(my_list)
print(my_list.reverse())   #reverse the list
print(my_list)
print(my_list.extend(["chips , salt"]))
print(my_list)
print(my_list[0])   #hello
print(my_list[6])   #chips


