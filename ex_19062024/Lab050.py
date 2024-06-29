# even odd function by lambda expresssion

# def even_odd_function(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
#
# Result = even_odd_function(43)
# print(Result)

Result1= lambda num: "even" if num % 2 == 0 else "odd"
#"even" if num % 2 == 0 else "odd"   this is one liner if else code

print(Result1(48))

print(Result1(43))