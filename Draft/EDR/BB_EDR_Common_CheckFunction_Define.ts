function BB_Check_GB_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_1 : DeltaVLgt_GB;
	var Action = "Check " + Type + " Value: DeltaVLgt_GB";
	var ParameterValue = DeltaVLgt_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 26 );

	// GEEA2_HX11_EDR_List_2 : MaxDeltaVLgt_GB;
	var Action = "Check " + Type + " Value: MaxDeltaVLgt_GB";
	var ParameterValue = MaxDeltaVLgt_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 1 );

	// GEEA2_HX11_EDR_List_3 : TimeMaxDeltaVLgt_GB;
	var Action = "Check " + Type + " Value: TimeMaxDeltaVLgt_GB";
	var ParameterValue = TimeMaxDeltaVLgt_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 27, 1 );

	// GEEA2_HX11_EDR_List_4 : AccClippingFlag_GB;
	var Action = "Check " + Type + " Value: AccClippingFlag_GB";
	var ParameterValue = AccClippingFlag_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 28, 2 );

	// GEEA2_HX11_EDR_List_5 : VehSpdLgt_GB;
	var Action = "Check " + Type + " Value: VehSpdLgt_GB";
	var ParameterValue = VehSpdLgt_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 30, 11 );

	// GEEA2_HX11_EDR_List_6 : BrkPedVal_GB;
	var Action = "Check " + Type + " Value: BrkPedVal_GB";
	var ParameterValue = BrkPedVal_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 41, 11 );

	// GEEA2_HX11_EDR_List_7 : BBSD_GB;
	var Action = "Check " + Type + " Value: BBSD_GB";
	var ParameterValue = BBSD_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 52, 1 );

	// GEEA2_HX11_EDR_List_8 : AccrPedRat_GB;
	var Action = "Check " + Type + " Value: AccrPedRat_GB";
	var ParameterValue = AccrPedRat_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 53, 11 );

	// GEEA2_HX11_EDR_List_9 : EngN_GB;
	var Action = "Check " + Type + " Value: EngN_GB";
	var ParameterValue = EngN_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 64, 11 );

	// GEEA2_HX11_EDR_List_10 : IG_Crash_GB;
	var Action = "Check " + Type + " Value: IG_Crash_GB";
	var ParameterValue = IG_Crash_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 75, 2 );

	// GEEA2_HX11_EDR_List_11 : IG_Read_GB;
	var Action = "Check " + Type + " Value: IG_Read_GB";
	var ParameterValue = IG_Read_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 77, 2 );

	// GEEA2_HX11_EDR_List_12 : CompletionStatus_GB;
	var Action = "Check " + Type + " Value: CompletionStatus_GB";
	var ParameterValue = CompletionStatus_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 79, 1 );

	// GEEA2_HX11_EDR_List_13 : TimeBtwEvents_GB;
	var Action = "Check " + Type + " Value: TimeBtwEvents_GB";
	var ParameterValue = TimeBtwEvents_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 80, 1 );

	// GEEA2_HX11_EDR_List_14 : VIN_GB;
	var Action = "Check " + Type + " Value: VIN_GB";
	var ParameterValue = VIN_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 81, 17 );

	// GEEA2_HX11_EDR_List_15 : HWN_GB ;
	var Action = "Check " + Type + " Value: HWN_GB ";
	var ParameterValue = HWN_GB ;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 98, 64 );

	// GEEA2_HX11_EDR_List_16 : SN_GB;
	var Action = "Check " + Type + " Value: SN_GB";
	var ParameterValue = SN_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 162, 64 );

	// GEEA2_HX11_EDR_List_17 : SWN_GB;
	var Action = "Check " + Type + " Value: SWN_GB";
	var ParameterValue = SWN_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 226, 64 );

	// GEEA2_HX11_EDR_List_18 : HighRateAccelLgt_GB;
	var Action = "Check " + Type + " Value: HighRateAccelLgt_GB";
	var ParameterValue = HighRateAccelLgt_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 290, 126 );

	// GEEA2_HX11_EDR_List_19 : HighRateAccelLat_GB;
	var Action = "Check " + Type + " Value: HighRateAccelLat_GB";
	var ParameterValue = HighRateAccelLat_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 416, 126 );

	// GEEA2_HX11_EDR_List_20 : DeltaVLat_GB;
	var Action = "Check " + Type + " Value: DeltaVLat_GB";
	var ParameterValue = DeltaVLat_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 542, 26 );

	// GEEA2_HX11_EDR_List_21 : MaxDeltaVLat_GB;
	var Action = "Check " + Type + " Value: MaxDeltaVLat_GB";
	var ParameterValue = MaxDeltaVLat_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 568, 1 );

	// GEEA2_HX11_EDR_List_22 : MaxResDeltaV_GB;
	var Action = "Check " + Type + " Value: MaxResDeltaV_GB";
	var ParameterValue = MaxResDeltaV_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 569, 2 );

	// GEEA2_HX11_EDR_List_23 : TimeMaxDeltaVLat_GB;
	var Action = "Check " + Type + " Value: TimeMaxDeltaVLat_GB";
	var ParameterValue = TimeMaxDeltaVLat_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 571, 1 );

	// GEEA2_HX11_EDR_List_24 : TimeMaxResDeltaV_GB;
	var Action = "Check " + Type + " Value: TimeMaxResDeltaV_GB";
	var ParameterValue = TimeMaxResDeltaV_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 572, 1 );

	// GEEA2_HX11_EDR_List_25 : YawRate_GB ;
	var Action = "Check " + Type + " Value: YawRate_GB ";
	var ParameterValue = YawRate_GB ;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 573, 22 );

	// GEEA2_HX11_EDR_List_26 : PinionSteerAg_GB;
	var Action = "Check " + Type + " Value: PinionSteerAg_GB";
	var ParameterValue = PinionSteerAg_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 595, 22 );

	// GEEA2_HX11_EDR_List_27 : Tend_GB;
	var Action = "Check " + Type + " Value: Tend_GB";
	var ParameterValue = Tend_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 617, 1 );

	// GEEA2_HX11_EDR_List_28 : EventYear_GB;
	var Action = "Check " + Type + " Value: EventYear_GB";
	var ParameterValue = EventYear_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 618, 1 );

	// GEEA2_HX11_EDR_List_29 : EventMonth_GB;
	var Action = "Check " + Type + " Value: EventMonth_GB";
	var ParameterValue = EventMonth_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 619, 1 );

	// GEEA2_HX11_EDR_List_30 : EventDay_GB;
	var Action = "Check " + Type + " Value: EventDay_GB";
	var ParameterValue = EventDay_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 620, 1 );

	// GEEA2_HX11_EDR_List_31 : EventHour_GB;
	var Action = "Check " + Type + " Value: EventHour_GB";
	var ParameterValue = EventHour_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 621, 1 );

	// GEEA2_HX11_EDR_List_32 : EventMinute_GB;
	var Action = "Check " + Type + " Value: EventMinute_GB";
	var ParameterValue = EventMinute_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 622, 1 );

	// GEEA2_HX11_EDR_List_33 : EventSecond_GB;
	var Action = "Check " + Type + " Value: EventSecond_GB";
	var ParameterValue = EventSecond_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 623, 1 );

	// GEEA2_HX11_EDR_List_34 : TrsmStGearLvr_GB;
	var Action = "Check " + Type + " Value: TrsmStGearLvr_GB";
	var ParameterValue = TrsmStGearLvr_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 624, 11 );

	// GEEA2_HX11_EDR_List_35 : EngThrtRate_GB;
	var Action = "Check " + Type + " Value: EngThrtRate_GB";
	var ParameterValue = EngThrtRate_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 635, 11 );

	// GEEA2_HX11_EDR_List_36 : BrkPedRate_GB;
	var Action = "Check " + Type + " Value: BrkPedRate_GB";
	var ParameterValue = BrkPedRate_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 646, 11 );

	// GEEA2_HX11_EDR_List_37 : ParkSysStatus_GB;
	var Action = "Check " + Type + " Value: ParkSysStatus_GB";
	var ParameterValue = ParkSysStatus_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 657, 11 );

	// GEEA2_HX11_EDR_List_38 : SteerLampStatus_GB;
	var Action = "Check " + Type + " Value: SteerLampStatus_GB";
	var ParameterValue = SteerLampStatus_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 668, 11 );

	// GEEA2_HX11_EDR_List_39 : DrPT_FireTimer_GB;
	var Action = "Check " + Type + " Value: DrPT_FireTimer_GB";
	var ParameterValue = DrPT_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 679, 2 );

	// GEEA2_HX11_EDR_List_40 : DrFrontAB_FireTimer_GB;
	var Action = "Check " + Type + " Value: DrFrontAB_FireTimer_GB";
	var ParameterValue = DrFrontAB_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 681, 2 );

	// GEEA2_HX11_EDR_List_41 : DrFrontAB2th_FireTimer_GB;
	var Action = "Check " + Type + " Value: DrFrontAB2th_FireTimer_GB";
	var ParameterValue = DrFrontAB2th_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 683, 2 );

	// GEEA2_HX11_EDR_List_42 : DrSideAB_FireTimer_GB;
	var Action = "Check " + Type + " Value: DrSideAB_FireTimer_GB";
	var ParameterValue = DrSideAB_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 685, 2 );

	// GEEA2_HX11_EDR_List_43 : DrCurtainAB_FireTimer_GB;
	var Action = "Check " + Type + " Value: DrCurtainAB_FireTimer_GB";
	var ParameterValue = DrCurtainAB_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 687, 2 );

	// GEEA2_HX11_EDR_List_44 : BBSP_GB;
	var Action = "Check " + Type + " Value: BBSP_GB";
	var ParameterValue = BBSP_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 689, 1 );

	// GEEA2_HX11_EDR_List_45 : PaPT_FireTimer_GB;
	var Action = "Check " + Type + " Value: PaPT_FireTimer_GB";
	var ParameterValue = PaPT_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 690, 2 );

	// GEEA2_HX11_EDR_List_46 : PACOS_GB;
	var Action = "Check " + Type + " Value: PACOS_GB";
	var ParameterValue = PACOS_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 692, 1 );

	// GEEA2_HX11_EDR_List_47 : PaFrontAB_FireTimer_GB;
	var Action = "Check " + Type + " Value: PaFrontAB_FireTimer_GB";
	var ParameterValue = PaFrontAB_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 693, 2 );

	// GEEA2_HX11_EDR_List_48 : PaFrontAB2th_FireTimer_GB;
	var Action = "Check " + Type + " Value: PaFrontAB2th_FireTimer_GB";
	var ParameterValue = PaFrontAB2th_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 695, 2 );

	// GEEA2_HX11_EDR_List_49 : PaSideAB_FireTimer_GB;
	var Action = "Check " + Type + " Value: PaSideAB_FireTimer_GB";
	var ParameterValue = PaSideAB_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 697, 2 );

	// GEEA2_HX11_EDR_List_50 : PaCurtainAB_FireTimer_GB;
	var Action = "Check " + Type + " Value: PaCurtainAB_FireTimer_GB";
	var ParameterValue = PaCurtainAB_FireTimer_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 699, 2 );

	// GEEA2_HX11_EDR_List_51 : FrntAirbagWarnLampSts_GB;
	var Action = "Check " + Type + " Value: FrntAirbagWarnLampSts_GB";
	var ParameterValue = FrntAirbagWarnLampSts_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 701, 1 );

	// GEEA2_HX11_EDR_List_52 : TirePresWlStatus_GB;
	var Action = "Check " + Type + " Value: TirePresWlStatus_GB";
	var ParameterValue = TirePresWlStatus_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 702, 1 );

	// GEEA2_HX11_EDR_List_53 : BrkSysWIStatus_GB;
	var Action = "Check " + Type + " Value: BrkSysWIStatus_GB";
	var ParameterValue = BrkSysWIStatus_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 703, 1 );

	// GEEA2_HX11_EDR_List_54 : CruiseCtrlVal_GB;
	var Action = "Check " + Type + " Value: CruiseCtrlVal_GB";
	var ParameterValue = CruiseCtrlVal_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 704, 11 );

	// GEEA2_HX11_EDR_List_55 : AdpCruiseCtrlVal_GB;
	var Action = "Check " + Type + " Value: AdpCruiseCtrlVal_GB";
	var ParameterValue = AdpCruiseCtrlVal_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 715, 11 );

	// GEEA2_HX11_EDR_List_56 : AbsCtrlActv_GB;
	var Action = "Check " + Type + " Value: AbsCtrlActv_GB";
	var ParameterValue = AbsCtrlActv_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 726, 11 );

	// GEEA2_HX11_EDR_List_57 : AebVal_GB;
	var Action = "Check " + Type + " Value: AebVal_GB";
	var ParameterValue = AebVal_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 737, 11 );

	// GEEA2_HX11_EDR_List_58 : EscVal_GB;
	var Action = "Check " + Type + " Value: EscVal_GB";
	var ParameterValue = EscVal_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 748, 11 );

	// GEEA2_HX11_EDR_List_59 : TrctCtrlVal_GB;
	var Action = "Check " + Type + " Value: TrctCtrlVal_GB";
	var ParameterValue = TrctCtrlVal_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 759, 11 );

	// GEEA2_HX11_EDR_List_60 : TimeFromLastTimer2T0_GB;
	var Action = "Check " + Type + " Value: TimeFromLastTimer2T0_GB";
	var ParameterValue = TimeFromLastTimer2T0_GB;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 770, 2 );

}


function BB_Check_NHTSA_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_61 : DeltaVLgt_NHTSA;
	var Action = "Check " + Type + " Value: DeltaVLgt_NHTSA";
	var ParameterValue = DeltaVLgt_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 26 );

	// GEEA2_HX11_EDR_List_62 : MaxDeltaVLgt_NHTSA;
	var Action = "Check " + Type + " Value: MaxDeltaVLgt_NHTSA";
	var ParameterValue = MaxDeltaVLgt_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 1 );

	// GEEA2_HX11_EDR_List_63 : TimeMaxDeltaVLgt_NHTSA;
	var Action = "Check " + Type + " Value: TimeMaxDeltaVLgt_NHTSA";
	var ParameterValue = TimeMaxDeltaVLgt_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 27, 1 );

	// GEEA2_HX11_EDR_List_64 : BrkPedVal_NHTSA;
	var Action = "Check " + Type + " Value: BrkPedVal_NHTSA";
	var ParameterValue = BrkPedVal_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 28, 11 );

	// GEEA2_HX11_EDR_List_65 : EngN_NHTSA;
	var Action = "Check " + Type + " Value: EngN_NHTSA";
	var ParameterValue = EngN_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 39, 11 );

	// GEEA2_HX11_EDR_List_66 : EngNFront_NHTSA;
	var Action = "Check " + Type + " Value: EngNFront_NHTSA";
	var ParameterValue = EngNFront_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 50, 22 );

	// GEEA2_HX11_EDR_List_67 : EngNRear_NHTSA;
	var Action = "Check " + Type + " Value: EngNRear_NHTSA";
	var ParameterValue = EngNRear_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 72, 22 );

	// GEEA2_HX11_EDR_List_68 : IG_Crash_NHTSA;
	var Action = "Check " + Type + " Value: IG_Crash_NHTSA";
	var ParameterValue = IG_Crash_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 94, 2 );

	// GEEA2_HX11_EDR_List_69 : CompletionStatus_NHTSA;
	var Action = "Check " + Type + " Value: CompletionStatus_NHTSA";
	var ParameterValue = CompletionStatus_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 96, 1 );

	// GEEA2_HX11_EDR_List_70 : TimeBtwEvents_NHTSA;
	var Action = "Check " + Type + " Value: TimeBtwEvents_NHTSA";
	var ParameterValue = TimeBtwEvents_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 97, 1 );

	// GEEA2_HX11_EDR_List_71 : HighRateAccelLgt_NHTSA;
	var Action = "Check " + Type + " Value: HighRateAccelLgt_NHTSA";
	var ParameterValue = HighRateAccelLgt_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 98, 126 );

	// GEEA2_HX11_EDR_List_72 : HighRateAccelLat_NHTSA;
	var Action = "Check " + Type + " Value: HighRateAccelLat_NHTSA";
	var ParameterValue = HighRateAccelLat_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 224, 126 );

	// GEEA2_HX11_EDR_List_73 : DeltaVLat_NHTSA;
	var Action = "Check " + Type + " Value: DeltaVLat_NHTSA";
	var ParameterValue = DeltaVLat_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 350, 26 );

	// GEEA2_HX11_EDR_List_74 : MaxDeltaVLat_NHTSA;
	var Action = "Check " + Type + " Value: MaxDeltaVLat_NHTSA";
	var ParameterValue = MaxDeltaVLat_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 376, 1 );

	// GEEA2_HX11_EDR_List_75 : TimeMaxDeltaVLat_NHTSA;
	var Action = "Check " + Type + " Value: TimeMaxDeltaVLat_NHTSA";
	var ParameterValue = TimeMaxDeltaVLat_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 377, 1 );

	// GEEA2_HX11_EDR_List_76 : EngThrtRate_NHTSA;
	var Action = "Check " + Type + " Value: EngThrtRate_NHTSA";
	var ParameterValue = EngThrtRate_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 378, 11 );

	// GEEA2_HX11_EDR_List_77 : FrntAirbagWarnLampSts_NHTSA;
	var Action = "Check " + Type + " Value: FrntAirbagWarnLampSts_NHTSA";
	var ParameterValue = FrntAirbagWarnLampSts_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 389, 1 );

	// GEEA2_HX11_EDR_List_78 : NormalAcc_NHTSA;
	var Action = "Check " + Type + " Value: NormalAcc_NHTSA";
	var ParameterValue = NormalAcc_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 390, 126 );

	// GEEA2_HX11_EDR_List_79 : MultiEventNumber_NHTSA;
	var Action = "Check " + Type + " Value: MultiEventNumber_NHTSA";
	var ParameterValue = MultiEventNumber_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 516, 1 );

	// GEEA2_HX11_EDR_List_80 : DrFrontAB_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: DrFrontAB_FireTimer_NHTSA";
	var ParameterValue = DrFrontAB_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 517, 2 );

	// GEEA2_HX11_EDR_List_81 : DrFrontAB2th_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: DrFrontAB2th_FireTimer_NHTSA";
	var ParameterValue = DrFrontAB2th_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 519, 2 );

	// GEEA2_HX11_EDR_List_82 : DrFrontAB3rd_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: DrFrontAB3rd_FireTimer_NHTSA";
	var ParameterValue = DrFrontAB3rd_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 521, 2 );

	// GEEA2_HX11_EDR_List_83 : PaFrontAB_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: PaFrontAB_FireTimer_NHTSA";
	var ParameterValue = PaFrontAB_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 523, 2 );

	// GEEA2_HX11_EDR_List_84 : PaFrontAB2th_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: PaFrontAB2th_FireTimer_NHTSA";
	var ParameterValue = PaFrontAB2th_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 525, 2 );

	// GEEA2_HX11_EDR_List_85 : PaFrontAB3rd_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: PaFrontAB3rd_FireTimer_NHTSA";
	var ParameterValue = PaFrontAB3rd_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 527, 2 );

	// GEEA2_HX11_EDR_List_86 : DrPT_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: DrPT_FireTimer_NHTSA";
	var ParameterValue = DrPT_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 529, 2 );

	// GEEA2_HX11_EDR_List_87 : PaPT_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: PaPT_FireTimer_NHTSA";
	var ParameterValue = PaPT_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 531, 2 );

	// GEEA2_HX11_EDR_List_88 : BBSD_NHTSA;
	var Action = "Check " + Type + " Value: BBSD_NHTSA";
	var ParameterValue = BBSD_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 533, 1 );

	// GEEA2_HX11_EDR_List_89 : STSD_NHTSA;
	var Action = "Check " + Type + " Value: STSD_NHTSA";
	var ParameterValue = STSD_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 534, 1 );

	// GEEA2_HX11_EDR_List_90 : PACOS_NHTSA;
	var Action = "Check " + Type + " Value: PACOS_NHTSA";
	var ParameterValue = PACOS_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 535, 1 );

	// GEEA2_HX11_EDR_List_91 : BBSP_NHTSA;
	var Action = "Check " + Type + " Value: BBSP_NHTSA";
	var ParameterValue = BBSP_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 536, 1 );

	// GEEA2_HX11_EDR_List_92 : STSP_NHTSA;
	var Action = "Check " + Type + " Value: STSP_NHTSA";
	var ParameterValue = STSP_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 537, 1 );

	// GEEA2_HX11_EDR_List_93 : OCSPa_NHTSA;
	var Action = "Check " + Type + " Value: OCSPa_NHTSA";
	var ParameterValue = OCSPa_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 538, 1 );

	// GEEA2_HX11_EDR_List_94 : VehSpdLgt_NHTSA;
	var Action = "Check " + Type + " Value: VehSpdLgt_NHTSA";
	var ParameterValue = VehSpdLgt_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 539, 11 );

	// GEEA2_HX11_EDR_List_95 : PinionSteerAg_NHTSA;
	var Action = "Check " + Type + " Value: PinionSteerAg_NHTSA";
	var ParameterValue = PinionSteerAg_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 550, 22 );

	// GEEA2_HX11_EDR_List_96 : AbsCtrlActv_NHTSA;
	var Action = "Check " + Type + " Value: AbsCtrlActv_NHTSA";
	var ParameterValue = AbsCtrlActv_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 572, 11 );

	// GEEA2_HX11_EDR_List_97 : EscVal_NHTSA;
	var Action = "Check " + Type + " Value: EscVal_NHTSA";
	var ParameterValue = EscVal_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 583, 11 );

	// GEEA2_HX11_EDR_List_98 : RearLeftPT_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: RearLeftPT_FireTimer_NHTSA";
	var ParameterValue = RearLeftPT_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 594, 2 );

	// GEEA2_HX11_EDR_List_99 : RightPT_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: RightPT_FireTimer_NHTSA";
	var ParameterValue = RightPT_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 596, 2 );

	// GEEA2_HX11_EDR_List_100 : DrSideAB_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: DrSideAB_FireTimer_NHTSA";
	var ParameterValue = DrSideAB_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 598, 2 );

	// GEEA2_HX11_EDR_List_101 : PaSideAB_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: PaSideAB_FireTimer_NHTSA";
	var ParameterValue = PaSideAB_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 600, 2 );

	// GEEA2_HX11_EDR_List_102 : DrCurtainAB_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: DrCurtainAB_FireTimer_NHTSA";
	var ParameterValue = DrCurtainAB_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 602, 2 );

	// GEEA2_HX11_EDR_List_103 : PaCurtainAB_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: PaCurtainAB_FireTimer_NHTSA";
	var ParameterValue = PaCurtainAB_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 604, 2 );

	// GEEA2_HX11_EDR_List_104 : SBRP_NHTSA;
	var Action = "Check " + Type + " Value: SBRP_NHTSA";
	var ParameterValue = SBRP_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 606, 1 );

	// GEEA2_HX11_EDR_List_105 : VehRollAgl_NHTSA;
	var Action = "Check " + Type + " Value: VehRollAgl_NHTSA";
	var ParameterValue = VehRollAgl_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 607, 61 );

	// GEEA2_HX11_EDR_List_106 : IG_Read_NHTSA;
	var Action = "Check " + Type + " Value: IG_Read_NHTSA";
	var ParameterValue = IG_Read_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 668, 2 );

	// GEEA2_HX11_EDR_List_107 : TimeMaxResDeltaV_NHTSA;
	var Action = "Check " + Type + " Value: TimeMaxResDeltaV_NHTSA";
	var ParameterValue = TimeMaxResDeltaV_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 670, 1 );

	// GEEA2_HX11_EDR_List_108 : DrFrontAB2thDis_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: DrFrontAB2thDis_FireTimer_NHTSA";
	var ParameterValue = DrFrontAB2thDis_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 671, 1 );

	// GEEA2_HX11_EDR_List_109 : DrFrontAB3rdDis_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: DrFrontAB3rdDis_FireTimer_NHTSA";
	var ParameterValue = DrFrontAB3rdDis_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 672, 1 );

	// GEEA2_HX11_EDR_List_110 : PaFrontAB2thDis_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: PaFrontAB2thDis_FireTimer_NHTSA";
	var ParameterValue = PaFrontAB2thDis_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 673, 1 );

	// GEEA2_HX11_EDR_List_111 : PaFrontAB3rdDis_FireTimer_NHTSA;
	var Action = "Check " + Type + " Value: PaFrontAB3rdDis_FireTimer_NHTSA";
	var ParameterValue = PaFrontAB3rdDis_FireTimer_NHTSA;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 674, 1 );

}


function BB_Check_Header_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_112 : DataAreaPriority_Header;
	var Action = "Check " + Type + " Value: DataAreaPriority_Header";
	var ParameterValue = DataAreaPriority_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 1 );

	// GEEA2_HX11_EDR_List_113 : DataAreaReadStatus_Header;
	var Action = "Check " + Type + " Value: DataAreaReadStatus_Header";
	var ParameterValue = DataAreaReadStatus_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1, 1 );

	// GEEA2_HX11_EDR_List_114 : GlobalTime_Header;
	var Action = "Check " + Type + " Value: GlobalTime_Header";
	var ParameterValue = GlobalTime_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2, 4 );

	// GEEA2_HX11_EDR_List_115 : EventYear_Header;
	var Action = "Check " + Type + " Value: EventYear_Header";
	var ParameterValue = EventYear_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 6, 1 );

	// GEEA2_HX11_EDR_List_116 : EventMonth_Header;
	var Action = "Check " + Type + " Value: EventMonth_Header";
	var ParameterValue = EventMonth_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 7, 1 );

	// GEEA2_HX11_EDR_List_117 : EventDay_Header;
	var Action = "Check " + Type + " Value: EventDay_Header";
	var ParameterValue = EventDay_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 8, 1 );

	// GEEA2_HX11_EDR_List_118 : EventHour_Header;
	var Action = "Check " + Type + " Value: EventHour_Header";
	var ParameterValue = EventHour_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 9, 1 );

	// GEEA2_HX11_EDR_List_119 : EventMinute_Header;
	var Action = "Check " + Type + " Value: EventMinute_Header";
	var ParameterValue = EventMinute_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 10, 1 );

	// GEEA2_HX11_EDR_List_120 : EventSecond_Header;
	var Action = "Check " + Type + " Value: EventSecond_Header";
	var ParameterValue = EventSecond_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 11, 1 );

	// GEEA2_HX11_EDR_List_121 : LifeTimeEventNb_Header;
	var Action = "Check " + Type + " Value: LifeTimeEventNb_Header";
	var ParameterValue = LifeTimeEventNb_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 12, 2 );

	// GEEA2_HX11_EDR_List_122 : ERTimeStamp_Header;
	var Action = "Check " + Type + " Value: ERTimeStamp_Header";
	var ParameterValue = ERTimeStamp_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 14, 2 );

	// GEEA2_HX11_EDR_List_123 : LifeTimeCrashCntOfFront_Header;
	var Action = "Check " + Type + " Value: LifeTimeCrashCntOfFront_Header";
	var ParameterValue = LifeTimeCrashCntOfFront_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 16, 2 );

	// GEEA2_HX11_EDR_List_124 : LifeTimeCrashCntOfSide_Header;
	var Action = "Check " + Type + " Value: LifeTimeCrashCntOfSide_Header";
	var ParameterValue = LifeTimeCrashCntOfSide_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 18, 2 );

	// GEEA2_HX11_EDR_List_125 : LifeTimeCrashCntOfRear_Header;
	var Action = "Check " + Type + " Value: LifeTimeCrashCntOfRear_Header";
	var ParameterValue = LifeTimeCrashCntOfRear_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 20, 2 );

	// GEEA2_HX11_EDR_List_126 : LifeTimeCrashNbOfRoll_Header;
	var Action = "Check " + Type + " Value: LifeTimeCrashNbOfRoll_Header";
	var ParameterValue = LifeTimeCrashNbOfRoll_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 22, 2 );

	// GEEA2_HX11_EDR_List_127 : LifeTimeCrashCntOfPitch_Header;
	var Action = "Check " + Type + " Value: LifeTimeCrashCntOfPitch_Header";
	var ParameterValue = LifeTimeCrashCntOfPitch_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 24, 2 );

	// GEEA2_HX11_EDR_List_128 : LifeTimeCrashNbOfPed_Header;
	var Action = "Check " + Type + " Value: LifeTimeCrashNbOfPed_Header";
	var ParameterValue = LifeTimeCrashNbOfPed_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 2 );

	// GEEA2_HX11_EDR_List_129 : LifeTimeCrashCntOfSlowRoll_Header;
	var Action = "Check " + Type + " Value: LifeTimeCrashCntOfSlowRoll_Header";
	var ParameterValue = LifeTimeCrashCntOfSlowRoll_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 28, 2 );

	// GEEA2_HX11_EDR_List_130 : CompletionStatus_Header;
	var Action = "Check " + Type + " Value: CompletionStatus_Header";
	var ParameterValue = CompletionStatus_Header;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 30, 1 );

}


function BB_Check_ECE_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_214 : DeltaVLgt_ECE;
	var Action = "Check " + Type + " Value: DeltaVLgt_ECE";
	var ParameterValue = DeltaVLgt_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 26 );

	// GEEA2_HX11_EDR_List_215 : MaxDeltaVLgt_ECE;
	var Action = "Check " + Type + " Value: MaxDeltaVLgt_ECE";
	var ParameterValue = MaxDeltaVLgt_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 1 );

	// GEEA2_HX11_EDR_List_216 : TimeMaxDeltaVLgt_ECE;
	var Action = "Check " + Type + " Value: TimeMaxDeltaVLgt_ECE";
	var ParameterValue = TimeMaxDeltaVLgt_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 27, 1 );

	// GEEA2_HX11_EDR_List_217 : VehSpdLgt_ECE;
	var Action = "Check " + Type + " Value: VehSpdLgt_ECE";
	var ParameterValue = VehSpdLgt_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 28, 11 );

	// GEEA2_HX11_EDR_List_218 : AccrPedRat_ECE;
	var Action = "Check " + Type + " Value: AccrPedRat_ECE";
	var ParameterValue = AccrPedRat_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 39, 11 );

	// GEEA2_HX11_EDR_List_219 : BrkPedVal_ECE;
	var Action = "Check " + Type + " Value: BrkPedVal_ECE";
	var ParameterValue = BrkPedVal_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 50, 11 );

	// GEEA2_HX11_EDR_List_220 : IG_Crash_ECE;
	var Action = "Check " + Type + " Value: IG_Crash_ECE";
	var ParameterValue = IG_Crash_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 61, 2 );

	// GEEA2_HX11_EDR_List_221 : IG_Read_ECE;
	var Action = "Check " + Type + " Value: IG_Read_ECE";
	var ParameterValue = IG_Read_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 63, 2 );

	// GEEA2_HX11_EDR_List_222 : BBSD_ECE;
	var Action = "Check " + Type + " Value: BBSD_ECE";
	var ParameterValue = BBSD_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 65, 1 );

	// GEEA2_HX11_EDR_List_223 : FrntAirbagWarnLampSts_ECE;
	var Action = "Check " + Type + " Value: FrntAirbagWarnLampSts_ECE";
	var ParameterValue = FrntAirbagWarnLampSts_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 66, 1 );

	// GEEA2_HX11_EDR_List_224 : DrFrontAB_FireTimer_ECE;
	var Action = "Check " + Type + " Value: DrFrontAB_FireTimer_ECE";
	var ParameterValue = DrFrontAB_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 67, 2 );

	// GEEA2_HX11_EDR_List_225 : PaFrontAB_FireTimer_ECE;
	var Action = "Check " + Type + " Value: PaFrontAB_FireTimer_ECE";
	var ParameterValue = PaFrontAB_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 69, 2 );

	// GEEA2_HX11_EDR_List_226 : MultiEventNumber_ECE;
	var Action = "Check " + Type + " Value: MultiEventNumber_ECE";
	var ParameterValue = MultiEventNumber_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 71, 1 );

	// GEEA2_HX11_EDR_List_227 : TimeBtwEvents_ECE;
	var Action = "Check " + Type + " Value: TimeBtwEvents_ECE";
	var ParameterValue = TimeBtwEvents_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 72, 1 );

	// GEEA2_HX11_EDR_List_228 : CompletionStatus_ECE;
	var Action = "Check " + Type + " Value: CompletionStatus_ECE";
	var ParameterValue = CompletionStatus_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 73, 1 );

	// GEEA2_HX11_EDR_List_229 : HighRateAccelLat_ECE;
	var Action = "Check " + Type + " Value: HighRateAccelLat_ECE";
	var ParameterValue = HighRateAccelLat_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 74, 126 );

	// GEEA2_HX11_EDR_List_230 : HighRateAccelLgt_ECE;
	var Action = "Check " + Type + " Value: HighRateAccelLgt_ECE";
	var ParameterValue = HighRateAccelLgt_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 200, 126 );

	// GEEA2_HX11_EDR_List_231 : NormalAcc_ECE;
	var Action = "Check " + Type + " Value: NormalAcc_ECE";
	var ParameterValue = NormalAcc_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 326, 61 );

	// GEEA2_HX11_EDR_List_232 : DeltaVLat_ECE;
	var Action = "Check " + Type + " Value: DeltaVLat_ECE";
	var ParameterValue = DeltaVLat_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 387, 26 );

	// GEEA2_HX11_EDR_List_233 : MaxDeltaVLat_ECE;
	var Action = "Check " + Type + " Value: MaxDeltaVLat_ECE";
	var ParameterValue = MaxDeltaVLat_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 413, 1 );

	// GEEA2_HX11_EDR_List_234 : TimeMaxDeltaVLat_ECE;
	var Action = "Check " + Type + " Value: TimeMaxDeltaVLat_ECE";
	var ParameterValue = TimeMaxDeltaVLat_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 414, 1 );

	// GEEA2_HX11_EDR_List_235 : TimeMaxResDeltaV_ECE;
	var Action = "Check " + Type + " Value: TimeMaxResDeltaV_ECE";
	var ParameterValue = TimeMaxResDeltaV_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 415, 1 );

	// GEEA2_HX11_EDR_List_236 : EngN_ECE;
	var Action = "Check " + Type + " Value: EngN_ECE";
	var ParameterValue = EngN_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 416, 11 );

	// GEEA2_HX11_EDR_List_237 : EngNFront_ECE;
	var Action = "Check " + Type + " Value: EngNFront_ECE";
	var ParameterValue = EngNFront_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 427, 22 );

	// GEEA2_HX11_EDR_List_238 : EngNRear_ECE;
	var Action = "Check " + Type + " Value: EngNRear_ECE";
	var ParameterValue = EngNRear_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 449, 22 );

	// GEEA2_HX11_EDR_List_239 : EngNFront800V_ECE;
	var Action = "Check " + Type + " Value: EngNFront800V_ECE";
	var ParameterValue = EngNFront800V_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 471, 22 );

	// GEEA2_HX11_EDR_List_240 : EngNRear800V_ECE;
	var Action = "Check " + Type + " Value: EngNRear800V_ECE";
	var ParameterValue = EngNRear800V_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 493, 22 );

	// GEEA2_HX11_EDR_List_241 : VehRollAgl_ECE;
	var Action = "Check " + Type + " Value: VehRollAgl_ECE";
	var ParameterValue = VehRollAgl_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 515, 61 );

	// GEEA2_HX11_EDR_List_242 : VehRollRate_ECE;
	var Action = "Check " + Type + " Value: VehRollRate_ECE";
	var ParameterValue = VehRollRate_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 576, 122 );

	// GEEA2_HX11_EDR_List_243 : AbsCtrlActv_ECE;
	var Action = "Check " + Type + " Value: AbsCtrlActv_ECE";
	var ParameterValue = AbsCtrlActv_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 698, 11 );

	// GEEA2_HX11_EDR_List_244 : EscVal_ECE;
	var Action = "Check " + Type + " Value: EscVal_ECE";
	var ParameterValue = EscVal_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 709, 11 );

	// GEEA2_HX11_EDR_List_245 : PinionSteerAg_ECE;
	var Action = "Check " + Type + " Value: PinionSteerAg_ECE";
	var ParameterValue = PinionSteerAg_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 720, 22 );

	// GEEA2_HX11_EDR_List_246 : BBSP_ECE;
	var Action = "Check " + Type + " Value: BBSP_ECE";
	var ParameterValue = BBSP_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 742, 1 );

	// GEEA2_HX11_EDR_List_247 : PAB_ECE;
	var Action = "Check " + Type + " Value: PAB_ECE";
	var ParameterValue = PAB_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 743, 1 );

	// GEEA2_HX11_EDR_List_248 : DrFrontAB2th_FireTimer_ECE;
	var Action = "Check " + Type + " Value: DrFrontAB2th_FireTimer_ECE";
	var ParameterValue = DrFrontAB2th_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 744, 2 );

	// GEEA2_HX11_EDR_List_249 : PaFrontAB2th_FireTimer_ECE;
	var Action = "Check " + Type + " Value: PaFrontAB2th_FireTimer_ECE";
	var ParameterValue = PaFrontAB2th_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 746, 2 );

	// GEEA2_HX11_EDR_List_250 : DrSideAB_FireTimer_ECE;
	var Action = "Check " + Type + " Value: DrSideAB_FireTimer_ECE";
	var ParameterValue = DrSideAB_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 748, 2 );

	// GEEA2_HX11_EDR_List_251 : PaSideAB_FireTimer_ECE;
	var Action = "Check " + Type + " Value: PaSideAB_FireTimer_ECE";
	var ParameterValue = PaSideAB_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 750, 2 );

	// GEEA2_HX11_EDR_List_252 : DrCurtainAB_FireTimer_ECE;
	var Action = "Check " + Type + " Value: DrCurtainAB_FireTimer_ECE";
	var ParameterValue = DrCurtainAB_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 752, 2 );

	// GEEA2_HX11_EDR_List_253 : PaCurtainAB_FireTimer_ECE;
	var Action = "Check " + Type + " Value: PaCurtainAB_FireTimer_ECE";
	var ParameterValue = PaCurtainAB_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 754, 2 );

	// GEEA2_HX11_EDR_List_254 : DrPT_FireTimer_ECE;
	var Action = "Check " + Type + " Value: DrPT_FireTimer_ECE";
	var ParameterValue = DrPT_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 756, 2 );

	// GEEA2_HX11_EDR_List_255 : PaPT_FireTimer_ECE;
	var Action = "Check " + Type + " Value: PaPT_FireTimer_ECE";
	var ParameterValue = PaPT_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 758, 2 );

	// GEEA2_HX11_EDR_List_256 : STSD_ECE;
	var Action = "Check " + Type + " Value: STSD_ECE";
	var ParameterValue = STSD_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 760, 1 );

	// GEEA2_HX11_EDR_List_257 : STSP_ECE;
	var Action = "Check " + Type + " Value: STSP_ECE";
	var ParameterValue = STSP_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 761, 1 );

	// GEEA2_HX11_EDR_List_258 : OCSDr_ECE;
	var Action = "Check " + Type + " Value: OCSDr_ECE";
	var ParameterValue = OCSDr_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 762, 1 );

	// GEEA2_HX11_EDR_List_259 : OCSPa_ECE;
	var Action = "Check " + Type + " Value: OCSPa_ECE";
	var ParameterValue = OCSPa_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 763, 1 );

	// GEEA2_HX11_EDR_List_260 : BB2L_ECE;
	var Action = "Check " + Type + " Value: BB2L_ECE";
	var ParameterValue = BB2L_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 764, 1 );

	// GEEA2_HX11_EDR_List_261 : BB2R_ECE;
	var Action = "Check " + Type + " Value: BB2R_ECE";
	var ParameterValue = BB2R_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 765, 1 );

	// GEEA2_HX11_EDR_List_262 : BB2M_ECE;
	var Action = "Check " + Type + " Value: BB2M_ECE";
	var ParameterValue = BB2M_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 766, 1 );

	// GEEA2_HX11_EDR_List_263 : TirePresWlStatus_ECE;
	var Action = "Check " + Type + " Value: TirePresWlStatus_ECE";
	var ParameterValue = TirePresWlStatus_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 767, 1 );

	// GEEA2_HX11_EDR_List_264 : HighRateAccelLgt_ECE;
	var Action = "Check " + Type + " Value: HighRateAccelLgt_ECE";
	var ParameterValue = HighRateAccelLgt_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 768, 11 );

	// GEEA2_HX11_EDR_List_265 : HighRateAccelLat_ECE;
	var Action = "Check " + Type + " Value: HighRateAccelLat_ECE";
	var ParameterValue = HighRateAccelLat_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 779, 11 );

	// GEEA2_HX11_EDR_List_266 : YawRate_ECE;
	var Action = "Check " + Type + " Value: YawRate_ECE";
	var ParameterValue = YawRate_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 790, 22 );

	// GEEA2_HX11_EDR_List_267 : TrctCtrlVal_ECE;
	var Action = "Check " + Type + " Value: TrctCtrlVal_ECE";
	var ParameterValue = TrctCtrlVal_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 812, 11 );

	// GEEA2_HX11_EDR_List_268 : AebVal_ECE;
	var Action = "Check " + Type + " Value: AebVal_ECE";
	var ParameterValue = AebVal_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 823, 11 );

	// GEEA2_HX11_EDR_List_269 : CruiseCtrlVal_ECE;
	var Action = "Check " + Type + " Value: CruiseCtrlVal_ECE";
	var ParameterValue = CruiseCtrlVal_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 834, 11 );

	// GEEA2_HX11_EDR_List_270 : AdpCruiseCtrlVal_ECE;
	var Action = "Check " + Type + " Value: AdpCruiseCtrlVal_ECE";
	var ParameterValue = AdpCruiseCtrlVal_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 845, 11 );

	// GEEA2_HX11_EDR_List_271 : VRU_FireTimer_ECE;
	var Action = "Check " + Type + " Value: VRU_FireTimer_ECE";
	var ParameterValue = VRU_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 856, 2 );

	// GEEA2_HX11_EDR_List_272 : VRUWarningIndicator_ECE;
	var Action = "Check " + Type + " Value: VRUWarningIndicator_ECE";
	var ParameterValue = VRUWarningIndicator_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 858, 1 );

	// GEEA2_HX11_EDR_List_273 : BBSDM_ECE;
	var Action = "Check " + Type + " Value: BBSDM_ECE";
	var ParameterValue = BBSDM_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 859, 1 );

	// GEEA2_HX11_EDR_List_274 : FarSideAB_FireTimer_ECE;
	var Action = "Check " + Type + " Value: FarSideAB_FireTimer_ECE";
	var ParameterValue = FarSideAB_FireTimer_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 860, 2 );

	// GEEA2_HX11_EDR_List_275 : ECallSystemStatus_ECE;
	var Action = "Check " + Type + " Value: ECallSystemStatus_ECE";
	var ParameterValue = ECallSystemStatus_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 862, 1 );

	// GEEA2_HX11_EDR_List_276 : LaneDepartWarnSys_ECE;
	var Action = "Check " + Type + " Value: LaneDepartWarnSys_ECE";
	var ParameterValue = LaneDepartWarnSys_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 863, 11 );

	// GEEA2_HX11_EDR_List_277 : CorrectiveSteering_ECE;
	var Action = "Check " + Type + " Value: CorrectiveSteering_ECE";
	var ParameterValue = CorrectiveSteering_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 874, 11 );

	// GEEA2_HX11_EDR_List_278 : EmergencySteering_ECE;
	var Action = "Check " + Type + " Value: EmergencySteering_ECE";
	var ParameterValue = EmergencySteering_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 885, 11 );

	// GEEA2_HX11_EDR_List_279 : ACSFAStateAPA_ECE;
	var Action = "Check " + Type + " Value: ACSFAStateAPA_ECE";
	var ParameterValue = ACSFAStateAPA_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 896, 11 );

	// GEEA2_HX11_EDR_List_280 : ACSFAStateRPA_ECE;
	var Action = "Check " + Type + " Value: ACSFAStateRPA_ECE";
	var ParameterValue = ACSFAStateRPA_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 907, 11 );

	// GEEA2_HX11_EDR_List_281 : ACSFAStateAVP_ECE;
	var Action = "Check " + Type + " Value: ACSFAStateAVP_ECE";
	var ParameterValue = ACSFAStateAVP_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 918, 11 );

	// GEEA2_HX11_EDR_List_282 : ACSFB1StateHWA_ECE;
	var Action = "Check " + Type + " Value: ACSFB1StateHWA_ECE";
	var ParameterValue = ACSFB1StateHWA_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 929, 11 );

	// GEEA2_HX11_EDR_List_283 : ACSFB2State_ECE;
	var Action = "Check " + Type + " Value: ACSFB2State_ECE";
	var ParameterValue = ACSFB2State_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 940, 11 );

	// GEEA2_HX11_EDR_List_284 : ACSFCStateLKA_ECE;
	var Action = "Check " + Type + " Value: ACSFCStateLKA_ECE";
	var ParameterValue = ACSFCStateLKA_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 951, 11 );

	// GEEA2_HX11_EDR_List_285 : ACSFCStateHWA_ECE;
	var Action = "Check " + Type + " Value: ACSFCStateHWA_ECE";
	var ParameterValue = ACSFCStateHWA_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 962, 11 );

	// GEEA2_HX11_EDR_List_286 : ACSFDState_ECE;
	var Action = "Check " + Type + " Value: ACSFDState_ECE";
	var ParameterValue = ACSFDState_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 973, 11 );

	// GEEA2_HX11_EDR_List_287 : ACSFEStateEMA_ECE;
	var Action = "Check " + Type + " Value: ACSFEStateEMA_ECE";
	var ParameterValue = ACSFEStateEMA_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 984, 11 );

	// GEEA2_HX11_EDR_List_288 : ACSFEStateELKA_ECE;
	var Action = "Check " + Type + " Value: ACSFEStateELKA_ECE";
	var ParameterValue = ACSFEStateELKA_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 995, 11 );

	// GEEA2_HX11_EDR_List_289 : ACSFEStateNOP_ECE;
	var Action = "Check " + Type + " Value: ACSFEStateNOP_ECE";
	var ParameterValue = ACSFEStateNOP_ECE;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1006, 11 );

}


function BB_Check_OEM_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_131 : DrFrontAB_FireTimer_OEM;
	var Action = "Check " + Type + " Value: DrFrontAB_FireTimer_OEM";
	var ParameterValue = DrFrontAB_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 2 );

	// GEEA2_HX11_EDR_List_134 : PaFrontAB_FireTimer_OEM;
	var Action = "Check " + Type + " Value: PaFrontAB_FireTimer_OEM";
	var ParameterValue = PaFrontAB_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2, 2 );

	// GEEA2_HX11_EDR_List_137 : DrPT_FireTimer_OEM;
	var Action = "Check " + Type + " Value: DrPT_FireTimer_OEM";
	var ParameterValue = DrPT_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 4, 2 );

	// GEEA2_HX11_EDR_List_138 : PaPT_FireTimer_OEM;
	var Action = "Check " + Type + " Value: PaPT_FireTimer_OEM";
	var ParameterValue = PaPT_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 6, 2 );

	// GEEA2_HX11_EDR_List_139 : DrSideAB_FireTimer_OEM;
	var Action = "Check " + Type + " Value: DrSideAB_FireTimer_OEM";
	var ParameterValue = DrSideAB_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 8, 2 );

	// GEEA2_HX11_EDR_List_140 : PaSideAB_FireTimer_OEM;
	var Action = "Check " + Type + " Value: PaSideAB_FireTimer_OEM";
	var ParameterValue = PaSideAB_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 10, 2 );

	// GEEA2_HX11_EDR_List_141 : DrCurtainAB_FireTimer_OEM;
	var Action = "Check " + Type + " Value: DrCurtainAB_FireTimer_OEM";
	var ParameterValue = DrCurtainAB_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 12, 2 );

	// GEEA2_HX11_EDR_List_142 : PaCurtainAB_FireTimer_OEM;
	var Action = "Check " + Type + " Value: PaCurtainAB_FireTimer_OEM";
	var ParameterValue = PaCurtainAB_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 14, 2 );

	// GEEA2_HX11_EDR_List_143 : HVD_FireTimer_OEM;
	var Action = "Check " + Type + " Value: HVD_FireTimer_OEM";
	var ParameterValue = HVD_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 16, 2 );

	// GEEA2_HX11_EDR_List_144 : RearLeftBH_FireTimer_OEM;
	var Action = "Check " + Type + " Value: RearLeftBH_FireTimer_OEM";
	var ParameterValue = RearLeftBH_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 18, 2 );

	// GEEA2_HX11_EDR_List_145 : RearRightBH_FireTimer_OEM;
	var Action = "Check " + Type + " Value: RearRightBH_FireTimer_OEM";
	var ParameterValue = RearRightBH_FireTimer_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 20, 2 );

	// GEEA2_HX11_EDR_List_146 : SBRP_OEM;
	var Action = "Check " + Type + " Value: SBRP_OEM";
	var ParameterValue = SBRP_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 22, 1 );

	// GEEA2_HX11_EDR_List_147 : AccrPedlStatus_OEM;
	var Action = "Check " + Type + " Value: AccrPedlStatus_OEM";
	var ParameterValue = AccrPedlStatus_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 23, 1 );

	// GEEA2_HX11_EDR_List_148 : AmbientAirTemp_OEM;
	var Action = "Check " + Type + " Value: AmbientAirTemp_OEM";
	var ParameterValue = AmbientAirTemp_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 24, 2 );

	// GEEA2_HX11_EDR_List_149 : BattVoltKL15_OEM;
	var Action = "Check " + Type + " Value: BattVoltKL15_OEM";
	var ParameterValue = BattVoltKL15_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 28 );

	// GEEA2_HX11_EDR_List_151 : BBSD_OEM;
	var Action = "Check " + Type + " Value: BBSD_OEM";
	var ParameterValue = BBSD_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 54, 1 );

	// GEEA2_HX11_EDR_List_152 : BBSP_OEM;
	var Action = "Check " + Type + " Value: BBSP_OEM";
	var ParameterValue = BBSP_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 55, 1 );

	// GEEA2_HX11_EDR_List_153 : BB2L_OEM;
	var Action = "Check " + Type + " Value: BB2L_OEM";
	var ParameterValue = BB2L_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 56, 1 );

	// GEEA2_HX11_EDR_List_154 : BB2R_OEM;
	var Action = "Check " + Type + " Value: BB2R_OEM";
	var ParameterValue = BB2R_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 57, 1 );

	// GEEA2_HX11_EDR_List_155 : BB2M_OEM;
	var Action = "Check " + Type + " Value: BB2M_OEM";
	var ParameterValue = BB2M_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 58, 1 );

	// GEEA2_HX11_EDR_List_156 : BrkSysPress_OEM;
	var Action = "Check " + Type + " Value: BrkSysPress_OEM";
	var ParameterValue = BrkSysPress_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 59, 28 );

	// GEEA2_HX11_EDR_List_157 : DoorDrvrSts_OEM;
	var Action = "Check " + Type + " Value: DoorDrvrSts_OEM";
	var ParameterValue = DoorDrvrSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 87, 1 );

	// GEEA2_HX11_EDR_List_158 : DoorPassSts_OEM;
	var Action = "Check " + Type + " Value: DoorPassSts_OEM";
	var ParameterValue = DoorPassSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 88, 1 );

	// GEEA2_HX11_EDR_List_159 : DoorLeReSts_OEM;
	var Action = "Check " + Type + " Value: DoorLeReSts_OEM";
	var ParameterValue = DoorLeReSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 89, 1 );

	// GEEA2_HX11_EDR_List_160 : DoorRiReSts_OEM;
	var Action = "Check " + Type + " Value: DoorRiReSts_OEM";
	var ParameterValue = DoorRiReSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 90, 1 );

	// GEEA2_HX11_EDR_List_161 : HybridMode_OEM;
	var Action = "Check " + Type + " Value: HybridMode_OEM";
	var ParameterValue = HybridMode_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 91, 1 );

	// GEEA2_HX11_EDR_List_162 : DoorDrvrLockSts_OEM;
	var Action = "Check " + Type + " Value: DoorDrvrLockSts_OEM";
	var ParameterValue = DoorDrvrLockSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 92, 1 );

	// GEEA2_HX11_EDR_List_163 : DoorPassLockSts_OEM;
	var Action = "Check " + Type + " Value: DoorPassLockSts_OEM";
	var ParameterValue = DoorPassLockSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 93, 1 );

	// GEEA2_HX11_EDR_List_164 : DoorLeReLockSts_OEM;
	var Action = "Check " + Type + " Value: DoorLeReLockSts_OEM";
	var ParameterValue = DoorLeReLockSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 94, 1 );

	// GEEA2_HX11_EDR_List_165 : DoorRiReLockSts_OEM;
	var Action = "Check " + Type + " Value: DoorRiReLockSts_OEM";
	var ParameterValue = DoorRiReLockSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 95, 1 );

	// GEEA2_HX11_EDR_List_166 : PostImpctBrkStatus_OEM;
	var Action = "Check " + Type + " Value: PostImpctBrkStatus_OEM";
	var ParameterValue = PostImpctBrkStatus_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 96, 1 );

	// GEEA2_HX11_EDR_List_167 : DoorDrvrLockSts_OEM;
	var Action = "Check " + Type + " Value: DoorDrvrLockSts_OEM";
	var ParameterValue = DoorDrvrLockSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 97, 1 );

	// GEEA2_HX11_EDR_List_168 : DoorPassLockSts_OEM;
	var Action = "Check " + Type + " Value: DoorPassLockSts_OEM";
	var ParameterValue = DoorPassLockSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 98, 1 );

	// GEEA2_HX11_EDR_List_169 : DoorLeReLockSts_OEM;
	var Action = "Check " + Type + " Value: DoorLeReLockSts_OEM";
	var ParameterValue = DoorLeReLockSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 99, 1 );

	// GEEA2_HX11_EDR_List_170 : DoorRiReLockSts_OEM;
	var Action = "Check " + Type + " Value: DoorRiReLockSts_OEM";
	var ParameterValue = DoorRiReLockSts_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 100, 1 );

	// GEEA2_HX11_EDR_List_171 : CoordLongitude_OEM;
	var Action = "Check " + Type + " Value: CoordLongitude_OEM";
	var ParameterValue = CoordLongitude_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 101, 24 );

	// GEEA2_HX11_EDR_List_172 : CoordLatitude_OEM;
	var Action = "Check " + Type + " Value: CoordLatitude_OEM";
	var ParameterValue = CoordLatitude_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 125, 24 );

	// GEEA2_HX11_EDR_List_173 : AccrPedRat_OEM;
	var Action = "Check " + Type + " Value: AccrPedRat_OEM";
	var ParameterValue = AccrPedRat_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 149, 102 );

	// GEEA2_HX11_EDR_List_174 : BrkPedRate_OEM;
	var Action = "Check " + Type + " Value: BrkPedRate_OEM";
	var ParameterValue = BrkPedRate_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 251, 102 );

	// GEEA2_HX11_EDR_List_175 : TrsmStGearLvr_OEM;
	var Action = "Check " + Type + " Value: TrsmStGearLvr_OEM";
	var ParameterValue = TrsmStGearLvr_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 353, 11 );

	// GEEA2_HX11_EDR_List_176 : PinionSteerAg_OEM;
	var Action = "Check " + Type + " Value: PinionSteerAg_OEM";
	var ParameterValue = PinionSteerAg_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 364, 102 );

	// GEEA2_HX11_EDR_List_177 : BrkSysCylPMstActQf_OEM;
	var Action = "Check " + Type + " Value: BrkSysCylPMstActQf_OEM";
	var ParameterValue = BrkSysCylPMstActQf_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 466, 2bit );

	// GEEA2_HX11_EDR_List_178 : BrkPedlTrvlQf_OEM;
	var Action = "Check " + Type + " Value: BrkPedlTrvlQf_OEM";
	var ParameterValue = BrkPedlTrvlQf_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 466, 2bit );

	// GEEA2_HX11_EDR_List_180 : DrvrSeatPosPercSeatPosSldQF_OEM;
	var Action = "Check " + Type + " Value: DrvrSeatPosPercSeatPosSldQF_OEM";
	var ParameterValue = DrvrSeatPosPercSeatPosSldQF_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 466, 2bit );

	// GEEA2_HX11_EDR_List_182 : PassSeatPosPercSeatPosSldQF_OEM;
	var Action = "Check " + Type + " Value: PassSeatPosPercSeatPosSldQF_OEM";
	var ParameterValue = PassSeatPosPercSeatPosSldQF_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 466, 2bit );

	// GEEA2_HX11_EDR_List_183 : AmbTIndcdWithUnitQF_OEM;
	var Action = "Check " + Type + " Value: AmbTIndcdWithUnitQF_OEM";
	var ParameterValue = AmbTIndcdWithUnitQF_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 467, 2bit );

	// GEEA2_HX11_EDR_List_185 : DrvrSeatPosPercSeatPosSldPerc_OEM;
	var Action = "Check " + Type + " Value: DrvrSeatPosPercSeatPosSldPerc_OEM";
	var ParameterValue = DrvrSeatPosPercSeatPosSldPerc_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 468, 2 );

	// GEEA2_HX11_EDR_List_186 : PassSeatPosPercSeatPosSldPerc_OEM;
	var Action = "Check " + Type + " Value: PassSeatPosPercSeatPosSldPerc_OEM";
	var ParameterValue = PassSeatPosPercSeatPosSldPerc_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 470, 2 );

	// GEEA2_HX11_EDR_List_187 : SBR2L_OEM;
	var Action = "Check " + Type + " Value: SBR2L_OEM";
	var ParameterValue = SBR2L_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 472, 1 );

	// GEEA2_HX11_EDR_List_188 : SBR2M_OEM;
	var Action = "Check " + Type + " Value: SBR2M_OEM";
	var ParameterValue = SBR2M_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 473, 1 );

	// GEEA2_HX11_EDR_List_189 : SBR2R_OEM;
	var Action = "Check " + Type + " Value: SBR2R_OEM";
	var ParameterValue = SBR2R_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 474, 1 );

	// GEEA2_HX11_EDR_List_190 : DeploymentCnt_OEM;
	var Action = "Check " + Type + " Value: DeploymentCnt_OEM";
	var ParameterValue = DeploymentCnt_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 475, 1 );

	// GEEA2_HX11_EDR_List_191 : DelayFromEDR_OEM;
	var Action = "Check " + Type + " Value: DelayFromEDR_OEM";
	var ParameterValue = DelayFromEDR_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 476, 1bit );

	// GEEA2_HX11_EDR_List_192 : DelayFromEDR_OEM;
	var Action = "Check " + Type + " Value: DelayFromEDR_OEM";
	var ParameterValue = DelayFromEDR_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 476, 1bit );

	// GEEA2_HX11_EDR_List_193 : DelayFromEDR_OEM;
	var Action = "Check " + Type + " Value: DelayFromEDR_OEM";
	var ParameterValue = DelayFromEDR_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 476, 1bit );

	// GEEA2_HX11_EDR_List_194 : DelayFromEDR_OEM;
	var Action = "Check " + Type + " Value: DelayFromEDR_OEM";
	var ParameterValue = DelayFromEDR_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 476, 1bit );

	// GEEA2_HX11_EDR_List_197 : DelayFromEDR_OEM;
	var Action = "Check " + Type + " Value: DelayFromEDR_OEM";
	var ParameterValue = DelayFromEDR_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 476, 1bit );

	// GEEA2_HX11_EDR_List_198 : BrkSysPress_OEM;
	var Action = "Check " + Type + " Value: BrkSysPress_OEM";
	var ParameterValue = BrkSysPress_OEM;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 477, 102 );

}


function BB_Check_Sensor_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_199 : SRSU_R_Sensor;
	var Action = "Check " + Type + " Value: SRSU_R_Sensor";
	var ParameterValue = SRSU_R_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 161 );

	// GEEA2_HX11_EDR_List_200 : SRSU_L_Sensor;
	var Action = "Check " + Type + " Value: SRSU_L_Sensor";
	var ParameterValue = SRSU_L_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 161, 161 );

	// GEEA2_HX11_EDR_List_201 : PPS_PRSU_R_Sensor;
	var Action = "Check " + Type + " Value: PPS_PRSU_R_Sensor";
	var ParameterValue = PPS_PRSU_R_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 322, 201 );

	// GEEA2_HX11_EDR_List_202 : PPS_PRSU_L_Sensor;
	var Action = "Check " + Type + " Value: PPS_PRSU_L_Sensor";
	var ParameterValue = PPS_PRSU_L_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 523, 201 );

	// GEEA2_HX11_EDR_List_203 : PPS_GRSU_R_Sensor;
	var Action = "Check " + Type + " Value: PPS_GRSU_R_Sensor";
	var ParameterValue = PPS_GRSU_R_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 724, 201 );

	// GEEA2_HX11_EDR_List_204 : PPS_GRSU_L_Sensor;
	var Action = "Check " + Type + " Value: PPS_GRSU_L_Sensor";
	var ParameterValue = PPS_GRSU_L_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 925, 201 );

	// GEEA2_HX11_EDR_List_205 : FRSU_R_Sensor;
	var Action = "Check " + Type + " Value: FRSU_R_Sensor";
	var ParameterValue = FRSU_R_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1126, 201 );

	// GEEA2_HX11_EDR_List_206 : FRSU_L_Sensor;
	var Action = "Check " + Type + " Value: FRSU_L_Sensor";
	var ParameterValue = FRSU_L_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1327, 201 );

	// GEEA2_HX11_EDR_List_207 : PRSU_R_Sensor;
	var Action = "Check " + Type + " Value: PRSU_R_Sensor";
	var ParameterValue = PRSU_R_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1528, 161 );

	// GEEA2_HX11_EDR_List_208 : PRSU_L_Sensor;
	var Action = "Check " + Type + " Value: PRSU_L_Sensor";
	var ParameterValue = PRSU_L_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1689, 161 );

	// GEEA2_HX11_EDR_List_209 : AccelLgt_Sensor;
	var Action = "Check " + Type + " Value: AccelLgt_Sensor";
	var ParameterValue = AccelLgt_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1850, 201 );

	// GEEA2_HX11_EDR_List_210 : AccelLatt_Sensor;
	var Action = "Check " + Type + " Value: AccelLatt_Sensor";
	var ParameterValue = AccelLatt_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2051, 201 );

	// GEEA2_HX11_EDR_List_211 : ImuDataAccelLgtt_Sensor;
	var Action = "Check " + Type + " Value: ImuDataAccelLgtt_Sensor";
	var ParameterValue = ImuDataAccelLgtt_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2252, 51 );

	// GEEA2_HX11_EDR_List_212 : ImuDataAccelLatt_Sensor;
	var Action = "Check " + Type + " Value: ImuDataAccelLatt_Sensor";
	var ParameterValue = ImuDataAccelLatt_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2303, 51 );

	// GEEA2_HX11_EDR_List_213 : ImuDataYawt_Sensor;
	var Action = "Check " + Type + " Value: ImuDataYawt_Sensor";
	var ParameterValue = ImuDataYawt_Sensor;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2354, 102 );

}


