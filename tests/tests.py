import unittest

import numpy as np
from numpy.testing import assert_array_almost_equal

from app import normalized_difference


class TestMethods(unittest.TestCase):
    def test_normalized_difference(self):

        a = np.array([[1, 2, 3], [4, 5, 6]])
        b = np.array([[2, 4, 6], [8, 10, 12]])

        expected = np.array(
            [
                [-0.33333333, -0.33333333, -0.33333333],
                [-0.33333333, -0.33333333, -0.33333333],
            ]
        )

        nd = normalized_difference(a, b)

        assert_array_almost_equal(nd, expected)
