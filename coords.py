# coords.py

import numpy as np
import transformations


class Coords(object):
    """Class for mapping general vectors into world coordinates.

    """
    def __init__(self, lat=np.zeros(1), lng=np.zeros(1),
                 vrt=np.zeros(1), basis="iec"):
        """Setup initial arrays of coordinate values

        Keyword Arguments:
        lat -- (default np.zeros(1)) Lateral coordinates
        lng -- (default np.zeros(1)) Longitudinal coordinates
        vrt -- (default np.zeros(1)) Vertical coordinates
        basis -- (default "iec") Basis flag
        """
        self._lat = lat
        self._lng = lng
        self._vrt = vrt

        # array holding the trajectory vectory
        self.r = []

        self._basis = basis
        self.map_coords()

    def get_basis(self):
        """Return the basis flag
        """
        return self._basis

    def copy(self):
        """Return a copy of the Coords object

        """
        return Coords(self._lat, self._lng, self._vrt, self._basis)

    def map_coords(self):
        """Map the coordinates into the basis
        """
        if (self._basis == "iec"):
            self.r = np.column_stack((self._lat, self._lng,
                                     self._vrt))
        elif (self._basis == "dicom"):
            self.r = np.column_stack((self._lat, -1*self._vrt,
                                     self._lng))
        else:
            raise Exception("Invalid basis flag")

    def change_basis(self, basis):
        """Change the basis by using the coordinate mapping function

        .. todo:: Implement the coordinate transfromation with the
        homogeneous coordinate mapping

        Keyword Arguments:
        basis -- Flag of desired basis
        """
        if basis == self._basis:
            print("Already in that basis.\n")
        else:
            self._basis = basis
            self.map_coords()

    def get_traj(self):
        """Access function to get the trajectory.

        :return r: Trajectory vector in selected basis.

        """
        return self.r
