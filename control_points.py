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

"""""


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

        cp -- Control point
        """
        # copy previous control point and then set the values
        # specified in the new control point
        self.cpts.append(self.cpts[-1])

        for key, val in cp.iteritems():
            self.cpts[-1][key] = val
