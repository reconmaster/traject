"""Tests for the traject.trajects module."""

import unittest
import numpy as np

from ..trajects import *


class TestTrajectory(unittest.TestCase):

    def setUp(self):
        """Setup trajectory class.
        """
        # pseudo random seed
        self.seed = int(np.random.randint(2**31-1))
        np.random.seed(self.seed)
        print('Random seed for the tests:', self.seed)

        # time in seconds (less than 5 mins)
        self.time = np.random.randint(300)
        self.views = np.random.randint(1700)

        self.traj = Trajectory(self.time, self.views)

    def test_valid_times(self):
        """Make sure the times are valid.
        """
        self.assertGreaterEqual(len(self.traj.t), 1)

        self.assertTrue(np.all(np.logical_and(self.traj.t >= 0.0,
                                              self.traj.t <=
                                              np.float(self.time))),
                        "Invalid time array.")

    def test_valid_vectors(self):
        """Ensure that the position vectors are physical
        """
        pass

    def test_read_fvecs(self):
        """Ensure a frame vector file is read correctly.

        .. todo:: I think I need some sort of mocking going on here.
        """
        # # need to fix this so it mocks function?
        # self.read_fvecs('filename.csv')

        # self.assertEqual(self.r_src.ndim, 3)

        # # make sure there are more entries than just the initialization
        # self.assertGreater(self.r_src.size, 3)
        pass


class TestCirc(unittest.TestCase):

    def setUp(self):
        # pseudo random seed
        self.seed = int(np.random.randint(2**31-1))
        np.random.seed(self.seed)
        print('Random seed for the tests:', self.seed)

        # time in seconds (less than 2 min)
        self.time = np.random.randint(120)
        self.views = np.random.randint(600)

        self.traj = Circle(self.time, self.views, )


if __name__ == '__main__':
    unittest.main()
