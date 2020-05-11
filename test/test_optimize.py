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

    def test_argmax_interpolated2(self):
        a, b, c = [0.00021424366603001315, -0.006707034546251528, 0.13929253965589541]
        x = np.arange(50)
        y = a * x ** 2 + b * x + c
        argmax = np.argmax_interpolated(-y)
        err = np.abs(argmax + b / (2 * a))
        assert err < 1e-10
