# -*- coding: utf-8 -*-
# Copyright (c) 2015-2020 Robert Jördens <rj@quartiq.de>. All rights reserved.
# SPDX-License-Identifier: GPL-3.0-or-later

# Instantiating Constants for 'RFC' parameter
cInstCheckForWLM = -1
cInstResetCalc = 0
cInstReturnMode = cInstResetCalc
cInstNotification = 1
cInstCopyPattern = 2
cInstCopyAnalysis = cInstCopyPattern
cInstControlWLM = 3
cInstControlDelay = 4
cInstControlPriority = 5

# Notification Constants for 'Mode' parameter
cNotifyInstallCallback = 0
cNotifyRemoveCallback = 1
cNotifyInstallWaitEvent = 2
cNotifyRemoveWaitEvent = 3
cNotifyInstallCallbackEx = 4
cNotifyInstallWaitEventEx = 5

# ResultError Constants of Set...-functions
ResERR_NoErr = 0
ResERR_WlmMissing = -1
ResERR_CouldNotSet = -2
ResERR_ParmOutOfRange = -3
ResERR_WlmOutOfResources = -4
ResERR_WlmInternalError = -5
ResERR_NotAvailable = -6
ResERR_WlmBusy = -7
ResERR_NotInMeasurementMode = -8
ResERR_OnlyInMeasurementMode = -9
ResERR_ChannelNotAvailable = -10
ResERR_ChannelTemporarilyNotAvailable = -11
ResERR_CalOptionNotAvailable = -12
ResERR_CalWavelengthOutOfRange = -13
ResERR_BadCalibrationSignal = -14
ResERR_UnitNotAvailable = -15
ResERR_FileNotFound = -16
ResERR_FileCreation = -17

# Mode Constants for Callback-Export and WaitForWLMEvent-function
cmiResultMode = 1
cmiRange = 2
cmiPulse = 3
cmiPulseMode = cmiPulse
cmiWideLine = 4
cmiWideMode = cmiWideLine
cmiFast = 5
cmiFastMode = cmiFast
cmiExposureMode = 6
cmiExposureValue1 = 7
cmiExposureValue2 = 8
cmiDelay = 9
cmiShift = 10
cmiShift2 = 11
cmiReduce = 12
cmiReduced = cmiReduce
cmiScale = 13
cmiTemperature = 14
cmiLink = 15
cmiOperation = 16
cmiDisplayMode = 17
cmiPattern1a = 18
cmiPattern1b = 19
cmiPattern2a = 20
cmiPattern2b = 21
cmiMin1 = 22
cmiMax1 = 23
cmiMin2 = 24
cmiMax2 = 25
cmiNowTick = 26
cmiCallback = 27
cmiFrequency1 = 28
cmiFrequency2 = 29
cmiDLLDetach = 30
cmiVersion = 31
cmiAnalysisMode = 32
cmiDeviationMode = 33
cmiDeviationReference = 34
cmiDeviationSensitivity = 35
cmiAppearance = 36
cmiAutoCalMode = 37
cmiWavelength1 = 42
cmiWavelength2 = 43
cmiLinewidth = 44
cmiLinewidthMode = 45
cmiLinkDlg = 56
cmiAnalysis = 57
cmiAnalogIn = 66
cmiAnalogOut = 67
cmiDistance = 69
cmiWavelength3 = 90
cmiWavelength4 = 91
cmiWavelength5 = 92
cmiWavelength6 = 93
cmiWavelength7 = 94
cmiWavelength8 = 95
cmiVersion0 = cmiVersion
cmiVersion1 = 96
cmiDLLAttach = 121
cmiSwitcherSignal = 123
cmiSwitcherMode = 124
cmiExposureValue11 = cmiExposureValue1
cmiExposureValue12 = 125
cmiExposureValue13 = 126
cmiExposureValue14 = 127
cmiExposureValue15 = 128
cmiExposureValue16 = 129
cmiExposureValue17 = 130
cmiExposureValue18 = 131
cmiExposureValue21 = cmiExposureValue2
cmiExposureValue22 = 132
cmiExposureValue23 = 133
cmiExposureValue24 = 134
cmiExposureValue25 = 135
cmiExposureValue26 = 136
cmiExposureValue27 = 137
cmiExposureValue28 = 138
cmiPatternAverage = 139
cmiPatternAvg1 = 140
cmiPatternAvg2 = 141
cmiAnalogOut1 = cmiAnalogOut
cmiAnalogOut2 = 142
cmiMin11 = cmiMin1
cmiMin12 = 146
cmiMin13 = 147
cmiMin14 = 148
cmiMin15 = 149
cmiMin16 = 150
cmiMin17 = 151
cmiMin18 = 152
cmiMin21 = cmiMin2
cmiMin22 = 153
cmiMin23 = 154
cmiMin24 = 155
cmiMin25 = 156
cmiMin26 = 157
cmiMin27 = 158
cmiMin28 = 159
cmiMax11 = cmiMax1
cmiMax12 = 160
cmiMax13 = 161
cmiMax14 = 162
cmiMax15 = 163
cmiMax16 = 164
cmiMax17 = 165
cmiMax18 = 166
cmiMax21 = cmiMax2
cmiMax22 = 167
cmiMax23 = 168
cmiMax24 = 169
cmiMax25 = 170
cmiMax26 = 171
cmiMax27 = 172
cmiMax28 = 173
cmiAvg11 = cmiPatternAvg1
cmiAvg12 = 174
cmiAvg13 = 175
cmiAvg14 = 176
cmiAvg15 = 177
cmiAvg16 = 178
cmiAvg17 = 179
cmiAvg18 = 180
cmiAvg21 = cmiPatternAvg2
cmiAvg22 = 181
cmiAvg23 = 182
cmiAvg24 = 183
cmiAvg25 = 184
cmiAvg26 = 185
cmiAvg27 = 186
cmiAvg28 = 187
cmiPatternAnalysisWritten = 202
cmiSwitcherChannel = 203
cmiAnalogOut3 = 237
cmiAnalogOut4 = 238
cmiAnalogOut5 = 239
cmiAnalogOut6 = 240
cmiAnalogOut7 = 241
cmiAnalogOut8 = 242
cmiIntensity = 251
cmiPower = 267
cmiActiveChannel = 300
cmiPIDCourse = 1030
cmiPIDUseTa = 1031
cmiPIDUseT = cmiPIDUseTa
cmiPID_T = 1033
cmiPID_P = 1034
cmiPID_I = 1035
cmiPID_D = 1036
cmiDeviationSensitivityDim = 1040
cmiDeviationSensitivityFactor = 1037
cmiDeviationPolarity = 1038
cmiDeviationSensitivityEx = 1039
cmiDeviationUnit = 1041
cmiPIDConstdt = 1059
cmiPID_dt = 1060
cmiPID_AutoClearHistory = 1061
cmiDeviationChannel = 1063
cmiAutoCalPeriod = 1120
cmiAutoCalUnit = 1121
cmiServerInitialized = 1124
cmiWavelength9 = 1130
cmiExposureValue19 = 1155
cmiExposureValue29 = 1180
cmiMin19 = 1205
cmiMin29 = 1230
cmiMax19 = 1255
cmiMax29 = 1280
cmiAvg19 = 1305
cmiAvg29 = 1330
cmiWavelength10 = 1355
cmiWavelength11 = 1356
cmiWavelength12 = 1357
cmiWavelength13 = 1358
cmiWavelength14 = 1359
cmiWavelength15 = 1360
cmiWavelength16 = 1361
cmiWavelength17 = 1362
cmiExternalInput = 1400
cmiPressure = 1465
cmiBackground = 1475
cmiDistanceMode = 1476
cmiInterval = 1477
cmiIntervalMode = 1478
cmiCalibrationEffect = 1480
cmiLinewidth1 = cmiLinewidth
cmiLinewidth2 = 1481
cmiLinewidth3 = 1482
cmiLinewidth4 = 1483
cmiLinewidth5 = 1484
cmiLinewidth6 = 1485
cmiLinewidth7 = 1486
cmiLinewidth8 = 1487
cmiLinewidth9 = 1488
cmiLinewidth10 = 1489
cmiLinewidth11 = 1490
cmiLinewidth12 = 1491
cmiLinewidth13 = 1492
cmiLinewidth14 = 1493
cmiLinewidth15 = 1494
cmiLinewidth16 = 1495
cmiLinewidth17 = 1496

cmi = {
    "ResultMode": cmiResultMode,
    "Range": cmiRange,
    "Pulse": cmiPulse,
    "PulseMode": cmiPulseMode,
    "WideLine": cmiWideLine,
    "WideMode": cmiWideMode,
    "Fast": cmiFast,
    "FastMode": cmiFastMode,
    "ExposureMode": cmiExposureMode,
    "ExposureValue1": cmiExposureValue1,
    "ExposureValue2": cmiExposureValue2,
    "Delay": cmiDelay,
    "Shift": cmiShift,
    "Shift2": cmiShift2,
    "Reduce": cmiReduce,
    "Reduced": cmiReduced,
    "Scale": cmiScale,
    "Temperature": cmiTemperature,
    "Link": cmiLink,
    "Operation": cmiOperation,
    "DisplayMode": cmiDisplayMode,
    "Pattern1a": cmiPattern1a,
    "Pattern1b": cmiPattern1b,
    "Pattern2a": cmiPattern2a,
    "Pattern2b": cmiPattern2b,
    "Min1": cmiMin1,
    "Max1": cmiMax1,
    "Min2": cmiMin2,
    "Max2": cmiMax2,
    "NowTick": cmiNowTick,
    "Callback": cmiCallback,
    "Frequency1": cmiFrequency1,
    "Frequency2": cmiFrequency2,
    "DLLDetach": cmiDLLDetach,
    "Version": cmiVersion,
    "AnalysisMode": cmiAnalysisMode,
    "DeviationMode": cmiDeviationMode,
    "DeviationReference": cmiDeviationReference,
    "DeviationSensitivity": cmiDeviationSensitivity,
    "Appearance": cmiAppearance,
    "AutoCalMode": cmiAutoCalMode,
    "Wavelength1": cmiWavelength1,
    "Wavelength2": cmiWavelength2,
    "Linewidth": cmiLinewidth,
    "LinewidthMode": cmiLinewidthMode,
    "LinkDlg": cmiLinkDlg,
    "Analysis": cmiAnalysis,
    "AnalogIn": cmiAnalogIn,
    "AnalogOut": cmiAnalogOut,
    "Distance": cmiDistance,
    "Wavelength3": cmiWavelength3,
    "Wavelength4": cmiWavelength4,
    "Wavelength5": cmiWavelength5,
    "Wavelength6": cmiWavelength6,
    "Wavelength7": cmiWavelength7,
    "Wavelength8": cmiWavelength8,
    "Version0": cmiVersion0,
    "Version1": cmiVersion1,
    "DLLAttach": cmiDLLAttach,
    "SwitcherSignal": cmiSwitcherSignal,
    "SwitcherMode": cmiSwitcherMode,
    "ExposureValue11": cmiExposureValue11,
    "ExposureValue12": cmiExposureValue12,
    "ExposureValue13": cmiExposureValue13,
    "ExposureValue14": cmiExposureValue14,
    "ExposureValue15": cmiExposureValue15,
    "ExposureValue16": cmiExposureValue16,
    "ExposureValue17": cmiExposureValue17,
    "ExposureValue18": cmiExposureValue18,
    "ExposureValue21": cmiExposureValue21,
    "ExposureValue22": cmiExposureValue22,
    "ExposureValue23": cmiExposureValue23,
    "ExposureValue24": cmiExposureValue24,
    "ExposureValue25": cmiExposureValue25,
    "ExposureValue26": cmiExposureValue26,
    "ExposureValue27": cmiExposureValue27,
    "ExposureValue28": cmiExposureValue28,
    "PatternAverage": cmiPatternAverage,
    "PatternAvg1": cmiPatternAvg1,
    "PatternAvg2": cmiPatternAvg2,
    "AnalogOut1": cmiAnalogOut1,
    "AnalogOut2": cmiAnalogOut2,
    "Min11": cmiMin11,
    "Min12": cmiMin12,
    "Min13": cmiMin13,
    "Min14": cmiMin14,
    "Min15": cmiMin15,
    "Min16": cmiMin16,
    "Min17": cmiMin17,
    "Min18": cmiMin18,
    "Min21": cmiMin21,
    "Min22": cmiMin22,
    "Min23": cmiMin23,
    "Min24": cmiMin24,
    "Min25": cmiMin25,
    "Min26": cmiMin26,
    "Min27": cmiMin27,
    "Min28": cmiMin28,
    "Max11": cmiMax11,
    "Max12": cmiMax12,
    "Max13": cmiMax13,
    "Max14": cmiMax14,
    "Max15": cmiMax15,
    "Max16": cmiMax16,
    "Max17": cmiMax17,
    "Max18": cmiMax18,
    "Max21": cmiMax21,
    "Max22": cmiMax22,
    "Max23": cmiMax23,
    "Max24": cmiMax24,
    "Max25": cmiMax25,
    "Max26": cmiMax26,
    "Max27": cmiMax27,
    "Max28": cmiMax28,
    "Avg11": cmiAvg11,
    "Avg12": cmiAvg12,
    "Avg13": cmiAvg13,
    "Avg14": cmiAvg14,
    "Avg15": cmiAvg15,
    "Avg16": cmiAvg16,
    "Avg17": cmiAvg17,
    "Avg18": cmiAvg18,
    "Avg21": cmiAvg21,
    "Avg22": cmiAvg22,
    "Avg23": cmiAvg23,
    "Avg24": cmiAvg24,
    "Avg25": cmiAvg25,
    "Avg26": cmiAvg26,
    "Avg27": cmiAvg27,
    "Avg28": cmiAvg28,
    "PatternAnalysisWritten": cmiPatternAnalysisWritten,
    "SwitcherChannel": cmiSwitcherChannel,
    "AnalogOut3": cmiAnalogOut3,
    "AnalogOut4": cmiAnalogOut4,
    "AnalogOut5": cmiAnalogOut5,
    "AnalogOut6": cmiAnalogOut6,
    "AnalogOut7": cmiAnalogOut7,
    "AnalogOut8": cmiAnalogOut8,
    "Intensity": cmiIntensity,
    "Power": cmiPower,
    "ActiveChannel": cmiActiveChannel,
    "PIDCourse": cmiPIDCourse,
    "PIDUseTa": cmiPIDUseTa,
    "PIDUseT": cmiPIDUseT,
    "PID_T": cmiPID_T,
    "PID_P": cmiPID_P,
    "PID_I": cmiPID_I,
    "PID_D": cmiPID_D,
    "DeviationSensitivityDim": cmiDeviationSensitivityDim,
    "DeviationSensitivityFactor": cmiDeviationSensitivityFactor,
    "DeviationPolarity": cmiDeviationPolarity,
    "DeviationSensitivityEx": cmiDeviationSensitivityEx,
    "DeviationUnit": cmiDeviationUnit,
    "PIDConstdt": cmiPIDConstdt,
    "PID_dt": cmiPID_dt,
    "PID_AutoClearHistory": cmiPID_AutoClearHistory,
    "DeviationChannel": cmiDeviationChannel,
    "AutoCalPeriod": cmiAutoCalPeriod,
    "AutoCalUnit": cmiAutoCalUnit,
    "ServerInitialized": cmiServerInitialized,
    "Wavelength9": cmiWavelength9,
    "ExposureValue19": cmiExposureValue19,
    "ExposureValue29": cmiExposureValue29,
    "Min19": cmiMin19,
    "Min29": cmiMin29,
    "Max19": cmiMax19,
    "Max29": cmiMax29,
    "Avg19": cmiAvg19,
    "Avg29": cmiAvg29,
    "Wavelength10": cmiWavelength10,
    "Wavelength11": cmiWavelength11,
    "Wavelength12": cmiWavelength12,
    "Wavelength13": cmiWavelength13,
    "Wavelength14": cmiWavelength14,
    "Wavelength15": cmiWavelength15,
    "Wavelength16": cmiWavelength16,
    "Wavelength17": cmiWavelength17,
    "ExternalInput": cmiExternalInput,
    "Pressure": cmiPressure,
    "Background": cmiBackground,
    "DistanceMode": cmiDistanceMode,
    "Interval": cmiInterval,
    "IntervalMode": cmiIntervalMode,
    "CalibrationEffect": cmiCalibrationEffect,
    "Linewidth1": cmiLinewidth1,
    "Linewidth2": cmiLinewidth2,
    "Linewidth3": cmiLinewidth3,
    "Linewidth4": cmiLinewidth4,
    "Linewidth5": cmiLinewidth5,
    "Linewidth6": cmiLinewidth6,
    "Linewidth7": cmiLinewidth7,
    "Linewidth8": cmiLinewidth8,
    "Linewidth9": cmiLinewidth9,
    "Linewidth10": cmiLinewidth10,
    "Linewidth11": cmiLinewidth11,
    "Linewidth12": cmiLinewidth12,
    "Linewidth13": cmiLinewidth13,
    "Linewidth14": cmiLinewidth14,
    "Linewidth15": cmiLinewidth15,
    "Linewidth16": cmiLinewidth16,
    "Linewidth17": cmiLinewidth17,
}

cmi_rev = {}
for k, v in cmi.items():
    cmi_rev.setdefault(v, []).append(k)


# WLM Control Mode Constants
cCtrlWLMShow = 1
cCtrlWLMHide = 2
cCtrlWLMExit = 3
cCtrlWLMWait = 0x0010
cCtrlWLMStartSilent = 0x0020
cCtrlWLMSilent = 0x0040

# Operation Mode Constants (for "Operation" and "GetOperationState" functions
cStop = 0
cAdjustment = 1
cMeasurement = 2

# Base Operation Constants (To be used exclusively,
# only one of this list at a time,
# but still can be combined with "Measurement Action Addition Constants".
# See below.
cCtrlStopAll = cStop
cCtrlStartAdjustment = cAdjustment
cCtrlStartMeasurement = cMeasurement
cCtrlStartRecord = 0x0004
cCtrlStartReplay = 0x0008
cCtrlStoreArray = 0x0010
cCtrlLoadArray = 0x0020

# Additional Operation Flag Constants
# (combine with "Base Operation Constants" above.
cCtrlDontOverwrite = 0x0000
cCtrlOverwrite = 0x1000  # don't combine with cCtrlFileDialog
cCtrlFileGiven = 0x0000
cCtrlFileDialog = 0x2000  # don't combine with
# cCtrlOverwrite and cCtrlFileASCII
cCtrlFileBinary = 0x0000  # .smr, .ltr
cCtrlFileASCII = 0x4000  # .smx, .ltx, don't combine with
# cCtrlFileDialog

# Measurement Control Mode Constants
cCtrlMeasDelayRemove = 0
cCtrlMeasDelayGenerally = 1
cCtrlMeasDelayOnce = 2
cCtrlMeasDelayDenyUntil = 3
cCtrlMeasDelayIdleOnce = 4
cCtrlMeasDelayIdleEach = 5
cCtrlMeasDelayDefault = 6

# Measurement Triggering Action Constants
cCtrlMeasurementContinue = 0
cCtrlMeasurementInterrupt = 1
cCtrlMeasurementTriggerPoll = 2
cCtrlMeasurementTriggerSuccess = 3

# ExposureRange Constants
cExpoMin = 0
cExpoMax = 1
cExpo2Min = 2
cExpo2Max = 3

# Amplitude Constants
cMin1 = 0
cMin2 = 1
cMax1 = 2
cMax2 = 3
cAvg1 = 4
cAvg2 = 5

# Measurement Range Constants
cRange_250_410 = 4
cRange_250_425 = 0
cRange_300_410 = 3
cRange_350_500 = 5
cRange_400_725 = 1
cRange_700_1100 = 2
cRange_800_1300 = 6
cRange_900_1500 = cRange_800_1300
cRange_1100_1700 = 7
cRange_1100_1800 = cRange_1100_1700

# Unit Constants for Get-/SetResultMode, GetLinewidth,
# Convert... and Calibration
cReturnWavelengthVac = 0
cReturnWavelengthAir = 1
cReturnFrequency = 2
cReturnWavenumber = 3
cReturnPhotonEnergy = 4

# Power Unit Constants
cPower_muW = 0
cPower_dBm = 1

# Source Type Constants for Calibration
cHeNe633 = 0
cHeNe1152 = 0
cNeL = 1
cOther = 2
cFreeHeNe = 3

# Unit Constants for Autocalibration
cACOnceOnStart = 0
cACMeasurements = 1
cACDays = 2
cACHours = 3
cACMinutes = 4

# Pattern- and Analysis Constants
cPatternDisable = 0
cPatternEnable = 1
cAnalysisDisable = cPatternDisable
cAnalysisEnable = cPatternEnable

cSignal1Interferometers = 0
cSignal1WideInterferometer = 1
cSignal1Grating = 1
cSignal2Interferometers = 2
cSignal2WideInterferometer = 3
cSignalAnalysis = 4
cSignalAnalysisX = cSignalAnalysis
cSignalAnalysisY = cSignalAnalysis + 1

# Return errorvalues of GetFrequency, GetWavelength and GetWLMVersion
ErrNoValue = 0
ErrNoSignal = -1
ErrBadSignal = -2
ErrLowSignal = -3
ErrBigSignal = -4
ErrWlmMissing = -5
ErrNotAvailable = -6
InfNothingChanged = -7
ErrNoPulse = -8
ErrDiv0 = -13
ErrOutOfRange = -14
ErrUnitNotAvailable = -15
ErrMaxErr = ErrUnitNotAvailable

# Return errorvalues of GetTemperature and GetPressure
ErrTemperature = -1000
ErrTempNotMeasured = ErrTemperature + ErrNoValue
ErrTempNotAvailable = ErrTemperature + ErrNotAvailable
ErrTempWlmMissing = ErrTemperature + ErrWlmMissing

# Return errorvalues of GetDistance
# real errorvalues are ErrDistance combined with those of GetWavelength
ErrDistance = -1000000000
ErrDistanceNotAvailable = ErrDistance + ErrNotAvailable
ErrDistanceWlmMissing = ErrDistance + ErrWlmMissing

# Return flags of ControlWLMEx in combination with Show or Hide,
# Wait and Res = 1
flServerStarted = 0x0001
flErrDeviceNotFound = 0x0002
flErrDriverError = 0x0004
flErrUSBError = 0x0008
flErrUnknownDeviceError = 0x0010
flErrWrongSN = 0x0020
flErrUnknownSN = 0x0040
flErrTemperatureError = 0x0080
flErrPressureError = 0x0100
flErrCancelledManually = 0x0200
flErrUnknownError = 0x1000

# Return file info flags of SetOperationFile
flFileInfoDoesntExist = 0x0000
flFileInfoExists = 0x0001
flFileInfoCantWrite = 0x0002
flFileInfoCantRead = 0x0004
flFileInfoInvalidName = 0x0008
cFileParameterError = -1
