#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # a, b is len(tuple_a) len(tuple_b)
    # c is ((tuple_a[0] if a >= 1 else 0)/
    #+ (tuple_b[0] if b >= 1 else 0)/
    # (tuple_a[1] if a >= 2 else 0)/
    #+ (tuple_b[1] if b >= 2 else 0))
    a = list(tuple_a) + [0] * 2
    b = list(tuple_b) + [0] * 2
    new_tuple = [x + y for x,y in zip(a, b)]
    return tuple(new_tuple[0:2])
