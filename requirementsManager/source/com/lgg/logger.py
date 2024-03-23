import json
import logging.config
import logging.handlers
import pathlib
from datetime import datetime
from enum import Enum
import traceback

###################################################################################################################
### Enumeration that indicates the severity of an error detected by the application
class Severity(Enum):
    NON_CRITICAL = 1
    CRITICAL = 2
    MAX_SEVERITY = 3

###################################################################################################################
### The Logger class abstracts the python logging functionality from the application
class Logger:
    ###################################################################################################################
    ### Constructor
    def __init__(self, logName):
        self.name = logName
        self.logger = logging.getLogger(self.name)
    
    ###################################################################################################################
    ### Function to initialize the Logger's configuration
    def initialize(self, configFilePath):
        # Convert the string into a path
        configFile = pathlib.Path(configFilePath)

        # Open the specified configuration file and load it
        with open(configFile) as file:
            logConfig = json.load(file)

        # Use the JSON Log Configuration data to initialize the Logger
        logging.config.dictConfig(config=logConfig)

    ###################################################################################################################
    ### Logs a debug message
    def logMessage(self, logText):
        self.logger.debug(logText)

    ###################################################################################################################
    ### Logs an Error Message
    def logError(self, logText, severity):
        # Based on the severity, log a message
        match severity:
            case Severity.NON_CRITICAL:
                self.logger.warning(self.__generateErrorMessage(logText,severity))
            case Severity.CRITICAL:
                self.logger.critical(self.__generateErrorMessage(logText,severity))
            case Severity.MAX_SEVERITY:
                self.logger.exception(self.__generateErrorMessage("Unknown Log Type"), Severity.CRITICAL)
            case _:
                self.logger.exception(self.__generateErrorMessage("Unknown Log Type", Severity.CRITICAL))

    ###################################################################################################################
    ### Private Function to format the log for an error
    def __generateErrorMessage(self, logText, severity):
        logSpacer = f"{'':=^80}"
        return f'{logSpacer}\n{severity}::{datetime.now()}: {logText}\n{traceback.format_stack()[-3:][0]}'