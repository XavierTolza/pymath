import numpy as np


def min_max_normalize(x, **kwargs):
    res = x - np.nanmin(x, **kwargs)
    res = res / np.nanmax(res, **kwargs)
    res[np.isnan(res)] = 0
    return res
