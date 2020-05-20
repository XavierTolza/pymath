from unittest import TestCase
import pymath as np


class Test(TestCase):
    def test_linregress(self):
        y = x = np.arange(10)
        a, b = np.linregress(x, y)
        assert a == 1 and b == 0

    def test_linregress2(self):
        a, b = np.random.randint(-10, 10, (2, 100, 100))
        x = np.random.randint(-100, 100, 50)
        y = a[None] * x[:, None, None] + b[None]
        found_a, found_b = np.linregress(x[:, None, None], y)
        assert np.all(np.abs(found_a - a) < 1e-6)
        assert np.all(np.abs(found_b - b) < 1e-6)

    def test_linregress3(self):
        success = False
        try:
            x = np.random.normal(0, 1, (50))
            y = np.random.normal(0, 1, (50, 100))
            np.linregress(x, y)
        except ValueError:
            success = True
        assert success
