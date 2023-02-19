'''Write a function that takes a list of numbers as input and returns the sum of the squares
 of only the even numbers in the list.

For example, given the input list [1, 2, 3, 4, 5, 6], the function should return 56, which
 is the sum of the squares of 2, 4, and 6.'''

# 1) Define a function that remove the odds numbers
# 2) Individually calculate the sum of the square of each number
# 3) sum the squares

# Look to the ChatGPT adice to solve this problem:

list = [1, 2, 3, 4, 5, 6]

def sum_of_squares_of_evens(numbers):
    return sum(x*x for x in numbers if x % 2 == 0)

print(sum_of_squares_of_evens(list))

'''Below there is my solution, my solution worked but was too long... ChatGPT solution is way better!!!'''

# def just_even(numbers):
#     even_list = []
#     for i in numbers: 
#         if i % 2 == 0:
#             even_list.append(i)
#     return even_list

# def square(list):
#     square_list = []
#     for j in list:
#         square_list.append(j*j)
#     return square_list

# def sum(numbers):
#     sum = 0
#     for i in numbers:
#         sum += i
#     return sum


# even_list = just_even(list)
# square_list = square(even_list)
# sum_result = sum(square_list)
# print(sum_result)
