from itertools import product
from unittest import TestCase

import pymath as np


class Test(TestCase):
    def test_cartesian_product(self):
        a, b = np.random.randint(0, 10, (2, 100))
        cart = np.cartesian_product(a, b)
        check = np.array(list(product(a, b)))
        assert np.all(check == cart)
