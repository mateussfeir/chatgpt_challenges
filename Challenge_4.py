'''Write a function that takes a list of integers as input and returns a new list
 containing only the even numbers from the input list. For example, given the input
  list [1, 2, 3, 4, 5, 6], the function should return [2, 4, 6].'''

list = [1, 2, 3, 4, 5, 6]

def only_even(list):
    even_list = []
    for number in list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

print(only_even(list))
