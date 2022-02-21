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
CALL(AA_${Project}_HeadDefine.ts);

// *******************************************************
               // Test Information
// *******************************************************
CommonInformation();


// *******************************************************
               // Test Log Variables Path Define
// *******************************************************
//Modify below parameter according different
G_DTCStatusCheck = true;
var Test_ObjectStr = "${TestObjectStr}";//"BBSD"
var SetObjectFunc = ${SetObjectFunction};


var StorePath= G_PathArray[3] + "Regression\\" + Test_ObjectStr + ".log";




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
	CommentStep("Set " + Test_ObjectStr + " to " + BatHigh_Vol  + " v to Test Battery High DTC" );
    var QualifyTime = ${QualifyTime}
    SetObjectFunc.apply(this,${ActiveFault_Args})
	//1.1.
	//-----------------------------TEST STEP------------------------------//
	CommentSubStep("Check Battery High DTC Active");
	var ret = ActualResults(); 

    
    //1.2.
	//-----------------------------TEST STEP------------------------------//
    CommentSubStep("Set " + Test_ObjectStr + " to 12v");
    var DisQualifyTime = ${DisQualifyTime}
    SetObjectFunc.apply(this,${HistoricFault_Args})
    Thread.Sleep(BatHighQualifyTime +1000)
	//1.3.
	//-----------------------------TEST STEP------------------------------//
	CommentSubStep("Check Battery High DTC Historic");
	var ret = ActualResults(); 
    CompareResultsDefine(ret,"OFF",BatHigh_DTC + "-HISTORIC");
	//1.4.
	//-----------------------------TEST STEP------------------------------//
	CommentSubStep("Clear DTC");
    ClearDTC();
	Thread.Sleep(BatHighQualifyTime + 1000);
	var ret = ActualResults(); 
    CompareResultsDefine(ret,"OFF","None");
    


	
	

	CAN.StopLogging();	
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