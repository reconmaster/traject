# -*- coding: utf-8 -*-
import numpy as np

from traject import trajects
from traject import beamxml

# trajectories
virtiso = trajects.Trajectory()

# after centering the phantom on the table, we need to calculate the
# position of the table with the spot detected with the laser moved to
# the virtual isocenter "treatment" position
couch_lat0 = float(raw_input('Enter starting couch lat position (cm): '))
couch_vrt0 = float(raw_input('Enter starting couch vrt position (cm): '))
couch_lng0 = float(raw_input('Enter starting couch lng position (cm): '))

# couch_vrt0 = 103.13
# couch_lng0 = 75.98
# couch_lat0 = 99.86

######################################################################
# need Varian Standard angles
ang0 = 364.
ang1 = 0.

# number of control points
num_pts = 200
angs = np.linspace(ang0, ang1, num_pts)

# radius for virtual isocenter
rvirt = 12.

# calculate table positions
couch_lat = couch_lat0 - rvirt*np.sin(np.deg2rad(angs))
couch_vrt = couch_vrt0 - rvirt*np.cos(np.deg2rad(angs))

######################################################################
# populate the trajectories

# initial points
virtiso.set_init_cp({'ang': angs[0],
                     'couch_lat': couch_lat[0],
                     'couch_vrt': couch_vrt[0],
                     'couch_lng': couch_lng0,
                     'kv_det_lat': -rvirt})

# now loop through and create add control points from the smooth
# function for gantry and angle
for i in np.arange(len(angs) - 1):
    virtiso.add_cp({'ang': angs[i],
                    'couch_lat': couch_lat[i],
                    'couch_vrt': couch_vrt[i]})

# create xml objects
virtiso_xml = beamxml.BeamXML('virtiso.xml')

print("Creating virtual isocenter scan...")
virtiso_xml.populate(virtiso)
virtiso_xml.write_xml()
