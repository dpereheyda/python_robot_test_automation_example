from selenium.webdriver.common.by import By
from page_objects.element import BasePageElement


class MainPageLocators(BasePageElement):
    """A class for main page locators. All main page locators should come here"""

    logo = (By.CSS_SELECTOR, f'img[autotest-attr-logo]')
    admin_button = (By.CSS_SELECTOR, 'div[autotest-attr="menu-admin"]')
    page_title = (By.CSS_SELECTOR, f'h1[autotest-attr-title]')

    @staticmethod
    def get_tab(attribute_value):
        tab = (By.CSS_SELECTOR, f'button[autotest-attr="{attribute_value}"]')
        return tab

    @staticmethod
    def get_selected_tab(attribute_value):
        selected_tab = (By.CSS_SELECTOR, f'button[autotest-attr="{attribute_value}"][aria-selected="true"]')
        return selected_tab

