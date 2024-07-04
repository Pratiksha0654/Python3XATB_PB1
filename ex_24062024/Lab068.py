list1 = [1,2,3,4,5,6,7,8,9]

def is_odd(num):
    return num%2 != 0

List2 = filter(is_odd, list1)
print(list (List2))     #[1, 3, 5, 7, 9]
