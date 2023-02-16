import matplotlib.pyplot as plt
import PIL
import os


def collage(images, labels=None, figsize=None, colsrows=None):
    if labels: 
        if len(labels) != len(images): raise Exception('invalid length')

    figsize = figsize if figsize else (10, 10)
    figure = plt.figure(figsize=figsize)
    colsrows = colsrows if colsrows else (len(images), 1)
    cols, rows = colsrows[0], colsrows[1]

    for i in range(0, cols * rows):
        figure.add_subplot(rows, cols, i + 1)
        if labels: plt.title(labels[i])
        plt.axis("off")
        plt.imshow(images[i])

    plt.show()