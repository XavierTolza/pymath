import numpy as np


def broadcast_ok(*args):
    try:
        np.broadcast(*args)
    except ValueError:
        return False
    return True
