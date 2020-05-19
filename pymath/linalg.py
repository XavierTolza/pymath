import numpy as np
from numpy.linalg import *


def distance(v1, v2, axis=-1, **kwargs):
    return np.linalg.norm(np.array(v1) - np.array(v2), axis=axis, **kwargs)
