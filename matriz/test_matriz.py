import unittest
import numpy as np

from matriz import search_consecutive


class TestSearchConsecutive(unittest.TestCase):
    def test_search_consecutive(self):
        matriz = np.array([[1, 4, 8, 10, 5],
                           [2, 5, 5, 6, 1],
                           [1, 6, 6, 6, 6],
                           [1, 7, 7, 7, 7],
                           [1, 7, 6, 5, 4]])

        np.testing.assert_equal(search_consecutive(
            matriz), [True, True, False])
        np.testing.assert_equal(search_consecutive(
            matriz.T), [False, True, True])


if __name__ == '__main__':
    unittest.main()
