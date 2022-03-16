
class Your_Sleep_Score_Hours_Missed_Page:

    def __init__(self, driver):
        self.driver = driver
        self.login_selector = '#sl-flow > header > div > a.sl-header__login'
        self.email_button_selector = '#transparent-button'
        self.home_logo_link_selector = '#sl-flow > header > div > a.sl-header__logo > img'
        self.hours_input_selector = '#id-58'
        self.continue_button_selector = "#sl-flow > div.sl-content > div > div > div.sl-button-wrapper > button"

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

    def get_hours_input(self):
        ele = self.driver.get_element(self.hours_input_selector)
        return ele
