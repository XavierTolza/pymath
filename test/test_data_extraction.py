from unittest import TestCase
import pymath as np


class Test(TestCase):
    def test_argmin2d(self):
        A = np.random.normal(0, 1, (100, 12, 50, 30))
        argmin = np.argmin2d(A)
        assert argmin.shape == (100, 12, 2)
        min = A.reshape(-1, 50, 30)[np.arange(1200), argmin.reshape(-1, 2)[:, 0], argmin.reshape(-1, 2)[:, 1]].reshape(
            (100, 12, 1, 1))
        assert np.all(min <= A)
        assert np.all(np.min(A, axis=(-1, -2)) == min[:, :, 0, 0])
