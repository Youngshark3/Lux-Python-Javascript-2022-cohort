import math
# This imports the mathematics library in python


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
# this functions checks if this the number is a perfect square.
# a perfect square is a number which can be multiplied by itself.


def isFibonacci(n):

    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)


digit = input("Enter a number: ")
print(digit)
if (isFibonacci(int(digit)) == True):
    print((digit), "is a Fibonacci Number")
else:
    print((digit), "is a not Fibonacci Number ")
