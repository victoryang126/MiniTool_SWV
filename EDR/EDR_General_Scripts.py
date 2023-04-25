

SCRIPT_BEGIN = """
// ******************************************************************************************
// **************************Veoneer Electronics document************************************
// ******************************************************************************************
// Result Test:
// ******************************************************************************************
// Test case ID:
// ******************************************************************************************
// Equipment: Test PC, VN1630A, Aria Test Enviroment
// ******************************************************************************************
// Requirement under test: N/A
// ******************************************************************************************
// Author: 
// ******************************************************************************************
// Full Automation: Yes
// 
// ******************************************************************************************
              // External Function
// ******************************************************************************************
CALL(BB_EDR_Common_Define.ts);
var fso = new ActiveXObject("Scripting.FileSystemObject");

// ******************************************************************************************
               // Parameter Initilize
// ******************************************************************************************

// ******************************************************************************************
               // Define parameters
// ******************************************************************************************


// ******************************************************************************************
               // Common Function
// ******************************************************************************************
CommonInformation();

// ******************************************************************************************
               // Test Steps
// ******************************************************************************************
if(CheckTestEnvironment())                                  //Check test condition
{	
"""




SCRIPT_END = """

}
else
{
    RESULT.InterpretEqualResult('Check Test Bench condition: ',['0000','Not Normal'],'Normal');
}
// ******************************************************************************************
                        // Re-Initialize
// ******************************************************************************************
ReInitialize();
// ******************************************************************************************
                   // Extract Result
// ******************************************************************************************
var tst : TestStatus  = ExtractTestStatus(RESULT.ResultName);
RESULT.TestVerdict(tst);
"""