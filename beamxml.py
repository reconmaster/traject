######################################################################
# Library for managing Developer Mode xml files
######################################################################
import numpy as np
import xml.etree.ElementTree as ET

class beamxml:
    '''General trajectory object

    Contains methods for reading and generating Developer Mode xml
    files.
    '''

    ###################################
    # Required entries
    ###################################

    ###################################
    # Optional entries
    ###################################

    def __init__(self):
        ''' Initialize the trajectory '''

    def read_xml(self, xml_file):
        ''' Read in an xml file and populate the trajectory. '''

        self.tree = ET.parse(xml_file)
        self.root = self.tree.getroot()

    def write_xml(self, xml_file):
        ''' Write the trajectory element tree to an xml file. '''

        self.tree.write(xml_file)
