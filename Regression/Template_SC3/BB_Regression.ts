//1. 通过Python获取所有DCS的缩写

//*********************************Part4: Parameter Define/Initilize*************************************************

var G_Loop_Fault = {'CrossC': '500', 'STB': '500', 'GND': '500', 'HighRes': '500', 'LowRes': '500', 'Open': '500', 'CFG': '500'};
var G_SupportLoop = ['DrSideAB', 'DrFrontAB', 'PaSideAB', 'PaFrontAB', 'DrPT1', 'DrCurtainAB', 'PaCurtainAB', 'PaPT1', 'RearDrPT', 'RearPaPT', 'DrKnee', 'DrPT2'];
var G_CrossCLoop = ['DrSideAB', 'DrFrontAB', 'PaSideAB', 'PaFrontAB', 'DrPT1', 'DrCurtainAB', 'PaCurtainAB', 'PaPT1', 'RearDrPT', 'RearPaPT', 'DrKnee', 'DrPT2'];
var G_NSCrossCLoop = [];
var G_RSU_Fault = {'Open': '100', 'STB': '100', 'STG': '100'};
var G_SupportRSU = ['SRSU_L', 'PRSU_R', 'SRSU_R', 'PRSU_L', 'FRSU_L', 'FRSU_R'];
var G_DCS_Fault = {'CrossC': '100', 'STB': '100', 'GND': '100', 'Open': '100', 'TooHigh': '100', 'TooLow': '100', 'BadSensor': '100', 'CFG': 'undefined'};
var G_SupportDCS = ['BB2L', 'BB2M', 'BB1L', 'BB2R', 'BB1R', 'BB3L', 'BB3R'];
var G_CrossCDCS = ['BB2M', 'BB1L', 'BB2R', 'BB1R', 'BB3L', 'BB3R'];
var G_NSCrossCDCS = ['BB2L'];
var DrSideAB = {
    "ARiA_HW_Name": "LOOP1",
    "FaultIndex": "00",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_00_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_00_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_00_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_00_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_00_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_00_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_00_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var DrFrontAB = {
    "ARiA_HW_Name": "LOOP2",
    "FaultIndex": "01",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_01_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_01_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_01_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_01_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_01_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_01_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_01_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var PaSideAB = {
    "ARiA_HW_Name": "LOOP3",
    "FaultIndex": "02",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_02_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_02_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_02_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_02_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_02_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_02_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_02_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var PaFrontAB = {
    "ARiA_HW_Name": "LOOP4",
    "FaultIndex": "03",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_03_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_03_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_03_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_03_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_03_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_03_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_03_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var DrPT1 = {
    "ARiA_HW_Name": "LOOP5",
    "FaultIndex": "04",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_04_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_04_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_04_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_04_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_04_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_04_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_04_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var DrCurtainAB = {
    "ARiA_HW_Name": "LOOP6",
    "FaultIndex": "05",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_05_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_05_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_05_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_05_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_05_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_05_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_05_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var PaCurtainAB = {
    "ARiA_HW_Name": "LOOP7",
    "FaultIndex": "06",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_06_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_06_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_06_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_06_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_06_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_06_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_06_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var PaPT1 = {
    "ARiA_HW_Name": "LOOP8",
    "FaultIndex": "07",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_07_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_07_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_07_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_07_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_07_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_07_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_07_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var RearDrPT = {
    "ARiA_HW_Name": "LOOP9",
    "FaultIndex": "08",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_08_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_08_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_08_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_08_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_08_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_08_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_08_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var RearPaPT = {
    "ARiA_HW_Name": "LOOP10",
    "FaultIndex": "09",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_09_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_09_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_09_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_09_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_09_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_09_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_09_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var DrKnee = {
    "ARiA_HW_Name": "LOOP11",
    "FaultIndex": "10",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_10_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_10_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_10_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_10_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_10_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_10_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_10_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var DrPT2 = {
    "ARiA_HW_Name": "LOOP12",
    "FaultIndex": "11",
    "Normal": "INHERENT",
    "CrossC": "CROSS_CONNECTED",
    "STB": "BUSS_HI_ON",
    "GND": "BUSS_Lo_ON",
    "HighRes": "HRES_FAULT",
    "LowRes": "LRES_FAULT",
    "Open": "OPEN",
    "CFG": "NotConfig",
    "CrossCDTC": "LOOPSMGR_F_LOP_CROSS_CONNECT_11_0_define",
    "CrossCQualify": [
        "2000",
        "3000"
    ],
    "CrossCDisQualify": [
        "500",
        "1000"
    ],
    "STBDTC": "LOOPSMGR_F_LOP_SHT_TO_PLUS_11_0_define",
    "STBQualify": [
        "2000",
        "3000"
    ],
    "STBDisQualify": [
        "500",
        "1000"
    ],
    "GNDDTC": "LOOPSMGR_F_LOP_SHT_TO_GND_11_0_define",
    "GNDQualify": [
        "2000",
        "3000"
    ],
    "GNDDisQualify": [
        "500",
        "1000"
    ],
    "HighResDTC": "LOOPSMGR_F_LOP_HIGH_RES_11_0_define",
    "HighResQualify": [
        "2000",
        "3000"
    ],
    "HighResDisQualify": [
        "500",
        "1000"
    ],
    "LowResDTC": "LOOPSMGR_F_LOP_LOW_RES_11_0_define",
    "LowResQualify": [
        "2000",
        "3000"
    ],
    "LowResDisQualify": [
        "500",
        "1000"
    ],
    "OpenDTC": "LOOPSMGR_F_LOP_OPEN_11_0_define",
    "OpenQualify": [
        "2000",
        "3000"
    ],
    "OpenDisQualify": [
        "500",
        "1000"
    ],
    "CFGDTC": "LOOPSMGR_F_LOP_UNEXPECTED_SQUIB_11_0_define",
    "CFGQualify": [
        "2000",
        "3000"
    ],
    "CFGDisQualify": [
        "OPEN"
    ]
};
var SRSU_L = {
    "ARiA_HW_Name": "1",
    "FaultIndex": "0",
    "Normal": "INHERENT",
    "Open": "Open",
    "STB": "STB",
    "STG": "STG",
    "OpenDTC": "RSUMGR_F_RSU_SAT_OPEN_0_0_define",
    "OpenQualify": [
        "560",
        "1000"
    ],
    "OpenDisQualify": [
        "560",
        "1000"
    ],
    "STBDTC": "RSUMGR_F_RSU_SAT_SHT_BAT_0_0_define,RSUMGR_F_RSU_SAT_SHT_BAT_2_0_define",
    "STBQualify": [
        "560",
        "1000"
    ],
    "STBDisQualify": [
        "560",
        "1000"
    ],
    "STGDTC": "RSUMGR_F_RSU_SAT_SHT_GND_0_0_define,RSUMGR_F_RSU_SAT_SHT_GND_2_0_define",
    "STGQualify": [
        "560",
        "1000"
    ],
    "STGDisQualify": [
        "560",
        "1000"
    ]
};
var PRSU_R = {
    "ARiA_HW_Name": "2",
    "FaultIndex": "2",
    "Normal": "INHERENT",
    "Open": "Open",
    "STB": "STB",
    "STG": "STG",
    "OpenDTC": "RSUMGR_F_RSU_SAT_OPEN_2_0_define",
    "OpenQualify": [
        "560",
        "1000"
    ],
    "OpenDisQualify": [
        "560",
        "1000"
    ],
    "STBDTC": "RSUMGR_F_RSU_SAT_SHT_BAT_0_0_define,RSUMGR_F_RSU_SAT_SHT_BAT_2_0_define",
    "STBQualify": [
        "560",
        "1000"
    ],
    "STBDisQualify": [
        "560",
        "1000"
    ],
    "STGDTC": "RSUMGR_F_RSU_SAT_SHT_GND_0_0_define,RSUMGR_F_RSU_SAT_SHT_GND_2_0_define",
    "STGQualify": [
        "560",
        "1000"
    ],
    "STGDisQualify": [
        "560",
        "1000"
    ]
};
var SRSU_R = {
    "ARiA_HW_Name": "3",
    "FaultIndex": "3",
    "Normal": "INHERENT",
    "Open": "Open",
    "STB": "STB",
    "STG": "STG",
    "OpenDTC": "RSUMGR_F_RSU_SAT_OPEN_3_0_define",
    "OpenQualify": [
        "560",
        "1000"
    ],
    "OpenDisQualify": [
        "560",
        "1000"
    ],
    "STBDTC": "RSUMGR_F_RSU_SAT_SHT_BAT_3_0_define,RSUMGR_F_RSU_SAT_SHT_BAT_5_0_define",
    "STBQualify": [
        "560",
        "1000"
    ],
    "STBDisQualify": [
        "560",
        "1000"
    ],
    "STGDTC": "RSUMGR_F_RSU_SAT_SHT_GND_3_0_define,RSUMGR_F_RSU_SAT_SHT_GND_5_0_define",
    "STGQualify": [
        "560",
        "1000"
    ],
    "STGDisQualify": [
        "560",
        "1000"
    ]
};
var PRSU_L = {
    "ARiA_HW_Name": "4",
    "FaultIndex": "5",
    "Normal": "INHERENT",
    "Open": "Open",
    "STB": "STB",
    "STG": "STG",
    "OpenDTC": "RSUMGR_F_RSU_SAT_OPEN_5_0_define",
    "OpenQualify": [
        "560",
        "1000"
    ],
    "OpenDisQualify": [
        "560",
        "1000"
    ],
    "STBDTC": "RSUMGR_F_RSU_SAT_SHT_BAT_3_0_define,RSUMGR_F_RSU_SAT_SHT_BAT_5_0_define",
    "STBQualify": [
        "560",
        "1000"
    ],
    "STBDisQualify": [
        "560",
        "1000"
    ],
    "STGDTC": "RSUMGR_F_RSU_SAT_SHT_GND_3_0_define,RSUMGR_F_RSU_SAT_SHT_GND_5_0_define",
    "STGQualify": [
        "560",
        "1000"
    ],
    "STGDisQualify": [
        "560",
        "1000"
    ]
};
var FRSU_L = {
    "ARiA_HW_Name": "5",
    "FaultIndex": "8",
    "Normal": "INHERENT",
    "Open": "Open",
    "STB": "STB",
    "STG": "STG",
    "OpenDTC": "RSUMGR_F_RSU_SAT_OPEN_8_0_define",
    "OpenQualify": [
        "560",
        "1000"
    ],
    "OpenDisQualify": [
        "560",
        "1000"
    ],
    "STBDTC": "RSUMGR_F_RSU_SAT_SHT_BAT_8_0_define",
    "STBQualify": [
        "560",
        "1000"
    ],
    "STBDisQualify": [
        "560",
        "1000"
    ],
    "STGDTC": "RSUMGR_F_RSU_SAT_SHT_GND_8_0_define",
    "STGQualify": [
        "560",
        "1000"
    ],
    "STGDisQualify": [
        "560",
        "1000"
    ]
};
var FRSU_R = {
    "ARiA_HW_Name": "6",
    "FaultIndex": "11",
    "Normal": "INHERENT",
    "Open": "Open",
    "STB": "STB",
    "STG": "STG",
    "OpenDTC": "RSUMGR_F_RSU_SAT_OPEN_11_0_define",
    "OpenQualify": [
        "560",
        "1000"
    ],
    "OpenDisQualify": [
        "560",
        "1000"
    ],
    "STBDTC": "RSUMGR_F_RSU_SAT_SHT_BAT_11_0_define",
    "STBQualify": [
        "560",
        "1000"
    ],
    "STBDisQualify": [
        "560",
        "1000"
    ],
    "STGDTC": "RSUMGR_F_RSU_SAT_SHT_GND_11_0_define",
    "STGQualify": [
        "560",
        "1000"
    ],
    "STGDisQualify": [
        "560",
        "1000"
    ]
};
var BB2L = {
    "ARiA_HW_Name": "SW_Channel_DCS_0",
    "FaultIndex": 0,
    "Normal": "200R",
    "Buckled": "400R",
    "UnBuckled": "100R",
    "CrossC": "undefined",
    "STB": "STB",
    "GND": "undefined",
    "Open": "undefined",
    "TooHigh": "undefined",
    "TooLow": "undefined",
    "BadSensor": "undefined",
    "CFG": "undefined",
    "StatusDID": "FDC3",
    "StatusDID_RespLength": "5",
    "StatusDID_Start": 7,
    "StatusDID_End": 8,
    "DIDExpectBuckled": "0",
    "DIDExpectUnBuckled": "1",
    "StatusMessage": "ACU_SRS_2",
    "StatusSignal": "SRS_Row2LeftSeatBeltSt",
    "MsgExpectBuckled": "0x00",
    "MsgExpectUnBuckled": "0x01",
    "CrossCDTC": "SB1DCSDRVR_F_DCS_CROSS_CONNECT_0_0_define",
    "CrossCQualify": [
        "3200",
        "3600"
    ],
    "CrossCDisQualify": [
        "3200",
        "3600"
    ],
    "STBDTC": "SB1DCSDRVR_F_DCS_SHT_PLUS_0_0_define",
    "STBQualify": [
        "3200",
        "3600"
    ],
    "STBDisQualify": [
        "3200",
        "3600"
    ],
    "GNDDTC": "SB1DCSDRVR_F_DCS_SHT_GND_0_0_define",
    "GNDQualify": [
        "3200",
        "3600"
    ],
    "GNDDisQualify": [
        "3200",
        "3600"
    ],
    "TooHighDTC": "SB1DCSDRVR_F_DCS_TOO_HIGH_0_0_define",
    "TooHighQualify": [
        "3200",
        "3600"
    ],
    "TooHighDisQualify": [
        "3200",
        "3600"
    ],
    "TooLowDTC": "SB1DCSDRVR_F_DCS_TOO_LOW_0_0_define",
    "TooLowQualify": [
        "3200",
        "3600"
    ],
    "TooLowDisQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDTC": "SB1DCSDRVR_F_DCS_BAD_SENSOR_0_0_define",
    "BadSensorQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDisQualify": [
        "3200",
        "3600"
    ],
    "OpenDTC": "SB1DCSDRVR_F_DCS_OPEN_0_0_define",
    "OpenQualify": [
        "3200",
        "3600"
    ],
    "OpenDisQualify": [
        "3200",
        "3600"
    ],
    "CFGDTC": "SB1DCSDRVR_F_DCS_CFG_0_0_define",
    "CFGQualify": [
        "3200",
        "3600"
    ],
    "CFGDisQualify": [
        "3200",
        "3600"
    ],
    "Status": [
        "Buckled",
        "UnBuckled"
    ]
};
var BB2M = {
    "ARiA_HW_Name": "SW_Channel_DCS_1",
    "FaultIndex": 1,
    "Normal": "200R",
    "Buckled": "400R",
    "UnBuckled": "100R",
    "CrossC": "CROSS_CONNECTED",
    "STB": "STB",
    "GND": "undefined",
    "Open": "undefined",
    "TooHigh": "undefined",
    "TooLow": "undefined",
    "BadSensor": "undefined",
    "CFG": "undefined",
    "StatusDID": "FDC4",
    "StatusDID_RespLength": "5",
    "StatusDID_Start": 7,
    "StatusDID_End": 8,
    "DIDExpectBuckled": "0",
    "DIDExpectUnBuckled": "1",
    "StatusMessage": "ACU_SRS_2",
    "StatusSignal": "SRS_Row2MiddleSeatBeltSt",
    "MsgExpectBuckled": "0x00",
    "MsgExpectUnBuckled": "0x01",
    "CrossCDTC": "SB1DCSDRVR_F_DCS_CROSS_CONNECT_1_0_define",
    "CrossCQualify": [
        "3200",
        "3600"
    ],
    "CrossCDisQualify": [
        "3200",
        "3600"
    ],
    "STBDTC": "SB1DCSDRVR_F_DCS_SHT_PLUS_1_0_define",
    "STBQualify": [
        "3200",
        "3600"
    ],
    "STBDisQualify": [
        "3200",
        "3600"
    ],
    "GNDDTC": "SB1DCSDRVR_F_DCS_SHT_GND_1_0_define",
    "GNDQualify": [
        "3200",
        "3600"
    ],
    "GNDDisQualify": [
        "3200",
        "3600"
    ],
    "TooHighDTC": "SB1DCSDRVR_F_DCS_TOO_HIGH_1_0_define",
    "TooHighQualify": [
        "3200",
        "3600"
    ],
    "TooHighDisQualify": [
        "3200",
        "3600"
    ],
    "TooLowDTC": "SB1DCSDRVR_F_DCS_TOO_LOW_1_0_define",
    "TooLowQualify": [
        "3200",
        "3600"
    ],
    "TooLowDisQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDTC": "SB1DCSDRVR_F_DCS_BAD_SENSOR_1_0_define",
    "BadSensorQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDisQualify": [
        "3200",
        "3600"
    ],
    "OpenDTC": "SB1DCSDRVR_F_DCS_OPEN_1_0_define",
    "OpenQualify": [
        "3200",
        "3600"
    ],
    "OpenDisQualify": [
        "3200",
        "3600"
    ],
    "CFGDTC": "SB1DCSDRVR_F_DCS_CFG_1_0_define",
    "CFGQualify": [
        "3200",
        "3600"
    ],
    "CFGDisQualify": [
        "3200",
        "3600"
    ],
    "Status": [
        "Buckled",
        "UnBuckled"
    ]
};
var BB1L = {
    "ARiA_HW_Name": "SW_Channel_DCS_2",
    "FaultIndex": 2,
    "Normal": "200R",
    "Buckled": "400R",
    "UnBuckled": "100R",
    "CrossC": "CROSS_CONNECTED",
    "STB": "STB",
    "GND": "undefined",
    "Open": "undefined",
    "TooHigh": "undefined",
    "TooLow": "undefined",
    "BadSensor": "undefined",
    "CFG": "undefined",
    "StatusDID": "FDC0",
    "StatusDID_RespLength": "5",
    "StatusDID_Start": 7,
    "StatusDID_End": 8,
    "DIDExpectBuckled": "0",
    "DIDExpectUnBuckled": "1",
    "StatusMessage": "ACU_SRS_2",
    "StatusSignal": "SRS_DriverSeatBeltSt",
    "MsgExpectBuckled": "0x00",
    "MsgExpectUnBuckled": "0x01",
    "CrossCDTC": "SB1DCSDRVR_F_DCS_CROSS_CONNECT_2_0_define",
    "CrossCQualify": [
        "3200",
        "3600"
    ],
    "CrossCDisQualify": [
        "3200",
        "3600"
    ],
    "STBDTC": "SB1DCSDRVR_F_DCS_SHT_PLUS_2_0_define",
    "STBQualify": [
        "3200",
        "3600"
    ],
    "STBDisQualify": [
        "3200",
        "3600"
    ],
    "GNDDTC": "SB1DCSDRVR_F_DCS_SHT_GND_2_0_define",
    "GNDQualify": [
        "3200",
        "3600"
    ],
    "GNDDisQualify": [
        "3200",
        "3600"
    ],
    "TooHighDTC": "SB1DCSDRVR_F_DCS_TOO_HIGH_2_0_define",
    "TooHighQualify": [
        "3200",
        "3600"
    ],
    "TooHighDisQualify": [
        "3200",
        "3600"
    ],
    "TooLowDTC": "SB1DCSDRVR_F_DCS_TOO_LOW_2_0_define",
    "TooLowQualify": [
        "3200",
        "3600"
    ],
    "TooLowDisQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDTC": "SB1DCSDRVR_F_DCS_BAD_SENSOR_2_0_define",
    "BadSensorQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDisQualify": [
        "3200",
        "3600"
    ],
    "OpenDTC": "SB1DCSDRVR_F_DCS_OPEN_2_0_define",
    "OpenQualify": [
        "3200",
        "3600"
    ],
    "OpenDisQualify": [
        "3200",
        "3600"
    ],
    "CFGDTC": "SB1DCSDRVR_F_DCS_CFG_2_0_define",
    "CFGQualify": [
        "3200",
        "3600"
    ],
    "CFGDisQualify": [
        "3200",
        "3600"
    ],
    "Status": [
        "Buckled",
        "UnBuckled"
    ]
};
var BB2R = {
    "ARiA_HW_Name": "SW_Channel_DCS_3",
    "FaultIndex": 3,
    "Normal": "200R",
    "Buckled": "400R",
    "UnBuckled": "100R",
    "CrossC": "CROSS_CONNECTED",
    "STB": "STB",
    "GND": "undefined",
    "Open": "undefined",
    "TooHigh": "undefined",
    "TooLow": "undefined",
    "BadSensor": "undefined",
    "CFG": "undefined",
    "StatusDID": "FDC5",
    "StatusDID_RespLength": "5",
    "StatusDID_Start": 7,
    "StatusDID_End": 8,
    "DIDExpectBuckled": "0",
    "DIDExpectUnBuckled": "1",
    "StatusMessage": "ACU_SRS_2",
    "StatusSignal": "SRS_Row2RightSeatBeltSt",
    "MsgExpectBuckled": "0x00",
    "MsgExpectUnBuckled": "0x01",
    "CrossCDTC": "SB1DCSDRVR_F_DCS_CROSS_CONNECT_3_0_define",
    "CrossCQualify": [
        "3200",
        "3600"
    ],
    "CrossCDisQualify": [
        "3200",
        "3600"
    ],
    "STBDTC": "SB1DCSDRVR_F_DCS_SHT_PLUS_3_0_define",
    "STBQualify": [
        "3200",
        "3600"
    ],
    "STBDisQualify": [
        "3200",
        "3600"
    ],
    "GNDDTC": "SB1DCSDRVR_F_DCS_SHT_GND_3_0_define",
    "GNDQualify": [
        "3200",
        "3600"
    ],
    "GNDDisQualify": [
        "3200",
        "3600"
    ],
    "TooHighDTC": "SB1DCSDRVR_F_DCS_TOO_HIGH_3_0_define",
    "TooHighQualify": [
        "3200",
        "3600"
    ],
    "TooHighDisQualify": [
        "3200",
        "3600"
    ],
    "TooLowDTC": "SB1DCSDRVR_F_DCS_TOO_LOW_3_0_define",
    "TooLowQualify": [
        "3200",
        "3600"
    ],
    "TooLowDisQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDTC": "SB1DCSDRVR_F_DCS_BAD_SENSOR_3_0_define",
    "BadSensorQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDisQualify": [
        "3200",
        "3600"
    ],
    "OpenDTC": "SB1DCSDRVR_F_DCS_OPEN_3_0_define",
    "OpenQualify": [
        "3200",
        "3600"
    ],
    "OpenDisQualify": [
        "3200",
        "3600"
    ],
    "CFGDTC": "SB1DCSDRVR_F_DCS_CFG_3_0_define",
    "CFGQualify": [
        "3200",
        "3600"
    ],
    "CFGDisQualify": [
        "3200",
        "3600"
    ],
    "Status": [
        "Buckled",
        "UnBuckled"
    ]
};
var BB1R = {
    "ARiA_HW_Name": "SW_Channel_DCS_4",
    "FaultIndex": 4,
    "Normal": "200R",
    "Buckled": "400R",
    "UnBuckled": "100R",
    "CrossC": "CROSS_CONNECTED",
    "STB": "STB",
    "GND": "undefined",
    "Open": "undefined",
    "TooHigh": "undefined",
    "TooLow": "undefined",
    "BadSensor": "undefined",
    "CFG": "undefined",
    "StatusDID": "FDC1",
    "StatusDID_RespLength": "5",
    "StatusDID_Start": 7,
    "StatusDID_End": 8,
    "DIDExpectBuckled": "0",
    "DIDExpectUnBuckled": "1",
    "StatusMessage": "ACU_SRS_2",
    "StatusSignal": "SRS_PsngrSeatBeltSt",
    "MsgExpectBuckled": "0x00",
    "MsgExpectUnBuckled": "0x01",
    "CrossCDTC": "SB1DCSDRVR_F_DCS_CROSS_CONNECT_4_0_define",
    "CrossCQualify": [
        "3200"
    ],
    "CrossCDisQualify": [
        "3200"

    ],
    "STBDTC": "SB1DCSDRVR_F_DCS_SHT_PLUS_4_0_define",
    "STBQualify": [
        "3200",
        "3600"
    ],
    "STBDisQualify": [
        "3200",
        "3600"
    ],
    "GNDDTC": "SB1DCSDRVR_F_DCS_SHT_GND_4_0_define",
    "GNDQualify": [
        "3200",
        "3600"
    ],
    "GNDDisQualify": [
        "3200",
        "3600"
    ],
    "TooHighDTC": "SB1DCSDRVR_F_DCS_TOO_HIGH_4_0_define",
    "TooHighQualify": [
        "3200",
        "3600"
    ],
    "TooHighDisQualify": [
        "3200",
        "3600"
    ],
    "TooLowDTC": "SB1DCSDRVR_F_DCS_TOO_LOW_4_0_define",
    "TooLowQualify": [
        "3200",
        "3600"
    ],
    "TooLowDisQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDTC": "SB1DCSDRVR_F_DCS_BAD_SENSOR_4_0_define",
    "BadSensorQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDisQualify": [
        "3200",
        "3600"
    ],
    "OpenDTC": "SB1DCSDRVR_F_DCS_OPEN_4_0_define",
    "OpenQualify": [
        "3200",
        "3600"
    ],
    "OpenDisQualify": [
        "3200",
        "3600"
    ],
    "CFGDTC": "SB1DCSDRVR_F_DCS_CFG_4_0_define",
    "CFGQualify": [
        "3200",
        "3600"
    ],
    "CFGDisQualify": [
        "3200",
        "3600"
    ],
    "Status": [
        "Buckled",
        "UnBuckled"
    ]
};
var BB3L = {
    "ARiA_HW_Name": "SW_Channel_DCS_5",
    "FaultIndex": 5,
    "Normal": "200R",
    "Buckled": "400R",
    "UnBuckled": "100R",
    "CrossC": "CROSS_CONNECTED",
    "STB": "STB",
    "GND": "undefined",
    "Open": "undefined",
    "TooHigh": "undefined",
    "TooLow": "undefined",
    "BadSensor": "undefined",
    "CFG": "undefined",
    "StatusDID": "FDC6",
    "StatusDID_RespLength": "5",
    "StatusDID_Start": 7,
    "StatusDID_End": 8,
    "DIDExpectBuckled": "0",
    "DIDExpectUnBuckled": "1",
    "StatusMessage": "ACU_SRS_2",
    "StatusSignal": "SRS_Row3LeftSeatBeltSt",
    "MsgExpectBuckled": "0x00",
    "MsgExpectUnBuckled": "0x01",
    "CrossCDTC": "SB1DCSDRVR_F_DCS_CROSS_CONNECT_5_0_define",
    "CrossCQualify": [
        "3200",
        "3600"
    ],
    "CrossCDisQualify": [
        "3200",
        "3600"
    ],
    "STBDTC": "SB1DCSDRVR_F_DCS_SHT_PLUS_5_0_define",
    "STBQualify": [
        "3200",
        "3600"
    ],
    "STBDisQualify": [
        "3200",
        "3600"
    ],
    "GNDDTC": "SB1DCSDRVR_F_DCS_SHT_GND_5_0_define",
    "GNDQualify": [
        "3200",
        "3600"
    ],
    "GNDDisQualify": [
        "3200",
        "3600"
    ],
    "TooHighDTC": "SB1DCSDRVR_F_DCS_TOO_HIGH_5_0_define",
    "TooHighQualify": [
        "3200",
        "3600"
    ],
    "TooHighDisQualify": [
        "3200",
        "3600"
    ],
    "TooLowDTC": "SB1DCSDRVR_F_DCS_TOO_LOW_5_0_define",
    "TooLowQualify": [
        "3200",
        "3600"
    ],
    "TooLowDisQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDTC": "SB1DCSDRVR_F_DCS_BAD_SENSOR_5_0_define",
    "BadSensorQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDisQualify": [
        "3200",
        "3600"
    ],
    "OpenDTC": "SB1DCSDRVR_F_DCS_OPEN_5_0_define",
    "OpenQualify": [
        "3200",
        "3600"
    ],
    "OpenDisQualify": [
        "3200",
        "3600"
    ],
    "CFGDTC": "SB1DCSDRVR_F_DCS_CFG_5_0_define",
    "CFGQualify": [
        "3200",
        "3600"
    ],
    "CFGDisQualify": [
        "3200",
        "3600"
    ],
    "Status": [
        "Buckled",
        "UnBuckled"
    ]
};
var BB3R = {
    "ARiA_HW_Name": "SW_Channel_DCS_6",
    "FaultIndex": 6,
    "Normal": "200R",
    "Buckled": "400R",
    "UnBuckled": "100R",
    "CrossC": "CROSS_CONNECTED",
    "STB": "STB",
    "GND": "undefined",
    "Open": "undefined",
    "TooHigh": "undefined",
    "TooLow": "undefined",
    "BadSensor": "undefined",
    "CFG": "undefined",
    "StatusDID": "FDC8",
    "StatusDID_RespLength": "5",
    "StatusDID_Start": 7,
    "StatusDID_End": 8,
    "DIDExpectBuckled": "0",
    "DIDExpectUnBuckled": "1",
    "StatusMessage": "ACU_SRS_2",
    "StatusSignal": "SRS_Row3RightSeatBeltSt",
    "MsgExpectBuckled": "0x00",
    "MsgExpectUnBuckled": "0x01",
    "CrossCDTC": "SB1DCSDRVR_F_DCS_CROSS_CONNECT_6_0_define",
    "CrossCQualify": [
        "3200",
        "3600"
    ],
    "CrossCDisQualify": [
        "3200",
        "3600"
    ],
    "STBDTC": "SB1DCSDRVR_F_DCS_SHT_PLUS_6_0_define",
    "STBQualify": [
        "3200",
        "3600"
    ],
    "STBDisQualify": [
        "3200",
        "3600"
    ],
    "GNDDTC": "SB1DCSDRVR_F_DCS_SHT_GND_6_0_define",
    "GNDQualify": [
        "3200",
        "3600"
    ],
    "GNDDisQualify": [
        "3200",
        "3600"
    ],
    "TooHighDTC": "SB1DCSDRVR_F_DCS_TOO_HIGH_6_0_define",
    "TooHighQualify": [
        "3200",
        "3600"
    ],
    "TooHighDisQualify": [
        "3200",
        "3600"
    ],
    "TooLowDTC": "SB1DCSDRVR_F_DCS_TOO_LOW_6_0_define",
    "TooLowQualify": [
        "3200",
        "3600"
    ],
    "TooLowDisQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDTC": "SB1DCSDRVR_F_DCS_BAD_SENSOR_6_0_define",
    "BadSensorQualify": [
        "3200",
        "3600"
    ],
    "BadSensorDisQualify": [
        "3200",
        "3600"
    ],
    "OpenDTC": "SB1DCSDRVR_F_DCS_OPEN_6_0_define",
    "OpenQualify": [
        "3200",
        "3600"
    ],
    "OpenDisQualify": [
        "3200",
        "3600"
    ],
    "CFGDTC": "SB1DCSDRVR_F_DCS_CFG_6_0_define",
    "CFGQualify": [
        "3200",
        "3600"
    ],
    "CFGDisQualify": [
        "3200",
        "3600"
    ],
    "Status": [
        "Buckled",
        "UnBuckled"
    ]
};
var ID0x260 = {
    "MsgName": "BCS_2",
    "MsgID": "0x260",
    "MsgDLC": "8",
    "CycleTime": "10",
    "InValidSg": {
        "BCS_VehSpd": {
            "InValidSgValue": "0x10AB"
        },
        "BCS_VehSpdVD": {
            "InValidSgValue": "0x00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_BCS_0_define",
    "InValidDlcDTC": "COM_BCS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_BCS_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x3b6 = {
    "MsgName": "BCS_6_P",
    "MsgID": "0x3b6",
    "MsgDLC": "8",
    "CycleTime": "20",
    "InValidSg": {
        "BCS_YawRateSt": {
            "InValidSgValue": "0x00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_BCS_0_define",
    "InValidDlcDTC": "COM_BCS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_BCS_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x268 = {
    "MsgName": "BCS_3",
    "MsgID": "0x268",
    "MsgDLC": "8",
    "CycleTime": "20",
    "InValidSg": {
        "undefined": {
            "InValidSgValue": "undefined"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "undefined",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_BCS_0_define",
    "InValidDlcDTC": "COM_BCS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "undefined",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "undefined"
    ],
    "InValidSgDisQualify": [
        "undefined"
    ]
};
var ID0x26a = {
    "MsgName": "BCS_11",
    "MsgID": "0x26a",
    "MsgDLC": "8",
    "CycleTime": "20",
    "InValidSg": {
        "undefined": {
            "InValidSgValue": "undefined"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "undefined",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_BCS_0_define",
    "InValidDlcDTC": "COM_BCS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "undefined",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "undefined"
    ],
    "InValidSgDisQualify": [
        "undefined"
    ]
};
var ID0x397 = {
    "MsgName": "BCS_EPB_1",
    "MsgID": "0x397",
    "MsgDLC": "8",
    "CycleTime": "20",
    "InValidSg": {
        "BCS_EPB_SwStVd": {
            "InValidSgValue": "0x00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_BCS_0_define",
    "InValidDlcDTC": "COM_BCS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_BCS_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x18d = {
    "MsgName": "EMS_1",
    "MsgID": "0x18d",
    "MsgDLC": "8",
    "CycleTime": "10",
    "InValidSg": {
        "EMS_BrakePedalVD": {
            "InValidSgValue": "0x00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_EMS_0_define",
    "InValidDlcDTC": "COM_EMS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_EMS_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x182 = {
    "MsgName": "EMS_2",
    "MsgID": "0x182",
    "MsgDLC": "8",
    "CycleTime": "10",
    "InValidSg": {
        "EMS_EngSpd": {
            "InValidSgValue": "0x2711"
        },
        "EMS_EngSpdVD": {
            "InValidSgValue": "0x00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_EMS_0_define",
    "InValidDlcDTC": "COM_EMS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_EMS_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x279 = {
    "MsgName": "EMS_6",
    "MsgID": "0x279",
    "MsgDLC": "8",
    "CycleTime": "10",
    "InValidSg": {
        "EMS_GasPedalActPstVD": {
            "InValidSgValue": "0x00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_EMS_0_define",
    "InValidDlcDTC": "COM_EMS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_EMS_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x262 = {
    "MsgName": "EMS_9",
    "MsgID": "0x262",
    "MsgDLC": "8",
    "CycleTime": "10",
    "InValidSg": {
        "EMS_GasPedalActPstforMRRVD": {
            "InValidSgValue": "0x00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_EMS_0_define",
    "InValidDlcDTC": "COM_EMS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_EMS_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x3B8 = {
    "MsgName": "EMS_10",
    "MsgID": "0x3B8",
    "MsgDLC": "8",
    "CycleTime": "100",
    "InValidSg": {
        "undefined": {
            "InValidSgValue": "undefined"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "undefined",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_EMS_0_define",
    "InValidDlcDTC": "COM_EMS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "undefined",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "undefined"
    ],
    "InValidSgDisQualify": [
        "undefined"
    ]
};
var ID0x1ac = {
    "MsgName": "TCU_2",
    "MsgID": "0x1ac",
    "MsgDLC": "8",
    "CycleTime": "10",
    "InValidSg": {
        "TCU_GearForDisp": {
            "InValidSgValue": "0x00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_TCU_0_define",
    "InValidDlcDTC": "COM_TCU_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_TCU_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x3a6 = {
    "MsgName": "GW_IFC_MRR_1_P",
    "MsgID": "0x3a6",
    "MsgDLC": "8",
    "CycleTime": "20",
    "InValidSg": {
        "undefined": {
            "InValidSgValue": "undefined"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "undefined",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_GW_0_define",
    "InValidDlcDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "undefined",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "undefined"
    ],
    "InValidSgDisQualify": [
        "undefined"
    ]
};
var ID0x186 = {
    "MsgName": "GW_IFC_MRR_2_P",
    "MsgID": "0x186",
    "MsgDLC": "8",
    "CycleTime": "20",
    "InValidSg": {
        "undefined": {
            "InValidSgValue": "undefined"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "undefined",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_GW_0_define",
    "InValidDlcDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "undefined",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "undefined"
    ],
    "InValidSgDisQualify": [
        "undefined"
    ]
};
var ID0x3ac = {
    "MsgName": "GW_ICM_HVAC_P",
    "MsgID": "0x3ac",
    "MsgDLC": "8",
    "CycleTime": "100",
    "InValidSg": {
        "ICM_TotalOdometer": {
            "InValidSgValue": "0xF4240"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_GW_0_define",
    "InValidDlcDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x35a = {
    "MsgName": "GW_ACU_3_P",
    "MsgID": "0x35a",
    "MsgDLC": "8",
    "CycleTime": "500",
    "InValidSg": {
        "ACU_Time_Second": {
            "InValidSgValue": "0x3C"
        },
        "ACU_Time_Month": {
            "InValidSgValue": "0x0D"
        },
        "ACU_Time_Minute": {
            "InValidSgValue": "0x3C"
        },
        "ACU_Time_Hour": {
            "InValidSgValue": "0x18"
        },
        "ACU_Time_Day": {
            "InValidSgValue": "0x00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_GW_0_define",
    "InValidDlcDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};
var ID0x375 = {
    "MsgName": "GW_BCM_2_P",
    "MsgID": "0x375",
    "MsgDLC": "8",
    "CycleTime": "20",
    "InValidSg": {
        "undefined": {
            "InValidSgValue": "undefined"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "undefined",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_GW_0_define",
    "InValidDlcDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "undefined",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "undefined"
    ],
    "InValidSgDisQualify": [
        "undefined"
    ]
};
var ID0x3a2 = {
    "MsgName": "GWM_BCM_TPMS_1",
    "MsgID": "0x3a2",
    "MsgDLC": "8",
    "CycleTime": "500",
    "InValidSg": {
        "undefined": {
            "InValidSgValue": "undefined"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "undefined",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_GW_0_define",
    "InValidDlcDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "undefined",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "undefined"
    ],
    "InValidSgDisQualify": [
        "undefined"
    ]
};
var ID0x3a3 = {
    "MsgName": "GW_IFC_1_P",
    "MsgID": "0x3a3",
    "MsgDLC": "8",
    "CycleTime": "500",
    "InValidSg": {
        "undefined": {
            "InValidSgValue": "undefined"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "undefined",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_GW_0_define",
    "InValidDlcDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "undefined",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "undefined"
    ],
    "InValidSgDisQualify": [
        "undefined"
    ]
};
var ID0x391 = {
    "MsgName": "GW_BCM_1_P",
    "MsgID": "0x391",
    "MsgDLC": "8",
    "CycleTime": "100",
    "InValidSg": {
        "undefined": {
            "InValidSgValue": "undefined"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "undefined",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_GW_0_define",
    "InValidDlcDTC": "COM_GW_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "undefined",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "undefined"
    ],
    "InValidSgDisQualify": [
        "undefined"
    ]
};
var ID0x264 = {
    "MsgName": "SAS_1",
    "MsgID": "0x264",
    "MsgDLC": "8",
    "CycleTime": "10",
    "InValidSg": {
        "SAS_SteeringAngleVD": {
            "InValidSgValue": "0x00"
        },
        "SAS_SteeringAngle": {
            "InValidSgValue": "0x3D00"
        }
    },
    "LostComm": "Yes",
    "InValidDlc": "7",
    "InValidSgWL": "OFF",
    "LostCommWL": "OFF",
    "InValidDlcWL": "OFF",
    "LostCommDTC": "COM_F_LOST_COMM_SAS_0_define",
    "InValidDlcDTC": "COM_SAS_SIGNAL_DLC_INVALID_0_define",
    "InValidSgDTC": "COM_SAS_SIGNAL_DLC_INVALID_0_define",
    "LostCommQualify": [
        "1800",
        "2000"
    ],
    "LostCommDisQualify": [
        "800",
        "1200"
    ],
    "InValidDlcQualify": [
        "1800",
        "2000"
    ],
    "InValidDlcDisQualify": [
        "800",
        "1200"
    ],
    "InValidSgQualify": [
        "1800",
        "2000"
    ],
    "InValidSgDisQualify": [
        "800",
        "1200"
    ]
};


// you can refer below parameter to set specific Loop/RSU/DCS to Specific status
//SetDCSCondition("G_BBSP","STB") set to G_BBSP to STB Fault
//All Parmater must use below string in each array Except  SetLoopCondition("Loop","AllNormal")  and SetDCSCondition("DCS","AllNormal");

//


////*********************************固定Parameters*************************************************


var Monitor_CycleTime = 400;


var G_DCSCrossC_SelectStr = "";
var G_DCSCrossC_SelectObj = {};

var G_DCSNSCrossC_SelectStr = "";
var G_DCSNSCrossC_SelectObj = {};

var G_RSUCrossC_SelectStr = "";
var G_RSUCrossC_SelectObj = {};

var G_LoopCrossC_SelectStr = "";
var G_LoopCrossC_SelectObj = {};

var G_LoopNSCrossC_SelectStr = "";
var G_LoopNSCrossC_SelectObj = {};


//*********************************Part6: Functional list*************************************************



// ---------------------------------------------------------------------------------------------
// Description:		Get the bit value of the content Read by DID 
//					use to read Status or Fault status by DID
// Parameters: 		Response: the content read by  CAN.SendDiagByValues(SID+DID)      
//					## No Need No: "total No of bytes "  this is resposne data length,no include RespSID + DID
//					Start: "offset Left to Right" Bit Offset
//					End: "offset Left to Right" + "No of bits"
// Return value: 	eg DID: DDDD, get the respone :0x62 0xDD 0xDD 0xFF 0xFD
//					 No:2 bytes, Start:6, End:8
//					
//					Result is "01"slice string "11111101"  from 6 to 8
// Example: 		ResponseValueToBit("5823",6,8)
// --------------------------------------------------------------------------------------------- 	
function ResponseValueToBit(Response, Start, End)
{
	//ReadDigByValues  will response a array ,eg :["0000","0x62 0xDD 0xDD 0xFF 0xFD" ]
	// get the result read by DID and change ”0x62 0xDD 0xDD 0xFF 0xFD " to "62DDDDFFFD" via RegExp
	var L_Result = Response.replace(/(0x|\s)/gi,"")
	// var L_Content = L_Result.slice(6,6 + No * 2);
	var L_Content = L_Result.slice(6,);
	var L_TempBin = HexToBin(L_Content); //Hex to bit
	var L_ReturnValue = L_TempBin.slice(Start,End);
	return L_ReturnValue;
}



// ---------------------------------------------------------------------------------------------
// Description:		Set DCS Not Support Fault, eg if Make Break Sensor not Support Open Fault, if Set to OPEN State, should no fault report
//					this should follow project specific
// Parameters: 		StrName : String ,such as "BBSD" this  must be same name of the variable defined in DCS_Object.ts (for all sensor)
//					Type: "GND","OPEN","TooLow","TooHigh","BadSensor","CrossC"
// Return value: 	if set condition Pass ,XML Result will show "PASS", or will show "Failed"
// Example: 		SetDCSNSFault("BBSD","GND")  or
//					
// --------------------------------------------------------------------------------------------- 	
function SetDCSNSFault(SensorName,Type)
{
	if(SensorName != "DCS")
	{
		var L_Object = StrToVariable(SensorName);
	}

    // PS.ClearLeakageVBATBusHigh();
    
    var L_ARiA_HW_Name = L_Object["ARiA_HW_Name"] //get the ARIA_HW_Name in loadbox

   switch(Type)
   {
		case "GND":
			RESULT.InterpretEqualResult("Set " + SensorName + " GND(NotSupport Fault) :" ,SLS.SendRequest(L_ARiA_HW_Name,"0R"));
			break;
		case "Open":
			RESULT.InterpretEqualResult("Set " + SensorName + " OPEN(NotSupport Fault) :"  ,SLS.SendRequest(L_ARiA_HW_Name,"OPEN"));
			break;
		case "TooHigh":
			RESULT.InterpretEqualResult("Set " + SensorName + " TooHigh(NotSupport Fault) :",SLS.SendRequest(L_ARiA_HW_Name,"550R"));
			break;
		case "TooLow":
			RESULT.InterpretEqualResult("Set " + SensorName + " TooLow(NotSupport Fault):",SLS.SendRequest(L_ARiA_HW_Name,"50R"));
			break;
		case "BadSensor":
			RESULT.InterpretEqualResult("Set " + SensorName + " BadSensor(NotSupport Fault):",SLS.SendRequest(L_ARiA_HW_Name,"200R"));
			break;
		case "CrossC":
			SetDCSNSCrossC(SensorName)
			break;
		default:
			RESULT.InterpretEqualResult("Not support Type called in SetDCSNSFault function ",["0000","ArgumentsWrong"],"ArgumentsRight");
   }
}

// ---------------------------------------------------------------------------------------------
// Description:		Set DCS different conditions Not Support Set "NotConfig Error currently"
//					if you want to use this function, you can't set the same fault for more than two sensor 
//					or test the fault priority
// Parameters: 		StrName : String ,such as "BBSD" this  must be same name defined in G_Support_DCS
//					Type: Status definition : :"Buckled" "UnBuckled"   "Occupied" "Empty" "Forward" "Upper" "Rearward" "Lower" "Normal"
//						and Fault  defned in G_DCS_Fault
// Return value: 	if set condition Pass ,XML Result will show "PASS", or will show "Failed"
// Example: 		SetDCSCondition("BBSD","Buckled")  or SetDCSCondition("BBSD","Normal")
//					SetDCSCondition("DCS","AllNormal") : this is used to reset all DCS to a specific state 
// --------------------------------------------------------------------------------------------- 			
function  SetDCSCondition(SensorName,Type)
{
	//Change a str to a Object, eg "BBSD" to BBSD 
	if(SensorName != "DCS")
	{
		var L_Object = StrToVariable(SensorName);
	}
	
	//before set any status ,will ClearLeakageVBATBusHigh

    
	//Not Support this status or Fault
	
	if((Type == "AllNormal"))
	{
		SetBattCondition("Normal")
		for(var i = 0;i < G_SupportDCS.length;i++)
		{
			var L_Object = StrToVariable(G_SupportDCS[i]);
			var L_ARiA_HW_Name = L_Object["ARiA_HW_Name"]
			RESULT.InterpretEqualResult("Set " + G_SupportDCS[i] + " Normal:" + L_Object["Normal"] ,SLS.SendRequest(L_ARiA_HW_Name,L_Object["Normal"]));
		}
		return;
	}

	var L_ARiA_HW_Name = L_Object["ARiA_HW_Name"] ;//get the ARIA_HW_Name in loadbox
    if(L_Object[Type] == undefined || L_Object[Type] == "undefined")
    {
		RESULT.InsertComment(SensorName + " Not Support " + Type);
		SetDCSNSFault(SensorName,Type);
	}
	else if(Type == "Normal")
    {
		SetBattCondition("Normal")
		RESULT.InterpretEqualResult("Set " + SensorName + " " + Type + " :" + L_Object[Type],SLS.SendRequest(L_ARiA_HW_Name,L_Object[Type]));
    }
    else if(Type == "CrossC")
    {
        SetDCSCrossC(SensorName);
    }
    else if(Type ==  "STB")
	{
		SetBattCondition("STB")
		RESULT.InterpretEqualResult("Set " + SensorName + " STB Fault",SLS.SendRequest(L_ARiA_HW_Name,"BUSS_HI_ON"));
    }
    else if(Type == "CFG")
    {
        SetDCSNotConfig(SensorName);
    }
    else
	{
		RESULT.InterpretEqualResult("Set " + SensorName + " " + Type + " :" + L_Object[Type],SLS.SendRequest(L_ARiA_HW_Name,L_Object[Type]));
    }
    
}


// ---------------------------------------------------------------------------------------------
// Description:		Set Loop different conditions  Not Support Set "NotConfig Error currently"
//					if you want to use this function, you can't set the same fault for more than two sensor 
//					or test the fault priority
// Parameters: 		StrName : String ,such as "BBSD" this  must be same name defined in G_Support_Loop
//					Type: Status definition : :"Normal","AllNormal",
//					and Fault  defned in G_Loop_Fault
// Return value: 	if set condition Pass ,XML Result will show "PASS", or will show "Failed"
// Example: 		SetLoopCondition("G_DrPT1","Open")  or
//					SetLoopCondition("Loop","AllNormal") : this is used to reset all Loop to a specific state 
// --------------------------------------------------------------------------------------------- 			
function  SetLoopCondition(LoopName,Type)
{
	//Change a str to a Object, eg "BBSD" to BBSD 
	if(LoopName != "Loop")
	{
		var L_Object = StrToVariable(LoopName);
	}


	//before set any status ,will ClearLeakageVBATBusHigh and ClearLeakageGNDBusHigh


	if(Type == "AllNormal")
	{
		SetBattCondition("Normal")
		//Reset All DCS to Normal Status
		for(var i = 0;i < G_SupportLoop.length;i++)
		{
			var L_Object = StrToVariable(G_SupportLoop[i])
			var L_ARiA_HW_Name = L_Object["ARiA_HW_Name"]
			RESULT.InterpretEqualResult("Set " + G_SupportLoop[i] + " Normal:" + L_Object["Normal"] ,SQUIB.SendRequest(L_ARiA_HW_Name,L_Object["Normal"]));
		}
		return ;
    }

    var L_ARiA_HW_Name = L_Object["ARiA_HW_Name"] //get the ARIA_HW_Name in loadbox
	// RESULT.InsertComment(Type == "Normal")
    //Not Support this status or Fault
    if(L_Object[Type] == undefined || L_Object[Type] == "undefined")
    {
        RESULT.InsertComment(LoopName + " Not Support " + Type)
	}
	else if(Type == "Normal")
    {
		
		SetBattCondition("Normal")
		RESULT.InterpretEqualResult("Set " + LoopName + " " + Type + " :" + L_Object[Type],SQUIB.SendRequest(L_ARiA_HW_Name,L_Object[Type]));
    }
    else if(Type == "CrossC")
    {
        SetLoopCrossC(LoopName);
    }
	else if(Type ==  "STB")
	{
		SetBattCondition("STB")
		RESULT.InterpretEqualResult("Set " + LoopName + " STB Fault",SQUIB.SendRequest(L_ARiA_HW_Name,"BUSS_HI_ON"));
	}
	else if(Type == "GND")
	{
		SetBattCondition("GND")
		RESULT.InterpretEqualResult("Set " + LoopName + " GND Fault",SQUIB.SendRequest(L_ARiA_HW_Name,"BUSS_Lo_ON"));
	}
    else if(Type == "CFG")
    {
        SetLoopNotConfig(LoopName);
    }
    else
	{
		RESULT.InterpretEqualResult("Set " + LoopName + " " + Type + " :" + L_Object[Type],SQUIB.SendRequest(L_ARiA_HW_Name,L_Object[Type]));
    }
    
}

// ---------------------------------------------------------------------------------------------
// Description:		Set ENS to different Status
// Parameters: 		ENSName
//					
//					
// Return value: 	
//Example:         
// ---------------------------------------------------------------------------------------------
function SetENSCondition(ENSName,Type)
{
	//Change a str to a Object, eg "BBSD" to BBSD 

	var L_Object = StrToVariable(ENSName);
	var L_ARiA_HW_Name = L_Object["ARiA_HW_Name"] ;//get the ARIA_HW_Name in loadbox
	//before set any status ,will ClearLeakageVBATBusHigh and ClearLeakageGNDBusHigh

    if(Type ==  "STB")
	{
		RESULT.InterpretEqualResult("Set " + ENSName + " STB Fault",SLS.SendRequest(L_ARiA_HW_Name,"BUSS_HI_ON"));
		SetBattCondition("STB")
	}
	else if(Type == "Normal")
    {
		SetBattCondition("Normal")
		RESULT.InterpretEqualResult("Set " + ENSName + " " + Type + " :" + L_Object[Type],SLS.SendRequest(L_ARiA_HW_Name,L_Object[Type]));
    }
	else if(Type == "GND")
	{
		RESULT.InterpretEqualResult("Set " + ENSName + " GND Fault",SLS.SendRequest(L_ARiA_HW_Name,"BUSS_Lo_ON"));
		SetBattCondition("GND")
	}
    else if (Type == "Open")
    {
        RESULT.InterpretEqualResult("Set " + ENSName + " " + Type + " :" + L_Object[Type],SLS.SendRequest(L_ARiA_HW_Name,"OPEN"));
	}
	else
	{
		RESULT.InterpretEqualResult("Set " + ENSName + " " + Type + " :" + L_Object[Type],SLS.SendRequest(L_ARiA_HW_Name,L_Object[Type]));
    }
}

// ---------------------------------------------------------------------------------------------
// Description:		Set Lamps to different status
// Parameters: 		
//					
//					
// Return value: 	
// Example:         
// ---------------------------------------------------------------------------------------------
function SetLampsCondition(LampsNanme,Type)
{
	//Change a str to a Object, eg "BBSD" to BBSD 
	
	var L_Object = StrToVariable(LampsNanme);
	var L_ARiA_HW_Name = L_Object["ARiA_HW_Name"] ;//get the ARIA_HW_Name in loadbox
	//before set any status ,will ClearLeakageVBATBusHigh and ClearLeakageGNDBusHigh


    if(Type ==  "STB")
	{
		RESULT.InterpretEqualResult("Set " + LampsNanme + " STB Fault",SLS.SendRequest(L_ARiA_HW_Name,"BUSS_HI_ON"));
		SetBattCondition("STB")
	}
	else if(Type == "Normal")
    {
		SetBattCondition("Normal")
		RESULT.InterpretEqualResult("Set " + LampsNanme + " " + Type + " :" + L_Object[Type],SLS.SendRequest(L_ARiA_HW_Name,L_Object[Type]));
    }
	else if(Type == "GND")
	{
		RESULT.InterpretEqualResult("Set " + LampsNanme + " GND Fault",SLS.SendRequest(L_ARiA_HW_Name,"BUSS_Lo_ON"));
		SetBattCondition("GND")
	}
    else if (Type == "Open")
    {
        RESULT.InterpretEqualResult("Set " + LampsNanme + " " + Type + " :" + L_Object[Type],SLS.SendRequest(L_ARiA_HW_Name,"OPEN"));
	}
	else
	{
		RESULT.InterpretEqualResult("Set " + LampsNanme + " " + Type + " :" + L_Object[Type],SLS.SendRequest(L_ARiA_HW_Name,L_Object[Type]));
    }
}


// ---------------------------------------------------------------------------------------------
// Description:		Set RSU different conditions
//					if you want to use this function, you can't set the same fault for more than two sensor 
//					or test the fault priority
// Parameters: 		StrName : String ,such as "BBSD" this  must be same name defined in G_Support_DCS
//					Type: Status definition : :"Normal"  Normal status,clear fault
//					and Fault  defned in G_Loop_Fault
// Return value: 	if set condition Pass ,XML Result will show "PASS", or will show "Failed"
// Example: 		SetRSUCondition("G_SRSU_L","Open")  or
//					SetRSUCondition("G_SRSU_L","Normal") : this is used to reset RSU to a specific state 
// --------------------------------------------------------------------------------------------- 			
function  SetRSUCondition(RSUName,Type)
{
	//Change a str to a Object, eg "BBSD" to BBSD 
	if(RSUName != "RSU")
	{
		var L_Object = StrToVariable(RSUName);
	}

    var L_ARiA_HW_Name = parseInt(L_Object["ARiA_HW_Name"],10) //get the ARIA_HW_Name in loadbox
	// var L_ARiA_HW_Name = L_Object["ARiA_HW_Name"];
	// RESULT.InsertComment(L_ARiA_HW_Name);
    //Not Support this status or Fault
    if(L_Object[Type] == undefined || L_Object[Type] == "undefined")
    {
        RESULT.InsertComment(RSUName + " Not Support " + Type)
    }
    else if(Type=="Open")
	{
		RESULT.InterpretEqualResult("Set " + RSUName + " " + Type,RSU.SetFaultOpen(L_ARiA_HW_Name));
	}
	else if(Type=="STB")
	{
		RESULT.InterpretEqualResult("Set " + RSUName + " " + Type,RSU.SetFaultShortBattery(L_ARiA_HW_Name));
	}
	else if(Type=="STG")
	{
		RESULT.InterpretEqualResult("Set " + RSUName + " " + Type,RSU.SetFaultShortGround(L_ARiA_HW_Name));
	}
	else if(Type=="COMM")
	{
		RESULT.InterpretEqualResult("Set " + RSUName + " " + Type,RSU.SetFaultParity(L_ARiA_HW_Name));
	}
	else if(Type=="Nodata")
	{
		RESULT.InterpretEqualResult("Set " + RSUName + " " + Type,RSU.SetFaultNoData(L_ARiA_HW_Name));
	}
	else if(Type=="Mancester")
	{
		RESULT.InterpretEqualResult("Set " + RSUName + " " + Type,RSU.SetFaultMancester(L_ARiA_HW_Name));
	}
	else if(Type=="Normal")
	{
		RESULT.InterpretEqualResult("Set " + RSUName + " " + Type,RSU.ClearFault(L_ARiA_HW_Name));
	}
    
}





// ---------------------------------------------------------------------------------------------
// Description:		Check if the DCS actual status meet the expectStatus
// Parameters: 		StrName: eg: "G_BBSD" 
//					ExpectStatus: : "Buckled" "UnBuckled","Empty","Occupied","Faulty","NoFault"
//					"NotConfig"
// Return value: 	
// Example: 		CheckDCSStatusByDID("BBSD","Buckled")
// --------------------------------------------------------------------------------------------- 	
function CheckDCSStatusByDID(SensorName,ExpectStatus)
{
	//MessageBox.Show(StrName);
	//Get a Object via a string  ,eg "BBSD" to  BBSD object
	var L_Object = StrToVariable(SensorName);
	
	//Get the DID which can be used to read the status of DCS
    var L_DID = L_Object["StatusDID"];
    
    if(L_DID == "undefined" || L_DID == undefined)
    {
        RESULT.InsertComment(SensorName + "Not Support using DID to read Status");
        return ;
    }
    // MessageBox.Show(L_DID);
    //Get the ResponseLength,offset of start, offset of end
	// var L_Num = L_Object["StatusDID_RespLength"];
	var L_StStart = L_Object["StatusDID_Start"];
	var L_StEnd = L_Object["StatusDID_End"];
	//var L_Request ="0x22 0x" + DID;
	// get the result read by DID 
	CAN.SetDiagnosticAdressingMode(G_CAN_Channel,G_Internal_Req_ID,G_Internal_Res_ID);
	Thread.Sleep(200);
	var L_Response = CAN.SendDiagByValues("0x22 0x" + L_DID)[1];
    // MessageBox.Show(L_Response);
	RESULT.InsertComment("Response Value read by DID==>" + L_Response)
	//Handel the response value to a bit value
	//Status  value 
	// var L_AcStatusValue = ResponseValueToBit(L_Response,L_Num,L_StStart,L_StEnd);
	var L_AcStatusValue = ResponseValueToBit(L_Response,L_StStart,L_StEnd);
	//Get the expectstatus and compare it with actual value
	RESULT.InterpretEqualResult("Check " + SensorName + " " + ExpectStatus + " Status by DID",["0000",L_AcStatusValue],L_Object["DIDExpect" + ExpectStatus]);
	


}




// ---------------------------------------------------------------------------------------------
// Description:		Check if the DCS actual status meet the expectStatus via FRC
// Parameters: 		StrName: eg: "BBSD" 
//					ExpectStatus: eg: "Buckled" "Empty"
// Return value: 	
// Example: 		CheckDCSStatusByDID("BBSD","Buckled")	
// --------------------------------------------------------------------------------------------- 	
function CheckDCSStatusBySignal(SensorName,ExpectStatus)
{
	
	//Get a Object via a string  ,eg "BBSD" to  BBSD object
	var L_Object = StrToVariable(SensorName);
	
	//if the DCS has no attributes of StatusMessageCAN,return 0
	//this means its status or fault can't be checked by Signal 
	//in this condition,when you call this function,will no any exception to being throw to disturb test running
	//don't need add any "if" to judge if this DCS status can be check by Signal when calling function in loops
	//
	if(L_Object.StatusMessage == undefined || L_Object.StatusMessage == "undefined")
	{
        RESULT.InsertComment(SensorName + " Not Support using Message to read Status");
		return 0;
	}
	// RESULT.InsertComment(L_Object["StatusMessage"] +L_Object["StatusSignal"] )
	//Get the status via Signal
	var L_AcStatusValue = CAN.GetSignalFromFrame(G_CAN_Channel,L_Object["StatusMessage"],L_Object["StatusSignal"])[1]

	//Get the expectstatus and compare it with actual value
	RESULT.InterpretEqualResult("Check " + SensorName + " " + ExpectStatus + " Status by Signal",["0000",L_AcStatusValue],L_Object["MsgExpect" + ExpectStatus]);
	
}

// ---------------------------------------------------------------------------------------------
// Description:		Set Cross couple error 
// Parameters: 		StrName,ID2_Str : eg: "BBSD","STSDX"
//					
// Return value: 	if set condition Pass ,XML Result will show "PASS", or will show "Failed"
// Example: 		SetCrossC("STSDX")
// --------------------------------------------------------------------------------------------- 	
function SetDCSCrossC(SensorName)
{
	//Get the Object via the string
	var L_Object = StrToVariable(SensorName);

    for(var i = 0; i < G_CrossCDCS.length; i++)
    {
        if(G_CrossCDCS[i] != SensorName)
        {
            G_DCSCrossC_SelectStr = G_CrossCDCS[i];
            break;
        }
    }
    G_DCSCrossC_SelectObj = StrToVariable(G_DCSCrossC_SelectStr);
    

	RESULT.InterpretEqualResult("Set " + SensorName + " CrossConnect.",SLS.SendRequest(L_Object["ARiA_HW_Name"],"BUSS_HI_ON"));
	RESULT.InterpretEqualResult("Set " + G_DCSCrossC_SelectStr + " CrossConnect.",SLS.SendRequest(G_DCSCrossC_SelectObj["ARiA_HW_Name"],"BUSS_HI_ON"));

}

// ---------------------------------------------------------------------------------------------
// Description:		Set Cross couple for sensor that not Support CrossC fault 
// Parameters: 		StrName,ID2_Str : eg: "BBSD","STSDX"
//					
// Return value: 	
// Example: 		SetDCSNSCrossC("STSDX")
// --------------------------------------------------------------------------------------------- 	
function SetDCSNSCrossC(SensorName)
{
	//Get the Object via the string
	var L_Object = StrToVariable(SensorName);

    for(var i = 0; i < G_NSCrossCDCS.length; i++)
    {
        if(G_NSCrossCDCS[i] != SensorName)
        {
            G_DCSNSCrossC_SelectStr = G_NSCrossCDCS[i];
            break;
        }
    }
    G_DCSNSCrossC_SelectObj = StrToVariable(G_DCSNSCrossC_SelectStr);
    

	RESULT.InterpretEqualResult("Set " + SensorName + " CrossConnect(NotSupport Fault).",SLS.SendRequest(L_Object["ARiA_HW_Name"],"BUSS_HI_ON"));
	RESULT.InterpretEqualResult("Set " + G_DCSNSCrossC_SelectStr + " CrossConnect(NotSupport Fault).",SLS.SendRequest(G_DCSNSCrossC_SelectObj["ARiA_HW_Name"],"BUSS_HI_ON"));

}

// ---------------------------------------------------------------------------------------------
// Description:		Set Cross couple error 
// Parameters: 		StrName,ID2_Str : eg: "BBSD","STSDX"
//					
// Return value: 	if set condition Pass ,XML Result will show "PASS", or will show "Failed"
// Example: 		SetCrossC("STSDX","STSDZ")
// --------------------------------------------------------------------------------------------- 	
function SetLoopCrossC(LoopName)
{
	//Get the Object via the string
	var L_Object = StrToVariable(LoopName);

    for(var i = 0; i < G_CrossCLoop.length; i++)
    {
        if(G_CrossCLoop[i] != LoopName)
        {
            G_LoopCrossC_SelectStr = G_CrossCLoop[i];
            break;
        }
    }
    G_LoopCrossC_SelectObj = StrToVariable(G_LoopCrossC_SelectStr);
    

	RESULT.InterpretEqualResult("Set " + LoopName + " CrossConnect.",SQUIB.SendRequest(L_Object["ARiA_HW_Name"],"BUSS_HI_ON"));
	RESULT.InterpretEqualResult("Set " + G_LoopCrossC_SelectStr + " CrossConnect.",SQUIB.SendRequest(G_LoopCrossC_SelectObj["ARiA_HW_Name"],"BUSS_HI_ON"));

}

// ---------------------------------------------------------------------------------------------
// Description:		Set DCS Not Config Error, Current there is no good way to write a common function to set DCS Config Error
// Parameters: 		
//					
// Return value: 	
// Example: 		
// --------------------------------------------------------------------------------------------- 	
function SetDCSNotConfig(SensorName)
{

}
// ---------------------------------------------------------------------------------------------
// Description:		Set Loop Not Config Error, Current there is no good way to write a common function to set Loop Config Error
// Parameters: 		
//					
// Return value: 	
// Example: 		
// --------------------------------------------------------------------------------------------- 
function SetLoopNotConfig(LoopName)
{

}

// ---------------------------------------------------------------------------------------------
// Description:		Set Msg InValid DLC，InValid Signal,Stop to send MSg,Recover to send default value
// Parameters: 		ObjectStr: the string name of the object,
//					Type: A string
//					Signal:Signal name if need,if not need any value is OK
// Return value: 	None
//Example:          SetMsgConditions("ID180","LostComm",0)
//					SetMsgConditions("ID180","InValidSg",Signal)
//					SetMsgConditions("ID180","InValidDlc",0)
//					SetMsgConditions("ID180","Normal",0)
// ---------------------------------------------------------------------------------------------

function SetMsgConditions(ObjectStr,Type,Signal) 
{	     
	var L_Object = StrToVariable(ObjectStr)          
	var L_MsgName = L_Object["MsgName"];//get the message name  	
	var L_CycleTime = int(L_Object["CycleTime"])  	
	var L_MSgID = int(L_Object["MsgID"]);  	
	if(Type == "LostComm") 	
	{ 		RESULT.InterpretEqualResult("Stop send Msg " + ObjectStr,CAN.PeriodicDisableFrame(L_MsgName)); 
	} 	
	else if(Type == "InValidSg")
	{ 		
		RESULT.InterpretEqualResult("Set " + ObjectStr + "Invalid Signal value",CAN.PeriodicChangeSignal(G_CAN_Channel,L_MsgName,Signal,parseInt(L_Object["InValidSg"][Signal]["InValidSgValue"],16))); 	
	} 	
	else if(Type == "InValidDlc")
	{ 		
		var L_InValidDlc = L_Object["InValidDlc"];
		RESULT.InterpretEqualResult("Changed " + ObjectStr + " to Invalid DLC " + L_InValidDlc,ARIA.SetPeriodicFrame(G_CAN_Channel,L_MSgID ,L_CycleTime,L_InValidDlc,[0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])); 		

	} 	
	else if(Type == "Normal") 	
	{ 		
		var L_MsgDLC = L_Object["MsgDLC"]; 		
		RESULT.InterpretEqualResult("Send the default frame",CAN.SetPeriodicFrame(G_CAN_Channel,L_MSgID ,L_CycleTime,L_MsgDLC,L_Object["DefaultFrame"])); 		
		
	} 
}

// ---------------------------------------------------------------------------------------------
// Description:		Function to changed string to Byte Arr

// ---------------------------------------------------------------------------------------------
function StrFrame2ByteFrame(StrArr)
{
	var L_ByteFrame:byte[] = [0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00]
	for(var i in StrArr)
	{
		L_ByteFrame[i] = byte(StrArr[i])
	}
	return L_ByteFrame;
}

// ---------------------------------------------------------------------------------------------
// Description:		
// Parameters: 		FaultInfo：“xxx_define，YYY_define"
//					Status:"-ACTIVE" or "-HISTORIC"
//					
// Return value: 	“xxx_define-ACTIVE，YYY_define-ACTIVE"
//Example:         
// ---------------------------------------------------------------------------------------------
function SplitFaultInfo(FaultInfo_Str,Status)
{
	var L_ReturnStr = "";
	var L_FaultList = FaultInfo_Str.split(",")
	for(var i = 0; i < L_FaultList.length; i++)
	{
		L_FaultList[i] = L_FaultList[i] + Status;
	}
	L_ReturnStr = L_FaultList.toString()
	
	return L_ReturnStr
}

// ---------------------------------------------------------------------------------------------
// Description:		Add the WL Lamp status to the fault info
//					-ACTIVE@ to -ACTIVE@ON or -ACTIVE@OFF
// Parameters: 		FaultInformation_Array
// Return value: 	["xxx_define-ACTIVE@ON，YYY_define-HISTORIC@ON,YYY_define-HISTORIC@OFF", "ON"]
//Example:         
// ---------------------------------------------------------------------------------------------
function SetSuffixToFaultInfo(FaultInfo_Str)
{
	var L_ReturnValue = ["",""]
    var L_FaultInformation_Array = FaultInfo_Str.split(",")
	// RESULT.InsertComment(2)
	var L_WL_Array = new Array()
    for(var i in L_FaultInformation_Array)
    {   
        var L_DTCObjectStr = "";
        
        if(L_FaultInformation_Array[i].match("-") != null)
        {
            var L_Position = L_FaultInformation_Array[i].indexOf("-");
            try
            {
                eval("L_DTCObjectStr = " + L_FaultInformation_Array[i].slice(0,L_Position));
            }
            catch(e)
            {
                L_DTCObjectStr = "FaultInfo is not Correct in GetDTCStatusViaDTCDefine,undefined,undefined"
            }
            var L_WL_Attributes = L_DTCObjectStr.split(",")[3] 
            // RESULT.InsertComment("i =" + i)
            if(L_WL_Attributes == "FLTMONR_WL_ON")
            {
                if(L_FaultInformation_Array[i].indexOf('ACTIVE') > 0)
                {
					L_FaultInformation_Array[i] += 'ON';
					L_WL_Array.push("ON")
                }
                else
                {
					L_FaultInformation_Array[i] += 'OFF';
					L_WL_Array.push("OFF")
                }
            }
            else if(L_WL_Attributes == "FLTMONR_WL_LATCHED")
            {
                if(L_FaultInformation_Array[i].indexOf('HISTORIC@IG_') > 0)
                {
					L_FaultInformation_Array[i] += 'OFF';
					L_WL_Array.push("OFF")
                }
                else 
                {
					L_FaultInformation_Array[i] += 'ON';
					L_WL_Array.push("ON")
                }
            }
            else if(L_WL_Attributes == "FLTMONR_WL_OFF")
            {
				L_FaultInformation_Array[i] += 'OFF';
				L_WL_Array.push("OFF")
            }
        }
        else
        {
            RESULT.InsertComment(L_FaultInformation_Array[i] + " Expect FaultInformation format is not correct FaultInformation ");
        }
    }
	L_ReturnValue[0] = L_FaultInformation_Array.toString();
	L_ReturnValue[1] = L_WL_Array.toString().indexOf("ON")>=0? "ON":"OFF";// when it contains "ON", the finally wL should be ON. or it should be OFF
    return L_ReturnValue
}