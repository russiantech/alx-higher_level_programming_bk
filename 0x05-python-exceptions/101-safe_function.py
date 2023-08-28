#!/usr/bin/python3
import sys
"""
    run/exec func safely.

    Args:
        fct: func to execute.
        args: argument(s) for this fct

    Returns:
        (on error)- None else result of call to fct.
"""


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
