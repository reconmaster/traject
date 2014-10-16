# trajects.py

import numpy as np
import matplotlib.pyplot as plt

import coords


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

        # source
        self.r_src = coords.Coords()

        # frame vectors
        # TODO populate this from the trajectory if necessary
        self.fvecs = []

    def read_fvecs(self, filename, header=1, basis='iec'):
        """Read external fvecs file and populate the trajectory
        Keyword Arguments:
        filename -- csv file with the frame vectors
        header   -- (default 1) number of lines to skip for the header
        basis    -- (default 'iec') basis the frame vectors are in
        """
        self.fvecs = np.genfromtxt(filename, delimiter=',',
                                   skip_header=header)

        # this part isn't right, it already assumes a basis when I
        # read in the frame vectors
        if basis == 'iec':
            self.r_src = coords.Coords(self.fvecs[:, 0], self.fvecs[:,
                                                                    1],
                                       self.fvecs[:,
                                                  2],
                                       basis)
        elif basis == 'dicom':
            self.r_src = coords.Coords(self.fvecs[:, 0], self.fvecs[:,
                                                                    2],
                                       self.fvecs[:,
                                                  1],
                                       basis)
        else:
            raise Exception('Unsupported basis.')


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
