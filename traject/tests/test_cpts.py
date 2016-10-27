# -*- coding: utf-8 -*-
"""Tests for traject.control_points module

"""
import unittest

from traject.control_points import ControlPoints
from traject.system_config import TrueBeam


class TestControlPoints(unittest.TestCase):

    def setUp(self):
        """Setup trajectory class
        """
        # use TrueBeam configuration for testing
        config = TrueBeam()

        self.cpts = ControlPoints(config)

        self.new_cp = {'ang': 180}

        self.cpts.add_cp(self.new_cp)

    def test_set_init_cp(self):
        """Test setting the starting control point
        """

        # new starting position
        new_init_cp = {'ang': 0, 'kv_det_lat': 14}

        self.cpts.set_init_cp(new_init_cp)

        self.assertEqual(self.cpts.get_pts()['kv_det_lat'][0],
                         new_init_cp['kv_det_lat'])

    def test_add_cp(self):
        """Test add control point method
        """
        self.assertEqual(self.cpts.get_pts()['ang'][-1],
                         self.new_cp['ang'])

        self.assertEqual(self.cpts.get_pts()['ang'][0],
                         self.cpts.sys_config.init_cfg['ang'])

    def test_gen_sym_funcs(self):
        """Tests for creating symbolic functions
        """
        self.cpts.gen_sym_funcs()


if __name__ == '__main__':
    unittest.main()
