#!/usr/bin/env python

#
# Generated Thu Oct 13 15:29:06 2016 by generateDS.py version 2.23a.
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
#   /home/amdavis/.virtualenvs/traject/bin/generateDS.py --export="write" -o "developer_mode.py" -s "developer_modes_subs.py" DeveloperModeSchema.xsd
#
# Current working directory (os.getcwd()):
#   traject
#

import sys
from lxml import etree as etree_

import ??? as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
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


class ArmAxesTypeSub(supermod.ArmAxesType):
    def __init__(self, Lat=None, Lng=None, Vrt=None, Pitch=None):
        super(ArmAxesTypeSub, self).__init__(Lat, Lng, Vrt, Pitch, )
supermod.ArmAxesType.subclass = ArmAxesTypeSub
# end class ArmAxesTypeSub


class KvFiltersPositionTypeSub(supermod.KvFiltersPositionType):
    def __init__(self, Shape=None, Foil=None):
        super(KvFiltersPositionTypeSub, self).__init__(Shape, Foil, )
supermod.KvFiltersPositionType.subclass = KvFiltersPositionTypeSub
# end class KvFiltersPositionTypeSub


class BladePositionsTypeSub(supermod.BladePositionsType):
    def __init__(self, KVX1=None, KVX2=None, KVY1=None, KVY2=None):
        super(BladePositionsTypeSub, self).__init__(KVX1, KVX2, KVY1, KVY2, )
supermod.BladePositionsType.subclass = BladePositionsTypeSub
# end class BladePositionsTypeSub


class ImagingTolerancesSub(supermod.ImagingTolerances):
    def __init__(self, Mvd=None, Kvd=None, Kvs=None, KvBlades=None):
        super(ImagingTolerancesSub, self).__init__(Mvd, Kvd, Kvs, KvBlades, )
supermod.ImagingTolerances.subclass = ImagingTolerancesSub
# end class ImagingTolerancesSub


class KvBladesTolerancesSub(supermod.KvBladesTolerances):
    def __init__(self, KVY1=None, KVY2=None, KVX1=None, KVX2=None):
        super(KvBladesTolerancesSub, self).__init__(KVY1, KVY2, KVX1, KVX2, )
supermod.KvBladesTolerances.subclass = KvBladesTolerancesSub
# end class KvBladesTolerancesSub


class ArmTolerancesSub(supermod.ArmTolerances):
    def __init__(self, Lat=None, Lng=None, Vrt=None, Pitch=None):
        super(ArmTolerancesSub, self).__init__(Lat, Lng, Vrt, Pitch, )
supermod.ArmTolerances.subclass = ArmTolerancesSub
# end class ArmTolerancesSub


class ArmPositionsTypeSub(supermod.ArmPositionsType):
    def __init__(self, SpecialPosition=None, Positions=None):
        super(ArmPositionsTypeSub, self).__init__(SpecialPosition, Positions, )
supermod.ArmPositionsType.subclass = ArmPositionsTypeSub
# end class ArmPositionsTypeSub


class KvBladePositionsTypeSub(supermod.KvBladePositionsType):
    def __init__(self, Tracking=None, Positions=None):
        super(KvBladePositionsTypeSub, self).__init__(Tracking, Positions, )
supermod.KvBladePositionsType.subclass = KvBladePositionsTypeSub
# end class KvBladePositionsTypeSub


class ArmAxesSub(supermod.ArmAxes):
    def __init__(self, Lat=None, Lng=None, Vrt=None, Pitch=None):
        super(ArmAxesSub, self).__init__(Lat, Lng, Vrt, Pitch, )
supermod.ArmAxes.subclass = ArmAxesSub
# end class ArmAxesSub


class ImageModeSub(supermod.ImageMode):
    def __init__(self, id=None, Overwrite=None):
        super(ImageModeSub, self).__init__(id, Overwrite, )
supermod.ImageMode.subclass = ImageModeSub
# end class ImageModeSub


class AcquisitionModeSub(supermod.AcquisitionMode):
    def __init__(self, id=None, Overwrite=None):
        super(AcquisitionModeSub, self).__init__(id, Overwrite, )
supermod.AcquisitionMode.subclass = AcquisitionModeSub
# end class AcquisitionModeSub


class ModeOverwriteSub(supermod.ModeOverwrite):
    def __init__(self, parameter=None, valueOf_=None):
        super(ModeOverwriteSub, self).__init__(parameter, valueOf_, )
supermod.ModeOverwrite.subclass = ModeOverwriteSub
# end class ModeOverwriteSub


class MovieSub(supermod.Movie):
    def __init__(self, Destination=None, Parameters=None):
        super(MovieSub, self).__init__(Destination, Parameters, )
supermod.Movie.subclass = MovieSub
# end class MovieSub


class MovieParametersSub(supermod.MovieParameters):
    def __init__(self, Width=None, Height=None, FrameRate=None, Crop=None, Invert=None, PixelValue0=None, PixelValue255=None, CutOff=None, Weight=None):
        super(MovieParametersSub, self).__init__(Width, Height, FrameRate, Crop, Invert, PixelValue0, PixelValue255, CutOff, Weight, )
supermod.MovieParameters.subclass = MovieParametersSub
# end class MovieParametersSub


class HistogramRoiSub(supermod.HistogramRoi):
    def __init__(self, X1=None, Y1=None, X2=None, Y2=None):
        super(HistogramRoiSub, self).__init__(X1, Y1, X2, Y2, )
supermod.HistogramRoi.subclass = HistogramRoiSub
# end class HistogramRoiSub


class ImageProcessingSub(supermod.ImageProcessing):
    def __init__(self, Timeout=0, ModeId=None, AutoBeamOff=None, ConfidenceThreshold=None, Markers=None):
        super(ImageProcessingSub, self).__init__(Timeout, ModeId, AutoBeamOff, ConfidenceThreshold, Markers, )
supermod.ImageProcessing.subclass = ImageProcessingSub
# end class ImageProcessingSub


class MarkerDefinitionsSub(supermod.MarkerDefinitions):
    def __init__(self, MarkerToleranceRadius=None, MarkerToleranceVolume=None):
        super(MarkerDefinitionsSub, self).__init__(MarkerToleranceRadius, MarkerToleranceVolume, )
supermod.MarkerDefinitions.subclass = MarkerDefinitionsSub
# end class MarkerDefinitionsSub


class MarkerDefinitionSub(supermod.MarkerDefinition):
    def __init__(self, Id=None, X=None, Y=None, Z=None, extensiontype_=None):
        super(MarkerDefinitionSub, self).__init__(Id, X, Y, Z, extensiontype_, )
supermod.MarkerDefinition.subclass = MarkerDefinitionSub
# end class MarkerDefinitionSub


class MarkerDefinitionToleranceRadiusSub(supermod.MarkerDefinitionToleranceRadius):
    def __init__(self, Id=None, X=None, Y=None, Z=None, ToleranceRadius=None):
        super(MarkerDefinitionToleranceRadiusSub, self).__init__(Id, X, Y, Z, ToleranceRadius, )
supermod.MarkerDefinitionToleranceRadius.subclass = MarkerDefinitionToleranceRadiusSub
# end class MarkerDefinitionToleranceRadiusSub


class MarkerDefinitionToleranceVolumeSub(supermod.MarkerDefinitionToleranceVolume):
    def __init__(self, Id=None, X=None, Y=None, Z=None, Vertices=None, Indices=None):
        super(MarkerDefinitionToleranceVolumeSub, self).__init__(Id, X, Y, Z, Vertices, Indices, )
supermod.MarkerDefinitionToleranceVolume.subclass = MarkerDefinitionToleranceVolumeSub
# end class MarkerDefinitionToleranceVolumeSub


class MVParametersSub(supermod.MVParameters):
    def __init__(self, Energy=None, DoseRate=None):
        super(MVParametersSub, self).__init__(Energy, DoseRate, )
supermod.MVParameters.subclass = MVParametersSub
# end class MVParametersSub


class KVParametersSub(supermod.KVParameters):
    def __init__(self, KiloVolts=None, MilliAmperes=None, MilliSeconds=None, FocalSpot='Large', FluoroLevelControl='Low', AutoBrightnessControl=False, DoseRecording=True, FrameRate=0):
        super(KVParametersSub, self).__init__(KiloVolts, MilliAmperes, MilliSeconds, FocalSpot, FluoroLevelControl, AutoBrightnessControl, DoseRecording, FrameRate, )
supermod.KVParameters.subclass = KVParametersSub
# end class KVParametersSub


class AcquisitionParametersSub(supermod.AcquisitionParameters):
    def __init__(self, ImageMode=None, AcquisitionMode=None, CalibrationSet=None, ImageDestination=None, NotificationDestination=None, Movie=None, RaiseFault=None, Cache=None, HistogramRoi=None, ImageProcessing=None, MV=None, KV=None):
        super(AcquisitionParametersSub, self).__init__(ImageMode, AcquisitionMode, CalibrationSet, ImageDestination, NotificationDestination, Movie, RaiseFault, Cache, HistogramRoi, ImageProcessing, MV, KV, )
supermod.AcquisitionParameters.subclass = AcquisitionParametersSub
# end class AcquisitionParametersSub


class VectorSub(supermod.Vector):
    def __init__(self, X=None, Y=None, Z=None):
        super(VectorSub, self).__init__(X, Y, Z, )
supermod.Vector.subclass = VectorSub
# end class VectorSub


class PlacementSub(supermod.Placement):
    def __init__(self, Origin=None, AxisX=None, AxisY=None, AxisZ=None):
        super(PlacementSub, self).__init__(Origin, AxisX, AxisY, AxisZ, )
supermod.Placement.subclass = PlacementSub
# end class PlacementSub


class CoefficientsSub(supermod.Coefficients):
    def __init__(self, a0=None, a1=None, a2=None, a3=None):
        super(CoefficientsSub, self).__init__(a0, a1, a2, a3, )
supermod.Coefficients.subclass = CoefficientsSub
# end class CoefficientsSub


class FitDataSub(supermod.FitData):
    def __init__(self, FitType=None, Coefficients=None):
        super(FitDataSub, self).__init__(FitType, Coefficients, )
supermod.FitData.subclass = FitDataSub
# end class FitDataSub


class ModelSystemSub(supermod.ModelSystem):
    def __init__(self, ModelSystem_pinned=None, CouchLat=None, CouchLng=None, CouchVrt=None, CouchRtn=None, CouchPit=None, CouchRol=None):
        super(ModelSystemSub, self).__init__(ModelSystem_pinned, CouchLat, CouchLng, CouchVrt, CouchRtn, CouchPit, CouchRol, )
supermod.ModelSystem.subclass = ModelSystemSub
# end class ModelSystemSub


class BasicSurrogateModelSub(supermod.BasicSurrogateModel):
    def __init__(self, TargetPosition_surrogate=None):
        super(BasicSurrogateModelSub, self).__init__(TargetPosition_surrogate, )
supermod.BasicSurrogateModel.subclass = BasicSurrogateModelSub
# end class BasicSurrogateModelSub


class AmplitudeFitSurrogateModelSub(supermod.AmplitudeFitSurrogateModel):
    def __init__(self, X=None, Y=None, Z=None):
        super(AmplitudeFitSurrogateModelSub, self).__init__(X, Y, Z, )
supermod.AmplitudeFitSurrogateModel.subclass = AmplitudeFitSurrogateModelSub
# end class AmplitudeFitSurrogateModelSub


class SurrogateModelPlugInSub(supermod.SurrogateModelPlugIn):
    def __init__(self, module=None, name=None, anytypeobjs_=None):
        super(SurrogateModelPlugInSub, self).__init__(module, name, anytypeobjs_, )
supermod.SurrogateModelPlugIn.subclass = SurrogateModelPlugInSub
# end class SurrogateModelPlugInSub


class SurrogateModelSub(supermod.SurrogateModel):
    def __init__(self, Basic=None, AmplitudeFit=None, PlugIn=None):
        super(SurrogateModelSub, self).__init__(Basic, AmplitudeFit, PlugIn, )
supermod.SurrogateModel.subclass = SurrogateModelSub
# end class SurrogateModelSub


class BasicMotionModelSub(supermod.BasicMotionModel):
    def __init__(self):
        super(BasicMotionModelSub, self).__init__()
supermod.BasicMotionModel.subclass = BasicMotionModelSub
# end class BasicMotionModelSub


class GatingMotionModelSub(supermod.GatingMotionModel):
    def __init__(self, AmplitudeDirection_model=None):
        super(GatingMotionModelSub, self).__init__(AmplitudeDirection_model, )
supermod.GatingMotionModel.subclass = GatingMotionModelSub
# end class GatingMotionModelSub


class MotionModelPlugInSub(supermod.MotionModelPlugIn):
    def __init__(self, module=None, name=None, anytypeobjs_=None):
        super(MotionModelPlugInSub, self).__init__(module, name, anytypeobjs_, )
supermod.MotionModelPlugIn.subclass = MotionModelPlugInSub
# end class MotionModelPlugInSub


class MotionModelSub(supermod.MotionModel):
    def __init__(self, Basic=None, Gating=None, PlugIn=None):
        super(MotionModelSub, self).__init__(Basic, Gating, PlugIn, )
supermod.MotionModel.subclass = MotionModelSub
# end class MotionModelSub


class AcquisitionTriggerSub(supermod.AcquisitionTrigger):
    def __init__(self, TriggerDelay=0, TriggerOnEnter=True, TriggerOnExit=False, SingleTrigger=True):
        super(AcquisitionTriggerSub, self).__init__(TriggerDelay, TriggerOnEnter, TriggerOnExit, SingleTrigger, )
supermod.AcquisitionTrigger.subclass = AcquisitionTriggerSub
# end class AcquisitionTriggerSub


class AcquisitionTriggersSub(supermod.AcquisitionTriggers):
    def __init__(self, MV=None, KV=None):
        super(AcquisitionTriggersSub, self).__init__(MV, KV, )
supermod.AcquisitionTriggers.subclass = AcquisitionTriggersSub
# end class AcquisitionTriggersSub


class ActionWindowSub(supermod.ActionWindow):
    def __init__(self, axis=None, MVBeamImpact=True, KVBeamImpact=False, MotionCompensationImpact=False, LowerLimit=None, UpperLimit=None, Delta=None, EntryDelay=0, LingerTimeout=0, FaultOnExit=False, AcquisitionTriggers=None):
        super(ActionWindowSub, self).__init__(axis, MVBeamImpact, KVBeamImpact, MotionCompensationImpact, LowerLimit, UpperLimit, Delta, EntryDelay, LingerTimeout, FaultOnExit, AcquisitionTriggers, )
supermod.ActionWindow.subclass = ActionWindowSub
# end class ActionWindowSub


class ActionWindowsSub(supermod.ActionWindows):
    def __init__(self, Basic=None, Segmental=None):
        super(ActionWindowsSub, self).__init__(Basic, Segmental, )
supermod.ActionWindows.subclass = ActionWindowsSub
# end class ActionWindowsSub


class BasicMotionCompensationSub(supermod.BasicMotionCompensation):
    def __init__(self, TrackingSource=None, CompensateRotation=False, Restriction_model=None):
        super(BasicMotionCompensationSub, self).__init__(TrackingSource, CompensateRotation, Restriction_model, )
supermod.BasicMotionCompensation.subclass = BasicMotionCompensationSub
# end class BasicMotionCompensationSub


class MotionCompensationPlugInSub(supermod.MotionCompensationPlugIn):
    def __init__(self, module=None, name=None, anytypeobjs_=None):
        super(MotionCompensationPlugInSub, self).__init__(module, name, anytypeobjs_, )
supermod.MotionCompensationPlugIn.subclass = MotionCompensationPlugInSub
# end class MotionCompensationPlugInSub


class MotionCompensationSub(supermod.MotionCompensation):
    def __init__(self, Basic=None, PlugIn=None):
        super(MotionCompensationSub, self).__init__(Basic, PlugIn, )
supermod.MotionCompensation.subclass = MotionCompensationSub
# end class MotionCompensationSub


class TrackingSourceSub(supermod.TrackingSource):
    def __init__(self, id=None, AcquisitionParameters=None, SurrogateModel=None, MotionModel=None, TrackingActionWindows=None):
        super(TrackingSourceSub, self).__init__(id, AcquisitionParameters, SurrogateModel, MotionModel, TrackingActionWindows, )
supermod.TrackingSource.subclass = TrackingSourceSub
# end class TrackingSourceSub


class MotionManagementParametersSub(supermod.MotionManagementParameters):
    def __init__(self, ModelSystem=None, TrackingSource=None, MotionCompensation=None, GlobalActionWindows=None):
        super(MotionManagementParametersSub, self).__init__(ModelSystem, TrackingSource, MotionCompensation, GlobalActionWindows, )
supermod.MotionManagementParameters.subclass = MotionManagementParametersSub
# end class MotionManagementParametersSub


class iToolsSub(supermod.iTools):
    def __init__(self, anytypeobjs_=None):
        super(iToolsSub, self).__init__(anytypeobjs_, )
supermod.iTools.subclass = iToolsSub
# end class iToolsSub


class ImagingPointsSub(supermod.ImagingPoints):
    def __init__(self, ImagingPoint=None):
        super(ImagingPointsSub, self).__init__(ImagingPoint, )
supermod.ImagingPoints.subclass = ImagingPointsSub
# end class ImagingPointsSub


class ImagingPointSub(supermod.ImagingPoint):
    def __init__(self, Cp=None, Acquisition=None, AcquisitionStart=None, AcquisitionStop=None, KvFilters=None, KvBlades=None, Mvd=None, Kvd=None, Kvs=None, MvdAfter=None, KvdAfter=None, KvsAfter=None):
        super(ImagingPointSub, self).__init__(Cp, Acquisition, AcquisitionStart, AcquisitionStop, KvFilters, KvBlades, Mvd, Kvd, Kvs, MvdAfter, KvdAfter, KvsAfter, )
supermod.ImagingPoint.subclass = ImagingPointSub
# end class ImagingPointSub


class AcquisitionSub(supermod.Acquisition):
    def __init__(self, AcquisitionId=None, AcquisitionSpecs=None, AcquisitionParameters=None):
        super(AcquisitionSub, self).__init__(AcquisitionId, AcquisitionSpecs, AcquisitionParameters, )
supermod.Acquisition.subclass = AcquisitionSub
# end class AcquisitionSub


class AcquisitionSpecsSub(supermod.AcquisitionSpecs):
    def __init__(self, Handshake=None, KV=None, MVDose=None):
        super(AcquisitionSpecsSub, self).__init__(Handshake, KV, MVDose, )
supermod.AcquisitionSpecs.subclass = AcquisitionSpecsSub
# end class AcquisitionSpecsSub


class DuringTreatmentSub(supermod.DuringTreatment):
    def __init__(self):
        super(DuringTreatmentSub, self).__init__()
supermod.DuringTreatment.subclass = DuringTreatmentSub
# end class DuringTreatmentSub


class OutsideTreatmentSub(supermod.OutsideTreatment):
    def __init__(self, MaxMu=None):
        super(OutsideTreatmentSub, self).__init__(MaxMu, )
supermod.OutsideTreatment.subclass = OutsideTreatmentSub
# end class OutsideTreatmentSub


class ImagingParametersSub(supermod.ImagingParameters):
    def __init__(self, DuringTreatment=None, OutsideTreatment=None, LatchBEL=True, LatchKVBEL=True, ImagingPoints=None, ImagingTolerances=None, MotionManagementParameters=None, iTools=None):
        super(ImagingParametersSub, self).__init__(DuringTreatment, OutsideTreatment, LatchBEL, LatchKVBEL, ImagingPoints, ImagingTolerances, MotionManagementParameters, iTools, )
supermod.ImagingParameters.subclass = ImagingParametersSub
# end class ImagingParametersSub


class MlcPositionsTypeSub(supermod.MlcPositionsType):
    def __init__(self, ID=None, B=None, A=None):
        super(MlcPositionsTypeSub, self).__init__(ID, B, A, )
supermod.MlcPositionsType.subclass = MlcPositionsTypeSub
# end class MlcPositionsTypeSub


class SubBeamTypeSub(supermod.SubBeamType):
    def __init__(self, Seq=None, SubbeamGUID=None, Name=None, MaxRadTime=None, TrackingTrainingOnly=None):
        super(SubBeamTypeSub, self).__init__(Seq, SubbeamGUID, Name, MaxRadTime, TrackingTrainingOnly, )
supermod.SubBeamType.subclass = SubBeamTypeSub
# end class SubBeamTypeSub


class CpSub(supermod.Cp):
    def __init__(self, TreatProgressEvent=None, SubBeam=None, Energy=None, Mu=None, DRate=None, GantryRtn=None, CollRtn=None, CouchVrt=None, CouchLat=None, CouchLng=None, CouchRtn=None, CouchPit=None, CouchRol=None, Y1=None, Y2=None, X1=None, X2=None, Mlc=None, Phase=None):
        super(CpSub, self).__init__(TreatProgressEvent, SubBeam, Energy, Mu, DRate, GantryRtn, CollRtn, CouchVrt, CouchLat, CouchLng, CouchRtn, CouchPit, CouchRol, Y1, Y2, X1, X2, Mlc, Phase, )
supermod.Cp.subclass = CpSub
# end class CpSub


class ControlPointsSub(supermod.ControlPoints):
    def __init__(self, Cp=None):
        super(ControlPointsSub, self).__init__(Cp, )
supermod.ControlPoints.subclass = ControlPointsSub
# end class ControlPointsSub


class ConformityTypeSub(supermod.ConformityType):
    def __init__(self, OverExposure=None, UnderExposure=None):
        super(ConformityTypeSub, self).__init__(OverExposure, UnderExposure, )
supermod.ConformityType.subclass = ConformityTypeSub
# end class ConformityTypeSub


class TrackingAxisSub(supermod.TrackingAxis):
    def __init__(self, Tol=None, MotionType=None):
        super(TrackingAxisSub, self).__init__(Tol, MotionType, )
supermod.TrackingAxis.subclass = TrackingAxisSub
# end class TrackingAxisSub


class TrackingMLCSub(supermod.TrackingMLC):
    def __init__(self, MotionType=None, ID=None, OpenUpCarriages=None, ExpectedTargetSpeed=None, YTargetRange=None):
        super(TrackingMLCSub, self).__init__(MotionType, ID, OpenUpCarriages, ExpectedTargetSpeed, YTargetRange, )
supermod.TrackingMLC.subclass = TrackingMLCSub
# end class TrackingMLCSub


class TrackingPhaseSub(supermod.TrackingPhase):
    def __init__(self, MaxPhaseLag=None):
        super(TrackingPhaseSub, self).__init__(MaxPhaseLag, )
supermod.TrackingPhase.subclass = TrackingPhaseSub
# end class TrackingPhaseSub


class TrackingAxisListSub(supermod.TrackingAxisList):
    def __init__(self, CouchVrt=None, CouchLat=None, CouchLng=None, Y12=None, X12=None, Mlc=None, Phase=None):
        super(TrackingAxisListSub, self).__init__(CouchVrt, CouchLat, CouchLng, Y12, X12, Mlc, Phase, )
supermod.TrackingAxisList.subclass = TrackingAxisListSub
# end class TrackingAxisListSub


class TrackingSub(supermod.Tracking):
    def __init__(self, Axes=None, ConformityTol=None, InitialCapabilityRatio=None):
        super(TrackingSub, self).__init__(Axes, ConformityTol, InitialCapabilityRatio, )
supermod.Tracking.subclass = TrackingSub
# end class TrackingSub


class TolTableSub(supermod.TolTable):
    def __init__(self, GantryRtn=None, CollRtn=None, CouchVrt=None, CouchLat=None, CouchLng=None, CouchRtn=None, CouchPit=None, CouchRol=None, Y12=None, X12=None):
        super(TolTableSub, self).__init__(GantryRtn, CollRtn, CouchVrt, CouchLat, CouchLng, CouchRtn, CouchPit, CouchRol, Y12, X12, )
supermod.TolTable.subclass = TolTableSub
# end class TolTableSub


class VelTableSub(supermod.VelTable):
    def __init__(self, GantryRtn=None, CollRtn=None, CouchVrt=None, CouchLat=None, CouchLng=None, CouchRtn=None, CouchPit=None, CouchRol=None, X1=None, X2=None, Y1=None, Y2=None):
        super(VelTableSub, self).__init__(GantryRtn, CollRtn, CouchVrt, CouchLat, CouchLng, CouchRtn, CouchPit, CouchRol, X1, X2, Y1, Y2, )
supermod.VelTable.subclass = VelTableSub
# end class VelTableSub


class AccsSub(supermod.Accs):
    def __init__(self, Acc1=None, Acc2=None, Acc3=None, Acc4=None):
        super(AccsSub, self).__init__(Acc1, Acc2, Acc3, Acc4, )
supermod.Accs.subclass = AccsSub
# end class AccsSub


class DevSub(supermod.Dev):
    def __init__(self, Id=None, MVBeamImpact=None, MotionImpact=None, SyncStop=None):
        super(DevSub, self).__init__(Id, MVBeamImpact, MotionImpact, SyncStop, )
supermod.Dev.subclass = DevSub
# end class DevSub


class BeamHoldDevicesSub(supermod.BeamHoldDevices):
    def __init__(self, Dev=None):
        super(BeamHoldDevicesSub, self).__init__(Dev, )
supermod.BeamHoldDevices.subclass = BeamHoldDevicesSub
# end class BeamHoldDevicesSub


class SetBeamSub(supermod.SetBeam):
    def __init__(self, SchemaVersion=None, Id=None, GUID=None, TrajectoryUploadInfo=None, TreatmentMode=None, MLCModel=None, TolTable=None, VelTable=None, Accs=None, ControlPoints=None, ImagingParameters=None, BeamHoldDevices=None, Tracking=None):
        super(SetBeamSub, self).__init__(SchemaVersion, Id, GUID, TrajectoryUploadInfo, TreatmentMode, MLCModel, TolTable, VelTable, Accs, ControlPoints, ImagingParameters, BeamHoldDevices, Tracking, )
supermod.SetBeam.subclass = SetBeamSub
# end class SetBeamSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
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
    parser = None
    doc = parsexml_(inFilename, parser)
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
    parser = None
    doc = parsexml_(StringIO(inString), parser)
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
    parser = None
    doc = parsexml_(inFilename, parser)
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
    print(USAGE_TEXT)
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
