# -*- coding: utf-8 -*-
"""Tests for traject.beamxml module

"""

import unittest

from traject.beamxml import BeamXML
from traject.trajects import Trajectory

# for debugging, place debug_here() whenever needed
import ipdb
debug_here = ipdb.set_trace


class TestBeamXML(unittest.TestCase):

    def setUp(self):
        """Setup beamxml object
        """
        self.bxml = BeamXML('test_scan.xml')

        # build a simple trajectory
        self.trj = Trajectory()

        # set initial control point
        self.trj.cpts.set_init_cp({'ang': 364.})

        # add a control point
        self.trj.add_cp({'ang': 184., 'kv_det_lat': -14.})

        # add a control point
        self.trj.add_cp({'ang': -4., 'kv_det_lng': -5})

        # populate XML object from the trajectory
        self.bxml.populate(self.trj)

    def test_set_control_points(self):
        """Test converting control points
        """
        # check that the correct values were set
        self.assertEqual(self.bxml.scan.SetBeam.
                         ControlPoints.Cp[0].get_GantryRtn(), 364.)

        self.assertEqual(self.bxml.scan.SetBeam.
                         ControlPoints.Cp[1].get_GantryRtn(), 184.)

        self.assertEqual(self.bxml.scan.SetBeam.
                         ControlPoints.Cp[-1].get_GantryRtn(), -4.)

        self.assertEqual(self.bxml.scan.SetBeam.ImagingParameters.
                         ImagingPoints.ImagingPoint[1].Kvd.Positions.
                         get_Lat(), -14.)

        self.assertEqual(self.bxml.scan.SetBeam.ImagingParameters.
                         ImagingPoints.ImagingPoint[2].Kvd.Positions.
                         get_Lat(), -14.)

        self.assertEqual(self.bxml.scan.SetBeam.ImagingParameters.
                         ImagingPoints.ImagingPoint[2].Kvd.Positions.
                         get_Lng(), -5.)

        # write test xml file for verification
        # self.bxml.write_xml()


if __name__ == '__main__':
    unittest.main()
