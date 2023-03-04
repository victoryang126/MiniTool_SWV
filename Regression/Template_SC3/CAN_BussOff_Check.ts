// ******************************************************************************************
// **************************Veoneer Electronics document************************************
// ******************************************************************************************
// Result Test: 
// *******************************************************
               // Script Information
// *******************************************************
// Test case ID: 
// *******************************************************
// Full Automation: Yes
// *******************************************************
	

// *******************************************************
               // External Function
// *******************************************************
CALL(AA_${TestProject}_HeadDefine.ts);

// *******************************************************
               // Test Information
// *******************************************************
CommonInformation();


// *******************************************************
               // Test Log Variables Path Define
// *******************************************************
//Modify below parameter according different
var Test_ObjectStr = "CAN1";
var BussOff_Setting = "BUSOFF";
var CAN_Channel = 2;
var BussOff_DTC = "COM_F_BUS_OFF_RECOVERY_0_define";
var QualifyTime = 3000;


var StorePath= G_PathArray[3] + "Regression\\"+ "CANC_" + Test_ObjectStr + "_BussOff.log";




// *******************************************************
               // Define/Re-Define parameters
// *******************************************************



// *******************************************************
               // Test Steps
// *******************************************************

if(CheckTestEnvironment())                                  //Check test condition
{
	
	CAN.StartLoggingToFile(StorePath);

	//1.
	//-----------------------------TEST STEP------------------------------//
	CommentStep("Set " + Test_ObjectStr + " CANH short to CANL " + QualifyTime + "ms");
	ARIA.AFT_iLoadBoxWrapper(Test_ObjectStr, BussOff_Setting);
	Thread.Sleep(QualifyTime + 1000);
	ARIA.AFT_iLoadBoxWrapper(Test_ObjectStr, "INHEREN");
	Thread.Sleep(100);
	CAN.ResetCAN(CAN_Channel,0);
	Thread.Sleep(QualifyTime + 1000);
	//2.
	//-----------------------------TEST STEP------------------------------//
	CommentStep("Check BussOff DTC Historic");
	var ret = ActualResults(); 
	CompareResultsDefine(ret,"OFF",BussOff_DTC + "-HISTORIC");
	//3.
	//-----------------------------TEST STEP------------------------------//
	CommentStep("Clear DTC");
	ClearDTC();
	Thread.Sleep(QualifyTime + 1000);
	var ret = ActualResults(); 
	var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
    CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])
	
	
	StopToLog();	
}
else
{
	RESULT.InterpretEqualResult("Check Test Bench condition: ",["0000","Not Normal"],"Normal");
}

// *******************************************************
                   // Re-Initialize
// *******************************************************
ReInitialize()
	
	
// *******************************************************
                   // Extract Result
// *******************************************************
var tst : TestStatus  = ExtractTestStatus(RESULT.ResultName);
RESULT.TestVerdict(tst);