import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")

class BaseClass:
    # driver defined in conftest.py

    def verifyDropdownMenuPresence(self):
        dropdown = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='c-header-bar-nav__small-menu js-header-small-menu open']/ul/li")), "Dropdown menu was not displayed after 3 seconds")

    def verifyDropdownMenuPresenceMobile(self):
        dropdown_mobile = WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='c-frontpagemobilenav__dropdown js-subnav-item toggled']/div/ul/li")), "Dropdown menu was not displayed after 3 seconds")

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        if (logger.hasHandlers()): # clear double logs
            logger.handlers.clear()
        logger.addHandler(fileHandler)  # fileHandler object (file location)
        logger.setLevel(logging.DEBUG) # INFO, DEBUG, ERROR, CRITICAL
        return logger
