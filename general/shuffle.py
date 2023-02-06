from sklearn.utils import shuffle as sklearn_shuffle

def shuffle(x, y):
    return sklearn_shuffle(x, y)