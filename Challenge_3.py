
'''Write a function that takes a string as input and returns a new string with all the vowels removed.
The vowels are 'a', 'e', 'i', 'o', and 'u'. For example, given the input string "hello world", the function should return "hll wrld".'''

def remove_vowels(word):
    new_word = ""
    for i in word:
        if i not in "aeiouAEIOU":
            new_word += i 
    return new_word
word = "hello world"

answer = remove_vowels(word)

print (answer)
