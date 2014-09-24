import unittest
import numpy as np

from ..coords import *


class TestCoords(unittest.TestCase):

    def setUp(self):
        """ Setup the coordinate system class
        """
        # pseudo random seed
        self.seed = int(np.random.randint(2**31-1))
        np.random.seed(self.seed)
        print('Random seed for the tests:', self.seed)

        self.lat = np.random.random(16)
        self.lng = np.random.random(16)
        self.vrt = np.random.random(16)

        # two different basis
        self.iec = Coords(self.lat, self.lng, self.vrt)
        self.dicom = Coords(self.lat, self.lng, self.vrt, "dicom")

    def test_valid_iec(self):
        """Check iec initialization
        """
        self.assertEqual(self.iec.get_basis(), "iec")

        # make sure non-zero coordinates
        self.assertGreaterEqual(len(self.iec._lat), 1)
        self.assertGreaterEqual(len(self.iec._lng), 1)
        self.assertGreaterEqual(len(self.iec._vrt), 1)

        # veryify correct mapping
        np.testing.assert_array_equal(self.iec.r[:, 0], self.iec._lat)
        np.testing.assert_array_equal(self.iec.r[:, 1], self.iec._lng)
        np.testing.assert_array_equal(self.iec.r[:, 2], self.iec._vrt)

    def test_valid_dicom(self):
        """Check dicom initialization
        """
        self.assertEqual(self.dicom.get_basis(), "dicom")

        # make sure non-zero coordinates
        self.assertGreaterEqual(len(self.dicom._lat), 1)
        self.assertGreaterEqual(len(self.dicom._lng), 1)
        self.assertGreaterEqual(len(self.dicom._vrt), 1)

        # verify correct mapping
        np.testing.assert_array_equal(self.dicom.r[:, 0], self.dicom._lat)
        np.testing.assert_array_equal(self.dicom.r[:, 1], -1*self.dicom._vrt)
        np.testing.assert_array_equal(self.dicom.r[:, 2], self.dicom._lng)

    def test_trans_dicom_to_iec(self):
        """Check coordinate system transform from DICOM to IEC.
        """
        self.dicom.change_basis("iec")

        self.assertEqual(self.dicom.get_basis(), "iec")
        np.testing.assert_array_equal(self.iec.r, self.dicom.r)

    def test_trans_iec_to_dicom(self):
        """Check coordinate system transform from IEC to DICOM.
        """
        self.iec.change_basis("dicom")

        self.assertEqual(self.iec.get_basis(), "dicom")
        np.testing.assert_array_equal(self.dicom.r, self.iec.r)


if __name__ == '__main__':
    unittest.main()
