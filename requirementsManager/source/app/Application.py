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
        self.logger = logger.Logger("reqLogger")

        # Private Member Variables
        self._reqFileIO = fileIO.FileIO()
        self._configFilePath = abspath(dirname(sys.argv[0])) + abspath("/config/requirementsConfigs/0_initialConfiguration_Markdown.json")
        self._sssPath = ""
        self._srsPath = ""
        self._outputPath = ""
        self._requirementToken = ""
        self._sssDelimeter = ""
        self._srsFileType = ""
        pass

    ################################################################################################################
    ### Initializes the application and all other components
    def initialize(self):
        # Initialize the Logging Service
        self.logger.initialize(abspath(dirname(sys.argv[0])) + abspath("/config/logConfigs/logConfig.json"))
        self.logger.logMessage("Initializing Requirements Manager")

        # Load the configuration file
        self.__loadConfiguration()

        # Call any other applications initialization logic

        self.logger.logMessage("Initialization Complete")

    ################################################################################################################
    ### This function runs the application. It reads in the System Spec, parses the requirements and then attempts
    ### to update or create files for each derived requirement. Finally the application will generate a report
    ### of its execution before exiting.
    def run(self):
        self.logger.logMessage("Running Requirements Manager")

        # Load the SSS data
        sssData = self.reqFileIO.read(self._sssPath)

        # Based on what file type is selected, call the appropriate system

        self.logger.logMessage("Requirements Manager Complete")


    ################################################################################################################
    ### This functions loads the configuration file into the member variables of the application to be used when
    ### running.
    def __loadConfiguration(self):
        # Read the Configuration File
        try:
            with open(self.configFilePath, 'r') as configFile:
                configJsonData = json.load(configFile)
        except FileNotFoundError:
            # Catch and log exception for the file not being found
            self.logger.logError("Configuration File Not Found", logger.Severity.CRITICAL)

        # TODO: Add logic for optionally assigning SRS Path        
        # Assign path and parsing values to be used in the Running State
        self.__configureRequiredValues(configJsonData)


    ################################################################################################################
    ### This functions retrieves the values that are required to be set in the JSON
    def __configureRequiredValues(self, jsonData):
        return (self.__configureValue(ApplicationTypes.SSS_PATH_JSON_ID, self._sssPath, jsonData) and 
                self.__configureValue(ApplicationTypes.OUTPUT_PATH_JSON_ID, self._outputPath, jsonData) and 
                self.__configureValue(ApplicationTypes.REQUIREMENT_TOKEN_JSON_ID, self._requirementToken, jsonData) and 
                self.__configureValue(ApplicationTypes.SRS_FILE_TYPE_JSON_ID, self._srsFileType, jsonData))

    ################################################################################################################
    ### This functions retrieves the values that are required to be set in the JSON
    def __configureValue(self, key, valueToSet, jsonData):
        isValueConfigured = False

        if key in jsonData:
            valueToSet = jsonData[key]
            isValueConfigured = True
        else:
            self.logger.logError(f'Configuration value not set: {key}', logger.Severity.CRITICAL)

        return isValueConfigured



if __name__ == '__main__':
    print("Requirements Manager Application Component")