"""Tests for the traject.trajects module."""

import unittest
import numpy as np

from ..trajects import *


class TestTrajectory(unittest.TestCase):

    def setUp(self):
        """Setup trajectory class.
        """

        # Default consfiguraion is the TrueBeam
        self.traj = Trajectory()

        # Here compose trajectory of all the different components to
        # verify they are being initialized
        self.traj.add_cp({'ang': 180})
        self.traj.add_cp({'det_lng': -5.0, 'src_lng': -5.0})

    def test_sym_pos_funcs(self):
        """Verify the endpoints of the symbolic functions are correct
        """
        # self.assertEqual(, )
        pass

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

        .. todo:: Modify these to check with the polygon positioning
                  restraints.

        """
        # check source, source radius is fixed unlike detector
        self.assertGreater(self.traj.r_src, 0)
        self.assertGreater(self.traj.r_det, 0)

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


if __name__ == '__main__':
    unittest.main()
