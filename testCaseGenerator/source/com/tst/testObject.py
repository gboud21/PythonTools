#Internal Imports
from testCaseGenerator.source.com import testObjectType

#######################################################################################################################
### This class parses the test case inputs
class TestObject:
    ###################################################################################################################
    ### Constructor
    def __init__(self, objectType: testObjectType.TestObjectType):
        self.__type = objectType