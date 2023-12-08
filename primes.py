"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError("Number of primes should be a positive integer")

    list = []
    current_num = 2  # Starting from the first prime number

    while len(list) < number_of_primes:
        if is_prime(current_num):
            list.append(current_num)
        current_num += 1

    return list
