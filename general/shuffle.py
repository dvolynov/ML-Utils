import numpy as np


def shuffle_samples(x, y):
    permutation = np.random.permutation(len(x))
    return x[permutation], y[permutation]