#!/usr/bin/python3
def magic_calculation(a, b):
    evals = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                evals += a ** b / i
        except:
            evals = b + a
            break
    return evals
