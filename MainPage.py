
class MainPage:
    def __init__(self, drv):
        self.button_selector = '#sl-flow > div.sl-content > div > div > div > div > div > button'
        self.login_selector = '#sl-flow > header > div > a.sl-header__login'
        self.email_button_selector = '#transparent-button'
        self.driver = drv

    def get_started_button(self):
        ele = self.driver.get_element(self.button_selector)
        return ele

    def login_button(self):
        ele = self.driver.get_element(self.login_selector)
        return ele

    def get_email_button(self):
        ele = self.driver.get_element(self.email_button_selector)
        return ele
