"""Library for managing Developer Mode xml files

"""
import developer_mode as dm


class BeamXML(object):
    """General trajectory object

    Contains methods for reading and generating Developer Mode xml
    files.

    """

    def __init__(self, xml_file, template='lo_fps.xml'):
        super(BeamXML, self).__init__()
        """Create a BeamXML instance

        Currently uses a skeleton xml file that we have used before to
        configure most of the imaging settings other than the control
        points for the trajectory.

        Keyword Arguments:
        xml_file -- output xml file
        template -- skeleton xml file for imaging settings

        """
        # populate the beamxml object from the template
        self.scan = dm.parse(template)

        self.outfile = xml_file

    def read_xml(self, xml_file):
        """Read in an xml file and populate the trajectory.

        .. todo:: Need to figure out how to run through the Control
                  Points and the Imaging Points to get the values I
                  need for the trajectory. Need to make sure the there
                  are the same number of Control Points and Imaging
                  Points.

        """
        pass

    def write_xml(self):
        """Export the beamxml object to a file
        """
        with open(self.outfile, 'w') as f:
            self.scan.export(f, 0)

        print("BeamXML file written to {}.".format(self.outfile))
