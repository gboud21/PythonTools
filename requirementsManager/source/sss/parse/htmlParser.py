# External Imports
from array import array

# Internal Imports
import requirementsManager.source.sss.irequirementParser as irequirementParser
from com.lgg import logger

###################################################################################################################
### The Logger class abstracts the python logging functionality from the application
class HTMLParser:
    ###################################################################################################################
    ### Constructor
    def __init__(self):
        pass
    
    ###################################################################################################################
    ### This function parses the specified Systems Requirement Specification file and stores the data in the data structure
    def parseRequirements(self, sssData) -> array:
        pass
