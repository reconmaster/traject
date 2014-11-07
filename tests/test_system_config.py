"""Tests for the traject.trajects module."""

import unittest
import numpy as np

from ..system_config import *


class TestControlPoint(unittest.TestCase):

    def setUp(self):
        """Setup trajectory class.
        """
        self.cp = ControlPoint()
