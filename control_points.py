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

        # dictionary for time and velocity steps for control points
        # that change
        self.time_steps = {}
        self.vel_steps = {}

        # max time to each control point
        self.max_t = None

        # create disctionary of symbolic position functions
        self.sym_funcs = {}

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

        ..todo:: Add function call before appending the control point
        to make sure that it is within the range specifiec by the
        system configuration.

        Keyword Arguments:
        cp -- Control point

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
        compressed_dict = {}

        for key in self.cpts[0].iterkeys():
            compressed_dict[key] = [x.get(key) for x in self.cpts]

        # now run through values and only calculate time if the
        # control points change
        for key, value in compressed_dict.iteritems():
            if value[1:] == value[:-1]:
                pass            # values are the same do nothing
            else:
                (self.time_steps[key],
                 self.vel_steps[key]) = self.calc_time_steps(key,
                                                             value)

        # return self.time_steps

        # use the calculated times to create dictionary of piecewise
        # functions
        t_array = np.array([j for j in self.time_steps.itervalues()])

        # find the maximum time where all of the control point
        # conditions are satisfied
        self.max_t = np.max(t_array, axis=1)

        # finally build the piecewise functions
        for key, value in self.time_steps.iteritems():
            self.sym_funcs[key] = self.write_sym_func(key, value,
                                                      compressed_dict[key])

    def calc_time_steps(self, key, value):
        """Calculate time steps for paramters that change

        Returns a list of times at which the values are
        reached. The piecewise function should be left open ended so
        that the maximum time here is used to calculate the total
        scan time.

        Also returns a list of velocities during those time steps.

        Keyword Arguments:
        key   -- parameter that changes
        value -- list of control point values for that parameter
        """
        # list of time points for piecewise function
        t = []

        # list of velocities for piecewise function
        v = []

        for j in np.arange(1, len(value)):
            # first check velocity direction
            if value[j] > value[j-1]:
                sign = 1        # positive velocity
            elif value[j] < value[j-1]:
                sign = -1       # negative velocity
            else:
                sign = 0        # no change

            # now create array of time points for piecewise function
            vel = self.sys_config.vel_lims[key] * sign

            v.append(vel)

            # as this is already a value we know to change, velocity
            # of zero means the
            if vel == 0:
                t.append(0.)
            else:
                t.append(float(value[j]-value[j-1])/vel)

        return t, v

    def write_sym_func(self, key, times, cpts):
        """Generate sympy piecewise function

        Use the max times and the times for the individiual time steps
        to create the required piecewise function.

        Keyword Arguments:
        key   -- Name of control point
        times -- Time steps for this control point
        cpts  -- Control point values
        """

        # string to be converted into piecewise function command
        func_str = ""

        for j in xrange(len(times)):
            if self.vel_steps[key] == 0:
                pass
            else:
                # Use some sort of calculation here to populate the
                # steps with the time parameter
                pass
