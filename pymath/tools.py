import numpy as np


def broadcast_ok(*args):
    try:
        np.broadcast(*args)
    except ValueError:
        return False
    return True


class dotdict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__
    __delattr__ = dict.__delitem__

