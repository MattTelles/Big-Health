class Your_Sleep_Score_3_Page:

    def __init__(self, driver):
        self.driver = driver
        self.checkboxes = []
        self.labels = []
        self.continue_button_selector = '#sl-flow > div.sl-content > div > div > div.sl-button-wrapper > button'
        self.login_selector = '#sl-flow > header > div > a.sl-header__login'
        self.email_button_selector = '#transparent-button'
        self.home_logo_link_selector = '#sl-flow > header > div > a.sl-header__logo > img'

    def load_checkboxes(self):
        check_boxes = self.driver.get_elements_by_tag('input')
        for check_box in check_boxes:
            cid = check_box.get_attribute('id')
            xpath = '//*[@for="{}"]'.format(cid)
            label = self.driver.get_element_by_xpath(xpath)
            self.labels.append(label.text)
            self.checkboxes.append(check_box)
        return self

    def get_checkboxes(self):
        self.load_checkboxes()
        return self.checkboxes

    def get_labels(self):
        self.load_checkboxes()
        return self.labels

    def get_checkbox(self, index):
        return self.checkboxes[index]

    def get_continue_button(self):
        ele = self.driver.get_element(self.continue_button_selector)
        return ele

    def login_button(self):
        ele = self.driver.get_element(self.login_selector)
        return ele

    def get_email_button(self):
        ele = self.driver.get_element(self.email_button_selector)
        return ele

    def get_logo_button(self):
        ele = self.driver.get_element(self.home_logo_link_selector)
        return ele

    def select_entry(self, index):
        self.load_checkboxes()
        self.checkboxes[index].click()
        return self