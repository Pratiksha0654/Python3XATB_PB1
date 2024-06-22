# Ternary operator
def ternary_operator(x, y, z):
    """
    Returns the maximum of three numbers using a ternary operator.
    """
    return x if x > y and x > z else y if y > z else z


# Example usage
a = 10
b = 50
c = 30
d = 40
result = ternary_operator(a, b, c)
print(result)  # Output: 50

