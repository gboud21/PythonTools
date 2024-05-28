# External Imports
import os

# Internal Imports
from com.tst import testCase

#######################################################################################################################
### This class parses the test case inputs
class TestParser:
    ###################################################################################################################
    ### Constructor
    def __init__(self):
        pass
    
    def parseTestScripts(self, rootDirectory: str):
        # Generate an array of file paths for all files that end in "*.json" and are children of the rootDirectory
        # Return the array
        testCases = []
        suffix = ".json"
        for root, dirs, files in os.walk(rootDirectory):
            for file in files:
                if file.endswith(suffix):
                    full_path = os.path.join(root, file)

                    # Create the Test Case Object and parse the test procedure
                    test = testCase.TestCase(full_path)
                    test.generateTestObjects()
                    testCases.append(test)
        return testCases