import unittest

from basic.numpy import Numpy


class NumpyTest(unittest.TestCase):

    mock = Numpy()


    def test_np_mask(self):
        self.mock.np_mask()

    def test_np_linspace(self):
        self.mock.np_linspace()

if __name__ == '__main__':
    unittest.main()