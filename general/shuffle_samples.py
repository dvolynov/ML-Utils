import numpy as np


def shuffle(x, y):
    permutation = np.random.permutation(len(x))
    return x[permutation], y[permutation]