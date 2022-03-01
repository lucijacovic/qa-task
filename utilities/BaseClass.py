import inspect
import logging
import pytest


@pytest.mark.usefixtures("setup")

class BaseClass:
    # driver defined in conftest.py

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        if (logger.hasHandlers()): # clear double logs
            logger.handlers.clear()
        logger.addHandler(fileHandler)  # fileHandler object (file location)
        logger.setLevel(logging.DEBUG)
        return logger
