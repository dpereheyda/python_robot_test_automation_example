from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from page_objects.main_page_locators import MainPageLocators
from robot.utils import asserts
from settings import *


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    def __init__(self):
        self.driver = None
        self.actions = ActionChains(self.driver)
        self.portal_url = PORTAL_URL


class MainPageActions(BasePage):
    def __init__(self):
        super().__init__()
        self.elements = MainPageLocators()
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-web-security")
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--safebrowsing-disable-extension-blacklist")
        chrome_options.add_argument("--safebrowsing-disable-download-protection")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_portal(self):
        self.driver.get(self.portal_url)
        self.check_main_page_loaded()

    def check_main_page_loaded(self):
        element = self.elements.get_element(self, *MainPageLocators.logo)
        asserts.assert_true(element, f'Logo is not found')

    def select_tab(self, attribute_value):
        element = self.elements.get_element(self, *MainPageLocators.get_tab(attribute_value))
        element.click()

    def check_tab_is_selected(self, attribute_value):
        element = self.elements.get_element(self, *MainPageLocators.get_selected_tab(attribute_value))
        asserts.assert_true(element, f'Tab with "test-data" attribute {attribute_value} is not selected')