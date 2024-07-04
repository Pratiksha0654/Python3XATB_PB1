letters = ['a','i','e','p','o','u','c','m',]

#filter vowels from list

def vowels (letters):
    vowels_list = ['a','e','i','o','u']
    return letters in vowels_list

list_vowels = filter(vowels, letters)
print(list(list_vowels))     #['a', 'i', 'e', 'o', 'u']