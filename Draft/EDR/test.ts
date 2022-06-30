function BB_Check_GB_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_1 : Delta–V, longitudinal;
	var Action = "Check " + Type + " Value: Delta–V, longitudinal";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 26 );

	// GEEA2_HX11_EDR_List_2 : Maximum delta–V, longitudinal;
	var Action = "Check " + Type + " Value: Maximum delta–V, longitudinal";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 1 );

	// GEEA2_HX11_EDR_List_3 : Time, maximum delta–V, longitudinal;
	var Action = "Check " + Type + " Value: Time, maximum delta–V, longitudinal";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 27, 1 );

	// GEEA2_HX11_EDR_List_4 : Clipping flag;
	var Action = "Check " + Type + " Value: Clipping flag";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 28, 2 );

	// GEEA2_HX11_EDR_List_5 : Vehicle real velocity;
	var Action = "Check " + Type + " Value: Vehicle real velocity";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 30, 11 );

	// GEEA2_HX11_EDR_List_6 : Vehicle brake status;
	var Action = "Check " + Type + " Value: Vehicle brake status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 41, 11 );

	// GEEA2_HX11_EDR_List_7 : Safety belt status, driver;
	var Action = "Check " + Type + " Value: Safety belt status, driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 52, 1 );

	// GEEA2_HX11_EDR_List_8 : Accelerator pedal, % full ;
	var Action = "Check " + Type + " Value: Accelerator pedal, % full ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 53, 11 );

	// GEEA2_HX11_EDR_List_9 : Engine Speed;
	var Action = "Check " + Type + " Value: Engine Speed";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 64, 11 );

	// GEEA2_HX11_EDR_List_10 : Ignition cycle, crash;
	var Action = "Check " + Type + " Value: Ignition cycle, crash";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 75, 2 );

	// GEEA2_HX11_EDR_List_11 : Ignition cycle, download;
	var Action = "Check " + Type + " Value: Ignition cycle, download";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 77, 2 );

	// GEEA2_HX11_EDR_List_12 : Complete file recorded (yes, no);
	var Action = "Check " + Type + " Value: Complete file recorded (yes, no)";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 79, 1 );

	// GEEA2_HX11_EDR_List_13 : Time from current event to last event ;
	var Action = "Check " + Type + " Value: Time from current event to last event ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 80, 1 );

	// GEEA2_HX11_EDR_List_14 : Vehicle Identification Number;
	var Action = "Check " + Type + " Value: Vehicle Identification Number";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 81, 17 );

	// GEEA2_HX11_EDR_List_15 : Number of ECU hardware that records EDR data ;
	var Action = "Check " + Type + " Value: Number of ECU hardware that records EDR data ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 98, 64 );

	// GEEA2_HX11_EDR_List_16 : Serial Number of ECU that records EDR data ;
	var Action = "Check " + Type + " Value: Serial Number of ECU that records EDR data ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 162, 64 );

	// GEEA2_HX11_EDR_List_17 : Number of ECU software that records EDR data ;
	var Action = "Check " + Type + " Value: Number of ECU software that records EDR data ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 226, 64 );

	// GEEA2_HX11_EDR_List_18 : Longitudinal acceleration;
	var Action = "Check " + Type + " Value: Longitudinal acceleration";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 290, 126 );

	// GEEA2_HX11_EDR_List_19 : Lateral acceleration;
	var Action = "Check " + Type + " Value: Lateral acceleration";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 416, 126 );

	// GEEA2_HX11_EDR_List_20 : Delta–V, lateral;
	var Action = "Check " + Type + " Value: Delta–V, lateral";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 542, 26 );

	// GEEA2_HX11_EDR_List_21 : Maximum delta–V, lateral;
	var Action = "Check " + Type + " Value: Maximum delta–V, lateral";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 568, 1 );

	// GEEA2_HX11_EDR_List_22 : Maximum delta–V, resultant;
	var Action = "Check " + Type + " Value: Maximum delta–V, resultant";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 569, 2 );

	// GEEA2_HX11_EDR_List_23 : Time, maximum delta–V, lateral;
	var Action = "Check " + Type + " Value: Time, maximum delta–V, lateral";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 571, 1 );

	// GEEA2_HX11_EDR_List_24 : Time, maximum delta–V, resultant;
	var Action = "Check " + Type + " Value: Time, maximum delta–V, resultant";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 572, 1 );

	// GEEA2_HX11_EDR_List_25 : Vehicle yaw rate;
	var Action = "Check " + Type + " Value: Vehicle yaw rate";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 573, 22 );

	// GEEA2_HX11_EDR_List_26 : Steering input;
	var Action = "Check " + Type + " Value: Steering input";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 595, 22 );

	// GEEA2_HX11_EDR_List_27 : Agorithm end time/Tend;
	var Action = "Check " + Type + " Value: Agorithm end time/Tend";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 617, 1 );

	// GEEA2_HX11_EDR_List_28 : Event year;
	var Action = "Check " + Type + " Value: Event year";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 618, 1 );

	// GEEA2_HX11_EDR_List_29 : Event  month;
	var Action = "Check " + Type + " Value: Event  month";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 619, 1 );

	// GEEA2_HX11_EDR_List_30 : Event  date;
	var Action = "Check " + Type + " Value: Event  date";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 620, 1 );

	// GEEA2_HX11_EDR_List_31 : Event  hour;
	var Action = "Check " + Type + " Value: Event  hour";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 621, 1 );

	// GEEA2_HX11_EDR_List_32 : Event  minute;
	var Action = "Check " + Type + " Value: Event  minute";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 622, 1 );

	// GEEA2_HX11_EDR_List_33 : Event  second;
	var Action = "Check " + Type + " Value: Event  second";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 623, 1 );

	// GEEA2_HX11_EDR_List_34 : Gear lever Position ;
	var Action = "Check " + Type + " Value: Gear lever Position ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 624, 11 );

	// GEEA2_HX11_EDR_List_35 : Engine throttle, % full ;
	var Action = "Check " + Type + " Value: Engine throttle, % full ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 635, 11 );

	// GEEA2_HX11_EDR_List_36 : Brake pedal position  ;
	var Action = "Check " + Type + " Value: Brake pedal position  ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 646, 11 );

	// GEEA2_HX11_EDR_List_37 : Parking system status             ;
	var Action = "Check " + Type + " Value: Parking system status             ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 657, 11 );

	// GEEA2_HX11_EDR_List_38 : Turn signal switch status;
	var Action = "Check " + Type + " Value: Turn signal switch status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 668, 11 );

	// GEEA2_HX11_EDR_List_39 : Pretensioner 1 deployment, time to fire,driver ;
	var Action = "Check " + Type + " Value: Pretensioner 1 deployment, time to fire,driver ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 679, 2 );

	// GEEA2_HX11_EDR_List_40 : Frontal air bag deployment, time to 1th stage, driver ;
	var Action = "Check " + Type + " Value: Frontal air bag deployment, time to 1th stage, driver ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 681, 2 );

	// GEEA2_HX11_EDR_List_41 : Frontal air bag deployment, time to 2th stage, driver ;
	var Action = "Check " + Type + " Value: Frontal air bag deployment, time to 2th stage, driver ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 683, 2 );

	// GEEA2_HX11_EDR_List_42 : Side air bag deployment, time to deploy,driver ;
	var Action = "Check " + Type + " Value: Side air bag deployment, time to deploy,driver ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 685, 2 );

	// GEEA2_HX11_EDR_List_43 : Side curtain/tube air bag deployment,time to deploy, driver side ;
	var Action = "Check " + Type + " Value: Side curtain/tube air bag deployment,time to deploy, driver side ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 687, 2 );

	// GEEA2_HX11_EDR_List_44 : Safety belt status, right front passenger (buckled, not buckled) ;
	var Action = "Check " + Type + " Value: Safety belt status, right front passenger (buckled, not buckled) ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 689, 1 );

	// GEEA2_HX11_EDR_List_45 : Pretensioner deployment, time to fire, right front passenger;
	var Action = "Check " + Type + " Value: Pretensioner deployment, time to fire, right front passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 690, 2 );

	// GEEA2_HX11_EDR_List_46 : Frontal air bag suppression switch status, right front passenger ;
	var Action = "Check " + Type + " Value: Frontal air bag suppression switch status, right front passenger ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 692, 1 );

	// GEEA2_HX11_EDR_List_47 : Frontal air bag deployment, time to 1th stage, right front passenger;
	var Action = "Check " + Type + " Value: Frontal air bag deployment, time to 1th stage, right front passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 693, 2 );

	// GEEA2_HX11_EDR_List_48 : Frontal air bag deployment, time to 2th stage, right front passenger.;
	var Action = "Check " + Type + " Value: Frontal air bag deployment, time to 2th stage, right front passenger.";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 695, 2 );

	// GEEA2_HX11_EDR_List_49 : Side air bag deployment, time to deploy,right front passenger ;
	var Action = "Check " + Type + " Value: Side air bag deployment, time to deploy,right front passenger ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 697, 2 );

	// GEEA2_HX11_EDR_List_50 : Side curtain/tube air bag deployment,time to deploy, right side ;
	var Action = "Check " + Type + " Value: Side curtain/tube air bag deployment,time to deploy, right side ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 699, 2 );

	// GEEA2_HX11_EDR_List_51 : Protection system warning lamp status， on/off ;
	var Action = "Check " + Type + " Value: Protection system warning lamp status， on/off ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 701, 1 );

	// GEEA2_HX11_EDR_List_52 : Alarm status of tire pressure monitoring system  ;
	var Action = "Check " + Type + " Value: Alarm status of tire pressure monitoring system  ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 702, 1 );

	// GEEA2_HX11_EDR_List_53 : Braking system fault status  ;
	var Action = "Check " + Type + " Value: Braking system fault status  ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 703, 1 );

	// GEEA2_HX11_EDR_List_54 : Cruise control at constant speed Mode status;
	var Action = "Check " + Type + " Value: Cruise control at constant speed Mode status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 704, 11 );

	// GEEA2_HX11_EDR_List_55 : ACC(Adaptive cruise control )Mode status ;
	var Action = "Check " + Type + " Value: ACC(Adaptive cruise control )Mode status ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 715, 11 );

	// GEEA2_HX11_EDR_List_56 : Anti-lock brake system status（ABS）;
	var Action = "Check " + Type + " Value: Anti-lock brake system status（ABS）";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 726, 11 );

	// GEEA2_HX11_EDR_List_57 : Auto Emerrgency Braking System Status ;
	var Action = "Check " + Type + " Value: Auto Emerrgency Braking System Status ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 737, 11 );

	// GEEA2_HX11_EDR_List_58 : Stability control status ;
	var Action = "Check " + Type + " Value: Stability control status ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 748, 11 );

	// GEEA2_HX11_EDR_List_59 : Traction Control System Status ;
	var Action = "Check " + Type + " Value: Traction Control System Status ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 759, 11 );

	// GEEA2_HX11_EDR_List_60 : Time from last time record data  to T0 ;
	var Action = "Check " + Type + " Value: Time from last time record data  to T0 ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 770, 2 );

}


function BB_Check_NHTSA_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_61 : Delta–V, longitudinal;
	var Action = "Check " + Type + " Value: Delta–V, longitudinal";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 26 );

	// GEEA2_HX11_EDR_List_62 : Maximum delta–V, longitudinal;
	var Action = "Check " + Type + " Value: Maximum delta–V, longitudinal";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 1 );

	// GEEA2_HX11_EDR_List_63 : Time, maximum delta–V, longitudinal;
	var Action = "Check " + Type + " Value: Time, maximum delta–V, longitudinal";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 27, 1 );

	// GEEA2_HX11_EDR_List_64 : Service brake;
	var Action = "Check " + Type + " Value: Service brake";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 28, 11 );

	// GEEA2_HX11_EDR_List_65 : Engine RPM (Combustion Engine);
	var Action = "Check " + Type + " Value: Engine RPM (Combustion Engine)";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 39, 11 );

	// GEEA2_HX11_EDR_List_66 : Engine rpm-front motor;
	var Action = "Check " + Type + " Value: Engine rpm-front motor";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 50, 22 );

	// GEEA2_HX11_EDR_List_67 : Engine rpm-rear motor;
	var Action = "Check " + Type + " Value: Engine rpm-rear motor";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 72, 22 );

	// GEEA2_HX11_EDR_List_68 : Power-on Cycle at Even;
	var Action = "Check " + Type + " Value: Power-on Cycle at Even";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 94, 2 );

	// GEEA2_HX11_EDR_List_69 : Event data recording completed;
	var Action = "Check " + Type + " Value: Event data recording completed";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 96, 1 );

	// GEEA2_HX11_EDR_List_70 : Time interval from this event to the last event;
	var Action = "Check " + Type + " Value: Time interval from this event to the last event";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 97, 1 );

	// GEEA2_HX11_EDR_List_71 : Longitudinal acceleration;
	var Action = "Check " + Type + " Value: Longitudinal acceleration";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 98, 126 );

	// GEEA2_HX11_EDR_List_72 : Lateral acceleration ;
	var Action = "Check " + Type + " Value: Lateral acceleration ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 224, 126 );

	// GEEA2_HX11_EDR_List_73 : Delta–V, lateral ;
	var Action = "Check " + Type + " Value: Delta–V, lateral ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 350, 26 );

	// GEEA2_HX11_EDR_List_74 : Maximum delta–V, lateral;
	var Action = "Check " + Type + " Value: Maximum delta–V, lateral";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 376, 1 );

	// GEEA2_HX11_EDR_List_75 : Time, maximum delta–V, lateral;
	var Action = "Check " + Type + " Value: Time, maximum delta–V, lateral";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 377, 1 );

	// GEEA2_HX11_EDR_List_76 : Engine throttle, % full ;
	var Action = "Check " + Type + " Value: Engine throttle, % full ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 378, 11 );

	// GEEA2_HX11_EDR_List_77 : Frontal air bag warning lamp;
	var Action = "Check " + Type + " Value: Frontal air bag warning lamp";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 389, 1 );

	// GEEA2_HX11_EDR_List_78 : Normal Acceleration;
	var Action = "Check " + Type + " Value: Normal Acceleration";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 390, 126 );

	// GEEA2_HX11_EDR_List_79 : Multi-event, number of event;
	var Action = "Check " + Type + " Value: Multi-event, number of event";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 516, 1 );

	// GEEA2_HX11_EDR_List_80 : Frontal airbag deployment, time to deploy, First stage, Driver ;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, time to deploy, First stage, Driver ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 517, 2 );

	// GEEA2_HX11_EDR_List_81 : Frontal airbag deployment, time to deploy, Second stage, Driver ;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, time to deploy, Second stage, Driver ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 519, 2 );

	// GEEA2_HX11_EDR_List_82 : Frontal airbag deployment, time to deploy, Third stage, Driver ;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, time to deploy, Third stage, Driver ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 521, 2 );

	// GEEA2_HX11_EDR_List_83 : Frontal airbag deployment, time to deploy, First stage, Passenger front passenger;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, time to deploy, First stage, Passenger front passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 523, 2 );

	// GEEA2_HX11_EDR_List_84 : Frontal airbag deployment, time to deploy, Second stage, Passenger front passenger;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, time to deploy, Second stage, Passenger front passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 525, 2 );

	// GEEA2_HX11_EDR_List_85 : Frontal airbag deployment, time to deploy, Third stage, Passenger front passenger.;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, time to deploy, Third stage, Passenger front passenger.";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 527, 2 );

	// GEEA2_HX11_EDR_List_86 : Driver shoulder belt pretensioner, time to deploy;
	var Action = "Check " + Type + " Value: Driver shoulder belt pretensioner, time to deploy";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 529, 2 );

	// GEEA2_HX11_EDR_List_87 : Passenger shoulder belt pretensioner, time to deploy;
	var Action = "Check " + Type + " Value: Passenger shoulder belt pretensioner, time to deploy";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 531, 2 );

	// GEEA2_HX11_EDR_List_88 : Seat Belt Status,Driver;
	var Action = "Check " + Type + " Value: Seat Belt Status,Driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 533, 1 );

	// GEEA2_HX11_EDR_List_89 : Seat Track Position ,Front driver;
	var Action = "Check " + Type + " Value: Seat Track Position ,Front driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 534, 1 );

	// GEEA2_HX11_EDR_List_90 : Frontal Airbag Suppression Switch Status, Front Passenger;
	var Action = "Check " + Type + " Value: Frontal Airbag Suppression Switch Status, Front Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 535, 1 );

	// GEEA2_HX11_EDR_List_91 : Seat Belt Status,Passenger;
	var Action = "Check " + Type + " Value: Seat Belt Status,Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 536, 1 );

	// GEEA2_HX11_EDR_List_92 : Seat Track Position ,Front Passenger;
	var Action = "Check " + Type + " Value: Seat Track Position ,Front Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 537, 1 );

	// GEEA2_HX11_EDR_List_93 : Occupant Size Classification, Front Passenger(OCS/OWS);
	var Action = "Check " + Type + " Value: Occupant Size Classification, Front Passenger(OCS/OWS)";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 538, 1 );

	// GEEA2_HX11_EDR_List_94 : Vehicle speed indicated;
	var Action = "Check " + Type + " Value: Vehicle speed indicated";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 539, 11 );

	// GEEA2_HX11_EDR_List_95 : Steering Angle;
	var Action = "Check " + Type + " Value: Steering Angle";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 550, 22 );

	// GEEA2_HX11_EDR_List_96 : ABS Activity;
	var Action = "Check " + Type + " Value: ABS Activity";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 572, 11 );

	// GEEA2_HX11_EDR_List_97 : Stability Control;
	var Action = "Check " + Type + " Value: Stability Control";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 583, 11 );

	// GEEA2_HX11_EDR_List_98 : Shoulder belt pretensioner, Rear Left, time to deploy;
	var Action = "Check " + Type + " Value: Shoulder belt pretensioner, Rear Left, time to deploy";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 594, 2 );

	// GEEA2_HX11_EDR_List_99 : Shoulder belt pretensioner, Rear Right, time to deploy;
	var Action = "Check " + Type + " Value: Shoulder belt pretensioner, Rear Right, time to deploy";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 596, 2 );

	// GEEA2_HX11_EDR_List_100 : Left side airbag, time to deploy ;
	var Action = "Check " + Type + " Value: Left side airbag, time to deploy ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 598, 2 );

	// GEEA2_HX11_EDR_List_101 : Right side airbag, time to deploy ;
	var Action = "Check " + Type + " Value: Right side airbag, time to deploy ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 600, 2 );

	// GEEA2_HX11_EDR_List_102 : Left side Inflatable Curtain, time to deploy ;
	var Action = "Check " + Type + " Value: Left side Inflatable Curtain, time to deploy ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 602, 2 );

	// GEEA2_HX11_EDR_List_103 : Right side Inflatable Curtain, time to deploy;
	var Action = "Check " + Type + " Value: Right side Inflatable Curtain, time to deploy";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 604, 2 );

	// GEEA2_HX11_EDR_List_104 : Occupant Passenger Presence, Front Passenger;
	var Action = "Check " + Type + " Value: Occupant Passenger Presence, Front Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 606, 1 );

	// GEEA2_HX11_EDR_List_105 : Roll Angle;
	var Action = "Check " + Type + " Value: Roll Angle";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 607, 61 );

	// GEEA2_HX11_EDR_List_106 : Power-on Cycle when download;
	var Action = "Check " + Type + " Value: Power-on Cycle when download";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 668, 2 );

	// GEEA2_HX11_EDR_List_107 : Time, maximum delta-V, resultant;
	var Action = "Check " + Type + " Value: Time, maximum delta-V, resultant";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 670, 1 );

	// GEEA2_HX11_EDR_List_108 : Frontal airbag deployment, Second stage disposal, Driver;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, Second stage disposal, Driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 671, 1 );

	// GEEA2_HX11_EDR_List_109 : Frontal airbag deployment, Third stage disposal, Driver;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, Third stage disposal, Driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 672, 1 );

	// GEEA2_HX11_EDR_List_110 : Frontal airbag deployment, Second stage disposal, Passenger;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, Second stage disposal, Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 673, 1 );

	// GEEA2_HX11_EDR_List_111 : Frontal airbag deployment, Third stage disposal, Passenger;
	var Action = "Check " + Type + " Value: Frontal airbag deployment, Third stage disposal, Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 674, 1 );

}


function BB_Check_ECE_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_214 : Delta–V, longitudinal;
	var Action = "Check " + Type + " Value: Delta–V, longitudinal";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 26 );

	// GEEA2_HX11_EDR_List_215 : Maximum delta–V, longitudinal;
	var Action = "Check " + Type + " Value: Maximum delta–V, longitudinal";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 1 );

	// GEEA2_HX11_EDR_List_216 : Time, maximum delta–V, longitudinal;
	var Action = "Check " + Type + " Value: Time, maximum delta–V, longitudinal";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 27, 1 );

	// GEEA2_HX11_EDR_List_217 : Speed, vehicle indicated/车速;
	var Action = "Check " + Type + " Value: Speed, vehicle indicated/车速";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 28, 11 );

	// GEEA2_HX11_EDR_List_218 : Accelerator pedal, % full ;
	var Action = "Check " + Type + " Value: Accelerator pedal, % full ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 39, 11 );

	// GEEA2_HX11_EDR_List_219 : Service brake,  on/off;
	var Action = "Check " + Type + " Value: Service brake,  on/off";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 50, 11 );

	// GEEA2_HX11_EDR_List_220 : Ignition cycle, crash;
	var Action = "Check " + Type + " Value: Ignition cycle, crash";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 61, 2 );

	// GEEA2_HX11_EDR_List_221 : Ignition cycle, download;
	var Action = "Check " + Type + " Value: Ignition cycle, download";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 63, 2 );

	// GEEA2_HX11_EDR_List_222 : Safety belt status, driver;
	var Action = "Check " + Type + " Value: Safety belt status, driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 65, 1 );

	// GEEA2_HX11_EDR_List_223 : Frontal air bag warning lamp            ;
	var Action = "Check " + Type + " Value: Frontal air bag warning lamp            ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 66, 1 );

	// GEEA2_HX11_EDR_List_224 : Frontal air bag deployment, time to deploy;
	var Action = "Check " + Type + " Value: Frontal air bag deployment, time to deploy";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 67, 2 );

	// GEEA2_HX11_EDR_List_225 : Frontal air bag deployment, time to deploy;
	var Action = "Check " + Type + " Value: Frontal air bag deployment, time to deploy";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 69, 2 );

	// GEEA2_HX11_EDR_List_226 : Multi-event, number of event;
	var Action = "Check " + Type + " Value: Multi-event, number of event";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 71, 1 );

	// GEEA2_HX11_EDR_List_227 : Time from event 1 to 2 ;
	var Action = "Check " + Type + " Value: Time from event 1 to 2 ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 72, 1 );

	// GEEA2_HX11_EDR_List_228 : Complete file recorded (yes, no);
	var Action = "Check " + Type + " Value: Complete file recorded (yes, no)";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 73, 1 );

	// GEEA2_HX11_EDR_List_229 : Lateral acceleration (post-crash) ;
	var Action = "Check " + Type + " Value: Lateral acceleration (post-crash) ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 74, 126 );

	// GEEA2_HX11_EDR_List_230 : Longitudinal acceleration (post-crash) ;
	var Action = "Check " + Type + " Value: Longitudinal acceleration (post-crash) ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 200, 126 );

	// GEEA2_HX11_EDR_List_231 : Normal Acceleration;
	var Action = "Check " + Type + " Value: Normal Acceleration";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 326, 61 );

	// GEEA2_HX11_EDR_List_232 : Delta–V, lateral;
	var Action = "Check " + Type + " Value: Delta–V, lateral";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 387, 26 );

	// GEEA2_HX11_EDR_List_233 : Maximum delta–V, lateral;
	var Action = "Check " + Type + " Value: Maximum delta–V, lateral";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 413, 1 );

	// GEEA2_HX11_EDR_List_234 : Time, maximum delta–V, lateral;
	var Action = "Check " + Type + " Value: Time, maximum delta–V, lateral";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 414, 1 );

	// GEEA2_HX11_EDR_List_235 : Time, maximum delta–V, resultant;
	var Action = "Check " + Type + " Value: Time, maximum delta–V, resultant";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 415, 1 );

	// GEEA2_HX11_EDR_List_236 : Engine rpm;
	var Action = "Check " + Type + " Value: Engine rpm";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 416, 11 );

	// GEEA2_HX11_EDR_List_237 : Engine rpm-front motor;
	var Action = "Check " + Type + " Value: Engine rpm-front motor";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 427, 22 );

	// GEEA2_HX11_EDR_List_238 : Engine rpm-rear motor;
	var Action = "Check " + Type + " Value: Engine rpm-rear motor";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 449, 22 );

	// GEEA2_HX11_EDR_List_239 : Engine rpm-front motor 800V;
	var Action = "Check " + Type + " Value: Engine rpm-front motor 800V";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 471, 22 );

	// GEEA2_HX11_EDR_List_240 : Engine rpm-rear motor 800V;
	var Action = "Check " + Type + " Value: Engine rpm-rear motor 800V";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 493, 22 );

	// GEEA2_HX11_EDR_List_241 : Vehicle roll angle ;
	var Action = "Check " + Type + " Value: Vehicle roll angle ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 515, 61 );

	// GEEA2_HX11_EDR_List_242 : Vehicle roll rate ;
	var Action = "Check " + Type + " Value: Vehicle roll rate ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 576, 122 );

	// GEEA2_HX11_EDR_List_243 : ABS Activity;
	var Action = "Check " + Type + " Value: ABS Activity";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 698, 11 );

	// GEEA2_HX11_EDR_List_244 : Stability Control;
	var Action = "Check " + Type + " Value: Stability Control";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 709, 11 );

	// GEEA2_HX11_EDR_List_245 : Steering input;
	var Action = "Check " + Type + " Value: Steering input";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 720, 22 );

	// GEEA2_HX11_EDR_List_246 : Safety belt status, front passenger ;
	var Action = "Check " + Type + " Value: Safety belt status, front passenger ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 742, 1 );

	// GEEA2_HX11_EDR_List_247 : Passenger air bag suppression status, front;
	var Action = "Check " + Type + " Value: Passenger air bag suppression status, front";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 743, 1 );

	// GEEA2_HX11_EDR_List_248 : Frontal air bag deployment, time to deploy, Second stage, Driver ;
	var Action = "Check " + Type + " Value: Frontal air bag deployment, time to deploy, Second stage, Driver ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 744, 2 );

	// GEEA2_HX11_EDR_List_249 : Frontal air bag deployment, time to deploy, Second stage, Passenger;
	var Action = "Check " + Type + " Value: Frontal air bag deployment, time to deploy, Second stage, Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 746, 2 );

	// GEEA2_HX11_EDR_List_250 : Side air bag deployment, time to deploy, driver;
	var Action = "Check " + Type + " Value: Side air bag deployment, time to deploy, driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 748, 2 );

	// GEEA2_HX11_EDR_List_251 : Side air bag deployment, time to deploy, front passenger;
	var Action = "Check " + Type + " Value: Side air bag deployment, time to deploy, front passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 750, 2 );

	// GEEA2_HX11_EDR_List_252 : Side curtain/tube air bag deployment, time to deploy, driver side;
	var Action = "Check " + Type + " Value: Side curtain/tube air bag deployment, time to deploy, driver side";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 752, 2 );

	// GEEA2_HX11_EDR_List_253 : Side curtain/tube air bag deployment, time to deploy, passenger side;
	var Action = "Check " + Type + " Value: Side curtain/tube air bag deployment, time to deploy, passenger side";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 754, 2 );

	// GEEA2_HX11_EDR_List_254 : Pretensioner deployment, time to fire, driver.;
	var Action = "Check " + Type + " Value: Pretensioner deployment, time to fire, driver.";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 756, 2 );

	// GEEA2_HX11_EDR_List_255 : Pretensioner deployment, time to fire, front passenger;
	var Action = "Check " + Type + " Value: Pretensioner deployment, time to fire, front passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 758, 2 );

	// GEEA2_HX11_EDR_List_256 : Seat track position switch, foremost, status, driver;
	var Action = "Check " + Type + " Value: Seat track position switch, foremost, status, driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 760, 1 );

	// GEEA2_HX11_EDR_List_257 : Seat track position switch, foremost, status, front passenger.;
	var Action = "Check " + Type + " Value: Seat track position switch, foremost, status, front passenger.";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 761, 1 );

	// GEEA2_HX11_EDR_List_258 : Occupant size classification, driver;
	var Action = "Check " + Type + " Value: Occupant size classification, driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 762, 1 );

	// GEEA2_HX11_EDR_List_259 : Occupant size classification, front passenger;
	var Action = "Check " + Type + " Value: Occupant size classification, front passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 763, 1 );

	// GEEA2_HX11_EDR_List_260 : Safety belt status, rear passengers left;
	var Action = "Check " + Type + " Value: Safety belt status, rear passengers left";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 764, 1 );

	// GEEA2_HX11_EDR_List_261 : Safety belt status, rear passengers right;
	var Action = "Check " + Type + " Value: Safety belt status, rear passengers right";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 765, 1 );

	// GEEA2_HX11_EDR_List_262 : Safety belt status, rear passengers midle;
	var Action = "Check " + Type + " Value: Safety belt status, rear passengers midle";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 766, 1 );

	// GEEA2_HX11_EDR_List_263 : Tyre Pressure Monitoring System (TPMS) Warning Lamp Status;
	var Action = "Check " + Type + " Value: Tyre Pressure Monitoring System (TPMS) Warning Lamp Status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 767, 1 );

	// GEEA2_HX11_EDR_List_264 : Longitudinal acceleration(pre – crash);
	var Action = "Check " + Type + " Value: Longitudinal acceleration(pre – crash)";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 768, 11 );

	// GEEA2_HX11_EDR_List_265 : Lateral acceleration(pre – crash);
	var Action = "Check " + Type + " Value: Lateral acceleration(pre – crash)";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 779, 11 );

	// GEEA2_HX11_EDR_List_266 : Yaw rate;
	var Action = "Check " + Type + " Value: Yaw rate";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 790, 22 );

	// GEEA2_HX11_EDR_List_267 : Traction Control Status ;
	var Action = "Check " + Type + " Value: Traction Control Status ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 812, 11 );

	// GEEA2_HX11_EDR_List_268 : AEBS status;
	var Action = "Check " + Type + " Value: AEBS status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 823, 11 );

	// GEEA2_HX11_EDR_List_269 : Cruise Control System;
	var Action = "Check " + Type + " Value: Cruise Control System";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 834, 11 );

	// GEEA2_HX11_EDR_List_270 : Adaptive Cruise Control Status (driving automation system level 1) ;
	var Action = "Check " + Type + " Value: Adaptive Cruise Control Status (driving automation system level 1) ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 845, 11 );

	// GEEA2_HX11_EDR_List_271 : VRU secondary safety system deployment, time to deploy;
	var Action = "Check " + Type + " Value: VRU secondary safety system deployment, time to deploy";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 856, 2 );

	// GEEA2_HX11_EDR_List_272 : VRU secondary safety system warning indicator status;
	var Action = "Check " + Type + " Value: VRU secondary safety system warning indicator status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 858, 1 );

	// GEEA2_HX11_EDR_List_273 : Safety belt status mid-position front ;
	var Action = "Check " + Type + " Value: Safety belt status mid-position front ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 859, 1 );

	// GEEA2_HX11_EDR_List_274 : Far side impact center airbag;
	var Action = "Check " + Type + " Value: Far side impact center airbag";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 860, 2 );

	// GEEA2_HX11_EDR_List_275 : Accident emergency call system status;
	var Action = "Check " + Type + " Value: Accident emergency call system status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 862, 1 );

	// GEEA2_HX11_EDR_List_276 : Lane departure warning system status;
	var Action = "Check " + Type + " Value: Lane departure warning system status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 863, 11 );

	// GEEA2_HX11_EDR_List_277 : Corrective steering function (CSF) status;
	var Action = "Check " + Type + " Value: Corrective steering function (CSF) status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 874, 11 );

	// GEEA2_HX11_EDR_List_278 : Emergency steering function (ESF) status;
	var Action = "Check " + Type + " Value: Emergency steering function (ESF) status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 885, 11 );

	// GEEA2_HX11_EDR_List_279 :  (ACSF) category A status-APA;
	var Action = "Check " + Type + " Value:  (ACSF) category A status-APA";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 896, 11 );

	// GEEA2_HX11_EDR_List_280 :  (ACSF) category A status-RPA;
	var Action = "Check " + Type + " Value:  (ACSF) category A status-RPA";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 907, 11 );

	// GEEA2_HX11_EDR_List_281 :  (ACSF) category A status-AVP;
	var Action = "Check " + Type + " Value:  (ACSF) category A status-AVP";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 918, 11 );

	// GEEA2_HX11_EDR_List_282 :  (ACSF) category B1 status-HWA(LK);
	var Action = "Check " + Type + " Value:  (ACSF) category B1 status-HWA(LK)";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 929, 11 );

	// GEEA2_HX11_EDR_List_283 : (ACSF) category B2 status;
	var Action = "Check " + Type + " Value: (ACSF) category B2 status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 940, 11 );

	// GEEA2_HX11_EDR_List_284 : (ACSF) category C status-LKA;
	var Action = "Check " + Type + " Value: (ACSF) category C status-LKA";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 951, 11 );

	// GEEA2_HX11_EDR_List_285 : (ACSF) category C status_x0002_HWA(ALCA);
	var Action = "Check " + Type + " Value: (ACSF) category C status_x0002_HWA(ALCA)";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 962, 11 );

	// GEEA2_HX11_EDR_List_286 : (ACSF) category D status;
	var Action = "Check " + Type + " Value: (ACSF) category D status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 973, 11 );

	// GEEA2_HX11_EDR_List_287 : (ACSF) category E status-EMA;
	var Action = "Check " + Type + " Value: (ACSF) category E status-EMA";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 984, 11 );

	// GEEA2_HX11_EDR_List_288 : (ACSF) category E status-ELKA;
	var Action = "Check " + Type + " Value: (ACSF) category E status-ELKA";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 995, 11 );

	// GEEA2_HX11_EDR_List_289 : (ACSF) category E status-NOP助;
	var Action = "Check " + Type + " Value: (ACSF) category E status-NOP助";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1006, 11 );

}


function BB_Check_Header_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_112 : Data Area Status;
	var Action = "Check " + Type + " Value: Data Area Status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 1 );

	// GEEA2_HX11_EDR_List_113 : Data Area Read Status;
	var Action = "Check " + Type + " Value: Data Area Read Status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1, 1 );

	// GEEA2_HX11_EDR_List_114 : Global Time;
	var Action = "Check " + Type + " Value: Global Time";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2, 4 );

	// GEEA2_HX11_EDR_List_115 : Time and Date indicated - Year;
	var Action = "Check " + Type + " Value: Time and Date indicated - Year";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 6, 1 );

	// GEEA2_HX11_EDR_List_116 : Time and Date indicated - Month;
	var Action = "Check " + Type + " Value: Time and Date indicated - Month";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 7, 1 );

	// GEEA2_HX11_EDR_List_117 : Time and Date indicated - Day;
	var Action = "Check " + Type + " Value: Time and Date indicated - Day";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 8, 1 );

	// GEEA2_HX11_EDR_List_118 : Time and Date indicated - Hour;
	var Action = "Check " + Type + " Value: Time and Date indicated - Hour";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 9, 1 );

	// GEEA2_HX11_EDR_List_119 : Time and Date indicated - Minutes;
	var Action = "Check " + Type + " Value: Time and Date indicated - Minutes";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 10, 1 );

	// GEEA2_HX11_EDR_List_120 : Time and Date indicated - Seconds;
	var Action = "Check " + Type + " Value: Time and Date indicated - Seconds";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 11, 1 );

	// GEEA2_HX11_EDR_List_121 : Total Event Count;
	var Action = "Check " + Type + " Value: Total Event Count";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 12, 2 );

	// GEEA2_HX11_EDR_List_122 : Autarky Time Stamp;
	var Action = "Check " + Type + " Value: Autarky Time Stamp";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 14, 2 );

	// GEEA2_HX11_EDR_List_123 : Crash Count Per Direction - Front;
	var Action = "Check " + Type + " Value: Crash Count Per Direction - Front";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 16, 2 );

	// GEEA2_HX11_EDR_List_124 : Crash Count Per Direction - Side;
	var Action = "Check " + Type + " Value: Crash Count Per Direction - Side";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 18, 2 );

	// GEEA2_HX11_EDR_List_125 : Crash Count Per Direction - Rear;
	var Action = "Check " + Type + " Value: Crash Count Per Direction - Rear";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 20, 2 );

	// GEEA2_HX11_EDR_List_126 : Crash Count Per Direction - Roll Over;
	var Action = "Check " + Type + " Value: Crash Count Per Direction - Roll Over";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 22, 2 );

	// GEEA2_HX11_EDR_List_127 : Crash Count Per Direction - Pitch Over;
	var Action = "Check " + Type + " Value: Crash Count Per Direction - Pitch Over";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 24, 2 );

	// GEEA2_HX11_EDR_List_128 : Crash Count Per Direction - EPP;
	var Action = "Check " + Type + " Value: Crash Count Per Direction - EPP";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 2 );

	// GEEA2_HX11_EDR_List_129 : Crash Count Per Direction - Slow Roll Over;
	var Action = "Check " + Type + " Value: Crash Count Per Direction - Slow Roll Over";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 28, 2 );

	// GEEA2_HX11_EDR_List_130 : Record Complete Status;
	var Action = "Check " + Type + " Value: Record Complete Status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 30, 1 );

}


function BB_Check_OEM_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_131 : Time to fire for crash protection-Frontal airbag deployment, First stage, Driver;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Frontal airbag deployment, First stage, Driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 2 );

	// GEEA2_HX11_EDR_List_134 : Time to fire for crash protection-Frontal airbag deployment, First stage, Passenger;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Frontal airbag deployment, First stage, Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2, 2 );

	// GEEA2_HX11_EDR_List_137 : Time to fire for crash protection-Driver shoulder belt pretensioner;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Driver shoulder belt pretensioner";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 4, 2 );

	// GEEA2_HX11_EDR_List_138 : Time to fire for crash protection-Passenger shoulder belt pretensioner;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Passenger shoulder belt pretensioner";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 6, 2 );

	// GEEA2_HX11_EDR_List_139 : Time to fire for crash protection-Left side airbag;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Left side airbag";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 8, 2 );

	// GEEA2_HX11_EDR_List_140 : Time to fire for crash protection-Right side airbag;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Right side airbag";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 10, 2 );

	// GEEA2_HX11_EDR_List_141 : Time to fire for crash protection-Left side Inflatable Curtain;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Left side Inflatable Curtain";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 12, 2 );

	// GEEA2_HX11_EDR_List_142 : Time to fire for crash protection-Right side Inflatable Curtain;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Right side Inflatable Curtain";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 14, 2 );

	// GEEA2_HX11_EDR_List_143 : Time to fire for crash protection-High Voltage (HV) Disconnect;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-High Voltage (HV) Disconnect";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 16, 2 );

	// GEEA2_HX11_EDR_List_144 : Time to fire for crash protection-Rear Bonnet Hinge Left;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Rear Bonnet Hinge Left";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 18, 2 );

	// GEEA2_HX11_EDR_List_145 : Time to fire for crash protection-Rear Bonnet Hinge Right;
	var Action = "Check " + Type + " Value: Time to fire for crash protection-Rear Bonnet Hinge Right";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 20, 2 );

	// GEEA2_HX11_EDR_List_146 : Occupant Passenger Presence, Front Passenger;
	var Action = "Check " + Type + " Value: Occupant Passenger Presence, Front Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 22, 1 );

	// GEEA2_HX11_EDR_List_147 : Accelerator Pedal Status;
	var Action = "Check " + Type + " Value: Accelerator Pedal Status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 23, 1 );

	// GEEA2_HX11_EDR_List_148 : Ambient air temperature;
	var Action = "Check " + Type + " Value: Ambient air temperature";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 24, 2 );

	// GEEA2_HX11_EDR_List_149 : Battery VoltageKL15;
	var Action = "Check " + Type + " Value: Battery VoltageKL15";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 26, 28 );

	// GEEA2_HX11_EDR_List_150 : Battery VoltageKL30 ;
	var Action = "Check " + Type + " Value: Battery VoltageKL30 ";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 54, 28 );

	// GEEA2_HX11_EDR_List_151 : Belt buckle status of Front Driver;
	var Action = "Check " + Type + " Value: Belt buckle status of Front Driver";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 82, 1 );

	// GEEA2_HX11_EDR_List_152 : Belt buckle status of Front Passenger;
	var Action = "Check " + Type + " Value: Belt buckle status of Front Passenger";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 83, 1 );

	// GEEA2_HX11_EDR_List_153 : Belt buckle status of second row Left;
	var Action = "Check " + Type + " Value: Belt buckle status of second row Left";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 84, 1 );

	// GEEA2_HX11_EDR_List_154 : Belt buckle status of second row Right;
	var Action = "Check " + Type + " Value: Belt buckle status of second row Right";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 85, 1 );

	// GEEA2_HX11_EDR_List_155 : Belt buckle status of second row Middle;
	var Action = "Check " + Type + " Value: Belt buckle status of second row Middle";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 86, 1 );

	// GEEA2_HX11_EDR_List_156 : Brake system pressure;
	var Action = "Check " + Type + " Value: Brake system pressure";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 87, 28 );

	// GEEA2_HX11_EDR_List_157 : Door Status - DoorDrvrSts;
	var Action = "Check " + Type + " Value: Door Status - DoorDrvrSts";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 115, 1 );

	// GEEA2_HX11_EDR_List_158 : Door Status - DoorPassSts;
	var Action = "Check " + Type + " Value: Door Status - DoorPassSts";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 116, 1 );

	// GEEA2_HX11_EDR_List_159 : Door Status - DoorLeReSts;
	var Action = "Check " + Type + " Value: Door Status - DoorLeReSts";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 117, 1 );

	// GEEA2_HX11_EDR_List_160 : Door Status -  DoorRiReSts;
	var Action = "Check " + Type + " Value: Door Status -  DoorRiReSts";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 118, 1 );

	// GEEA2_HX11_EDR_List_161 : Hybrid mode;
	var Action = "Check " + Type + " Value: Hybrid mode";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 119, 1 );

	// GEEA2_HX11_EDR_List_162 : PostCrash-Door Lock Status 1.DoorDrvrLockSts;
	var Action = "Check " + Type + " Value: PostCrash-Door Lock Status 1.DoorDrvrLockSts";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 120, 1 );

	// GEEA2_HX11_EDR_List_163 : PostCrash-Door Lock Status 2.DoorPassLockSts Sample;
	var Action = "Check " + Type + " Value: PostCrash-Door Lock Status 2.DoorPassLockSts Sample";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 121, 1 );

	// GEEA2_HX11_EDR_List_164 : PostCrash-Door Lock Status 3.DoorLeReLockSts sample;
	var Action = "Check " + Type + " Value: PostCrash-Door Lock Status 3.DoorLeReLockSts sample";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 122, 1 );

	// GEEA2_HX11_EDR_List_165 : PostCrash-Door Lock Status 4.DoorRiReLockSts sample;
	var Action = "Check " + Type + " Value: PostCrash-Door Lock Status 4.DoorRiReLockSts sample";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 123, 1 );

	// GEEA2_HX11_EDR_List_166 : Post impact braking status;
	var Action = "Check " + Type + " Value: Post impact braking status";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 124, 1 );

	// GEEA2_HX11_EDR_List_167 : PreCrash-Door Lock Status 1.DoorDrvrLockSts;
	var Action = "Check " + Type + " Value: PreCrash-Door Lock Status 1.DoorDrvrLockSts";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 125, 1 );

	// GEEA2_HX11_EDR_List_168 : PreCrash-Door Lock Status 2.DoorPassLockSts;
	var Action = "Check " + Type + " Value: PreCrash-Door Lock Status 2.DoorPassLockSts";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 126, 1 );

	// GEEA2_HX11_EDR_List_169 : PreCrash-Door Lock Status 3.DoorLeReLockSts;
	var Action = "Check " + Type + " Value: PreCrash-Door Lock Status 3.DoorLeReLockSts";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 127, 1 );

	// GEEA2_HX11_EDR_List_170 : PreCrash-Door Lock Status 4.DoorRiReLockSts;
	var Action = "Check " + Type + " Value: PreCrash-Door Lock Status 4.DoorRiReLockSts";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 128, 1 );

	// GEEA2_HX11_EDR_List_171 : Pre-crash environmental data Longitude - coordinates;
	var Action = "Check " + Type + " Value: Pre-crash environmental data Longitude - coordinates";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 129, 24 );

	// GEEA2_HX11_EDR_List_172 : Pre-crash environmental data Latitude - coordinates;
	var Action = "Check " + Type + " Value: Pre-crash environmental data Latitude - coordinates";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 153, 24 );

	// GEEA2_HX11_EDR_List_173 : Pre-crash handling - accelerator pedal position;
	var Action = "Check " + Type + " Value: Pre-crash handling - accelerator pedal position";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 177, 102 );

	// GEEA2_HX11_EDR_List_174 : Pre-crash handling - brake pedal position;
	var Action = "Check " + Type + " Value: Pre-crash handling - brake pedal position";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 279, 102 );

	// GEEA2_HX11_EDR_List_175 : Pre-crash handling - gear position;
	var Action = "Check " + Type + " Value: Pre-crash handling - gear position";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 381, 11 );

	// GEEA2_HX11_EDR_List_176 : Pre-crash handling - steering wheel;
	var Action = "Check " + Type + " Value: Pre-crash handling - steering wheel";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 392, 102 );

	// GEEA2_HX11_EDR_List_177 : QF - Brake System Pressure;
	var Action = "Check " + Type + " Value: QF - Brake System Pressure";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 494, 2 );

	// GEEA2_HX11_EDR_List_178 : QF - Brake Pedal Position;
	var Action = "Check " + Type + " Value: QF - Brake Pedal Position";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 494, 2 );

	// GEEA2_HX11_EDR_List_179 : QF - Driver Seat Height Position;
	var Action = "Check " + Type + " Value: QF - Driver Seat Height Position";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 494, 2 );

	// GEEA2_HX11_EDR_List_180 : QF - Driver Length Position;
	var Action = "Check " + Type + " Value: QF - Driver Length Position";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 494, 2 );

	// GEEA2_HX11_EDR_List_181 : QF - Passenger Seat Height Position;
	var Action = "Check " + Type + " Value: QF - Passenger Seat Height Position";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 494, 2 );

	// GEEA2_HX11_EDR_List_182 : QF - Passenger Length Position;
	var Action = "Check " + Type + " Value: QF - Passenger Length Position";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 494, 2 );

	// GEEA2_HX11_EDR_List_183 : QF - Ambient Temperature;
	var Action = "Check " + Type + " Value: QF - Ambient Temperature";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 494, 2 );

	// GEEA2_HX11_EDR_List_184 : QF - Battery Voltage;
	var Action = "Check " + Type + " Value: QF - Battery Voltage";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 494, 2 );

	// GEEA2_HX11_EDR_List_185 : Seat position - memory seats Driver Seat;
	var Action = "Check " + Type + " Value: Seat position - memory seats Driver Seat";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 496, 2 );

	// GEEA2_HX11_EDR_List_186 : Seat position - memory seats Passenger Seat;
	var Action = "Check " + Type + " Value: Seat position - memory seats Passenger Seat";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 498, 2 );

	// GEEA2_HX11_EDR_List_187 : 2nd row left seat belt reminder mat;
	var Action = "Check " + Type + " Value: 2nd row left seat belt reminder mat";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 500, 1 );

	// GEEA2_HX11_EDR_List_188 : 2nd row middle seat belt reminder mat;
	var Action = "Check " + Type + " Value: 2nd row middle seat belt reminder mat";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 501, 1 );

	// GEEA2_HX11_EDR_List_189 : 2nd row right seat belt reminder mat;
	var Action = "Check " + Type + " Value: 2nd row right seat belt reminder mat";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 502, 1 );

	// GEEA2_HX11_EDR_List_190 : Deployment Counter;
	var Action = "Check " + Type + " Value: Deployment Counter";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 503, 1 );

	// GEEA2_HX11_EDR_List_191 : Activated algorithms - Front;
	var Action = "Check " + Type + " Value: Activated algorithms - Front";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 504, 1 );

	// GEEA2_HX11_EDR_List_192 : Activated algorithms - Side Left;
	var Action = "Check " + Type + " Value: Activated algorithms - Side Left";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 504, 1 );

	// GEEA2_HX11_EDR_List_193 : Activated algorithms - Side Right;
	var Action = "Check " + Type + " Value: Activated algorithms - Side Right";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 504, 1 );

	// GEEA2_HX11_EDR_List_194 : Activated algorithms - Rear;
	var Action = "Check " + Type + " Value: Activated algorithms - Rear";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 504, 1 );

	// GEEA2_HX11_EDR_List_195 : Activated algorithms - Roll;
	var Action = "Check " + Type + " Value: Activated algorithms - Roll";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 504, 1 );

	// GEEA2_HX11_EDR_List_196 : Activated algorithms - Pitch;
	var Action = "Check " + Type + " Value: Activated algorithms - Pitch";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 504, 1 );

	// GEEA2_HX11_EDR_List_197 : Activated algorithms - Pedestrian;
	var Action = "Check " + Type + " Value: Activated algorithms - Pedestrian";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 504, 1 );

	// GEEA2_HX11_EDR_List_198 : Pre-crash handling - master cylinder pressure;
	var Action = "Check " + Type + " Value: Pre-crash handling - master cylinder pressure";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 505, 102 );

}


function BB_Check_Sensor_EDR(Type,DataRecord)
{
	// GEEA2_HX11_EDR_List_199 : Side Acceleration Sensors Front Row Right;
	var Action = "Check " + Type + " Value: Side Acceleration Sensors Front Row Right";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 0, 161 );

	// GEEA2_HX11_EDR_List_200 : Side Acceleration Sensors Front Row Left;
	var Action = "Check " + Type + " Value: Side Acceleration Sensors Front Row Left";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 161, 161 );

	// GEEA2_HX11_EDR_List_201 : Pedestrain Protection Pressure Sensor Right;
	var Action = "Check " + Type + " Value: Pedestrain Protection Pressure Sensor Right";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 322, 201 );

	// GEEA2_HX11_EDR_List_202 : Pedestrain Protection Pressure Sensor Left;
	var Action = "Check " + Type + " Value: Pedestrain Protection Pressure Sensor Left";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 523, 201 );

	// GEEA2_HX11_EDR_List_203 : Pedestrain Protection Acceleration Sensor Right;
	var Action = "Check " + Type + " Value: Pedestrain Protection Acceleration Sensor Right";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 724, 201 );

	// GEEA2_HX11_EDR_List_204 : Pedestrain Protection Acceleration Sensor Left;
	var Action = "Check " + Type + " Value: Pedestrain Protection Acceleration Sensor Left";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 925, 201 );

	// GEEA2_HX11_EDR_List_205 : Front Acceleration Sensor Right;
	var Action = "Check " + Type + " Value: Front Acceleration Sensor Right";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1126, 201 );

	// GEEA2_HX11_EDR_List_206 : Front Acceleration Sensor Left;
	var Action = "Check " + Type + " Value: Front Acceleration Sensor Left";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1327, 201 );

	// GEEA2_HX11_EDR_List_207 : Side Pressure Sensor Right;
	var Action = "Check " + Type + " Value: Side Pressure Sensor Right";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1528, 161 );

	// GEEA2_HX11_EDR_List_208 : Side Pressure Sensor Left;
	var Action = "Check " + Type + " Value: Side Pressure Sensor Left";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1689, 161 );

	// GEEA2_HX11_EDR_List_209 : Internal Acceleration Sensor CxHighG;
	var Action = "Check " + Type + " Value: Internal Acceleration Sensor CxHighG";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 1850, 201 );

	// GEEA2_HX11_EDR_List_210 : Internal Acceleration Sensor CyHighG;
	var Action = "Check " + Type + " Value: Internal Acceleration Sensor CyHighG";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2051, 201 );

	// GEEA2_HX11_EDR_List_211 : IMU X-Low G;
	var Action = "Check " + Type + " Value: IMU X-Low G";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2252, 51 );

	// GEEA2_HX11_EDR_List_212 : IMU Y-Low G;
	var Action = "Check " + Type + " Value: IMU Y-Low G";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2303, 51 );

	// GEEA2_HX11_EDR_List_213 : IMU Yaw rate;
	var Action = "Check " + Type + " Value: IMU Yaw rate";
	var ParameterValue = undefined;
	BB_Check_ParameterValue(Action, ParameterValue, DataRecord, 2354, 102 );

}


