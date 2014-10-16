# trajects.py

import numpy as np
import matplotlib.pyplot as plt

import coords
import system_config


###################################
# Class definition
###################################
class Trajectory(object):
    """General class for trajectory definitions.

    Parent class should hold general parameters relating to trajectory
    parameterization. This can include the frame vector array and
    anything else that is used in all of the trajectories.

    .. todo:: First develop code for just the source. Then modify so
              that the detector position can be described too (i.e. as
              a position of the detector's center).

    .. todo:: General trajectory should be expressed as a piecewise
              function over time where the components are compiled
              from rotation or translation.
    """

    def __init__(self, time, ns, r_src=100.0, sys='TrueBeam'):
        """ Initialize the trajectory class.
        Keyword Arguments:
        time  -- Time of trajectory in seconds.
        ns    -- Number of samples in the trajectory.
        r_src -- (default 100.0) Source radius (fixed).
        sys   -- (default 'TrueBeam') Imaging system.
        """

        self.time = time
        self.ns = ns

        self.sys = sys

        # a valid system configuration is needed to ensure that the
        # correct velocities are used to populate the trajectory
        if sys == 'TrueBeam':
            self.conf = system_config.TrueBeam()
        else:
            raise Exception("This system configuration has not been define.")

        # time is the independent parameter
        self.t = np.linspace(0, time, ns)

        # store the trajectory coordinates
        self.source = []


class Circ(Trajectory):
    """ Single circle trajectory
    """
    pass


# def _test():
#     """For running doctest
#     """
#     import doctest
#     doctest.testmod()

# if __name__ == "__main__":
#     _test()
