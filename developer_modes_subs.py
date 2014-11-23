#!/usr/bin/env python

#
# Generated Sun Nov 23 10:37:22 2014 by generateDS.py version 2.13a.
#
# Command line options:
#   ('--export', 'write')
#   ('-o', 'developer_mode.py')
#   ('-s', 'developer_modes_subs.py')
#
# Command line arguments:
#   DeveloperModeSchema.xsd
#
# Command line:
#   /home/amdavis/.local/bin/generateDS.py --export="write" -o "developer_mode.py" -s "developer_modes_subs.py" DeveloperModeSchema.xsd
#
# Current working directory (os.getcwd()):
#   traject
#

import sys

import ??? as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class VarianResearchBeamSub(supermod.VarianResearchBeam):
    def __init__(self, SchemaVersion=None, Scale=None, SetBeam=None):
        super(VarianResearchBeamSub, self).__init__(SchemaVersion, Scale, SetBeam, )
supermod.VarianResearchBeam.subclass = VarianResearchBeamSub
# end class VarianResearchBeamSub


class SetBeamSub(supermod.SetBeam):
    def __init__(self, SchemaVersion=None, Id=None, GUID=None, TreatmentMode=None, MLCModel=None, Tracking=None, TolTable=None, VelTable=None, Accs=None, ControlPoints=None, ImagingParameters=None, BeamHoldDevices=None):
        super(SetBeamSub, self).__init__(SchemaVersion, Id, GUID, TreatmentMode, MLCModel, Tracking, TolTable, VelTable, Accs, ControlPoints, ImagingParameters, BeamHoldDevices, )
supermod.SetBeam.subclass = SetBeamSub
# end class SetBeamSub


class AcquisitionSub(supermod.Acquisition):
    def __init__(self, AcquisitionId=None, AcquisitionSpecs=None, AcquisitionParameters=None):
        super(AcquisitionSub, self).__init__(AcquisitionId, AcquisitionSpecs, AcquisitionParameters, )
supermod.Acquisition.subclass = AcquisitionSub
# end class AcquisitionSub


class ArmPositionsTypeSub(supermod.ArmPositionsType):
    def __init__(self, SpecialPosition=None, Positions=None):
        super(ArmPositionsTypeSub, self).__init__(SpecialPosition, Positions, )
supermod.ArmPositionsType.subclass = ArmPositionsTypeSub
# end class ArmPositionsTypeSub


class ArmTolerancesSub(supermod.ArmTolerances):
    def __init__(self, Lat=None, Lng=None, Vrt=None, Pitch=None):
        super(ArmTolerancesSub, self).__init__(Lat, Lng, Vrt, Pitch, )
supermod.ArmTolerances.subclass = ArmTolerancesSub
# end class ArmTolerancesSub


class AcquisitionTriggerSub(supermod.AcquisitionTrigger):
    def __init__(self, TriggerDelay=None, TriggerOnEnter=None, TriggerOnExit=None, SingleTrigger=None, extensiontype_=None):
        super(AcquisitionTriggerSub, self).__init__(TriggerDelay, TriggerOnEnter, TriggerOnExit, SingleTrigger, extensiontype_, )
supermod.AcquisitionTrigger.subclass = AcquisitionTriggerSub
# end class AcquisitionTriggerSub


class TrackingTypeSub(supermod.TrackingType):
    def __init__(self, TrackingEnabled=None, CapabilityRatio=None):
        super(TrackingTypeSub, self).__init__(TrackingEnabled, CapabilityRatio, )
supermod.TrackingType.subclass = TrackingTypeSub
# end class TrackingTypeSub


class TolTableTypeSub(supermod.TolTableType):
    def __init__(self, GantryRtn=None, CollRtn=None, CouchVrt=None, CouchLat=None, CouchLng=None, CouchRtn=None, Y12=None, X12=None):
        super(TolTableTypeSub, self).__init__(GantryRtn, CollRtn, CouchVrt, CouchLat, CouchLng, CouchRtn, Y12, X12, )
supermod.TolTableType.subclass = TolTableTypeSub
# end class TolTableTypeSub


class VelTableTypeSub(supermod.VelTableType):
    def __init__(self, GantryRtn=None, CollRtn=None, CouchVrt=None, CouchLat=None, CouchLng=None, CouchRtn=None, X1=None, X2=None, Y1=None, Y2=None):
        super(VelTableTypeSub, self).__init__(GantryRtn, CollRtn, CouchVrt, CouchLat, CouchLng, CouchRtn, X1, X2, Y1, Y2, )
supermod.VelTableType.subclass = VelTableTypeSub
# end class VelTableTypeSub


class AccsTypeSub(supermod.AccsType):
    def __init__(self, Acc1=None, Acc2=None, Acc3=None, Acc4=None):
        super(AccsTypeSub, self).__init__(Acc1, Acc2, Acc3, Acc4, )
supermod.AccsType.subclass = AccsTypeSub
# end class AccsTypeSub


class ControlPointsTypeSub(supermod.ControlPointsType):
    def __init__(self, Cp=None):
        super(ControlPointsTypeSub, self).__init__(Cp, )
supermod.ControlPointsType.subclass = ControlPointsTypeSub
# end class ControlPointsTypeSub


class CpTypeSub(supermod.CpType):
    def __init__(self, TreatProgressEvent=None, SubBeam=None, Energy=None, Mu=None, DRate=None, GantryRtn=None, CollRtn=None, CouchVrt=None, CouchLat=None, CouchLng=None, CouchRtn=None, Y1=None, Y2=None, X1=None, X2=None, Mlc=None):
        super(CpTypeSub, self).__init__(TreatProgressEvent, SubBeam, Energy, Mu, DRate, GantryRtn, CollRtn, CouchVrt, CouchLat, CouchLng, CouchRtn, Y1, Y2, X1, X2, Mlc, )
supermod.CpType.subclass = CpTypeSub
# end class CpTypeSub


class SubBeamTypeSub(supermod.SubBeamType):
    def __init__(self, Seq=None, SubbeamGUID=None, Name=None, MaxRadTime=None, TrackingTrainingOnly=None):
        super(SubBeamTypeSub, self).__init__(Seq, SubbeamGUID, Name, MaxRadTime, TrackingTrainingOnly, )
supermod.SubBeamType.subclass = SubBeamTypeSub
# end class SubBeamTypeSub


class MlcTypeSub(supermod.MlcType):
    def __init__(self, ID=None, B=None, A=None):
        super(MlcTypeSub, self).__init__(ID, B, A, )
supermod.MlcType.subclass = MlcTypeSub
# end class MlcTypeSub


class ImagingParametersTypeSub(supermod.ImagingParametersType):
    def __init__(self, DuringTreatment=None, OutsideTreatment=None, CustomTargetPermission=False, ImagingVelTable=None, LatchBEL=True, LatchKVBEL=True, ImagingPoints=None, ImagingTolerances=None, GatingParameters=None):
        super(ImagingParametersTypeSub, self).__init__(DuringTreatment, OutsideTreatment, CustomTargetPermission, ImagingVelTable, LatchBEL, LatchKVBEL, ImagingPoints, ImagingTolerances, GatingParameters, )
supermod.ImagingParametersType.subclass = ImagingParametersTypeSub
# end class ImagingParametersTypeSub


class DuringTreatmentTypeSub(supermod.DuringTreatmentType):
    def __init__(self):
        super(DuringTreatmentTypeSub, self).__init__()
supermod.DuringTreatmentType.subclass = DuringTreatmentTypeSub
# end class DuringTreatmentTypeSub


class OutsideTreatmentTypeSub(supermod.OutsideTreatmentType):
    def __init__(self, MaxMu=None):
        super(OutsideTreatmentTypeSub, self).__init__(MaxMu, )
supermod.OutsideTreatmentType.subclass = OutsideTreatmentTypeSub
# end class OutsideTreatmentTypeSub


class ImagingVelTableTypeSub(supermod.ImagingVelTableType):
    def __init__(self, GantryRtn=None, CollRtn=None, CouchVrt=None, CouchLat=None, CouchLng=None, CouchRtn=None, X1=None, X2=None, Y1=None, Y2=None):
        super(ImagingVelTableTypeSub, self).__init__(GantryRtn, CollRtn, CouchVrt, CouchLat, CouchLng, CouchRtn, X1, X2, Y1, Y2, )
supermod.ImagingVelTableType.subclass = ImagingVelTableTypeSub
# end class ImagingVelTableTypeSub


class ImagingPointsTypeSub(supermod.ImagingPointsType):
    def __init__(self, ImagingPoint=None):
        super(ImagingPointsTypeSub, self).__init__(ImagingPoint, )
supermod.ImagingPointsType.subclass = ImagingPointsTypeSub
# end class ImagingPointsTypeSub


class ImagingPointTypeSub(supermod.ImagingPointType):
    def __init__(self, Cp=None, Acquisition=None, AcquisitionStart=None, AcquisitionStop=None, KvFilters=None, KvBlades=None, Mvd=None, Kvd=None, Kvs=None, MvdAfter=None, KvdAfter=None, KvsAfter=None):
        super(ImagingPointTypeSub, self).__init__(Cp, Acquisition, AcquisitionStart, AcquisitionStop, KvFilters, KvBlades, Mvd, Kvd, Kvs, MvdAfter, KvdAfter, KvsAfter, )
supermod.ImagingPointType.subclass = ImagingPointTypeSub
# end class ImagingPointTypeSub


class KvFiltersTypeSub(supermod.KvFiltersType):
    def __init__(self, Shape=None, Foil=None):
        super(KvFiltersTypeSub, self).__init__(Shape, Foil, )
supermod.KvFiltersType.subclass = KvFiltersTypeSub
# end class KvFiltersTypeSub


class KvBladesTypeSub(supermod.KvBladesType):
    def __init__(self, Tracking=None, Positions=None):
        super(KvBladesTypeSub, self).__init__(Tracking, Positions, )
supermod.KvBladesType.subclass = KvBladesTypeSub
# end class KvBladesTypeSub


class PositionsTypeSub(supermod.PositionsType):
    def __init__(self, KVX1=None, KVX2=None, KVY1=None, KVY2=None):
        super(PositionsTypeSub, self).__init__(KVX1, KVX2, KVY1, KVY2, )
supermod.PositionsType.subclass = PositionsTypeSub
# end class PositionsTypeSub


class ImagingTolerancesTypeSub(supermod.ImagingTolerancesType):
    def __init__(self, Mvd=None, Kvd=None, Kvs=None, KvBlades=None):
        super(ImagingTolerancesTypeSub, self).__init__(Mvd, Kvd, Kvs, KvBlades, )
supermod.ImagingTolerancesType.subclass = ImagingTolerancesTypeSub
# end class ImagingTolerancesTypeSub


class KvBladesType1Sub(supermod.KvBladesType1):
    def __init__(self, KVY1=None, KVY2=None, KVX1=None, KVX2=None):
        super(KvBladesType1Sub, self).__init__(KVY1, KVY2, KVX1, KVX2, )
supermod.KvBladesType1.subclass = KvBladesType1Sub
# end class KvBladesType1Sub


class GatingParametersTypeSub(supermod.GatingParametersType):
    def __init__(self, Source=None, Filter=None, QualityThreshold=None, KVGating=None, Position=None, Orientation=None, GatingWindow=None, MVAcquisitionTrigger=None, KVAcquisitionTrigger=None):
        super(GatingParametersTypeSub, self).__init__(Source, Filter, QualityThreshold, KVGating, Position, Orientation, GatingWindow, MVAcquisitionTrigger, KVAcquisitionTrigger, )
supermod.GatingParametersType.subclass = GatingParametersTypeSub
# end class GatingParametersTypeSub


class PositionTypeSub(supermod.PositionType):
    def __init__(self, X=None, Y=None, Z=None):
        super(PositionTypeSub, self).__init__(X, Y, Z, )
supermod.PositionType.subclass = PositionTypeSub
# end class PositionTypeSub


class OrientationTypeSub(supermod.OrientationType):
    def __init__(self, Qx=None, Qy=None, Qz=None, Q0=None):
        super(OrientationTypeSub, self).__init__(Qx, Qy, Qz, Q0, )
supermod.OrientationType.subclass = OrientationTypeSub
# end class OrientationTypeSub


class GatingWindowTypeSub(supermod.GatingWindowType):
    def __init__(self, Axis=None, Entry=None, Exit=None, EntryDelay=None, FaultOnExit=None):
        super(GatingWindowTypeSub, self).__init__(Axis, Entry, Exit, EntryDelay, FaultOnExit, )
supermod.GatingWindowType.subclass = GatingWindowTypeSub
# end class GatingWindowTypeSub


class MVAcquisitionTriggerTypeSub(supermod.MVAcquisitionTriggerType):
    def __init__(self, TriggerDelay=None, TriggerOnEnter=None, TriggerOnExit=None, SingleTrigger=None):
        super(MVAcquisitionTriggerTypeSub, self).__init__(TriggerDelay, TriggerOnEnter, TriggerOnExit, SingleTrigger, )
supermod.MVAcquisitionTriggerType.subclass = MVAcquisitionTriggerTypeSub
# end class MVAcquisitionTriggerTypeSub


class KVAcquisitionTriggerTypeSub(supermod.KVAcquisitionTriggerType):
    def __init__(self, TriggerDelay=None, TriggerOnEnter=None, TriggerOnExit=None, SingleTrigger=None):
        super(KVAcquisitionTriggerTypeSub, self).__init__(TriggerDelay, TriggerOnEnter, TriggerOnExit, SingleTrigger, )
supermod.KVAcquisitionTriggerType.subclass = KVAcquisitionTriggerTypeSub
# end class KVAcquisitionTriggerTypeSub


class BeamHoldDevicesTypeSub(supermod.BeamHoldDevicesType):
    def __init__(self, Dev=None):
        super(BeamHoldDevicesTypeSub, self).__init__(Dev, )
supermod.BeamHoldDevicesType.subclass = BeamHoldDevicesTypeSub
# end class BeamHoldDevicesTypeSub


class DevTypeSub(supermod.DevType):
    def __init__(self, Id=None):
        super(DevTypeSub, self).__init__(Id, )
supermod.DevType.subclass = DevTypeSub
# end class DevTypeSub


class AcquisitionSpecsTypeSub(supermod.AcquisitionSpecsType):
    def __init__(self, Handshake=None, KV=None, MVDose=None, Gating=None):
        super(AcquisitionSpecsTypeSub, self).__init__(Handshake, KV, MVDose, Gating, )
supermod.AcquisitionSpecsType.subclass = AcquisitionSpecsTypeSub
# end class AcquisitionSpecsTypeSub


class AcquisitionParametersTypeSub(supermod.AcquisitionParametersType):
    def __init__(self, ImageMode=None, AcquisitionMode=None, CalibrationSet=None, ImageDestination=None, NotificationDestination=None, Movie=None, RaiseFault=None, Cache=None, HistogramRoi=None, MV=None, KV=None):
        super(AcquisitionParametersTypeSub, self).__init__(ImageMode, AcquisitionMode, CalibrationSet, ImageDestination, NotificationDestination, Movie, RaiseFault, Cache, HistogramRoi, MV, KV, )
supermod.AcquisitionParametersType.subclass = AcquisitionParametersTypeSub
# end class AcquisitionParametersTypeSub


class ImageModeTypeSub(supermod.ImageModeType):
    def __init__(self, id=None, Overwrite=None):
        super(ImageModeTypeSub, self).__init__(id, Overwrite, )
supermod.ImageModeType.subclass = ImageModeTypeSub
# end class ImageModeTypeSub


class OverwriteTypeSub(supermod.OverwriteType):
    def __init__(self, parameter=None, valueOf_=None):
        super(OverwriteTypeSub, self).__init__(parameter, valueOf_, )
supermod.OverwriteType.subclass = OverwriteTypeSub
# end class OverwriteTypeSub


class AcquisitionModeTypeSub(supermod.AcquisitionModeType):
    def __init__(self, id=None, Overwrite=None):
        super(AcquisitionModeTypeSub, self).__init__(id, Overwrite, )
supermod.AcquisitionModeType.subclass = AcquisitionModeTypeSub
# end class AcquisitionModeTypeSub


class OverwriteType2Sub(supermod.OverwriteType2):
    def __init__(self, parameter=None, valueOf_=None):
        super(OverwriteType2Sub, self).__init__(parameter, valueOf_, )
supermod.OverwriteType2.subclass = OverwriteType2Sub
# end class OverwriteType2Sub


class MovieTypeSub(supermod.MovieType):
    def __init__(self, Destination=None, Parameters=None):
        super(MovieTypeSub, self).__init__(Destination, Parameters, )
supermod.MovieType.subclass = MovieTypeSub
# end class MovieTypeSub


class ParametersTypeSub(supermod.ParametersType):
    def __init__(self, width=None, height=None, frameRate=None, crop=None, invert=None, pixelValue0=None, pixelValue255=None, cutOff=None, weight=None):
        super(ParametersTypeSub, self).__init__(width, height, frameRate, crop, invert, pixelValue0, pixelValue255, cutOff, weight, )
supermod.ParametersType.subclass = ParametersTypeSub
# end class ParametersTypeSub


class HistogramRoiTypeSub(supermod.HistogramRoiType):
    def __init__(self, X1=None, Y1=None, X2=None, Y2=None):
        super(HistogramRoiTypeSub, self).__init__(X1, Y1, X2, Y2, )
supermod.HistogramRoiType.subclass = HistogramRoiTypeSub
# end class HistogramRoiTypeSub


class MVTypeSub(supermod.MVType):
    def __init__(self, Energy=None, DoseRate=None):
        super(MVTypeSub, self).__init__(Energy, DoseRate, )
supermod.MVType.subclass = MVTypeSub
# end class MVTypeSub


class KVTypeSub(supermod.KVType):
    def __init__(self, KiloVolts=None, MilliAmperes=None, MilliSeconds=None, eFocalSpot='Large', eFluoroLevelControl='Low', AutoBrightnessControl=False):
        super(KVTypeSub, self).__init__(KiloVolts, MilliAmperes, MilliSeconds, eFocalSpot, eFluoroLevelControl, AutoBrightnessControl, )
supermod.KVType.subclass = KVTypeSub
# end class KVTypeSub


class PositionsType3Sub(supermod.PositionsType3):
    def __init__(self, Lat=None, Lng=None, Vrt=None, Pitch=None):
        super(PositionsType3Sub, self).__init__(Lat, Lng, Vrt, Pitch, )
supermod.PositionsType3.subclass = PositionsType3Sub
# end class PositionsType3Sub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'VarianResearchBeam'
        rootClass = supermod.VarianResearchBeam
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'VarianResearchBeam'
        rootClass = supermod.VarianResearchBeam
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'VarianResearchBeam'
        rootClass = supermod.VarianResearchBeam
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'VarianResearchBeam'
        rootClass = supermod.VarianResearchBeam
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from ??? import *\n\n')
        sys.stdout.write('import ??? as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
