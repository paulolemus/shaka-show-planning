#!/usr/bin/env python3

# examples of how to iterate through lists to do stuff

# Example 1: modify each thing in list
print("Example 1:")

def modify1(numbers, func):
    for index, number in enumerate(numbers):
        numbers[index] = func(number)

numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(numbers)
modify1(numbers, lambda x: x * 5)
print(numbers)


# Example 2: modify each thing in list shortened
print("Example 2:")

numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(numbers)
numbers = [number * 5 for number in numbers]
print(numbers)

