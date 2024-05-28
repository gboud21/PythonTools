from enum import Enum

# Operation Type Constants
OPERATION_TYPE_ID = "operationType"
BREAKPOINT_ID = "breakpoint"
DELETE_ID = "delete"

class TestObjectType(Enum):
  BACKTRACE = 1
  BREAKPOINT = 2
  DELETE = 3
  KILL = 4
  WATCHPOINT = 5