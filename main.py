from ChromeWebDriver import ChromeWebDriver
from MainPage import MainPage
from Your_Sleep_Score_1_Page import Your_Sleep_Score_1_Page
from Your_Sleep_Score_2_Page import Your_Sleep_Score_2_Page
from Your_Sleep_Score_3_Page import Your_Sleep_Score_3_Page
from Your_Sleep_Score_4_Page import Your_Sleep_Score_4_Page
from Your_Sleep_Score_5_Page import Your_Sleep_Score_5_Page
from Your_Sleep_Score_6_Page import Your_Sleep_Score_6_Page
from time import sleep

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
page_2 = Your_Sleep_Score_2_Page(driver)
page_2.select_option_by_index(1)
page_2.get_continue_button().click()
page_3 = Your_Sleep_Score_3_Page(driver)
page_3.select_entry(2)
page_3.get_continue_button().click()
page_4 = Your_Sleep_Score_4_Page(driver)
page_4.select_option_by_index(2)
page_4.get_continue_button().click()
page_5 = Your_Sleep_Score_5_Page(driver)
page_5.select_option_by_index(4)
page_5.get_continue_button().click()

page_6 = Your_Sleep_Score_6_Page(driver)
labels = page_6.get_labels()
page_6.select_option_by_index(4)
page_6.get_continue_button().click()

sleep(5)
driver.shutdown()
