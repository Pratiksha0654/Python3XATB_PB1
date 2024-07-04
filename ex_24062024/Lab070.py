# filter vowels from list and print remianing list
letters =['a','e','i','o','u','p','q','t','k']
# letters_tuple = ('a','e','i','o','u','p','q','t','k')
# letters_set ={'a','e','i','o','u','p','q','t','k'}


def filter_vowels (letters):
    vowels = ['a','e','i','u','o']
    return letters in vowels

new_vowel_list = filter (filter_vowels, letters)
print(list(new_vowel_list))


 # how to print remaining list items


