# system_config
#
# File containing the configuration class which defines the parameters
# of the CBCT system.

import numpy as np


# class ControlPoint(object):
#     """Control points to define the trajectory

#     The control points set all of the position information for the
#     system. This is initially designed for the TrueBeam, but it could
#     be abstracted if some other system needs additional or different
#     control points.

#     The design for this is based on using the same control points as
#     Developer Mode to create a simulated trajectory. Ideally it will
#     be able to use the control points for simulation to create an xml
#     script that can be used with the TrueBeam.
#     """
#     def __init__(self, **kwargs):
#         """Populate control point object with values.

#         Need some sort of template with some sort of validation. I
#         like the configobj setup. Maybe XML is better here since
#         already need XML interface with the beamxml files.
#         """
#         super(ControlPoint, self).__init__()

#         for kw in kwargs.keys:
#             self.kw = kwargs[kw]


class SysConfig(object):
    """Class contains parameters for a given CBCT system.

    """
    def __init__(self):
        super(SysConfig, self).__init__()

        # limits on the geometry
        self.geo_lims = {}
        # limits on the velocity
        self.vel_lims = {}
        # initial configuration
        self.init_cfg = {}


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

    .. todo:: It may be better to have these values stored in a
              metadata file like xml? That way these could be the
              upper limits on the velocity if you wanted to reduce
              the transform velocity.

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
        self.geo_lims = {'ang_min': 0,
                         'ang_max': 360}

        # Here are the polygons that should be used to verify that the
        # poistion. Currently unbounded.
        self.kv_det_poly = 1
        self.kv_src_poly = 1
        self.mv_det_poly = 1

        # velocity limits, I can't find the c-arm velocities in the
        # manual so I am assuming the couch motion
        self.vel_lims = {'ang': 6.00,
                         'couch_vrt': 2.00,
                         'couch_lat': 4.00,
                         'couch_lng': 8.00,
                         'couch_rtn': 3.00,
                         'kv_det_vrt': 3.5,
                         'kv_det_lng': 3.5,
                         'kv_det_lat': 3.5,
                         'kv_src_vrt': 3.5,
                         'kv_src_lng': 3.5,
                         'kv_src_lat': 3.5}

        # frame rates
        self.frame_rate = {'dynamic_gain_fluoro': 11.0,
                           'dyanmic_gain_low_framerate_fluoro': 7.0}

        # typical initial configuration
        self.init_cfg = {'ang': 360.,
                         'kv_det_lat': 0.,
                         'kv_det_vrt': -50.,
                         'kv_det_lng': 0.,
                         'kv_src_vrt': 100.,
                         'kv_src_lng': 0.,
                         'mv_det_lat': 0.,
                         'mv_det_vrt': -50.,
                         'mv_det_lng': 0.,
                         'couch_rtn': 180.,
                         'couch_lat': 100.,
                         'couch_vrt': 100.,
                         'couch_lng': 100.}
