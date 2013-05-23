from functools import reduce


def gcd(a, b):
    """Returns greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a


def lcm_2(a, b):
    """Returns lowest common multiple."""
    return a*b // gcd(a, b)


def lcm(*args):
    """Returns lowest commone multipel of args."""
    return reduce(lcm_2, args)
