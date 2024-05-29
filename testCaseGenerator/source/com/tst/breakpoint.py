#Internal Imports
from testCaseGenerator.source.com import testObjectType
from testCaseGenerator.source.com.tst import itestObject

# File and Line Number Operation ID
BREAKPOINT_FL_ID = "breakpoint_file_line"

# Class, Function and Offset Operation ID
BREAKPOINT_CFO_ID = "breakpoint_class_function_offset"

# File and Function Operation ID
BREAKPOINT_FF_ID = "breakpoint_file_function"

#######################################################################################################################
### This class contains the data required to represent a Breakpoint 1 Command
class BreakpointObject(itestObject.ITestObject):
    ###################################################################################################################
    ### Constructor
    def __init__(self, jsonData):
        if BREAKPOINT_FL_ID in jsonData:
            self._initFileLineNumber(jsonData)
        elif BREAKPOINT_CFO_ID in jsonData:
            self._initClassFunctionOffset(jsonData)
        elif BREAKPOINT_FF_ID in jsonData:
            self._initFileFunction(jsonData)

    ###################################################################################################################
    ### Initializes a Breakpoint Object that has a File and Line Number
    def _initFileLineNumber(self, jsonData):
        # Assign the type of breakpoint
        self.__type = BREAKPOINT_FL_ID
        
        # Extract the values for this object from the JSON data
        if testObjectType.FILE_NAME_ID in jsonData:
            self.__fileName = jsonData[testObjectType.FILE_NAME_ID]

        if testObjectType.LINE_NUMBER_ID in jsonData:
            self.__lineNumber = jsonData[testObjectType.LINE_NUMBER_ID]

    ###################################################################################################################
    ### Initializes a Breakpoint Object that has a Class, Function and Offset
    def _initClassFunctionOffset(self, jsonData):
        # Assign the type of breakpoint
        self.__type = BREAKPOINT_CFO_ID
        
        # Extract the values for this object from the JSON data
        if testObjectType.CLASS_NAME_ID in jsonData:
            self.__className = jsonData[testObjectType.CLASS_NAME_ID]

        if testObjectType.FUNCTION_NAME_ID in jsonData:
            self.__functionName = jsonData[testObjectType.FUNCTION_NAME_ID]

        if testObjectType.OFFSET_ID in jsonData:
            self.__offset = jsonData[testObjectType.OFFSET_ID]

    ###################################################################################################################
    ### Initializes a Breakpoint Object that has a File and Function
    def _initFileFunction(self, jsonData):
        # Assign the type of breakpoint
        self.__type = BREAKPOINT_FF_ID
        
        # Extract the values for this object from the JSON data
        if testObjectType.CLASS_NAME_ID in jsonData:
            self.__fileName = jsonData[testObjectType.CLASS_NAME_ID]

        if testObjectType.FUNCTION_NAME_ID in jsonData:
            self.__functionName = jsonData[testObjectType.FUNCTION_NAME_ID]