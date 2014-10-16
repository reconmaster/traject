# system_config
#
# File containing the configuration class which defines the parameters
# of the CBCT system.

import numpy as np


class SysConfig(object):
    """Class contains parameters for a given CBCT system.

    """
    def __init__(self):
        super(SysConfig, self).__init__()

        # limits on the geometry
        self.geo_lims = {}
        # limits on the velocity
        self.vel_lims = {}


class TrueBeam(SysConfig):
    """Configuration for TrueBeam system

    These contraints put a rough limit on what is physically possible
    for the TrueBeam system. Not all of the combinations are valid,
    but this puts an absolute constraint on the different ranges of
    motion.

    .. todo:: Implement point-in-polygon method and checking algorithm
              to constraint the valid source and detector arm
              positions.

    .. todo:: Measure the veclocities of the c-arms to get a more
              accurate representation of the trajectories in
              simulation.

    Units
    =====
    displacement          -- cm
    angle                 -- deg
    displacement velocity -- cm/s
    angular velocity      -- deg/s
    frame rate            -- fps
    """
    def __init__(self):
        super(TrueBeam, self).__init__()

        # geometry limits
        self.geo_lims = {'gantry_rtn_min': 0,
                         'gantry_rtn_max': 360}

        # Here are the polygons that should be used to verify that the
        # poistion. Currently unbounded.
        self.kv_det_poly = 1
        self.kv_src_poly = 1
        self.mv_det_poly = 1

        # velocity limits, I can't find the c-arm velocities in the
        # manual so I am assuming the couch motion
        self.vel_lims = {'gantry_rtn': 6.00, 'couch_vrt': 2.00,
                         'couch_lat': 4.00, 'couch_lng': 8.00,
                         'couch_rtn': 3.00, 'kv_det': 3.5, 'kv_src':
                         3.5}

        # frame rates
        self.frame_rate = {'dynamic_gain_fluoro': 11.0,
                           'dyanmic_gain_low_framerate_fluoro': 7.0}
