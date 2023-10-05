#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum, difference, multiple and quotient of 10 and 5."""
    from calculator_1 import add, sub, mul, div

    x = 10
    y = 5

    print("{} + {} = {}".format(a, b, add(x, y)))
    print("{} - {} = {}".format(a, b, sub(x, y)))
    print("{} * {} = {}".format(a, b, mul(x, y)))
    print("{} / {} = {}".format(a, b, div(x, y)))
