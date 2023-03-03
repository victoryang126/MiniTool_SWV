from dataclasses import dataclass
from dataclasses import asdict,field
from typing import List,Any


# class AbstractField_Type:
#     CountryField = "CountryField"
#     DateField = "DateField"
#     ColorField = "ColorField"
#     MemberField = "ColorField"
#     DurationField = "DurationField"
#     DecimalField = "DecimalField"
#     BoolField = "BoolField"
#     IntegerField = "IntegerField"
#     LanguageField = "LanguageField"
#     ReviewMemberReferenceField = "ReviewMemberReferenceField"
#     ReferenceField = "ReferenceField"
#     TableField = "TableField"
#     TextField = "TextField"
#     UrlField = "UrlField"
#     WikiTextField = "WikiTextField"
#     OptionChoiceField = "OptionChoiceField"
#     RepositoryChoiceField = "RepositoryChoiceField"
#     ProjectChoiceField = "ProjectChoiceField"
#     TrackerChoiceField = "TrackerChoiceField"
#     TrackerItemChoiceField = "TrackerItemChoiceField"
#     UserChoiceField = "UserChoiceField"
#
# class AbstractReference_Type:
#     AttachmentReference = "AttachmentReference"
#     AssociationTypeReference = "AssociationTypeReference"
#     ChoiceOptionReference = "ChoiceOptionReference"
#     CommentReference = "CommentReference"
#     FieldReference = "FieldReference"
#     ProjectReference = "ProjectReference"
#     ReportReference = "ReportReference"
#     RepositoryReference = "RepositoryReference"
#     RoleReference = "RoleReference"
#     TrackerPermissionReference = "TrackerPermissionReference"
#     TrackerReference = "TrackerReference"
#     TrackerTypeReference = "TrackerTypeReference"
#     UserGroupReference = "UserGroupReference"
#     UserReference = "UserReference"
#     TrackerItemReference = "TrackerItemReference"
#
# class AbstractFieldValue_Type:
#     TableFieldValue = "TableFieldValue"
#     ChoiceFieldValue = "ChoiceFieldValue"
#     UrlFieldValue = "UrlFieldValue"
#     NotSupportedFieldValue = "NotSupportedFieldValue"
#     BoolFieldValue = "BoolFieldValue"
#     ColorFieldValue = "ColorFieldValue"
#     CountryFieldValue = "CountryFieldValue"
#     DateFieldValue = "DateFieldValue"
#     DecimalFieldValue = "DecimalFieldValue"
#     DurationFieldValue = "DurationFieldValue"
#     IntegerFieldValue = "IntegerFieldValue"
#     LanguageFieldValue = "LanguageFieldValue"
#     TextFieldValue = "TextFieldValue"
#     WikiTextFieldValue = "WikiTextFieldValue"
#     ReferredTestStepFieldValue = "ReferredTestStepFieldValue"
#
# class Value_Mapping:
#     descriptionFormat = "Wiki"
#     false = False
#     true = True
#     Testcase = "Testcase"
#     Testrun = "Testrun"

# class SuspectPropagation:
#     DO_NOT_PROPAGATE = "DO_NOT_PROPAGATE"
#     null = None
#     PROPAGATE = "PROPAGATE"
#     REVERSE = "REVERSE"

@dataclass
class AbstractFieldValue:
    fieldId :int
    name: str = None
    # type:str = None

@dataclass
class AbstractReference:
    id: int
    name: str = None
    type: str = None


@dataclass
class ChoiceFieldValue(AbstractFieldValue):
    values: List[Any] = field(default_factory=list)
    type: str = "ChoiceFieldValue"

@dataclass
class TableFieldValue(AbstractFieldValue):
    values: List[Any] = field(default_factory=list)
    type: str = "TableFieldValue"


@dataclass
class TextFieldValue(AbstractFieldValue):
    value: Any = None
    type: str = "TextFieldValue"

@dataclass
class BoolFieldValue(AbstractFieldValue):
    value: Any = None
    type: str = "BoolFieldValue"







@dataclass
class ReferenceData:
    suspectPropagation:str

@dataclass
class AbstractItemReference(AbstractReference):
    referenceData:ReferenceData = ReferenceData("DO_NOT_PROPAGATE")
    type: str = "TrackerItemReference"


@dataclass
class TrackerReference(AbstractReference):
    type: str = "TrackerReference"

@dataclass
class TrackerItemReference(AbstractReference):
    type: str = "TrackerItemReference"

@dataclass
class ChoiceOptionReference(AbstractReference):
    type:str = "ChoiceOptionReference"


def to_json(datacls:dataclass):
    return asdict(datacls)







