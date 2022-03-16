from selenium.webdriver.support.ui import Select


class Your_Sleep_Score_4_Page:

    def __init__(self, driver):
        self.driver = driver
        self.options = []
        self.labels = []
        self.continue_button_selector = '#sl-flow > div.sl-content > div > div > div.sl-button-wrapper > button'
        self.login_selector = '#sl-flow > header > div > a.sl-header__login'
        self.email_button_selector = '#transparent-button'
        self.home_logo_link_selector = '#sl-flow > header > div > a.sl-header__logo > img'
        self.how_long_selector = '#id-17'

    def load_options(self):
        select = Select(self.driver.get_element(self.how_long_selector))
        all_options = [o.get_attribute('value') for o in select.options]
        all_text = [o.text for o in select.options]
        for option in all_options:
            self.options.append(option)
        for text in all_text:
            self.labels.append(text)
        return self

    def get_options(self):
        self.load_options()
        return self.options

    def get_labels(self):
        self.load_options()
        return self.labels

    def login_button(self):
        ele = self.driver.get_element(self.login_selector)
        return ele

    def get_email_button(self):
        ele = self.driver.get_element(self.email_button_selector)
        return ele

    def get_logo_button(self):
        ele = self.driver.get_element(self.home_logo_link_selector)
        return ele

    def select_option_by_index(self, index):
        select = Select(self.driver.get_element(self.how_long_selector))
        select.select_by_index(index)
        return self

    def get_continue_button(self):
        ele = self.driver.get_element(self.continue_button_selector)
        return ele
