import numpy as np
from tensorflow.keras import utils


def color2index(color):
    if (color[0] + color[1] + color[2]) > 20:
        index = 1
    else:
        index = 0
    return index

def index2color(index2):
    index = np.argmax(index2)
    color = []
    if index == 0:
        color = [0, 0, 0]
    else:
        color = [255, 0, 0]
    return color


def rgb_to_ohe(y, num_classes): 
    y2 = y.copy()
    y = y.reshape(y.shape[0] * y.shape[1], 3)
    yt = []
    for i in range(len(y)):
        yt.append(utils.to_categorical(color2index(y[i]), num_classes=num_classes))
    yt = np.array(yt)
    yt = yt.reshape(y2.shape[0], y2.shape[1], num_classes)
    return yt