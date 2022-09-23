#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    my_count = len(argv)

    if my_count != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        quit(1)

    a = int(argv[1])
    b = int(argv[3])
    ops = ["+", "-", "*", "/"]
    
    def not_found():
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)

    def my_add():
        total = add(num1, num2)
        print("{:d} + {:d} = {:d}".format(num1, num2, total))
        return total

    def my_sub():
        total = sub(num1, num2)
        print("{:d} - {:d} = {:d}".format(num1, num2, total))
        return total

    def de_mul():
        total = mul(num1, num2)
        print("{:d} * {:d} = {:d}".format(num1, num2, total))
        return total

    def de_div():
        total = div(num1, num2)
        print("{:d} / {:d} = {:d}".format(num1, num2, total))
        return total

    options = {
            options = {
                "+": my_add,
                "-": my_sub,
                "*": my_mul,
                "/": my_div


