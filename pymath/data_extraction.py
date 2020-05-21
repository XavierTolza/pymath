import numpy as np


def argmin2d(array):
    shape = np.shape(array)[-2:]
    argmin = np.argmin(np.reshape(array, (-1, np.prod(shape))), axis=-1)
    res = np.transpose(np.unravel_index(argmin, shape))
    res = res.reshape(array.shape[:-2] + (2,))
    return res
