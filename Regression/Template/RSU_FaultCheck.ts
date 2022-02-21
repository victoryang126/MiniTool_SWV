
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
// CommonInformation();




// *******************************************************
               // Test Log Variables Path Define
// ******************************************************
G_DTCStatusCheck = true;
var Test_ObjectStr = "${TestObjectStr}";//"BBSD"
var Test_Object = ${TestObjectStr};
var ObjectType = "${ObjectType}";
var ObjectFault = G_${ObjectType}_Fault;
var SetObjectFunc = Set${ObjectType}Condition;


var StorePath = {};
for(var Fault in  ObjectFault)
{

	StorePath[Fault] = [G_PathArray[3] + "Regression\\" + ObjectType + "_" + Test_ObjectStr + "_" + Fault + "_Qualify.log",
						G_PathArray[3] + "Regression\\" + ObjectType + "_" + Test_ObjectStr + "_" + Fault + "_DisQualify.log",
						];	
}


// *******************************************************
               // Define/Re-Define parameters
// *******************************************************


// *******************************************************
               // Test Steps
// *******************************************************
if(CheckTestEnvironment())
// if(1)
{
	//1.Set bench to normal condition.
	//-----------------------------TEST STEP------------------------------//			
	CommentStep("Set All " + ObjectType + " to normal Status.");		
	// SetObjectFunc(ObjectType,"AllNormal");
	
	//1.2.Verify no DTC present.
	//-----------------------------TEST STEP------------------------------//
	CommentSubStep("Verify no DTC present.");
	var ret = ActualResults(); 
	CompareResultsDefine(ret,"OFF","None");
	Thread.Sleep(2000);
	
	for(var Fault in  ObjectFault)
	{
		
		// if this Fault is not Defined, it means not support
		if(Test_Object[Fault] !=undefined && Test_Object[Fault] != "undefined" && Fault != "CFG")
		{
			var FaultCycleTime = ObjectFault[Fault];
			// Check DTC Qualify
			CAN.SetDiagnosticAdressingMode(G_CAN_Channel,G_External_Phy_ID,G_External_Res_ID);
			CAN.StartLoggingToFile(StorePath[Fault][0],[G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]);

			//2.Test Fault Qualify
			//-----------------------------TEST STEP------------------------------//	
			CommentStep("Test " +Test_ObjectStr + " " + Fault + " Qualify" )
			

			//defined the time during which 19 02 AF shoud be send
			var DiagTime = int(Test_Object[Fault + "Qualify"][0]) + 3000;
			var HighRange = int(Test_Object[Fault + "Qualify"][1]);
			var LowRange = int(Test_Object[Fault + "Qualify"][0]);

			//2.1 Set Test_ObjectStr to Normal: " + Test_Object["Normal"]
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Set " + Test_ObjectStr + " to Normal: " + Test_Object["Normal"]);
			SetObjectFunc(Test_ObjectStr,"Normal");
			
			//2.2 Verify no DTC present.
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify no DTC present.");
			Thread.Sleep(DiagTime);
			var ret = ActualResults(); 
			CompareResultsDefine(ret,"OFF","None");
			
			

			//2.3."Set Sensor to Open Fault"
			//-----------------------------TEST STEP------------------------------//		
			CommentSubStep("Set " + Test_ObjectStr + " to "+  Fault);	
			SetObjectFunc(Test_ObjectStr,Fault);

			//2.4.Set Marked Frame
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Set Marked Frame then send 19 02 AF Repeatly ");
			SentMarkedFrame();

			//.Sent 19 02 AF Repeatly 
			//-----------------------------TEST STEP------------------------------//
			SendDiagPerodic(DiagTime)	


			//2.5.Verify Specific DCT present
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Active After Fault Qualifyed.");
			var ret = ActualResults(); 
			var FaultInfo_Str = "";
			var WL = "";
			if(Fault != "CrossC")
			{
				FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-ACTIVE@");
				
			}
			else
			{
				var CrossC_SelectObj = G_${ObjectType}CrossC_SelectObj;
				var DTC = Test_Object[Fault+"DTC"] + "," + CrossC_SelectObj["CrossCDTC"];
				FaultInfo_Str = SplitFaultInfo(DTC,"-ACTIVE@");
			}
			var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
			FaultInfo_Str = ReturnValue[0];
			WL = ReturnValue[1];
			CompareResultsDefine(ret,WL,FaultInfo_Str);
			
			
			CAN.StopLogging();


			//2.6.Verify Specific DCT present
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Active After IG.");
			IGNRestartWaitLampCheck();
			var ret = ActualResults(); 
			CompareResultsDefine(ret,WL,FaultInfo_Str);

			//2.7.Check the DTC Qualified Time
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Check the " + Fault + "DTC Qualified Time.");
			if(HighRange != 0)//only filled the low range data, it means don't need check the qualify time
			{
				var FaultInfoList = FaultInfo_Str.split(",");
				for(var i = 0; i < FaultInfoList.length; i++)
				{
					CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][0],FaultInfoList[i],LowRange,HighRange);
				}
			}
			

			// // Check DTC DisQualify
			CAN.SetDiagnosticAdressingMode(G_CAN_Channel,G_External_Phy_ID,G_External_Res_ID);
			CAN.StartLoggingToFile(StorePath[Fault][1],[G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]);

			//2.8.Test Fault Qualify
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Test " +Test_ObjectStr + " " + Fault + " DisQualify" )
			//defined the time during which 19 02 AF shoud be send
			var DiagTime = int(Test_Object[Fault + "DisQualify"][0]) + 3000;
			var HighRange = int(Test_Object[Fault + "DisQualify"][1]);
			var LowRange = int(Test_Object[Fault + "DisQualify"][0]);



			//2.9.Set Test_ObjectStr to Normal: " + Test_Object["Normal"]
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Set " + Test_ObjectStr + "to Normal: " + Test_Object["Normal"]);
			SetObjectFunc(Test_ObjectStr,"Normal");
			

			
			//2.10.Verify Specific DCT present
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC ACTIVE After Fault condition had been removed after 2000ms.");
			Thread.Sleep(DiagTime)
			var ret = ActualResults(); 
			var FaultInfo_Str = "";
			var WL = "";
			if(Fault != "CrossC")
			{
				FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-ACTIVE@");
				
			}
			else
			{
				var CrossC_SelectObj = G_${ObjectType}CrossC_SelectObj;
				var DTC = Test_Object[Fault+"DTC"] + "," + CrossC_SelectObj["CrossCDTC"];
				FaultInfo_Str = SplitFaultInfo(DTC,"-ACTIVE@");
			}
			var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
			FaultInfo_Str = ReturnValue[0];
			WL = ReturnValue[1];
			CompareResultsDefine(ret,WL,FaultInfo_Str);
			
			//2.11.IG Restart wait LampCheck
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("IG Restart wait LampCheck");
			IGNRestartWaitLampCheck();



			//2.12.Verify Specific DCT present
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC HISTORIC After Fault DisQualifyed after IG Restart.");
			Thread.Sleep(DiagTime)
			var ret = ActualResults(); 
			var FaultInfo_Str = "";
			var WL = "";
			if(Fault != "CrossC")
			{
				FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@IG_");
				
			}
			else
			{
				var CrossC_SelectObj = G_${ObjectType}CrossC_SelectObj;
				var DTC = Test_Object[Fault+"DTC"] + "," + CrossC_SelectObj["CrossCDTC"];
				FaultInfo_Str = SplitFaultInfo(DTC,"-HISTORIC@IG_");
			}
			var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
			FaultInfo_Str = ReturnValue[0];
			WL = ReturnValue[1];
			CompareResultsDefine(ret,WL,FaultInfo_Str);
			
			CAN.StopLogging();

			
			//2.13.IG Restart wait LampCheck
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("IG Restart wait LampCheck");
			IGNRestartWaitLampCheck();
			var ret = ActualResults(); 
			CompareResultsDefine(ret,WL,FaultInfo_Str);

			//2.14.Clear All DTC
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Clear All DTC");
			ClearDTC();
			Thread.Sleep(DiagTime);

			//2.15 Verify  no any DTC
			//-----------------------------TEST STEP------------------------------//		
			CommentSubStep("Verify  no any DTC");
			var ret = ActualResults(); 
			CompareResultsDefine(ret,"OFF","NONE");
						
		}
		
	}
	 
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