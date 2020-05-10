import numpy as np


def argmax_interpolated(arr):
    argmax = np.argmax(arr, axis=0)
    index = argmax[None] + np.arange(3)[:, None] - 1
    index = index + (np.arange(arr.shape[1]) * arr.shape[0])[None]
    y1, y2, y3 = arr.T.ravel()[index]
    frac = (y1 - y3) / (2 * (y3 - 2 * y2 + y1))
    return argmax + frac
