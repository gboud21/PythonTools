# External Imports
import json

# Internal Imports
from testCaseGenerator.source.com import testObjectType
from testCaseGenerator.source.com.tst import itestObject
from tst import breakpoint
from tst import delete

#######################################################################################################################
### This class parses the test case inputs
class TestCase:
    ###################################################################################################################
    ### Constructor
    def __init__(self, filePath: str):
        self.__filePath = filePath
        self.__testSteps = []

    def generateTestObjects(self):
        # Read in the data from the JSON File
        with open(self.__filePath, "r") as file:
            jsonData = json.load(file)

        # Iterate over the JSON Data adding each Test Object
        for index in jsonData:
            # If the Operation Type is identified then try to parse the object
            if testObjectType.OPERATION_TYPE_ID in jsonData[index]:
                if(jsonData[index][testObjectType.OPERATION_TYPE_ID][:testObjectType.BREAKPOINT_ID.__len__()] == testObjectType.BREAKPOINT_ID):
                    self.__testSteps.append(breakpoint.BreakpointObject(jsonData[index]))
                elif(jsonData[index][testObjectType.OPERATION_TYPE_ID][:testObjectType.DELETE_ID.__len__()]  == testObjectType.DELETE_ID):
                    self.__testSteps.append(delete.DeletetObject(jsonData[index]))
            # Otherwise generate an error
            else:
                print("Error")

        # Return the Test Procedure
        return self.__testSteps

    def getTestSteps(self):
        return self.__testSteps

    def getTestStep(self, stepNumber: int):
        return self.__testSteps[stepNumber]