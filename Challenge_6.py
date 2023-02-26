# Write a program that takes in a list of integers and returns
# the sum of all the even numbers in the list.

list_of_integers = [3, 5, 6, 3, 4, 8, 7]
even_list = []

def even_numbers (chosen_list):
    for number in chosen_list:
        if number %2 == 0:
            even_list.append(number)
    return even_list

print(sum(even_numbers(list_of_integers)))

''' GPT improvements'''

# def even_numbers(chosen_list):
#     """
#     Returns a list of even numbers from the input list.
    
#     Parameters:
#     chosen_list (list): A list of integers
    
#     Returns:
#     list: A list of even integers
#     """
#     even_list = []
#     for number in chosen_list:
#         if number % 2 == 0:
#             even_list.append(number)
#     return even_list

# list_of_integers = [3, 5, 6, 3, 4, 8, 7]
# print(sum(even_numbers(list_of_integers)))



