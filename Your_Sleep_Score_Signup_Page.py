
class Your_Sleep_Score_Signup_Page:

    def __init__(self, driver):
        self.driver = driver
        self.login_selector = '#sl-flow > header > div > a.sl-header__login'
        self.email_button_selector = '#transparent-button'
        self.home_logo_link_selector = '#sl-flow > header > div > a.sl-header__logo > img'
        self.first_name_input_xpath = '//*[@id="23781"]'
        self.last_name_input_xpath = '//*[@id="23782"]'
        self.email_input_xpath = '//*[@id="23785"]'
        self.password_input_xpath = '//*[@id="23787"]'
        self.privacy_policy_checkbox = '#sl-flow > div.sl-content > div > div > div > div > form > div:nth-child(5) > input'
        self.acknowledge_checkbox = '#sl-flow > div.sl-content > div > div > div > div > form > div:nth-child(6) > input'
        self.signup_button_selector = '#sl-flow > div.sl-content > div > div > div > div > form > div.sl-button-wrapper > button'


    def login_button(self):
        ele = self.driver.get_element(self.login_selector)
        return ele

    def get_email_button(self):
        ele = self.driver.get_element(self.email_button_selector)
        return ele

    def get_logo_button(self):
        ele = self.driver.get_element(self.home_logo_link_selector)
        return ele

    def get_signup_button(self):
        ele = self.driver.get_element(self.signup_button_selector)
        return ele

    def get_first_name(self):
        ele = self.driver.get_element_by_xpath(self.first_name_input_xpath)
        return ele

    def get_last_name(self):
        ele = self.driver.get_element_by_xpath(self.last_name_input_xpath)
        return ele

    def get_email(self):
        ele = self.driver.get_element_by_xpath(self.email_input_xpath)
        return ele

    def get_password(self):
        ele = self.driver.get_element_by_xpath(self.password_input_xpath)
        return ele

    def get_privacy_checkbox(self):
        ele = self.driver.get_element(self.privacy_policy_checkbox)
        return ele

    def get_acknowledge_checkbox(self):
        ele = self.driver.get_element(self.acknowledge_checkbox)
        return ele