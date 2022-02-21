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
var Test_ObjectStr = "${TestObjectStr}";
var Test_Object = ${TestObjectStr};

var IMUCurves = Test_Object["IMUCurves"];
var ExpectData = Test_Object["ExpectData"];
var Tolerance = Test_Object["Tolerance"];

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
//if(1)
{

	//1.0.Load IMU Curves
    //-----------------------------TEST STEP------------------------------//
    CommentStep("Load IMU Curves")
	LoadIMUCurves(IMUCurves);
	//2.0.Trigger Simulate
    //-----------------------------TEST STEP------------------------------//
    CommentStep("Trigger Simulate")
    CAN.StartLoggingToFile(StorePath);
	Thread.Sleep(1000);
	PS.TriggerMain();
	Thread.Sleep(1000);
	CAN.StopLogging();
	
    //3.0Check IMU Value in CAN Message
	//-----------------------------TEST STEP------------------------------//
    CommentStep("Check " + Test_ObjectStr + " Value in CAN Message");
	CheckIMUDataByMsg(Test_ObjectStr,ExpectData,Tolerance)
	
    //4.0Verify no DTC present
    //-----------------------------TEST STEP------------------------------//
	CommentStep("Verify no DTC present.");
	var ret = ActualResults();
	CompareResultsDefine(ret,"OFF","NONE");
	
}
else
{
	RESULT.InterpretEqualResult("Check Test Bench condition: ",["0000","Not Normal"],"Normal");
}


// *******************************************************
                   // Reinitilize
// *******************************************************
ReInitialize()

// *******************************************************
                   // Extract Result
// *******************************************************
var tst : TestStatus  = ExtractTestStatus(RESULT.ResultName);
RESULT.TestVerdict(tst);
