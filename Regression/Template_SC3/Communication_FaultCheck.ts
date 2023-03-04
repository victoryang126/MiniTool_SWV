// ******************************************************************************************
// **************************Veoneer Electronics document************************************
// ******************************************************************************************
// Result Test:
// *******************************************************
               // Script Information
// *******************************************************
// Test case ID: LOST_INVALID_Communication
// *******************************************************
// Full Automation: Yes
// *******************************************************

//
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

var Test_ObjectStr = "${TestObjectStr}";
var Test_Object = ${TestObjectStr};
var StorePathLostComm = ["",""];
var FaultCycleTime = Test_Object['CycleTime'];
// get the current default value from CAN
var MSgID = int(Test_Object["MsgID"])
 var DefaultFrame = CAN.ReceiveMostRecentFrame(MSgID)[1];
 Test_Object["DefaultFrame"] = StrFrame2ByteFrame(DefaultFrame.split(" "))
StorePathLostComm[0] = G_PathArray[3] + "Regression\\"+ "CANC_" + Test_ObjectStr + "_LostComm_Qualify.log";
StorePathLostComm[1] = G_PathArray[3] +  "Regression\\"+ "CANC_" + Test_ObjectStr + "_LostComm_DisQualify.log";




var StorePathInvalidDlc = ["",""];
StorePathInvalidDlc[0] = G_PathArray[3] +  "Regression\\"+ "CANC_" + Test_ObjectStr + "_InvalidDlc_Qualify.log";
StorePathInvalidDlc[1] = G_PathArray[3] +  "Regression\\"+ "CANC_" + Test_ObjectStr + "_InvalidDlc_DisQualify.log";


// *******************************************************
               // Parameter Initilize
// *******************************************************

  
// *******************************************************
               // Define/Re-Define parameters
// *******************************************************

// *******************************************************
               // Test Steps
// *******************************************************
if(CheckTestEnvironment())
// if(1)
{

   // --------------------------------------------------------------------//
            //Lost Communication Fault
   // --------------------------------------------------------------------//
    if(Test_Object["LostComm"] != "undefined")
    {
        var Fault = "LostComm";
        var ExpectDTC = Test_Object[Fault + "DTC"];
			//defined the time during which 19 02 AF shoud be send
        var DiagTime = int(Test_Object[Fault + "Qualify"][0]) + 3000;
        var HighRange = int(Test_Object[Fault + "Qualify"][1]);
        var LowRange = int(Test_Object[Fault + "Qualify"][0]);

        //1.0.Test Fault Qualify
        //-----------------------------TEST STEP------------------------------//
        CommentStep("Test " +Test_ObjectStr + " " + Fault + " Qualify" )
        SetDiagTarget(G_External_Phy_Diag_Channel);
        G_CANID_Filter = [Test_Object["MsgID"],G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]
		StartToLog(StorePathLostComm[0])
  

        //1.1 Stop to send Msg
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Stop to send " + Test_ObjectStr);
        SetMsgConditions(Test_ObjectStr,Fault,0)
        SentMarkedFrame();

        //1.2 Send Marked Frame and 19 02 AF repeatly
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Send Marked Frame and 19 02 AF repeatly");

        SendDiagPerodic(DiagTime);
        //1.3.Verify Specific DCT present
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Active After Fault Qualifyed.");
        var ret = ActualResults(); 
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-ACTIVE@");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);


         //1.4.IG restart
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Active After IG restart.");
        IGNRestartWaitLampCheck()
        var ret = ActualResults(); 
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-ACTIVE@");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);

        //Stop to log
        StopToLog();
        //1.5 Check the DTC Qualified Time
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Check the " + Test_ObjectStr + " " + Fault + "DTC Qualified Time.");
        if(HighRange != 0)//only filled the low range data, it means don't need check the qualify time
        {
            var FaultInfoList = FaultInfo_Str.split(",");
            for(var i = 0; i < FaultInfoList.length; i++)
            {
                CheckDTCQualifyOrDisQualifyTime(StorePathLostComm[0],FaultInfoList[i],LowRange,HighRange);
            }
        }
        

        //1.6Test Fault DisQualify
        var DiagTime = int(Test_Object[Fault + "DisQualify"][0]) + 3000;
        var HighRange = int(Test_Object[Fault + "DisQualify"][1]);
        var LowRange = int(Test_Object[Fault + "DisQualify"][0]);

        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Test " +Test_ObjectStr + " " + Fault + " DisQualify" )
        SetDiagTarget(G_External_Phy_Diag_Channel);
        G_CANID_Filter = [Test_Object["MsgID"],G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]
		StartToLog(StorePathLostComm[1])


        //1.7 Start to send Msg
        //-----------------------------TEST STEP------------------------------//
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Reload " + Test_ObjectStr + " to normal status");
        SetMsgConditions(Test_ObjectStr,"Normal","");
        SentMarkedFrame();

        //1.8 Send Marked Frame and 19 02 AF repeatly
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Send Marked Frame and 19 02 AF repeatly");

        SendDiagPerodic(DiagTime);
        //1.9.Verify Specific DCT present
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Historic After Fault DisQualifyed.");
        var ret = ActualResults(); 
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);



        //1.10.Verify Specific DCT present
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Historic After IG restart");
        IGNRestartWaitLampCheck()
        var ret = ActualResults(); 
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@IG_");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);



        //1.11.Verify Specific DCT present
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Historic After IG restart");
        IGNRestartWaitLampCheck()
        var ret = ActualResults(); 
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@2IG_");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);
    
    
        StopToLog();

        //1.12.Check the DTC DisQualified Time
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Check the " + Fault + "DTC DisQualified Time.");
        // CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][1],Test_Object[Fault+"DTC"] + "-HISTORIC",LowRange,HighRange);
        if(HighRange != 0)
        {
            var FaultInfoList = FaultInfo_Str.split(",");
            for(var i = 0; i < FaultInfoList.length; i++)
            {
                CheckDTCQualifyOrDisQualifyTime(StorePathLostComm[1],FaultInfoList[i],LowRange,HighRange);
            }
        }

        //1.13.Clear All DTC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Clear All DTC");
        ClearDTC();
        Thread.Sleep(6000);

        //1.14 Verify  no any DTC
        //-----------------------------TEST STEP------------------------------//		
        CommentSubStep("Verify  no any DTC");
        var ret = ActualResults(); 
        var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
        CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])
    }
    else
    {
        var Fault = "LostComm";

        //1.0.Test Fault Qualify
        //-----------------------------TEST STEP------------------------------//
        CommentStep("Test " +Test_ObjectStr + " no " + Fault + " Qualify" )
        SetDiagTarget(G_External_Phy_Diag_Channel);
        G_CANID_Filter = [Test_Object["MsgID"],G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]
		StartToLog(StorePathLostComm[0])



        //1.1 Stop to send Msg
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Stop to send " + Test_ObjectStr);
        SetMsgConditions(Test_ObjectStr,Fault,0)
        Thread.Sleep(10000);


         //1.2 Verify  no any DTC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify  no any DTC");
        var ret = ActualResults();
    	var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
        CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])


         //1.3 Start to send Msg
        //-----------------------------TEST STEP------------------------------//
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Reload " + Test_ObjectStr + " to normal status");
        SetMsgConditions(Test_ObjectStr,"Normal","");
        Thread.Sleep(10000);

         //1.4.Clear All DTC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Clear All DTC");
        ClearDTC();
        Thread.Sleep(6000);

        //1.5 Verify  no any DTC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify  no any DTC");
        var ret = ActualResults();
        var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
        CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])


    }
    //--------------------------------------------------------------------//
            //Invalid DLC
    //--------------------------------------------------------------------//

    if(Test_Object["InValidDlc"] != "undefined")
    {
        var Fault = "InValidDlc";
        var ExpectDTC = Test_Object[Fault + "DTC"];
        var DiagTime = int(Test_Object[Fault + "Qualify"][0]) + 3000;
        var HighRange = int(Test_Object[Fault + "Qualify"][1]);
        var LowRange = int(Test_Object[Fault + "Qualify"][0]);


        //2.0.Test Fault Qualify
        //-----------------------------TEST STEP------------------------------//
        CommentStep("Test " +Test_ObjectStr + " " + Fault + " Qualify" )
        SetDiagTarget(G_External_Phy_Diag_Channel);
        G_CANID_Filter = [Test_Object["MsgID"],G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]
		StartToLog(StorePathInvalidDlc[0])

        //2.1 Set a Invalid DLC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep(" set " + Test_ObjectStr + " to a Invald DLC");
        SetMsgConditions(Test_ObjectStr,Fault,"");
        SentMarkedFrame()

        //2.2 Send Marked Frame and 19 02 AF repeatly
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Send Marked Frame and 19 02 AF repeatly");

        SendDiagPerodic(DiagTime);
        //2.3.Verify Specific DCT present
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Active After Fault Qualifyed.");
        var ret = ActualResults();
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-ACTIVE@");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);



        //2.4Verify Specific DCT present
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Active After IG restart.");
        IGNRestartWaitLampCheck()
        var ret = ActualResults();
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-ACTIVE@");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);

        //Stop to log
        StopToLog();
        //2.5 Check the DTC Qualified Time
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Check the " + Test_ObjectStr + " " + Fault + "DTC Qualified Time.");
        if(HighRange != 0)//only filled the low range data, it means don't need check the qualify time
        {
            var FaultInfoList = FaultInfo_Str.split(",");
            for(var i = 0; i < FaultInfoList.length; i++)
            {
                CheckDTCQualifyOrDisQualifyTime(StorePathInvalidDlc[0],FaultInfoList[i],LowRange,HighRange);
            }
        }


        //2.6.Test Fault DisQualify

        var DiagTime = int(Test_Object[Fault + "DisQualify"][0]) + 3000;
        var HighRange = int(Test_Object[Fault + "DisQualify"][1]);
        var LowRange = int(Test_Object[Fault + "DisQualify"][0]);
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Test " +Test_ObjectStr + " " + Fault + " DisQualify" )
        SetDiagTarget(G_External_Phy_Diag_Channel);
        G_CANID_Filter = [Test_Object["MsgID"],G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]
		StartToLog(StorePathInvalidDlc[1])


        //2.7 Reload Default
        //-----------------------------TEST STEP------------------------------//
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Reload " + Test_ObjectStr + " to normal status");
        SetMsgConditions(Test_ObjectStr,"Normal","");
        SentMarkedFrame();

        //2.8 Send Marked Frame and 19 02 AF repeatly
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Send Marked Frame and 19 02 AF repeatly");

        SendDiagPerodic(DiagTime);
        //2.9.Verify Specific DCT present
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Historic After Fault DisQualifyed.");
        IGNRestartWaitLampCheck()
        var ret = ActualResults();
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);


         //2.10.Verify Specific DCT present
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Historic After Fault DisQualifyed.");
        IGNRestartWaitLampCheck()
        var ret = ActualResults();
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@IG_");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);



        
         //2.11.Verify Specific DCT present
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Historic After Fault DisQualifyed.");
        var ret = ActualResults();
        var FaultInfo_Str = "";
        var WL = "";
        FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@2IG_");
        var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
        FaultInfo_Str = ReturnValue[0];
        WL = ReturnValue[1];
        CompareResultsDefine(ret,WL,FaultInfo_Str);

        StopToLog();

        //2.12.Check the DTC DisQualified Time
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Check the " + Fault + "DTC DisQualified Time.");
        // CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][1],Test_Object[Fault+"DTC"] + "-HISTORIC",LowRange,HighRange);
        if(HighRange != 0)
        {
            var FaultInfoList = FaultInfo_Str.split(",");
            for(var i = 0; i < FaultInfoList.length; i++)
            {
                CheckDTCQualifyOrDisQualifyTime(StorePathInvalidDlc[1],FaultInfoList[i],LowRange,HighRange);
            }
        }

        //2.13.Clear All DTC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Clear All DTC");
        ClearDTC();
        Thread.Sleep(6000);

        //2.14 Verify  no any DTC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify  no any DTC");
        var ret = ActualResults();
        var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
        CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])
    }
    else
    {
        var Fault = "InValidDlc";

        Test_Object["InValidDlc"] = int(Test_Object["MsgDLC"]) - 1;

        //2.0.Test Fault Qualify
        //-----------------------------TEST STEP------------------------------//
        CommentStep("Test " +Test_ObjectStr + " no " + Fault + " Qualify" )
        SetDiagTarget(G_External_Phy_Diag_Channel);
        G_CANID_Filter = [Test_Object["MsgID"],G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]
		StartToLog(StorePathInvalidDlc[0])


        //2.1 Set a Invalid DLC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep(" set " + Test_ObjectStr + " to a Invald DLC");
        SetMsgConditions(Test_ObjectStr,Fault,"");;
        Thread.Sleep(10000);


         //2.2 Verify  no any DTC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify  no any DTC");
        var ret = ActualResults();
        var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
        CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])


         //2.3 Start to send Msg
        //-----------------------------TEST STEP------------------------------//
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Reload " + Test_ObjectStr + " to normal status");
        SetMsgConditions(Test_ObjectStr,"Normal","");
        Thread.Sleep(10000);

         //2.4.Clear All DTC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Clear All DTC");
        ClearDTC();
        Thread.Sleep(6000);

        //2.5 Verify  no any DTC
        //-----------------------------TEST STEP------------------------------//
        CommentSubStep("Verify  no any DTC");
        var ret = ActualResults();
        var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
        CompareResultsDefine(ret,Expect_Fault_Info[1],Expect_Fault_Info[0])


    }
    //--------------------------------------------------------------------//
            //Invalid Signal
    //--------------------------------------------------------------------//
    //first loop the array in the InValidSg
    for(var i in Test_Object["InValidSg"])
    {
        var TestGroup = Test_Object["InValidSg"][i];
        var Signal = TestGroup[0];
        var SignalValueList = TestGroup[1];
        var DTCName = TestGroup[2]
        for( var j in SignalValueList)
        {
            var SignalValue = SignalValueList[j];
            var InValidSgStorePath = new Array();
            InValidSgStorePath[0] = G_PathArray[3] +  "Regression\\"+ "CANC_" + Test_ObjectStr + "_" + Signal + "_" + SignalValue + "_InvalidSg_Qualify.log"
            InValidSgStorePath[1] = G_PathArray[3] +  "Regression\\"+ "CANC_" + Test_ObjectStr + "_" + Signal + "_" + SignalValue + "_InvalidSg_DisQualify.log"

            if(DTCName != 'undefined' && Signal !='undefined')
            {
                var Fault = "InValidSg";
                var ExpectDTC = Test_Object[Fault + "DTC"];
                var DiagTime = int(TestGroup[3][0]) + 3000;
                var HighRange = int(TestGroup[3][1]);
                var LowRange = int(TestGroup[3][0]);
                Test_Object[Fault+"DTC"] = DTCName;
                // RESULT.InsertComment(Fault + "Qualify")
                //3.0.Test Fault Qualify
                //-----------------------------TEST STEP------------------------------//
                CommentStep("Test " + Test_ObjectStr + " " + Fault + " Qualify" + " with set " + Signal + " InValidValue " + SignalValue)
                SetDiagTarget(G_External_Phy_Diag_Channel);
                G_CANID_Filter = [Test_Object["MsgID"],G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]
                StartToLog(InValidSgStorePath[0])
       

                //3.1 Set to Invalid Signal
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Set " + Test_ObjectStr + "Invalid Signal value "  + SignalValue);
                SetMsgConditions(Test_ObjectStr,Fault,Signal,SignalValue);
                SentMarkedFrame();

                //3.2 Send Marked Frame and 19 02 AF repeatly
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Send Marked Frame and 19 02 AF repeatly");
                SendDiagPerodic(DiagTime);


                //3.3.Verify Specific DCT present
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Active After Fault Qualifyed.");

                var ret = ActualResults();
                var FaultInfo_Str = "";
                var WL = "";
                FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-ACTIVE@");
                var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
                FaultInfo_Str = ReturnValue[0];
                WL = ReturnValue[1];
                CompareResultsDefine(ret,WL,FaultInfo_Str);
                //3.4.Verify Specific DCT present
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Active After IG Restart");
                IGNRestartWaitLampCheck()
                var ret = ActualResults();
                var FaultInfo_Str = "";
                var WL = "";
                FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-ACTIVE@");
                var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
                FaultInfo_Str = ReturnValue[0];
                WL = ReturnValue[1];
                CompareResultsDefine(ret,WL,FaultInfo_Str);

                //Stop to log
                StopToLog();
                //3.5 Check the DTC Qualified Time
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Check the " + Test_ObjectStr + " " + Fault + "DTC Qualified Time.");
                if(HighRange != 0)//only filled the low range data, it means don't need check the qualify time
                {
                    var FaultInfoList = FaultInfo_Str.split(",");
                    for(var i = 0; i < FaultInfoList.length; i++)
                    {
                        CheckDTCQualifyOrDisQualifyTime(InValidSgStorePath[0],FaultInfoList[i],LowRange,HighRange);
                    }
                }


                //3.6.Test Fault DisQualify


                var DiagTime = int(TestGroup[4][0]) + 3000;
                var HighRange = int(TestGroup[4][1]);
                var LowRange = int(TestGroup[4][0]);
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Test " + Test_ObjectStr + " " + Fault + " DisQualify" + " with set " + Signal + " InValidValue" )
                SetDiagTarget(G_External_Phy_Diag_Channel);
                G_CANID_Filter = [Test_Object["MsgID"],G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]
                StartToLog(InValidSgStorePath[1])
       


                //3.7 Reload to Msg normal status
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Reload " + Test_ObjectStr + " to normal status");
                SetMsgConditions(Test_ObjectStr,"Normal","");
                SentMarkedFrame()

                //3.8 Send Marked Frame and 19 02 AF repeatly
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Send Marked Frame and 19 02 AF repeatly");

                SendDiagPerodic(DiagTime);
                //3.9.Verify Specific DCT present
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Historic After Fault DisQualifyed.");
                var ret = ActualResults();
                var FaultInfo_Str = "";
                var WL = "";
                FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@");
                var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
                FaultInfo_Str = ReturnValue[0];
                WL = ReturnValue[1];
                CompareResultsDefine(ret,WL,FaultInfo_Str);



                //3.10.Verify Specific DCT present
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Historic After Fault DisQualifyed.");
                IGNRestartWaitLampCheck()
                var ret = ActualResults();
                var FaultInfo_Str = "";
                var WL = "";
                FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@IG_");
                var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
                FaultInfo_Str = ReturnValue[0];
                WL = ReturnValue[1];
                CompareResultsDefine(ret,WL,FaultInfo_Str);




                //3.11.Verify Specific DCT present
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Verify " + Test_ObjectStr + " " + Fault + "DTC Historic After Fault DisQualifyed.");
                var ret = ActualResults();
                var FaultInfo_Str = "";
                var WL = "";
                FaultInfo_Str = SplitFaultInfo(Test_Object[Fault+"DTC"],"-HISTORIC@2IG_");
                var ReturnValue = SetSuffixToFaultInfo(FaultInfo_Str);
                FaultInfo_Str = ReturnValue[0];
                WL = ReturnValue[1];
                CompareResultsDefine(ret,WL,FaultInfo_Str);

                StopToLog();

                //3.12.Check the DTC DisQualified Time
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Check the " + Fault + "DTC DisQualified Time.");
                // CheckDTCQualifyOrDisQualifyTime(StorePath[Fault][1],Test_Object[Fault+"DTC"] + "-HISTORIC",LowRange,HighRange);
                if(HighRange != 0)
                {
                    var FaultInfoList = FaultInfo_Str.split(",");
                    for(var i = 0; i < FaultInfoList.length; i++)
                    {
                        CheckDTCQualifyOrDisQualifyTime(InValidSgStorePath[1],FaultInfoList[i],LowRange,HighRange);
                    }
                }

                //3.13.Clear All DTC
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Clear All DTC");
                ClearDTC();
                Thread.Sleep(6000);

                //3.14 Verify  no any DTC
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Verify  no any DTC");
                var ret = ActualResults();
                var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
                CompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0])
            }
            else if(DTCName == 'undefined' && Signal !='undefined')
            {
                var Fault = "InValidSg";
                //3.0.Test Fault Qualify
                //-----------------------------TEST STEP------------------------------//
                CommentStep("Test " + Test_ObjectStr + " no " + Fault + " Qualify" + " with set " + Signal + " InValidValue " + SignalValue)
                SetDiagTarget(G_External_Phy_Diag_Channel);
                G_CANID_Filter = [Test_Object["MsgID"],G_Mask_ID,G_External_Phy_ID,G_External_Res_ID]
                StartToLog(InValidSgStorePath[0])
       


                //3.1 Set to Invalid Signal
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Set " + Test_ObjectStr + "Invalid Signal value " + SignalValue);
                SetMsgConditions(Test_ObjectStr,Fault,Signal,SignalValue);
                Thread.Sleep(10000);


                 //3.2 Verify  no any DTC
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Verify  no any DTC");
                var ret = ActualResults();
                var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
                CompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0])


                 //3.3 Start to send Msg
                //-----------------------------TEST STEP------------------------------//
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Reload " + Test_ObjectStr + " to normal status");
                SetMsgConditions(Test_ObjectStr,"Normal","");
                Thread.Sleep(10000);

                 //3.4.Clear All DTC
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Clear All DTC");
                ClearDTC();
                Thread.Sleep(6000);

                //3.5 Verify  no any DTC
                //-----------------------------TEST STEP------------------------------//
                CommentSubStep("Verify  no any DTC");
                var ret = ActualResults();
                var Expect_Fault_Info = SetSuffixToFaultInfo("NONE") 
                CompareResultsDefine(Ret,Expect_Fault_Info[1],Expect_Fault_Info[0])
                StopToLog();

            }


        }

    }

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