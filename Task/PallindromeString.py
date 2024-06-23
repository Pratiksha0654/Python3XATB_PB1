# i/p = naman , nitin, level
#  o/p = true

# i/p = pramod
# o/p = false

# palindrome string
def is_palindrome(word):
    if word == word[::-1]:
        print("given word is pallindrome")
    else:
        print("given word is not pallindrome")


result1 = is_palindrome("nitin")
result2 = is_palindrome("pramod")
result3 = is_palindrome("level")
result4 = is_palindrome("naman")

print(result1, result2, result3, result4)
