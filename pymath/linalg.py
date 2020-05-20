import numpy as np
from numpy.linalg import *
from pymath.tools import broadcast_ok


def distance(v1, v2, axis=-1, **kwargs):
    return np.linalg.norm(np.array(v1) - np.array(v2), axis=axis, **kwargs)


def linregress(x, y, axis=0):
    if not broadcast_ok(x, y):
        raise ValueError("X and Y must be broadcastable")
    sx = np.sum(x, axis=axis)
    sx2 = np.sum(x ** 2, axis=axis)
    N = np.shape(x)[axis]
    det = N * sx2 - sx ** 2
    sy = np.sum(y, axis=axis)
    sxy = np.sum(x * y, axis=axis)
    a = (N * sxy - sx * sy) / det
    b = (-sx * sxy + sx2 * sy) / det
    return np.array([a, b])
