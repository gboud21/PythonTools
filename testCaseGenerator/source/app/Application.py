# External Imports
import sys
from os.path import abspath
from os.path import dirname
import json

# Internal Imports
from app import ApplicationTypes
from com.fio import fileIO
from com.lgg import logger


###################################################################################################################
### The controlling application that is responsible for loading the configuration file and executing the control 
### logic
class Application:
    ################################################################################################################
    ### Constructor 
    def __init__(self):
        # Public Member Variables
        self.logger = logger.Logger("testGenLogger")

        # Private Member Variables
        self._fileIO = fileIO.FileIO()
        self._inputScriptPath = ""
        self._outputPath = ""
        pass

    ################################################################################################################
    ### Initializes the application and all other components
    def initialize(self):
        # Initialize the Logging Service
        self.logger.initialize(abspath(dirname(sys.argv[0])) + abspath("/config/logConfigs/logConfig.json"))
        self.logger.logMessage("Initializing Test Generator")

        # Load the configuration file
        self.__loadConfiguration()

        # Call any other applications initialization logic

        self.logger.logMessage("Initialization Complete")

    ################################################################################################################
    ### This function runs the application. It reads in the Input Scripts, parses the scripts and then attempts
    ### to create test scripts in the specified formats
    def run(self):
        self.logger.logMessage("Running Test Generator")

        # Compile a list of all the test files in the input path

        # For each Output Format
        # Create a directory structure that mirrors the directory structure for the test files

        # Iterate through the list of test scripts generating a test file in the appropriate directory structure
        # for each of the output formats

if __name__ == '__main__':
    print("Requirements Manager Application Component")