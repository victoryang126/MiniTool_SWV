// ******************************************************************************************
// **************************Veoneer Electronics document************************************
// ******************************************************************************************
// Result Test: 
// *******************************************************
               // Script Information
// *******************************************************
// Test case ID: Crash
// *******************************************************
// Full Automation: Yes
// *******************************************************
// 
// ******************************************************************************************
              // External Function
// ******************************************************************************************
CALL(AA_${TestProject}_HeadDefine.ts);

// *******************************************************
               // Test Information
// *******************************************************
CommonInformation();

// *******************************************************
               // Test Log Variables Path Define
// ******************************************************
G_DTCStatusCheck = true;
var Test_ObjectStr = "${TestObjectStr}";
var Test_Object = ${TestObjectStr};
var CrashCurves = Test_Object["CrashCurves"];
var ExpectDTC = Test_Object["DTC"];
var ExpectLoops = Test_Object["DeployLoops"];

var StorePath = G_PathArray[3] + "Regression\\" + Test_ObjectStr + ".log"
// ******************************************************************************************
               // Define/Re-Define parameters
// ******************************************************************************************



// ******************************************************************************************
               // Common Function
// ******************************************************************************************





// ******************************************************************************************
               // Test Steps
// ******************************************************************************************
if(CheckTestEnvironment())
// if(1)
{
    
    StartToLog(StorePath)
    //1.0.Load Crash Curves
    //-----------------------------TEST STEP------------------------------//
    CommentStep("Load Crash Curves" + Test_ObjectStr)
	
    CrashLoadPulse(CrashCurves);

    //2.0.CrashSimulate
    //-----------------------------TEST STEP------------------------------//
    CommentStep("CrashSimulate")
    CrashSimulate();
    CAN.InsertLogMessage('Trigger');
    Thread.Sleep(100);
    ${CrashOutput}
    Thread.Sleep(8000);
    //3.0.Check if deploy the expected loops
    //-----------------------------TEST STEP------------------------------//
    CommentStep("Check if deploy the expected loops and Crash output")
    CrashGetAllTTF();
    CompareLoopDeploy(ExpectLoops);

  

    //4.0.Check if expected DTC shown
    //-----------------------------TEST STEP------------------------------//
    CommentStep("Check if expected DTC shown")
    var ret = ActualResults(); 

    var ret = ActualResults(); 
    //add  sufix to the dtcdefine
    if(ExpectDTC == "NONE")
    {
        var ReturnValue = SetSuffixToFaultInfo("NONE") 
    }
    else
    {
        var FaultInfo_Str = SplitFaultInfo(ExpectDTC,"-ACTIVE@");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
    }
    CompareResultsDefine(ret,ReturnValue[1],ReturnValue[0]);

    //5.0.Check if expected DTC shown after IG
    //-----------------------------TEST STEP------------------------------//
    CommentStep("Check if expected DTC shown after IG")
    IGNRestartWaitLampCheck()
    var ret = ActualResults(); 
    //add  sufix to the dtcdefine
    if(ExpectDTC == "NONE")
    {
        var ReturnValue = SetSuffixToFaultInfo("NONE") 
    }
    else
    {
        var FaultInfo_Str = SplitFaultInfo(ExpectDTC,"-ACTIVE@");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
    }
    CompareResultsDefine(ret,ReturnValue[1],ReturnValue[0]);
   

    StopToLog();
}
else
{
	RESULT.InterpretEqualResult("Check Test Bench condition: ",["0000","Not Normal"],"Normal");
}


// ******************************************************************************************
                   // Reinitilize
// ******************************************************************************************
ReInitialize()

// ******************************************************************************************
                   // Extract Result
// ******************************************************************************************
var tst : TestStatus  = ExtractTestStatus(RESULT.ResultName);
RESULT.TestVerdict(tst);
