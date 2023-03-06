
SCRIPT_HEADER_1 = """
// ******************************************************************************************
// **************************Veoneer Electronics document************************************
// ******************************************************************************************
// Result Test: 
// *******************************************************
               // Script Information
// *******************************************************
// Test case ID:"""

SCRIPT_HEADER_2 = """
// *******************************************************
// Full Automation: Yes
// *******************************************************

// *******************************************************
               // External Function
// *******************************************************
CALL(BB_DCS_Common_Define.ts);
// *******************************************************
               // Test Information
// *******************************************************
CommonInformation();

// *******************************************************
               // Test Log Variables Path Define
// *******************************************************
"""

SCRIPT_HEADER_3 = """
// *******************************************************
               // Define/Re-Define parameters
// *******************************************************

// *******************************************************
               // Test Steps
// *******************************************************
"""
TEST_BEGIN = "if(CheckTestEnvironment())\n{\n"

TEST_END = """
}
else 	
{
	RESULT.InterpretEqualResult("Check Test Bench condition: ",["0000","Not Normal"],"Normal");
}

// *******************************************************
                   // Re-Initialize
// *******************************************************
ReInitialize();

// *******************************************************
                   // Extract Result
// *******************************************************
var tst : TestStatus  = ExtractTestStatus(RESULT.ResultName);
RESULT.TestVerdict(tst);
"""

FAULT_LOOP_START = """
    for(var Fault in GBB_DCS_Fault)
    {


        RESULT.InsertComment("###########################################################################################################################")
        RESULT.InsertComment("Test the " + Fault + "  Fault of " + Sensor )
        G_StepNumber = 0
        RESULT.InsertComment("###########################################################################################################################")
        if(Sensor_Obj[Fault] != undefined && Sensor_Obj[Fault] != "undefined" && Fault != "CFG")
        {
"""

FAULT_LOOP_END = """
        }

    }
"""