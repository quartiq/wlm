# -*- coding: utf-8 -*-
# Copyright (c) 2015-2020 Robert Jördens <rj@quartiq.de>. All rights reserved.
# SPDX-License-Identifier: GPL-3.0-or-later

import ctypes

from .wlm_constants import *


lib = ctypes.windll.wlmData

_lref = ctypes.POINTER(ctypes.c_long)
_dref = ctypes.POINTER(ctypes.c_double)


# Mode, IntVal, DblVal
CallbackProc = ctypes.WINFUNCTYPE(
    None, ctypes.c_long, ctypes.c_long, ctypes.c_double)
# Ver, Mode, IntVal, DblVal, Res1
CallbackProcEx = ctypes.WINFUNCTYPE(
    None, ctypes.c_long, ctypes.c_long, ctypes.c_long,
    ctypes.c_double, ctypes.c_long)

# Functions for general usage
lib.Instantiate.restype = ctypes.c_void_p
lib.Instantiate.argtypes = [
    ctypes.c_long, ctypes.c_long, ctypes.c_void_p, ctypes.c_long]

lib.WaitForWLMEvent.restype = ctypes.c_long
lib.WaitForWLMEvent.argtypes = [_lref, _lref, _dref]
lib.WaitForWLMEventEx.restype = ctypes.c_long
lib.WaitForWLMEventEx.argtypes = [
    _lref, _lref, _lref, _dref, _lref]
lib.WaitForNextWLMEvent.restype = ctypes.c_long
lib.WaitForNextWLMEvent.argtypes = [
    _lref, _lref, _dref]
lib.WaitForNextWLMEventEx.restype = ctypes.c_long
lib.WaitForNextWLMEventEx.argtypes = [
    _lref, _lref, _lref, _dref, _lref]
lib.ClearWLMEvents.restype = None
lib.ClearWLMEvents.argtypes = []

lib.ControlWLM.restype = ctypes.c_long
lib.ControlWLM.argtypes = [ctypes.c_long, ctypes.c_void_p, ctypes.c_long]
lib.ControlWLMEx.restype = ctypes.c_long
lib.ControlWLMEx.argtypes = [
    ctypes.c_long, ctypes.c_void_p, ctypes.c_long,
    ctypes.c_long, ctypes.c_long]
lib.SetMeasurementDelayMethod.restype = ctypes.c_long
lib.SetMeasurementDelayMethod.argtypes = [ctypes.c_long, ctypes.c_long]
lib.SetWLMPriority.restype = ctypes.c_long
lib.SetWLMPriority.argtypes = [ctypes.c_long, ctypes.c_long, ctypes.c_long]
lib.PresetWLMIndex.restype = ctypes.c_long
lib.PresetWLMIndex.argtypes = [ctypes.c_long]

lib.GetWLMVersion.restype = ctypes.c_long
lib.GetWLMVersion.argtypes = [ctypes.c_long]
lib.GetWLMIndex.restype = ctypes.c_long
lib.GetWLMIndex.argtypes = [ctypes.c_long]
lib.GetWLMCount.restype = ctypes.c_long
lib.GetWLMCount.argtypes = [ctypes.c_long]


# General Get... & Set...-functions
lib.GetWavelength.restype = ctypes.c_double
lib.GetWavelength.argtypes = [ctypes.c_double]
lib.GetWavelength2.restype = ctypes.c_double
lib.GetWavelength2.argtypes = [ctypes.c_double]
lib.GetWavelengthNum.restype = ctypes.c_double
lib.GetWavelengthNum.argtypes = [ctypes.c_long, ctypes.c_double]
lib.GetCalWavelength.restype = ctypes.c_double
lib.GetCalWavelength.argtypes = [ctypes.c_long, ctypes.c_double]
lib.GetCalibrationEffect.restype = ctypes.c_double
lib.GetCalibrationEffect.argtypes = [ctypes.c_double]
lib.GetFrequency.restype = ctypes.c_double
lib.GetFrequency.argtypes = [ctypes.c_double]
lib.GetFrequency2.restype = ctypes.c_double
lib.GetFrequency2.argtypes = [ctypes.c_double]
lib.GetFrequencyNum.restype = ctypes.c_double
lib.GetFrequencyNum.argtypes = [ctypes.c_long, ctypes.c_double]
lib.GetLinewidth.restype = ctypes.c_double
lib.GetLinewidth.argtypes = [ctypes.c_long, ctypes.c_double]
lib.GetLinewidthNum.restype = ctypes.c_double
lib.GetLinewidthNum.argtypes = [ctypes.c_long, ctypes.c_double]
lib.GetDistance.restype = ctypes.c_double
lib.GetDistance.argtypes = [ctypes.c_double]
lib.GetAnalogIn.restype = ctypes.c_double
lib.GetAnalogIn.argtypes = [ctypes.c_double]
lib.GetTemperature.restype = ctypes.c_double
lib.GetTemperature.argtypes = [ctypes.c_double]
lib.SetTemperature.restype = ctypes.c_long
lib.SetTemperature.argtypes = [ctypes.c_double]
lib.GetPressure.restype = ctypes.c_double
lib.GetPressure.argtypes = [ctypes.c_double]
lib.SetPressure.restype = ctypes.c_long
lib.SetPressure.argtypes = [ctypes.c_long, ctypes.c_double]
lib.GetExternalInput.restype = ctypes.c_double
lib.GetExternalInput.argtypes = [ctypes.c_long, ctypes.c_double]
lib.SetExternalInput.restype = ctypes.c_long
lib.SetExternalInput.argtypes = [ctypes.c_long, ctypes.c_double]

lib.GetExposure.restype = ctypes.c_ushort
lib.GetExposure.argtypes = [ctypes.c_ushort]
lib.SetExposure.restype = ctypes.c_long
lib.SetExposure.argtypes = [ctypes.c_ushort]
lib.GetExposure2.restype = ctypes.c_ushort
lib.GetExposure2.argtypes = [ctypes.c_ushort]
lib.SetExposure2.restype = ctypes.c_long
lib.SetExposure2.argtypes = [ctypes.c_ushort]
lib.GetExposureNum.restype = ctypes.c_long
lib.GetExposureNum.argtypes = [ctypes.c_long, ctypes.c_long, ctypes.c_long]
lib.SetExposureNum.restype = ctypes.c_long
lib.SetExposureNum.argtypes = [ctypes.c_long, ctypes.c_long, ctypes.c_long]
lib.GetExposureMode.restype = ctypes.c_bool
lib.GetExposureMode.argtypes = [ctypes.c_bool]
lib.SetExposureMode.restype = ctypes.c_long
lib.SetExposureMode.argtypes = [ctypes.c_bool]
lib.GetExposureModeNum.restype = ctypes.c_long
lib.GetExposureModeNum.argtypes = [ctypes.c_long, ctypes.c_bool]
lib.SetExposureModeNum.restype = ctypes.c_long
lib.SetExposureModeNum.argtypes = [ctypes.c_long, ctypes.c_bool]
lib.GetExposureRange.restype = ctypes.c_long
lib.GetExposureRange.argtypes = [ctypes.c_long]

lib.GetResultMode.restype = ctypes.c_ushort
lib.GetResultMode.argtypes = [ctypes.c_ushort]
lib.SetResultMode.restype = ctypes.c_long
lib.SetResultMode.argtypes = [ctypes.c_ushort]
lib.GetRange.restype = ctypes.c_ushort
lib.GetRange.argtypes = [ctypes.c_ushort]
lib.SetRange.restype = ctypes.c_long
lib.SetRange.argtypes = [ctypes.c_ushort]
lib.GetPulseMode.restype = ctypes.c_ushort
lib.GetPulseMode.argtypes = [ctypes.c_ushort]
lib.SetPulseMode.restype = ctypes.c_long
lib.SetPulseMode.argtypes = [ctypes.c_ushort]
lib.GetWideMode.restype = ctypes.c_ushort
lib.GetWideMode.argtypes = [ctypes.c_ushort]
lib.SetWideMode.restype = ctypes.c_long
lib.SetWideMode.argtypes = [ctypes.c_ushort]

lib.GetDisplayMode.restype = ctypes.c_long
lib.GetDisplayMode.argtypes = [ctypes.c_long]
lib.SetDisplayMode.restype = ctypes.c_long
lib.SetDisplayMode.argtypes = [ctypes.c_long]
lib.GetFastMode.restype = ctypes.c_bool
lib.GetFastMode.argtypes = [ctypes.c_bool]
lib.SetFastMode.restype = ctypes.c_long
lib.SetFastMode.argtypes = [ctypes.c_bool]

lib.GetLinewidthMode.restype = ctypes.c_bool
lib.GetLinewidthMode.argtypes = [ctypes.c_bool]
lib.SetLinewidthMode.restype = ctypes.c_long
lib.SetLinewidthMode.argtypes = [ctypes.c_bool]

lib.GetDistanceMode.restype = ctypes.c_bool
lib.GetDistanceMode.argtypes = [ctypes.c_bool]
lib.SetDistanceMode.restype = ctypes.c_long
lib.SetDistanceMode.argtypes = [ctypes.c_bool]

lib.GetSwitcherMode.restype = ctypes.c_long
lib.GetSwitcherMode.argtypes = [ctypes.c_long]
lib.SetSwitcherMode.restype = ctypes.c_long
lib.SetSwitcherMode.argtypes = [ctypes.c_long]
lib.GetSwitcherChannel.restype = ctypes.c_long
lib.GetSwitcherChannel.argtypes = [ctypes.c_long]
lib.SetSwitcherChannel.restype = ctypes.c_long
lib.SetSwitcherChannel.argtypes = [ctypes.c_long]
lib.GetSwitcherSignalStates.restype = ctypes.c_long
lib.GetSwitcherSignalStates.argtypes = [
    ctypes.c_long, _lref, _lref]
lib.SetSwitcherSignalStates.restype = ctypes.c_long
lib.SetSwitcherSignalStates.argtypes = [
    ctypes.c_long, ctypes.c_long, ctypes.c_long]
lib.SetSwitcherSignal.restype = ctypes.c_long
lib.SetSwitcherSignal.argtypes = [ctypes.c_long, ctypes.c_long, ctypes.c_long]

lib.GetAutoCalMode.restype = ctypes.c_long
lib.GetAutoCalMode.argtypes = [ctypes.c_long]
lib.SetAutoCalMode.restype = ctypes.c_long
lib.SetAutoCalMode.argtypes = [ctypes.c_long]
lib.GetAutoCalSetting.restype = ctypes.c_long
lib.GetAutoCalSetting.argtypes = [
    ctypes.c_long, _lref, ctypes.c_long, _lref]
lib.SetAutoCalSetting.restype = ctypes.c_long
lib.SetAutoCalSetting.argtypes = [
    ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long]

lib.GetActiveChannel.restype = ctypes.c_long
lib.GetActiveChannel.argtypes = [ctypes.c_long, _lref, ctypes.c_long]
lib.SetActiveChannel.restype = ctypes.c_long
lib.SetActiveChannel.argtypes = [
    ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_long]
lib.GetChannelsCount.restype = ctypes.c_long
lib.GetChannelsCount.argtypes = [ctypes.c_long]

lib.GetOperationState.restype = ctypes.c_ushort
lib.GetOperationState.argtypes = [ctypes.c_ushort]
lib.Operation.restype = ctypes.c_long
lib.Operation.argtypes = [ctypes.c_ushort]
lib.SetOperationFile.restype = ctypes.c_long
lib.SetOperationFile.argtypes = [ctypes.c_char_p]
lib.Calibration.restype = ctypes.c_long
lib.Calibration.argtypes = [
    ctypes.c_long, ctypes.c_long, ctypes.c_double, ctypes.c_long]
lib.RaiseMeasurementEvent.restype = ctypes.c_long
lib.RaiseMeasurementEvent.argtypes = [ctypes.c_long]
lib.TriggerMeasurement.restype = ctypes.c_long
lib.TriggerMeasurement.argtypes = [ctypes.c_long]
lib.GetInterval.restype = ctypes.c_long
lib.GetInterval.argtypes = [ctypes.c_long]
lib.SetInterval.restype = ctypes.c_long
lib.SetInterval.argtypes = [ctypes.c_long]
lib.GetIntervalMode.restype = ctypes.c_bool
lib.GetIntervalMode.argtypes = [ctypes.c_bool]
lib.SetIntervalMode.restype = ctypes.c_long
lib.SetIntervalMode.argtypes = [ctypes.c_bool]
lib.GetBackground.restype = ctypes.c_long
lib.GetBackground.argtypes = [ctypes.c_long]
lib.SetBackground.restype = ctypes.c_long
lib.SetBackground.argtypes = [ctypes.c_long]

lib.GetLinkState.restype = ctypes.c_bool
lib.GetLinkState.argtypes = [ctypes.c_bool]
lib.SetLinkState.restype = ctypes.c_long
lib.SetLinkState.argtypes = [ctypes.c_bool]
lib.LinkSettingsDlg.restype = None
lib.LinkSettingsDlg.argtypes = []

lib.GetPatternItemSize.restype = ctypes.c_long
lib.GetPatternItemSize.argtypes = [ctypes.c_long]
lib.GetPatternItemCount.restype = ctypes.c_long
lib.GetPatternItemCount.argtypes = [ctypes.c_long]
lib.GetPattern.restype = ctypes.POINTER(ctypes.c_ulong)
lib.GetPattern.argtypes = [ctypes.c_long]
lib.GetPatternNum.restype = ctypes.POINTER(ctypes.c_ulong)
lib.GetPatternNum.argtypes = [ctypes.c_long, ctypes.c_long]
lib.GetPatternData.restype = ctypes.c_long
lib.GetPatternData.argtypes = [ctypes.c_long, ctypes.POINTER(ctypes.c_ulong)]
lib.GetPatternDataNum.restype = ctypes.c_long
lib.GetPatternDataNum.argtypes = [
    ctypes.c_long, ctypes.c_long, ctypes.POINTER(ctypes.c_ulong)]
lib.SetPattern.restype = ctypes.c_long
lib.SetPattern.argtypes = [ctypes.c_long, ctypes.c_long]
lib.SetPatternData.restype = ctypes.c_long
lib.SetPatternData.argtypes = [ctypes.c_long, ctypes.POINTER(ctypes.c_ulong)]

lib.GetAnalysisMode.restype = ctypes.c_bool
lib.GetAnalysisMode.argtypes = [ctypes.c_bool]
lib.SetAnalysisMode.restype = ctypes.c_long
lib.SetAnalysisMode.argtypes = [ctypes.c_bool]
lib.GetAnalysisItemSize.restype = ctypes.c_long
lib.GetAnalysisItemSize.argtypes = [ctypes.c_long]
lib.GetAnalysisItemCount.restype = ctypes.c_long
lib.GetAnalysisItemCount.argtypes = [ctypes.c_long]
lib.GetAnalysis.restype = ctypes.POINTER(ctypes.c_ulong)
lib.GetAnalysis.argtypes = [ctypes.c_long]
lib.GetAnalysisData.restype = ctypes.c_long
lib.GetAnalysisData.argtypes = [ctypes.c_long, ctypes.POINTER(ctypes.c_ulong)]
lib.SetAnalysis.restype = ctypes.c_long
lib.SetAnalysis.argtypes = [ctypes.c_long, ctypes.c_long]

lib.GetMinPeak.restype = ctypes.c_long
lib.GetMinPeak.argtypes = [ctypes.c_long]
lib.GetMinPeak2.restype = ctypes.c_long
lib.GetMinPeak2.argtypes = [ctypes.c_long]
lib.GetMaxPeak.restype = ctypes.c_long
lib.GetMaxPeak.argtypes = [ctypes.c_long]
lib.GetMaxPeak2.restype = ctypes.c_long
lib.GetMaxPeak2.argtypes = [ctypes.c_long]
lib.GetAvgPeak.restype = ctypes.c_long
lib.GetAvgPeak.argtypes = [ctypes.c_long]
lib.GetAvgPeak2.restype = ctypes.c_long
lib.GetAvgPeak2.argtypes = [ctypes.c_long]
lib.SetAvgPeak.restype = ctypes.c_long
lib.SetAvgPeak.argtypes = [ctypes.c_long]

lib.GetAmplitudeNum.restype = ctypes.c_long
lib.GetAmplitudeNum.argtypes = [ctypes.c_long, ctypes.c_long, ctypes.c_long]
lib.GetIntensityNum.restype = ctypes.c_double
lib.GetIntensityNum.argtypes = [ctypes.c_long, ctypes.c_double]
lib.GetPowerNum.restype = ctypes.c_double
lib.GetPowerNum.argtypes = [ctypes.c_long, ctypes.c_double]

lib.GetDelay.restype = ctypes.c_ushort
lib.GetDelay.argtypes = [ctypes.c_ushort]
lib.SetDelay.restype = ctypes.c_long
lib.SetDelay.argtypes = [ctypes.c_ushort]
lib.GetShift.restype = ctypes.c_ushort
lib.GetShift.argtypes = [ctypes.c_ushort]
lib.SetShift.restype = ctypes.c_long
lib.SetShift.argtypes = [ctypes.c_ushort]
lib.GetShift2.restype = ctypes.c_ushort
lib.GetShift2.argtypes = [ctypes.c_ushort]
lib.SetShift2.restype = ctypes.c_long
lib.SetShift2.argtypes = [ctypes.c_ushort]


# Deviation (Laser Control) and PID-functions
lib.GetDeviationMode.restype = ctypes.c_bool
lib.GetDeviationMode.argtypes = [ctypes.c_bool]
lib.SetDeviationMode.restype = ctypes.c_long
lib.SetDeviationMode.argtypes = [ctypes.c_bool]
lib.GetDeviationReference.restype = ctypes.c_double
lib.GetDeviationReference.argtypes = [ctypes.c_double]
lib.SetDeviationReference.restype = ctypes.c_long
lib.SetDeviationReference.argtypes = [ctypes.c_double]
lib.GetDeviationSensitivity.restype = ctypes.c_long
lib.GetDeviationSensitivity.argtypes = [ctypes.c_long]
lib.SetDeviationSensitivity.restype = ctypes.c_long
lib.SetDeviationSensitivity.argtypes = [ctypes.c_long]
lib.GetDeviationSignal.restype = ctypes.c_double
lib.GetDeviationSignal.argtypes = [ctypes.c_double]
lib.GetDeviationSignalNum.restype = ctypes.c_double
lib.GetDeviationSignalNum.argtypes = [ctypes.c_long, ctypes.c_double]
lib.SetDeviationSignal.restype = ctypes.c_long
lib.SetDeviationSignal.argtypes = [ctypes.c_double]
lib.SetDeviationSignalNum.restype = ctypes.c_long
lib.SetDeviationSignalNum.argtypes = [ctypes.c_long, ctypes.c_double]
lib.RaiseDeviationSignal.restype = ctypes.c_double
lib.RaiseDeviationSignal.argtypes = [ctypes.c_long, ctypes.c_double]

lib.GetPIDCourse.restype = ctypes.c_long
lib.GetPIDCourse.argtypes = [ctypes.c_char_p]
lib.SetPIDCourse.restype = ctypes.c_long
lib.SetPIDCourse.argtypes = [ctypes.c_char_p]
lib.GetPIDCourseNum.restype = ctypes.c_long
lib.GetPIDCourseNum.argtypes = [ctypes.c_long, ctypes.c_char_p]
lib.SetPIDCourseNum.restype = ctypes.c_long
lib.SetPIDCourseNum.argtypes = [ctypes.c_long, ctypes.c_char_p]
lib.GetPIDSetting.restype = ctypes.c_long
lib.GetPIDSetting.argtypes = [
    ctypes.c_long, ctypes.c_long, _lref, _dref]
lib.SetPIDSetting.restype = ctypes.c_long
lib.SetPIDSetting.argtypes = [
    ctypes.c_long, ctypes.c_long, ctypes.c_long, ctypes.c_double]
lib.ClearPIDHistory.restype = ctypes.c_long
lib.ClearPIDHistory.argtypes = [ctypes.c_long]

# Other...-functions
lib.ConvertUnit.restype = ctypes.c_double
lib.ConvertUnit.argtypes = [ctypes.c_double, ctypes.c_long, ctypes.c_long]
lib.ConvertDeltaUnit.restype = ctypes.c_double
lib.ConvertDeltaUnit.argtypes = [
    ctypes.c_double, ctypes.c_double, ctypes.c_long,
    ctypes.c_long, ctypes.c_long]
