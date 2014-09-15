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
        self.assertTrue(np.all(np.logical_and(self.traj.t >= 0.0,
                                              self.traj.t <=
                                              np.float(self.time))))
