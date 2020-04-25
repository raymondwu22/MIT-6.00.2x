import math


def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) == 0:
        return float('NaN')
    lengths = [len(x) for x in L]
    mean = sum(lengths) / len(lengths)

    return math.sqrt(sum([(mean - x) ** 2 for x in lengths]) / len(lengths))