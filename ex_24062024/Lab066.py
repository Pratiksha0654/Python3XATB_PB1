# Filter in python

# This is built in function allows to filter
# can be used in list, set, tuple

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def is_even(num):
    return num % 2 == 0


even_numbers = filter(is_even, numbers)
# print(even_numbers)   #<filter object at 0x000001C43F233340>
print(list(even_numbers) )   #[2,4,6,8]