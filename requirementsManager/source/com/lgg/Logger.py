import json
import logging.config
import logging.handlers
import pathlib

class Logger:
    # Constructor
    def __init__(self, logName):
        self.name = logName
        self.logger = logging.getLogger(self.name)

    # Function to initialize the Logger's configuration
    def initialize(configFilePath):
        # Convert the string into a path
        configFile = pathlib.Path(configFilePath)

        # Open the specified configuration file and load it
        with open(configFile) as file:
            logConfig = json.load(file)

        # Use the JSON Log Configuration data to initialize the Logger
        logging.config.dictConfig(logConfig)
