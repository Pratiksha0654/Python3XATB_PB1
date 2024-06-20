# (end=)  used to chane the default line ending from newline(\n) to any other character
print("I am MT", end="\t<     ")

print("I am MT", end="-")
print("I am AT")

print("I am MT", end=":")
print("I am AT")

#end= and sep= can be used together

print("I","am","MT", sep="-", end=">")

# IndentationError: unexpected indent
#     print("I am AT")
# NameError: name 'Print' is not defined. Did you mean: 'print'?
# Print("I am AT")

