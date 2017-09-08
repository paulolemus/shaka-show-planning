#!/usr/bin/env python3

"""
Lambdas are anonymous functions, similar to lambdas in Scheme or JavaScript.
It is pretty much just a function without a name. Super simple!

The syntax:
    create a lambda function:
        lambda <parameter>: <expression>

    create and execute a lambda:
        (lambda <parameter>: <expression>)()

Closures are also in Python!
"""

# Example 1: Make/execute a lambda with no arguments
print("Example 1:")

print(lambda: True)
print((lambda: True)())


# Example 2: Make/execute a lambda with one argument
print("Example 2:")

print(lambda x: x * 2)
print((lambda x: x * 2)(4))

# Example 3: Assign lambda to a variable
print("Example 3:")

myfunc = lambda x: type(x) is int
print(myfunc)
print(myfunc(2))


# Example 4: Return a closure from a function
print("Example 4:")

def makeAdder(numberToAdd):
    return lambda number: number + numberToAdd

add4 = makeAdder(4)
print(add4(4))

