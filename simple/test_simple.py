import unittest

from simple import workin_with_list


class TestWorkingWithList(unittest.TestCase):
    def test_working_with_list(self):
        listaInput = [{'id': 1, 'edad': 46}, {'id': 2, 'edad': 47}, {'id': 3, 'edad': 100}, {'id': 4, 'edad': 3}, {'id': 5, 'edad': 45}, {
            'id': 6, 'edad': 59}, {'id': 7, 'edad': 97}, {'id': 8, 'edad': 3}, {'id': 9, 'edad': 38}, {'id': 10, 'edad': 18}]
        listaOutput = [{'id': 3, 'edad': 100}, {'id': 7, 'edad': 97}, {'id': 6, 'edad': 59}, {'id': 2, 'edad': 47}, {'id': 1, 'edad': 46}, {
            'id': 5, 'edad': 45}, {'id': 9, 'edad': 38}, {'id': 10, 'edad': 18}, {'id': 4, 'edad': 3}, {'id': 8, 'edad': 3}]
        self.assertEqual(workin_with_list(listaInput), listaOutput)


if __name__ == '__main__':
    unittest.main()
