# Write a program that takes in a list of strings and returns the shortest string in the list.

words_list = ['Banana', 'Avocado', 'Milk','Tofu']

# Find a way to count how many letter in the words, I'll use a dictionary

def shortest_string(any_list):
    shortest = any_list[0] # we are using [0] just to initialize the variable
    for word in any_list:
        if len(word) < len(shortest):
            shortest = word
    return shortest

print(shortest_string(words_list))
