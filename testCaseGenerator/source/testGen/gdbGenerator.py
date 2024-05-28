# Internal Imports
from com.tst import testCase

#######################################################################################################################
### This class generates a test script in the GDB Output Format
class GdbGenerator:
    ###################################################################################################################
    ### Constructor
    def __init__(self):
        pass

    ###################################################################################################################
    ### Generates the script to execute each of the test cases using GDB
    def generateGDBTestCases(self, testCaseList):
        # Loop over the list of test cases generating each test case
        for test in testCaseList:
            self._generateTestCase(test)
        pass
    
    ###################################################################################################################
    ### Private method to generate an individual test case
    def _generateTestCase(self, test: testCase.TestCase):
        pass