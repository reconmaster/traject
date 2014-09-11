# trajects.py

import numpy as np
import matplotlib.pyplot as plt


###################################
# Class definition
###################################
class trajectory(object):
    '''General class for trajectory definitions.

    Parent class should hold general parameters relating to trajectory
    parameterization. This can include the frame vector array and
    anything else that is used in all of the trajectories.
    '''

    def __init__(self, time, ns):
        """ Initialize the trajectory class.
        Keyword Arguments:
        time -- Time of trajectory in seconds.
        ns   -- Number of samples in the trajectory.
        """

        self.time = time
        self.ns = ns

        # time is the independent parameter
        self.t = np.linspace(0, time, ns)


class circ(trajectory):
    """ Single circle trajectory
    """


def _test():
    """For running doctest
    """
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
