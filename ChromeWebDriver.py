from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from os import getcwd
from selenium.webdriver.support import expected_conditions as EC


class ChromeWebDriver:

    def __init__(self):
        self.driver = None
        pass

    def open_window(self):
        if not self.driver:
            current_directory = getcwd()
            driver_name = current_directory + "\\" + "chromedriver.exe"
            self.driver = webdriver.Chrome(driver_name)
        return self

    def maximize(self):
        self.open_window()
        self.driver.maximize_window()
        return self

    def shutdown(self):
        if self.driver:
            self.driver.close()

    def fetch_page(self, page):
        self.open_window()
        if self.driver:
            self.driver.get(page)

    def get_element(self, selector):
        ele = self.driver.find_element(By.CSS_SELECTOR, selector)
        return ele

    def get_elements_by_tag(self, tag_name):
        elements = self.driver.find_elements_by_tag_name(tag_name)
        return elements

    def get_element_by_xpath(self, xpath):
        element = self.driver.find_element(By.XPATH, xpath)
        return element

    def get_elements_by_xpath(self, xpath):
        elements = self.driver.find_elements(By.XPATH, xpath)
        return elements
