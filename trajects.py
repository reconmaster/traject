# trajects.py

import numpy as np
import matplotlib.pyplot as plt

import coords
import system_config

import plots


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

        # source
        self.r_src = coords.Coords()

        # frame vectors
        # TODO populate this from the trajectory if necessary
        self.fvecs = []

        # plots
        self.vis_traj = None

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

    def visualize(self, label, r_traj, txt_width=470, frac_width=1):
        """
        Keyword Arguments:
        label      -- name of plot
        r_traj     -- trajectory to plot
        txt_width  -- (default 470) width in pts of document
        frac_width -- (default 1) fraction of page width
        """
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib import colors

        if self.vis_traj is None:
            self.vis_traj = plots.Plot(txt_width, frac_width)

        self.vis_traj.new_figure(label)

        ax = self.vis_traj.figs[label].add_subplot(111, projection='3d')

        r = r_traj.get_traj()
        basis = r_traj.get_basis()

        # ax.plot(r[:, 0], r[:, 1], r[:, 2])

        # view number provides the color map for now
        # TODO use time or velocity to map color
        N = r.shape[0]
        cn = colors.Normalize(0, N)
        for j in xrange(N-1):
            ax.plot(r[j:j+2, 0], r[j:j+2, 1], r[j:j+2, 2],
                    color=plt.cm.cool(cn(j)))

        if basis == 'iec':
            plt.xlabel('Lateral')
            plt.ylabel('Longitudinal')
            ax.set_zlabel('Vertical')
        elif basis == 'dicom':
            plt.xlabel('Lateral')
            plt.ylabel('Vertical')
            ax.set_zlabel('Longitudinal')
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
