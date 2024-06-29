#Dict   :unordered collection of key value pair
#name: pratiksha

my_dic =\
    {
    "name" : "amit",
    "age":89,
    "address":"banglore"
    }

print(my_dic)

#how we call dict and mention above attributes

my_dic1 = dict(name="Pratu",age=90,adress="bnglr")
print(my_dic1)   #{'name': 'Pratu', 'age': 90, 'adress': 'bnglr'}
print(len(my_dic1))
print(list(my_dic1.keys()))
print(list(my_dic1.values()))

for i in my_dic1.keys():
    print(i)

for i in my_dic1.values():
    print(i)

#how can I get both key and value ?

for k,v in my_dic1.items():
    print(k, v)

# name Pratu
# age 90
# adress bnglr



# In Python, several data types are ordered. The main ordered data types are:
#
# Lists: Mutable, ordered sequences.
# Example: [1, 2, 3, 'a', 'b']
# Tuples: Immutable, ordered sequences.
# Example: (1, 2, 3, 'a', 'b')
# Strings: Immutable, ordered sequences of characters.
# Example: "Hello"
