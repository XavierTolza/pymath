import numpy as np


def argmax_interpolated(arr):
    _arr = np.reshape(arr, (np.shape(arr)[0], -1))
    argmax = np.argmax(_arr, axis=0)
    if np.any(argmax == 0) or np.any(argmax == np.shape(_arr)[0] - 1):
        raise ValueError("A maximum value is outside interpolation range")
    index = argmax[None] + np.arange(3)[:, None] - 1
    index = index + (np.arange(_arr.shape[1]) * _arr.shape[0])[None]
    y1, y2, y3 = _arr.T.ravel()[index]
    frac = (y1 - y3) / (2 * (y3 - 2 * y2 + y1))
    return np.reshape(argmax + frac, arr.shape[1:])
