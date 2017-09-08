#!/usr/bin/env python3

"""
Basic class examples

"""

# Example 1:

class Customer:
    """A customer of a bank!

    Attributes:
        name: string customers name
        balance: float money in account
    """

    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

customer1 = Customer('Guy Brah')
customer2 = Customer('Paulo Lemus', 100.0)

print(customer1.name, customer1.balance)
print(customer2.name, customer2.balance)
