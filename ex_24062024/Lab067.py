my_dict = {
    'a': 1,
    'b': 2,
    'c': 3
}

#to print key and values :
for k,v in my_dict.items():
    print(k,v , sep=" | ")

op = 'b' in my_dict    # True
print(op)