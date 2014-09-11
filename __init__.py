# Traject, the CBCT Trajectory Library

# Copyright (c) 2014, Andrew Davis
# Produced at the University of Chicago
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of the copyright holders nor the names of any
#   contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

"""
=========
 Traject
=========

Provides
  1. Parametric representation of curves
  2. Visualization tools for these curves
  3. TrueBeam Developer Mode scripting from these curves

Description
===========
Library for managing parametric scanning CBCT trajectories. While
these trajectories can exist in abstract geometric space, they are
intended to mechanically implemented on physical systems. There are
nominal trajectories that uniformly distribute imaging points along a
3D curve that is defined geometrically. However, there is also a
generic vectorized description of the curve that specifies the
mechanical velocities of the motion stages that position the source
and detector.

This is initially designed to bridge the global coordinate systems of
"DICOM" imaging and IEC IGRT standards. As the DICOM coordinate system
is relative to the patient position, the current assumption is that
all of the global DICOM coordinates have the patient in the HFS
position. This means going from DICOM to IEC only involves a
coordinate transform of rotating +90 degrees around the x-axis.

:Author:
  Andrew Davis

:Organization:
  University of Chicago

:Version: 2014.09.05

Examples
========
Add some doctests here

"""


def setup_package():
    """Package testing setup method.
    """
