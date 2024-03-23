# External Imports
import sys
from os.path import abspath
from os.path import dirname

# Internal Imports
from com.lgg import logger

if __name__ == '__main__':
    lgg = logger.Logger("reqLogger")
    lgg.initialize(abspath(dirname(sys.argv[0])) + abspath("/config/logConfig.json"))
    lgg.logMessage("Starting Requirements Manager")
    lgg.logError("Test Error", logger.Severity.NON_CRITICAL)