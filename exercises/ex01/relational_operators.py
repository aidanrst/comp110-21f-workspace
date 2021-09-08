"""Exercise 01- Relational Operators."""

__author__ = "730433261"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
print(str(left) + " < " + str(right) + " is " + str(left < right))
print(str(left) + " >= " + str(right) + " is " + str(left >= right))
print(str(left) + " == " + str(right) + " is " + str(left == right))
print(str(left) + " != " + str(right) + " is " + str(left != right))