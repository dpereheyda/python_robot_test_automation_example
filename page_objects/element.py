from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import logging


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj):
        """Gets the text of the specified object"""
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")

    def get_element(self, obj, criteria, value, with_bug=False, timeout_delay=5, wait=5):
        driver = obj.driver
        wait = WebDriverWait(driver, wait)
        timeout = timeout_delay  # [seconds]
        timeout_start = time.time()
        while time.time() < timeout_start + timeout:
            try:
                element = wait.until(ec.visibility_of_element_located((criteria, value)))
                if element.is_displayed():
                    logging.info('Element has been found: ' + str(value))
                    return element
            except Exception as e:
                logging.info(f'Another exception - {e}')
                pass
        if not with_bug:
            logging.info('No element found: ' + value)