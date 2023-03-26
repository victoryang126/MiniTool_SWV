from typing import List,Any
import xml.etree.ElementTree as ET
def make_xpath(location: List[str]) -> str:
    """Convenience function to traverse the XML element tree more easily

    (This function is only used by the EcuExtractLoader.)"""
    return './ns:' + '/ns:'.join(location)


# The ARXML XML namespace for the EcuExtractLoader
NAMESPACE = 'http://autosar.org/schema/r4.0'
NAMESPACES = {'ns': NAMESPACE}

ECUC_VALUE_COLLECTION_XPATH = make_xpath([
    'AR-PACKAGES',
    'AR-PACKAGE'
    'ECU-INSTANCE'
    # 'ELEMENTS',
    # 'ECUC-VALUE-COLLECTION'
])
ECUC_MODULE_CONFIGURATION_VALUES_REF_XPATH = make_xpath([
    'ECUC-VALUES',
    'ECUC-MODULE-CONFIGURATION-VALUES-REF-CONDITIONAL',
    'ECUC-MODULE-CONFIGURATION-VALUES-REF'
])
ECUC_REFERENCE_VALUE_XPATH = make_xpath([
    'REFERENCE-VALUES',
    'ECUC-REFERENCE-VALUE'
])
DEFINITION_REF_XPATH = make_xpath(['DEFINITION-REF'])
VALUE_XPATH = make_xpath(['VALUE'])
VALUE_REF_XPATH = make_xpath(['VALUE-REF'])
SHORT_NAME_XPATH = make_xpath(['SHORT-NAME'])
PARAMETER_VALUES_XPATH = make_xpath(['PARAMETER-VALUES'])
REFERENCE_VALUES_XPATH = make_xpath([
    'REFERENCE-VALUES'
])
file = r"C:\Project\SAIC_ZP22\ARiA_Configuration\P10_02\20220930_gx2_ZP22 HEV_EP2_SDM-V01.arxml"
tree = ET.parse(file)
root = tree.getroot()
# ecuc_value_collection = root.find(ECUC_VALUE_COLLECTION_XPATH,
#                                        NAMESPACES)
print(root.tag)
class EcuExtractLoader(object):

    def __init__(self,db):
        self.db = db
