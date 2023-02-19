
'''Write a Python program that takes a list of numbers as input and outputs the sum of all the even numbers in the list.

Here's an example input and output:

Input: [1, 2, 3, 4, 5, 6]
Output: 12'''

list = [1, 2, 3, 4, 5, 6]

def sum(list):
    sum = 0
    for i in list:
        if i%2 == 0: # it means it's even
            sum +=i
    return sum

print(sum(list))
