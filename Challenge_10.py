# Write a program that takes in a string and returns True if the string is a palindrome 
# (reads the same backward as forward) and False otherwise.

def is_palindrome(s):
    return s == s[::-1] # The basic syntax for slicing is sequence[start:end:step]


user_input = input("User input: ")

print(is_palindrome(user_input))
