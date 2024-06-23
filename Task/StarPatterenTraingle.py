# star pattern right triangle

# def print_right_triangle(n):
#     """Prints a right triangle of stars with n rows."""
#     for i in range(n):
#         print('*' * (i + 1))

n = 5
for i in range(n):
    print('*' * (i + 1))

# revere traingle star pattern
for i in range(n - 1, 0, -1):
    print('*' * i)
