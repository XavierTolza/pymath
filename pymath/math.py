import numpy as np


def gaussian(x, sigma, mu=0):
    return np.exp(-(((x - mu) / sigma) ** 2) / 2) / (sigma * np.sqrt(2 * np.pi))


def mean_pm_std(x, factor=1, **kwargs):
    mean = np.nanmean(x, **kwargs)
    std = np.nanstd(x, **kwargs) * factor
    return np.array([mean - std, mean + std])


def median_pm_std(x, factor=1, **kwargs):
    mean = np.nanmedian(x, **kwargs)
    std = np.nanstd(x, **kwargs) * factor
    return np.array([mean - std, mean + std])
