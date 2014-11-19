"""Class for managing control points.

General idea is a class for maintaining a numpy array of control
points that are dictionary objects. The entries of the dictionary
correspond to the lat, lng, vrt, and gantry angle of the kv and mv
source and detector positions.

The initial position information is stored in the system configuration
class.

Gantry
======
gantry_rtn -- Gantry angle in IEC coordinate system

kV Detector
===========
kv_det_lat -- Lateral (detector offset)
kv_det_vrt -- Vertical (magnification)
kv_det_lng -- Longitudinal (axial position)

kV Source
=========
kv_src_lat -- Lateral (detector offset)
kv_src_vrt -- Vertical (magnification)
kv_src_lng -- Longitudinal (axial position)

MV Source
=========
mv_det_lat -- Lateral (detector offset)
mv_det_vrt -- Vertical (magnification)
mv_det_lng -- Longitudinal (axial position)

Couch
=====
couch_rtn -- Couch rotation
couch_lat -- Lateral
couch_vrt -- Vertical
couch_lng -- Longitudinal

"""

import numpy as np
import sympy as sp


class ControlPoints(object):
    """Class for controls points that define a trajectory.
    """
    def __init__(self, sys_config):
        """Initialze the control point class with a system config
        """
        super(ControlPoints, self).__init__()
        self.sys_config = sys_config

        # initialize the array of control points
        self.cpts = [self.sys_config.init_cfg]

        # create disctionary of symbolic position functions
        self.sym_funcs = None

        self.t = sp.symbols('t')

    def get_pts(self):
        """Return the control point array
        """
        return self.cpts

    def set_init_cp(self, init_cp):
        """Overide the default initial control point

        Keyword Arguments:
        init_cp -- new initial control point
        """
        for key, val in init_cp.iteritems():
            self.cpts[0][key] = val

    def add_cp(self, cp):
        """Add a new control point
        Keyword Arguments:
        cp --
        """
        # copy previous control point and then set the values
        # specified in the new control point
        self.cpts.append(self.cpts[-1].copy())

        for key, val in cp.iteritems():
            self.cpts[-1][key] = val

    def gen_sym_funcs(self):
        """Create array of symbolic piecewise functions

        This function creates a peicewise function for each degree of
        freedom specificed by the control points. It may be better to
        make the piecewise functions be associated with the same key.

        """
        # create compressed dictionary of values
        # for [x.get('key') for x in list]?


        # # get the number of degress of freedom
        # self.dof = len(self.cpts[0])

        # self.num_pts = len(self.cpts)

        # eval_strings = np.zeros((int(self.dof), int(self.num_pts)),
        #                         dtype=object)

        # # fill first column key values
        # i = 0
        # for key in self.cpts[0].iterkeys():
        #     eval_strings[i][0] = key

        # for j in xrange(len(self.cpts)):
        #     i=0

        #     for key, val in self.cpts[j].iteritems():
        #         # now use previous control point to calculate time and
        #         # velocity for each piece
        #         if j = 0:
        #             pass
        #         else:
        #             [

        # print eval_strings
