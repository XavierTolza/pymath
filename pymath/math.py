import numpy as np


def gaussian(x, sigma, mu=0):
    return np.exp(-(((x - mu) / sigma) ** 2) / 2) / (sigma * np.sqrt(2 * np.pi))
