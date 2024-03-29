# Internal Imports
from com.lgg import logger
import markdownParser

###################################################################################################################
### The Logger class abstracts the python logging functionality from the application
class SystemReqParser:
    ###################################################################################################################
    ### Constructor
    def __init__(self):
        pass
    
    ###################################################################################################################
    ### This function parses the specified Systems Requirement Specification file and stores the data in the data structure
    def parseRequirements(self, systemSpecPath):
        # Needs to read in the file, storing each line into a data structure
        # After reading in all of the requirements, pass the line of data into the requirement parser interface
        pass