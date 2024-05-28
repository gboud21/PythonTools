#Internal Imports
from testCaseGenerator.source.com import testObjectType
from tst import testObject

FILE_NAME_ID = "file"
CLASS_NAME_ID = "className"
LINE_NUMBER_ID = "lineNumber"
FUNCTION_NAME_ID = "functionName"
OFFSET_ID = "offset"

#######################################################################################################################
### This class contains the data required to represent a Delete Command
class DeletetObject(testObject.TestObject):
    ###################################################################################################################
    ### Constructor
    def __init__(self, jsonData):
        self.__type = testObjectType.TestObjectType.DELETE

        # Need to figure out effecient way to build this object from the json data, but for now will brute force
        if FILE_NAME_ID in jsonData:
            self.__fileName = jsonData[FILE_NAME_ID]
        elif CLASS_NAME_ID in jsonData:
            self.__className = jsonData[CLASS_NAME_ID]
        elif LINE_NUMBER_ID in jsonData:
            self.__lineNumber = jsonData[LINE_NUMBER_ID]
        elif FUNCTION_NAME_ID in jsonData:
            self.__functionName = jsonData[FUNCTION_NAME_ID]
        elif OFFSET_ID in jsonData:
            self.__offset = jsonData[OFFSET_ID]