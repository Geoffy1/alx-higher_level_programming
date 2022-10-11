#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        divided = a / b
    except (TypeError, ZeroDivisionError):
        divided = None
    finally:
        print("Inside result: {}".format(divided))
    return (divided)
