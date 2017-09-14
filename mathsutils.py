import numpy as np


def double_sigmoid(x, a, b, width):

    low_x = width * (1 / 4)
    high_x = width * (3 / 4)

    x_low_idx = (x < low_x)
    x_mid_idx = (x >= low_x) & (x < high_x)
    x_high_idx = (x >= high_x)

    x1 = x[x_low_idx]
    x2 = x[x_mid_idx]
    x3 = x[x_high_idx]

    y = np.empty_like(x)

    y[x_low_idx] = sigmoid(x1, a, b, 0, 0.5)
    y[x_mid_idx] = sigmoid(x2, a, b, width / 2, -0.5)
    y[x_high_idx] = sigmoid(x3, a, b, width, -1.5)

    return y


def single_sigmoid(x, a, b, width):

    return sigmoid(x, a, b, width / 2, 0)


def sigmoid(x, a, b, c, d):
    """
        `a` scales curve along y
        `b` sharpness of S bend
        `c` displaces curve along x
        `d` displaces curve along y

    """

    return a * ((1 / (1 + np.exp(-b * (x - c)))) - d)
