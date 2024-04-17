# Internal Imports
from com.lgg import logger
import requirementsManager.source.sss.irequirementParser as irequirementParser
from com.fio import fileIO

###################################################################################################################
### The SytemReqParser class is responsible for identifying the requirement attributes contained in the data read
### in from a SSS and creating the System Requirement Objects
class SystemReqController():
    ###################################################################################################################
    ### Constructor
    def __init__(self, reqParser: irequirementParser.IRequirementParser):
        self.requirementParser = reqParser
    
    ###################################################################################################################
    ### This function parses the specified Systems Requirement Specification file and stores the data in the data structure
    def parseRequirements(self, sssPath: str):
        # Needs to read in the file, storing each line into a data structure
        fileReader = fileIO.FileIO()
        fileData = fileReader.read(sssPath)

        # After reading in all of the requirements, pass the line of data into the requirement parser interface
        sssReqArray = self.requirementParser.parseRequirement(fileData)