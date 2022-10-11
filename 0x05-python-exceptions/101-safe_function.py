#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        resu = fct(*args)
        return resu
    except Exception as exze:
        print("Exception: {}".format(exze), file=sys.stderr)
        return None
