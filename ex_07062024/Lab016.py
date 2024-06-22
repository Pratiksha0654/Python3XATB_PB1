# String Methods

# .title()  >>Return a copy of the string with the first character of each word capitalized.
# .upper()  >>Return a copy of the string with all the characters capitalized.
# .lower()  >>Return a copy of the string with all the characters lowercase.
# .strip()  >>Return a copy of the string with leading and trailing whitespace removed.
# .replace()  >>Return a copy of the string with all occurrences of a substring replaced by a new substring.
# .split()  >>Return a list of words in the string, using whitespace as the delimiter.
# .find()
# .count()
# print, id, type, len(), max(), min(),

#indexing in string

name = "Harry Potter"
name = "Pratiksha"
print(name.title())  # Harry Potter
print(name.upper())  # HARRY POTTER
print(name.lower())  # harry potter
print(type(name))
print(id(name))    #1790521568688
print(len(name))
print(name[0])
print(name[1])
# print(name[10])      #IndexError: string index out of range
print(name[-1])  # reverse count >a
print(name[-2])  # h
print(name[-3])  # s
print(name[-9])  # p
# .strip()  >>Return a copy of the string with leading and trailing whitespace removed.
print("  pratiksha  ".strip())  # pratikshah
print("     pratiksha ".lstrip())  # abc   (removes left spaces)
print(" pratiksha      ".rstrip())  #    abc (removes right spaces)
print("  abc  ".replace("abc ", "pratiksha"))  # abc
print(name.split())
print(name.split("r"))
print(name.count("t")) #count exact match for a in given string
print(name.find("k")) #find index of chr



#String is immutable
# Once a String object is created, its value cannot be changed. Any operation that appears to modify the string actually creates a new string object.
# name[0]="p" #TypeError: 'str' object does not support item assignment
name="P"+"ratiksha"





