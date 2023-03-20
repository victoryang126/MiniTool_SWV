Func = """
function BB_Check_ParameterValue(Action,ParameterValue,DataRecord,Start,Length)
{
	var parameterValue_List2Str = BB_InsertValue2List(ParameterValue,Length)
	var expectStart = 0
    while(Length>0)
    {
        var tempLength = Length > 50?50:Length
        // RESULT.InsertComment(TempLength)
        BB_CompareIgnoreH(Action,BB_GetValueFromStirng(DataRecord,Start +3,tempLength),BB_GetValueFromStirng(parameterValue_List2Str,expectStart,tempLength));
        Start = Start + tempLength
        Length = Length - tempLength
		expectStart = expectStart + tempLength
    }
}

function BB_Check_ParameterList(Action,ParameterValue_List,DataRecord,Start,Length)
{
	// RESULT.InsertComment(ParameterValue_List)

	var expectStart = 0
	var parameterValue_List2Str = ParameterValue_List.toString().replace(/,/gi," ");
    while(Length>0)
    {
        var tempLength = Length > 50?50:Length
        // RESULT.InsertComment(tempLength)
        BB_CompareIgnoreH(Action,BB_GetValueFromStirng(DataRecord,Start +3,tempLength),BB_GetValueFromStirng(parameterValue_List2Str,expectStart,tempLength));
        // RESULT.InsertComment(tempLength)
		Start = Start + tempLength
        Length = Length - tempLength
		expectStart = expectStart + tempLength
    }
}



function BB_InsertValue2List(ParameterValue,ArrLength)
{	
	var tempList = new Array()
	for(var i = 0; i < ArrLength; i++)
	{
		tempList[i] = ParameterValue
	}
	return tempList.toString().replace(/,/gi," ");
}




function BB_ReturnCompareResultIgnoreH(ActualData,ExpectData)
{
	
	//create a Reg that ignore the data represent by "H"
	var L_Temp = "^" +  ExpectData.replace(/H/gi,"\\S") + "$";
	// var L_Temp = ExpectData.replace(/H/gi,"\\S");
	var L_Reg = new RegExp(L_Temp,'gi')
	var L_Match = ActualData.match(L_Reg); //if get the match, it shall return an array which contains the matched data
	if(L_Match == null)//Fail.Can't get the match data
	{
		return false;
	}
	else //Pass
	{
		return true;
	}
}

function BB_CompareIgnoreH(Action,ActualResp,ExpectResp)
{
	
	if(BB_ReturnCompareResultIgnoreH(ActualResp,ExpectResp))
	{
		RESULT.LogCustomAction(Action, ActualResp, ExpectResp, TestStatus.Passed);
	}
	else
	{
		RESULT.LogCustomAction(Action, ActualResp + "->Length->" + ActualResp.length, ExpectResp+ "->Length->" + ExpectResp.length, TestStatus.Failed);
	}
	

}

function BB_GetValueFromStirng(DiagValue,LowIndex,ArrLength)
{
    // RESULT.InsertComment(5)
	var tempList = new Array()
	var diagValueList = DiagValue.split(" ")
	var j = 0;
	for(var i = LowIndex; i < LowIndex + ArrLength; i++)
	{
		tempList[j] = diagValueList[i]
		j++;
	}
    // RESULT.InsertComment(tempList)
	return tempList.toString().replace(/,/gi," ");
}
"""