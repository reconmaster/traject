"""Library for managing Developer Mode xml files

"""
import os

import numpy as np
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
        self.package_directory = os.path.\
            dirname(os.path.abspath(__file__)) + "/"

        # populate the beamxml object from the template
        self.scan = dm.parse(self.package_directory + template)

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

        print("""Are you using and offset detector or not? Check collimator blades in
template xml file!""")

        print("BeamXML file written to {}.".format(self.outfile))

    def populate(self, trj):
        """Convert control point parameters into xml entries

        Only use set the values for which control point values have
        changed. Gantry rotations are under control point while the
        rest falls into the imaging points.

        Since the template xml file only contains the start and end
        points, the first control point modifies the control
        point. Subsequent control points are inserted before the last
        control point until the last control point is reached which
        modifies the settings for the last point in the template file.

        .. todo:: Make sure the appropriate collimator blade settings
                  are chosen based on the detector offset. This will
                  be necessary if attempting to move the detector
                  within an acquisiton instead of keeping the same
                  offset we have been using so far. Probably
                  best to set in the XML for now as a different
                  template.

        Keyword Arguments:
        trj -- Trajectory to be converted to xml file
        """
        # only set values for which control points have changed
        cpts = trj.cpts.get_pts()

        num_pts = [len(v) for v in cpts.itervalues()][0]

        # first make sure the number of control points and imaging
        # points match the numpber of control points in the trajectory
        for i in np.arange(1, num_pts):

            # one less control point in the template
            self.scan.SetBeam.ControlPoints.\
                add_Cp(dm.CpType())

            # now add imaging points if necessary
            if i+1 == num_pts:
                # last imaging point exists, just match to the control
                # point number
                self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                    ImagingPoint[i].set_Cp(i)
            else:
                # add imaging point
                self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                    insert_ImagingPoint_at(i, dm.ImagingPointType())

                # set corresponding control point number
                self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                    ImagingPoint[i].set_Cp(i)

        # use first control point to initialize starting values of the
        # configuration
        init_cp = trj.cpts.get_init_cp()

        # TODO: MV components still need to be incorporated
        # 'mv_det_lat'
        # 'mv_det_vrt'
        # 'mv_det_lng'
        for key, value in init_cp.iteritems():
            if key == 'ang':
                self.scan.SetBeam.ControlPoints.Cp[0].\
                    set_GantryRtn(value)
            elif key == 'couch_rtn':
                self.scan.SetBeam.ControlPoints.Cp[0].\
                    set_CouchRtn(value)
            # elif key == 'couch_lat':
            #     self.scan.SetBeam.ControlPoints.Cp[0].\
            #         set_CouchLat(value)
            # elif key == 'couch_vrt':
            #     self.scan.SetBeam.ControlPoints.Cp[0].\
            #         set_CouchVrt(value)
            elif key == 'couch_lng':
                self.scan.SetBeam.ControlPoints.Cp[0].\
                    set_CouchLng(value)
            # rest of the values go into ImagingPoint
            elif key == 'kv_det_lat':
                self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                    ImagingPoint[0].Kvd.Positions.set_Lat(value)
            elif key == 'kv_det_vrt':
                self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                    ImagingPoint[0].Kvd.Positions.set_Vrt(value)
            elif key == 'kv_det_lng':
                self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                    ImagingPoint[0].Kvd.Positions.set_Lng(value)
            elif key == 'kv_src_vrt':
                self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                    ImagingPoint[0].Kvs.Positions.set_Vrt(value)
            elif key == 'kv_src_lng':
                self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                    ImagingPoint[0].Kvs.Positions.set_Lng(value)
            else:
                print("{} not supported yet.".format(key))

        # now set the values for any of the control point parameters
        # that change in the trajectory

        for key, value in cpts.iteritems():

            for i in np.arange(len(value)):

                if key == 'ang':
                    self.scan.SetBeam.ControlPoints.Cp[i].\
                        set_GantryRtn(value[i])
                elif key == 'couch_rtn':
                    self.scan.SetBeam.ControlPoints.Cp[i].\
                        set_CouchRtn(value[i])
                # elif key == 'couch_lat':
                #     self.scan.SetBeam.ControlPoints.Cp[i].\
                #         set_CouchLat(value[i])
                # elif key == 'couch_vrt':
                #     self.scan.SetBeam.ControlPoints.Cp[i].\
                #         set_CouchVrt(value[i])
                elif key == 'couch_lng':
                    self.scan.SetBeam.ControlPoints.Cp[i].\
                        set_CouchLng(value[i])
                # rest of the value[i]s go into ImagingPoint
                elif key == 'kv_det_lat':
                    self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                        ImagingPoint[0].Kvd.Positions.set_Lat(value)
                elif key == 'kv_det_vrt':
                    self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                        ImagingPoint[i].Kvd.Positions.set_Vrt(value[i])
                elif key == 'kv_det_lng':
                    self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                        ImagingPoint[i].Kvd.Positions.set_Lng(value[i])
                elif key == 'kv_src_vrt':
                    self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                        ImagingPoint[i].Kvs.Positions.set_Vrt(value[i])
                elif key == 'kv_src_lng':
                    self.scan.SetBeam.ImagingParameters.ImagingPoints.\
                        ImagingPoint[i].Kvs.Positions.set_Lng(value[i])
                else:
                    print("{} not supported yet.".format(key))
