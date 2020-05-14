from unittest import TestCase
import pymath as np


class Test(TestCase):
    def test_min_max_normalize(self):
        x = np.random.randint(3, 10, (3, 5, 10))
        res = np.min_max_normalize(x, axis=0)
        assert res.max() == 1
        assert res.min() == 0
