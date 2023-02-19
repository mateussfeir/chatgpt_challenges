
'''Write a function that takes a list of integers as input and returns the second largest number in the list.
 If the list has less than two elements, the function should return None.

For example, given the input list [10, 5, 7, 3, 8], the function should return 8.'''

# 1) Return just the second largest number in the list.
# 2) If the list has less than two elements, return none.

list = [3, 5, 6, 2, 9, 4]

def second_largest(list):
    if len(list) < 2:
        return None
    else:
        largest = max(list)
        list.remove(largest)
        second_largest = max(list)
        return second_largest

answer = second_largest(list)

print(answer)

# In this exercise I've learned how to use the "max" tool
