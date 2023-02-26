# Write a program that takes in a string and returns the most common letter in the string.

user_input = input('Write anything: ')

# We need to create a dictionary to store the letters
# Defining a function that count how many times the same letter appears using a dictionary

def most_commom_letters(setence):
    letters_count = {}
    for letter in setence:
        if letter in letters_count:
           letters_count[letter] += 1
        else:
            letters_count[letter] = 1
    
    # print(f'Dictionary: {letters_count}')

    # Find the most commom letter

    most_commom = ""
    max_count = 0

    for letter, count in letters_count.items():
        if count >= max_count and letter != " ":
            most_commom = letter
            max_count = count
    print(f'The most commom letter: {most_commom}')
    print(f'It was found {max_count} time(s).')

most_commom_letters(user_input)
