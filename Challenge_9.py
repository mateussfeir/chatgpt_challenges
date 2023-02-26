# Write a program that takes in a list of integers and returns a new list that contains
# only the prime numbers in the original list.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

list_of_integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
prime_list = []
for n in list_of_integers:
    if is_prime(n):
        prime_list.append(n)

print(prime_list)
