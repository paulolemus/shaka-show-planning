#!/usr/bin/env python3

"""
List comprehension examples

List comprehension is a concept that allows you to create a list
in a very intuitive way. You pretty much speak english to make a list.
"""

# Example 1: create a list from 0 to 10
print("Example 1:")

numbers = [x for x in range(11)]
print(numbers)


# Example 2: Create a list of odd numbers from 1 to 11
print("Example 2:")

numbers = [x for x in range(12) if x % 2 == 1]
print(numbers)


# Example 3: Create a list from ints in list
print("Example 3:")

randomList = [1, 2, 3, 3.14, [1, 2], (lambda x: x * 2), 100]
numbers = [x for x in randomList if type(x) is int]
print(numbers)


# Example 4: Create list of lists from list, where inner lists are [original, original * 2]
print("Example 4:")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = [[number, number * 2] for number in numbers]
print(numbers)

# Example 5: Same as above, but accomplished with a lambda
print("Example 5:")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers = [(lambda x: [x, x * 2])(number) for number in numbers]
print(numbers)
