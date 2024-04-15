###################################################################################################################
## JSON Configuration IDs
SSS_PATH_JSON_ID = "SystemSpecPath"
SRS_PATH_JSON_ID = "SoftwareSpecPath"
OUTPUT_PATH_JSON_ID = "OutputPath"
REQUIREMENT_TOKEN_JSON_ID = "RequirementToken"
SSS_DELIMETER_JSON_ID = "SystemSpecDelimeter"
SRS_FILE_TYPE_JSON_ID = "SoftwareSpecFileType"

###################################################################################################################
### Enumeration that indicates the type of file to parse data from and to output data to
class FileType(Enum):
    MD = 1
    HTML = 2
    MAX_FILE_TYPE = 3
