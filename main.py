from ChromeWebDriver import ChromeWebDriver
from MainPage import MainPage
from Your_Sleep_Score_1_Page import Your_Sleep_Score_1_Page
from time import sleep
from selenium.webdriver.support.ui import Select

driver = ChromeWebDriver()
driver.maximize()
driver.fetch_page('https://onboarding.sleepio.com/sleepio/big-health')
main_page = MainPage(driver)
start_btn = main_page.get_started_button()
assert start_btn
login_btn = main_page.login_button()
assert login_btn
start_btn.click()
page_1 = Your_Sleep_Score_1_Page(driver)
chkboxes = page_1.get_checkboxes()
assert len(chkboxes) == 5
page_1.get_checkbox(0).click()
page_1.get_continue_button().click()
sleep(5)
how_long_selector = '#id-7'
how_long_list_selector = '#id-12'
select = Select(driver.get_element(how_long_selector))

all_options = [o.get_attribute('value') for o in select.options]
all_text = [o.text for o in select.options]
for option in all_options:
    print(option)
for text in all_text:
    print(text)
driver.shutdown()
