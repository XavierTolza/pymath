from unittest import TestCase

import pymath as np


class Test(TestCase):
    def test_argmax_interpolated(self):
        x = (np.arange(3) - 1)[None]
        real_max = np.random.uniform(-0.5, 0.5, 5)[:, None]
        a = np.reshape([-1], (-1, 1))
        b = -2 * a * real_max
        c = np.random.normal(0, 0.1, (a.shape[0], 1))
        y = a * (x ** 2) + b * x + c

        argmax = np.argmax_interpolated(y.T)
        import matplotlib.pyplot as plt
        plt.plot(x.ravel(), y.T)
        err = np.abs((argmax - 1) - real_max.ravel())
        assert err.max() < 1e-10
