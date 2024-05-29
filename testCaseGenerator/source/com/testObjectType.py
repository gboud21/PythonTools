from enum import Enum, auto

# Operation Type Constants
OPERATION_TYPE_ID = "operationType"
BREAKPOINT_ID = "breakpoint"
DELETE_ID = "delete"

# Parameter Constants
FILE_NAME_ID = "file"
CLASS_NAME_ID = "className"
LINE_NUMBER_ID = "lineNumber"
FUNCTION_NAME_ID = "functionName"
OFFSET_ID = "offset"

class TestObjectType(Enum):
  BACKTRACE = auto()
  BREAKPOINT = auto()
  DELETE = auto()
  KILL = auto()
  WATCHPOINT = auto()