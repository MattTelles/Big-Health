from selenium.webdriver.support.ui import Select


class Your_Sleep_Score_Age_Page:

    def __init__(self, driver):
        self.driver = driver
        self.options = []
        self.labels = []
        self.continue_button_selector = '#sl-flow > div.sl-content > div > div > div.sl-button-wrapper > button'
        self.login_selector = '#sl-flow > header > div > a.sl-header__login'
        self.email_button_selector = '#transparent-button'
        self.month_selector = "#select-month"
        self.day_selector = "#select-day"
        self.year_selector = "#select-year"

    def login_button(self):
        ele = self.driver.get_element(self.login_selector)
        return ele

    def get_email_button(self):
        ele = self.driver.get_element(self.email_button_selector)
        return ele

    def get_logo_button(self):
        ele = self.driver.get_element(self.home_logo_link_selector)
        return ele

    def get_continue_button(self):
        ele = self.driver.get_element(self.continue_button_selector)
        return ele

    def select_month(self, index):
        select = Select(self.driver.get_element(self.month_selector))
        select.select_by_index(index)
        return self

    def select_day(self, index):
        select = Select(self.driver.get_element(self.day_selector))
        select.select_by_index(index)
        return self

    def select_year(self, index):
        select = Select(self.driver.get_element(self.year_selector))
        select.select_by_index(index)
        return self

    def get_selected_year_text(self):
        select = Select(self.driver.get_element(self.year_selector))
        selected_option = select.first_selected_option
        return selected_option.text

    def get_selected_month_text(self):
        select = Select(self.driver.get_element(self.month_selector))
        selected_option = select.first_selected_option
        return selected_option.text

    def get_selected_day_text(self):
        select = Select(self.driver.get_element(self.day_selector))
        selected_option = select.first_selected_option
        return selected_option.text
