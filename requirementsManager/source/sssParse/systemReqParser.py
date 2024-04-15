# Internal Imports
from com.lgg import logger
import irequirementParser

###################################################################################################################
### The SytemReqParser class is responsible for identifying the requirement attributes contained in the data read
### in from a SSS and creating the System Requirement Objects
class SystemReqParser():
    ###################################################################################################################
    ### Constructor
    def __init__(self):
        pass
    
    ###################################################################################################################
    ### This function parses the specified Systems Requirement Specification file and stores the data in the data structure
    def parseRequirements(self, sssPath: str):
        # Needs to read in the file, storing each line into a data structure
        # After reading in all of the requirements, pass the line of data into the requirement parser interface
        pass