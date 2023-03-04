
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

	
	
	for(var Fault in  ObjectFault)
	{
		
		// if this Fault is not Defined, it means not support
		if(Test_Object[Fault] !=undefined && Test_Object[Fault] != "undefined" && Fault != "CFG")
		{
			var FaultCycleTime = ObjectFault[Fault];
			// Check DTC Qualify
			SetDiagTarget(G_External_Phy_Diag_Channel);
			StartToLog(StorePath[Fault][0])


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
			
			//1.2 Verify no DTC present.
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify no DTC present.");
			var ret = ActualResults(); 
			var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
			CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])
			Thread.Sleep(2000);
			

			//2.3."Set Sensor to Open Fault"
			//-----------------------------TEST STEP------------------------------//		
			CommentSubStep("Set " + Test_ObjectStr + " to "+  Fault + " and then send Marked Frame");	
			SetObjectFunc(Test_ObjectStr,Fault);
			SentMarkedFrame();
			//2.4.Set Marked Frame
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep( "send 19 02 AF Repeatly ");
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

			StopToLog();


			//2.6.Verify Specific DCT present
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Active After IG Restart.");
			IGNRestartWaitLampCheck()
			var ret = ActualResults(); 
			CompareResultsDefine(ret,WL,FaultInfo_Str);

			//2.7.Check the DTC Qualified Time
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Check the " + Fault + "DTC Qualified Time.");
			// CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][0],Test_Object[Fault+"DTC"] + "-ACTIVE",LowRange,HighRange);
			if(HighRange != 0)//only filled the low range data, it means don't need check the qualify time
			{
				var FaultInfoList = FaultInfo_Str.split(",");
				for(var i = 0; i < FaultInfoList.length; i++)
				{
					CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][0],FaultInfoList[i],LowRange,HighRange);
				}
			}
			

			// // Check DTC DisQualify
			SetDiagTarget(G_External_Phy_Diag_Channel);
			StartToLog(StorePath[Fault][1])


			//2.8.Test Fault Qualify
			//-----------------------------TEST STEP------------------------------//
			CommentStep("Test " +Test_ObjectStr + " " + Fault + " DisQualify" )	
			//defined the time during which 19 02 AF shoud be send

			var DiagTime = int(Test_Object[Fault + "DisQualify"][0]) + 3000;
			var HighRange = int(Test_Object[Fault + "DisQualify"][1]) ;
			var LowRange = int(Test_Object[Fault + "DisQualify"][0]) ;


			//2.9.Set Test_ObjectStr to Normal: " + Test_Object["Normal"]
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Set " + Test_ObjectStr + "to Normal: " + Test_Object["Normal"] + " and then send makred Frame");
			if(Fault != "CrossC")
			{
				SetObjectFunc(Test_ObjectStr,"Normal");
			}
			else
			{
				var CrossC_SelectStr = G_${ObjectType}CrossC_SelectStr;
				SetObjectFunc(Test_ObjectStr,"Normal");
				SetObjectFunc(CrossC_SelectStr,"Normal")
			}
			SentMarkedFrame();
			
			//2.10.Sent 19 02 08 Repeatly
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep(" send 19 02 AF Repeatly ");
			SendDiagPerodic(DiagTime)	


			//2.11.Verify Specific DCT present
			//-----------------------------TEST STEP------------------------------//	
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC HISTORIC After Fault DisQualifyed.");
			var ret = ActualResults(); 
			//if set to CorssC Fault, need check two DTC
			var ret = ActualResults(); 
			var FaultInfo_Str = "";
			var WL = "";
			if(Fault != "CrossC")
			{
				FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@");
				
			}
			else
			{
				var CrossC_SelectObj = G_${ObjectType}CrossC_SelectObj;
				var DTC = Test_Object[Fault+"DTC"] + "," + CrossC_SelectObj["CrossCDTC"];
				FaultInfo_Str = SplitFaultInfo(DTC,"-HISTORIC@");
			}
			var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
			FaultInfo_Str = ReturnValue[0];
			WL = ReturnValue[1];
			CompareResultsDefine(ret,WL,FaultInfo_Str);
		
			StopToLog();

			//2.12.Verify Specific DCT present
			//-----------------------------TEST STEP------------------------------//	
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC HISTORIC IG After Fault IG Restart");
			IGNRestartWaitLampCheck()
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



			//2.13.Verify Specific DCT present
			//-----------------------------TEST STEP------------------------------//	
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC HISTORIC IG After Fault IG Restart");
			IGNRestartWaitLampCheck()
			var ret = ActualResults(); 
			var FaultInfo_Str = "";
			var WL = "";
			if(Fault != "CrossC")
			{
				FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@2IG_");
				
			}
			else
			{
				var CrossC_SelectObj = G_${ObjectType}CrossC_SelectObj;
				var DTC = Test_Object[Fault+"DTC"] + "," + CrossC_SelectObj["CrossCDTC"];
				FaultInfo_Str = SplitFaultInfo(DTC,"-HISTORIC@2IG_");
			}
			var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
			FaultInfo_Str = ReturnValue[0];
			WL = ReturnValue[1];
			CompareResultsDefine(ret,WL,FaultInfo_Str);

			//2.14.Check the DTC DisQualified Time
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Check the " + Fault + "DTC DisQualified Time.");
			// CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][1],Test_Object[Fault+"DTC"] + "-HISTORIC",LowRange,HighRange);
			if(HighRange != 0)
			{
				var FaultInfoList = FaultInfo_Str.split(",");
				for(var i = 0; i < FaultInfoList.length; i++)
				{
					CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][1],FaultInfoList[i],LowRange,HighRange);
				}
			}
			
			//2.15.Clear All DTC
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Clear All DTC");
			ClearDTC()
			Thread.Sleep(6000);

			//2.16 Verify  no any DTC
			//-----------------------------TEST STEP------------------------------//		
			CommentSubStep("Verify  no any DTC");
			var ret = ActualResults(); 
			var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
			CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])
						
		}
		else if((Test_Object[Fault] == undefined || Test_Object[Fault] == "undefined") && Fault!= "CFG" )
		{
			SetDiagTarget(G_External_Phy_Diag_Channel);
			StartToLog(StorePath[Fault][0])


			//2. Test " +Test_ObjectStr + " Not Support " + Fault
			//-----------------------------TEST STEP------------------------------//	
			CommentStep("Test " +Test_ObjectStr + " Not Support " + Fault  )

			//2.1  "Set " + Test_ObjectStr + " to (not support) "+  Fault
			//-----------------------------TEST STEP------------------------------//		
			CommentSubStep("Set " + Test_ObjectStr + " to (not support) "+  Fault);	
			SetObjectFunc(Test_ObjectStr,Fault);
			
			//2.2 "Waiting for 10000ms"
			//-----------------------------TEST STEP------------------------------//		
			CommentSubStep("Waiting for 10000ms to wating for DTC Qualfiy if support");	
			Thread.Sleep(10000);

			//2.3 "Waiting for 10000ms"
			//-----------------------------TEST STEP------------------------------//		
			CommentSubStep("Verify " + Test_ObjectStr + " not Support  " + Fault + " So no any DTC");
			var ret = ActualResults(); 
			var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
			CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])


			//2.4.Set Test_ObjectStr to Normal: " + Test_Object["Normal"]
			//-----------------------------TEST STEP------------------------------//
			CommentSubStep("Set " + Test_ObjectStr + "to Normal: " + Test_Object["Normal"]);
			if(Fault != "CrossC")
			{
				SetObjectFunc(Test_ObjectStr,"Normal");
			}
			else
			{
				var NSCrossC_SelectStr = G_${ObjectType}NSCrossC_SelectStr;
				SetObjectFunc(Test_ObjectStr,"Normal");
				SetObjectFunc(NSCrossC_SelectStr,"Normal")
			}


			//2.5 Verify  no any DTC
			//-----------------------------TEST STEP------------------------------//		
			CommentSubStep("Verify  no any DTC");
			var ret = ActualResults(); 
			var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
			CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])
			
			StopToLog();
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