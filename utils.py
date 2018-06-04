import math


def round(f, n):
    """You must re-write round function by yourself, because the default round in python is depended on the computer setting you used."""
    return int(f * (10 ** n))/(10 ** n)


def dformat(f, n):
    epsilon = 10e-20
    if isinstance(f, float):
        return round(f, int(-math.log10(abs(f) + epsilon)) + n)
    if isinstance(f, tuple): # tuple of float, todo
        #result = tuple(map(lambda x: round(x, int(-math.log10(abs(x) + epsilon)) + n),f))
        result = tuple(map(lambda x: round(x, n),f))
        return result

