#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        var_1 = fct(*args)
        return (var_1)
    except Exception as Error:
        print("Exception: {}".format(Error), file=sys.stderr)
        return (None)
