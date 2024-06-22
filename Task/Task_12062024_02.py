# Tringle Program
# Input 3 side given
# output: 3 side equal> equilateral, 2 sides equal>isosceles, no side equal>scalene

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))

if a == b and b == c:
    print("Equilateral triangle")
elif a == b or b == c or a == c:
    print("Isosceles triangle")
else:
    print("Scalene triangle")
