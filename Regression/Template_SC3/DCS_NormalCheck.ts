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
G_DTCStatusCheck = true;
var Test_ObjectStr = "${TestObjectStr}";
var Test_Object = ${TestObjectStr};
var ObjectType = "${ObjectType}";
var SetObjectFunc = Set${ObjectType}Condition;

var ObjectStatus = Test_Object["Status"];

var StorePath1 = G_PathArray[3] + "Regression\\" + ObjectType + "_" + Test_ObjectStr + "_Normal.log";

// *******************************************************
               // Define/Re-Define parameters
// *******************************************************
var SwitchTime = 600;
// *******************************************************
               // Test Steps
// *******************************************************
if(CheckTestEnvironment())
// if(1)
{



	
	StartToLog(StorePath1)
	for(var i = 0; i < ObjectStatus.length;i++)
	{
		var Status = ObjectStatus[i];
		//3 Set Test_ObjectStr to Normal: " + Test_Object["Normal"]
		//-----------------------------TEST STEP------------------------------//
		CommentStep("Set " + Test_ObjectStr + " to " +  Status + ": " + Test_Object[Status]);
		SetObjectFunc(Test_ObjectStr,Status);
		
		
		//4.After 500ms,Check the DCSs status by Signal:
		//-----------------------------TEST STEP------------------------------//		
		Thread.Sleep(SwitchTime );
		CommentSubStep("After "+ SwitchTime + "ms,Check the " + Test_ObjectStr + " status by Signal:" + Status + " as in " +  Test_Object[Status]);	
		CheckDCSStatusBySignal(Test_ObjectStr,Status);

		//5."After 500ms,Check the DCSs status by DID:
		//-----------------------------TEST STEP------------------------------//		
		CommentSubStep("After "+ SwitchTime + "ms,Check the " + Test_ObjectStr + " status by DID:" + Status + " as in " +  Test_Object[Status]);
		CheckDCSStatusByDID(Test_ObjectStr,Status);
		
		
		//6.Verify no DTC present.
		//-----------------------------TEST STEP------------------------------//
		CommentSubStep("Verify no DTC present.");
		var ret = ActualResults(); 
		var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
		CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])

	
	}
	
	
	
	
    
	StopToLog();
	
	

	
	 
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