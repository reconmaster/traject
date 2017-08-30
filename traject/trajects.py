"""Module for modelling CBCT trajectories.

Module design is based on the idea of control points used in Varian's
Developer Mode. A variety of plotting and import/export functions are
included to interface with the Developer Mode scans on TrueBeam
"""

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import control_points
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

    .. todo:: General trajectory should be expressed as a piecewise
              function over time where the components are compiled
              from rotation or translation.
    """

    def __init__(self, sys='TrueBeam'):
        """ Initialize the trajectory class.

        Units should stay be consistent for all dimensions. The
        default is cm though it could be changed if necessary.

        The trajectory will be built from a set of control points. The
        number of views will then be determined by the frame rate
        which is also in the system configuration file.

        Currently only the system configuration is the only
        parameter. Once the total trajectory is built, the time will be
        represented based on the velocities in the system
        configuration. There will also need to be some additional
        error checking to make sure that the positions that are
        specified are allowed.

        From the actual trajectory that can be imaged with the
        physical system, the trajectory can be downsampled much in the
        same way the few-view studies will be done with the real
        data. That way the simulations and the real data downsampling
        will both work in the same way in the reconstruction.

        .. todo:: If allowing different units, add flags.

        Keyword Arguments:
        sys   -- (default 'TrueBeam') Imaging system.
        """

        # Setup the system configuration
        self.sys = sys

        # a valid system configuration is needed to ensure that the
        # correct velocities are used to populate the trajectory
        if sys == 'TrueBeam':
            self.conf = system_config.TrueBeam()
        else:
            raise Exception("This system configuration has not been defined.")

        # control point object
        self.cpts = control_points.ControlPoints(self.conf)

        # position is paramaterized by time
        #
        # TODO this needs to be populated based on the velocities from
        # the system configuration
        self.t = []

        # source
        self.r_src = coords.Coords()

        # det
        self.r_det = coords.Coords()

        # frame vectors
        # TODO populate this from the trajectory if necessary
        self.fvecs = []

        # plots
        self.vis_traj = None

    def add_cp(self, cp):
        """Add a control point to the trajectory

        Uses the control point structure in the system configuration
        to add a new control point in the trajectory

        Keyword Arguments:
        cp -- Control point dictionary with values to be modified.
        """
        self.cpts.add_cp(cp)

    def set_init_cp(self, cp):
        """Wrapper for setting initial control point

        Keyword Arguments:
        cp -- Initial control point settings
        """
        self.cpts.set_init_cp(cp)

    def generate_views(self):
        """Function for generating sampled positions for the trajectory

        """
        # first get the piecewise function
        self.cpts.gen_sym_funcs()

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
            self.r_src = coords.Coords(self.fvecs[:, 0],
                                       self.fvecs[:, 1],
                                       self.fvecs[:, 2],
                                       basis)
        elif basis == 'dicom':
            self.r_src = coords.Coords(self.fvecs[:, 0],
                                       self.fvecs[:, 2],
                                       self.fvecs[:, 1],
                                       basis)
        else:
            raise Exception('Unsupported basis.')

    def visualize(self):
        """Show 3D plot of source trajectory

        :todo: show both source and detector
        """

        if self.vis_traj is None:
            self.vis_traj = plt.figure()

        ax = self.vis_traj.add_subplot(111, projection='3d')

        r = self.r_src.get_traj()
        basis = self.r_src.get_basis()

        # ax.plot(r[:, 0], r[:, 1], r[:, 2])

        # view number provides the color map for now
        # TODO use time or velocity to map color
        N = r.shape[0]
        cn = mpl.colors.Normalize(0, N)
        for j in xrange(N - 1):
            ax.plot(r[j:j + 2, 0], r[j:j + 2, 1], r[j:j + 2, 2],
                    color=plt.cm.cool(cn(j)), linewidth=3.0)

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

        cm = plt.get_cmap('cool')
        cNorm = mpl.colors.Normalize(vmin=0, vmax=N)
        scalarMap = mpl.cm.ScalarMappable(norm=cNorm, cmap=cm)
        scalarMap.set_array(np.arange(N))
        cb = self.vis_traj.colorbar(scalarMap)
        cb.set_label('View number')

# def _test():
#     """For running doctest
#     """
#     import doctest
#     doctest.testmod()

# if __name__ == "__main__":
#     _test()
