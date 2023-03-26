"""
第二行：根元素，每个文档有且只有一个根元素，元素由开始标签、元素内容、结束标签组成，没有被其它元素包围的元素称为根元素。属性：xmls: 引用Schema的约束，xmlns:xsi：声明当前的XML文件是schema一个实例，xsi:schemaLocation：引用schema的位置；

<AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 autosar_4-2-2.xsd">

. . .

</AUTOSAR >

第三行：顶级包，此元素是添加到文件中的所有AUTOSAR元素的容器。

<AR-PACKAGES>

. . .

</AR-PACKAGES>

第四行：AUTOSAR包，包是AUTOSAR的主要组件，它包含彼此相关的AUTOSAR元素，如软件组件、行为和受支持的数据类型。它由一个名称和称为UUID的全局唯一标识符定义。它也可能包含子包。

<AR-PACKAGE UUID="8348d5fa-cd36-5935-e72f-9ac3852cc24f">

<SHORT-NAME>Package Name </SHORT-NAME>

<SUB-PACKAGES> . . . </SUB-PACKAGES>

<ELEMENTS> . . . </ELEMENTS>

</AR-PACKAGE>

文档中重要的AR-PACKAGE释义：

AR-PACKAGE：ECUSystem (Get ECUs)

AR-PACKAGE：ECUExtractVCU (Project description??)

AR-PACKAGE：VehicleTopology (Get Clusters)

AR-PACKAGE：Communication (Get Frames, PDUs and Signals)

AR-PACKAGE：Signal (Dynamic length attributes)

AR-PACKAGE：DataType (Signal Compu-method description)

AR-PACKAGE：SignalGroup (Signal groups description)

AR-PACKAGE：ComponentType (Components (prototypes)??)

AR-PACKAGE：Interface (ECU published signals)

3.2 ARXML中对应CANFD信号关键信息的路径

Channel (信号网段)：
CAN-CLUSTER -- SHORT-NAME

Frame ID:
CAN-CLUSTER -- PHYSICAL-CHANNELS -- PHYSICAL-CHANNEL -- CAN-FRAME-TRIGGERING – IDENTIFIER

Frame Name:
CAN-FRAME -- SHORT-NAME

备注：确定Frame Name路径的reference：CAN-CLUSTER -- PHYSICAL-CHANNELS -- PHYSICAL-CHANNEL -- CAN-FRAME-TRIGGERING -- FRAME-REF

Frame Length:
CAN-FRAME -- FRAME-LENGTH

PDU ID (Short ID):
I-SIGNAL-I-PDU -- CONTAINED-I-PDU-PROPS -- HEADER-ID-SHORT-HEADER

备注：确定PDU ID路径的reference：CAN-FRAME -- PDU-REF

PDU NAME:
NM-PDU -- SHORT-NAME 或 I-SIGNAL-I-PDU -- SHORT-NAME

PDU Length:
I-SIGNAL-I-PDU -- LENGTH

Signal Name:
SYSTEM-SIGNAL – SHORT-NAME

备注：确定Signal Name路径的reference：I-SIGNAL-TO-I-PDU-MAPPING -- I-SIGNAL-REF // I-SIGNAL -- SYSTEM-SIGNAL-REF

Signal Description:
SYSTEM-SIGNAL -- L-2

Start Bit:
I-SIGNAL-TO-I-PDU-MAPPING -- START-POSITION

Signal Length:
I-SIGNAL -- LENGTH

Signal Cycle Time:
I-SIGNAL-I-PDU -- I-PDU-TIMING-SPECIFICATIONS -- CYCLIC-TIMING -- TIME-PERIOD -- VALUE 或

I-SIGNAL-I-PDU -- I-PDU-TIMING-SPECIFICATIONS -- CYCLIC-TIMING -- TIME-OFFSET -- VALUE

备注：需要通过计算获得所需结果

Date Type:
SW- BASE-TYPE -- BASE-TYPE-ENCODING

备注：确定Date Type路径的reference： I-SIGNAL -- SW-DATA-DEF-PROPS -- BASE-TYPE-REF

Conversion:
COMPU-METHOD -- COMPU-INTERNAL-TO-PHYS -- COMPU-SCALES -- COMPU-SCALE -- COMPU-CONST – VT 或

COMPU-METHOD -- COMPU-INTERNAL-TO-PHYS -- COMPU-SCALES -- COMPU-SCALE -- COMPU-RATIONAL-COEFFS -- COMPU-NUMERATOR//COMPU-DENOMINATOR -- V

Range:
COMPU-METHOD -- COMPU-INTERNAL-TO-PHYS -- COMPU-SCALES -- COMPU-SCALE -- LOWER-LIMIT 或

COMPU-METHOD -- COMPU-INTERNAL-TO-PHYS -- COMPU-SCALES -- COMPU-SCALE -- UPPER-LIMIT

备注：确定LOWER-LIMIT和UPPER-LIMIT路径的reference： I-SIGNAL -- COMPU-METHOD-REF

Signal Value Description:
COMPU-METHOD -- COMPU-INTERNAL-TO-PHYS -- COMPU-SCALES -- COMPU-SCALE -- COMPU-CONST – VT 或

COMPU-METHOD -- COMPU-INTERNAL-TO-PHYS -- COMPU-SCALES -- COMPU-SCALE -- COMPU-RATIONAL-COEFFS -- COMPU-NUMERATOR//COMPU-DENOMINATOR -- V

备注：14、15、16强相关，需要通过一些计算提取所需结果

Initial Value:
I-SIGNAL -- INIT-VALUE -- NUMERICAL-VALUE-SPECIFICATION -- VALUE
————————————————
"""