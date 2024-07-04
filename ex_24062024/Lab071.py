# Map

# Iq>what is diff between map and function

numbers = [2, 3, 4, 5, 6, 7, 8, 9]

# def double_num(numbers):
#     return numbers * 2
# new_numbers = map(double_num, numbers)

# OR
# new_numbers= lambda numbers:numbers*2
new_numbers = map(lambda numbers:numbers*2, numbers)
print(list(new_numbers))  # [4, 6, 8, 10, 12, 14, 16, 18]
