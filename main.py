from ChromeWebDriver import ChromeWebDriver
from MainPage import MainPage
from Your_Sleep_Score_1_Page import Your_Sleep_Score_1_Page
from Your_Sleep_Score_2_Page import Your_Sleep_Score_2_Page
from Your_Sleep_Score_3_Page import Your_Sleep_Score_3_Page
from Your_Sleep_Score_4_Page import Your_Sleep_Score_4_Page
from Your_Sleep_Score_5_Page import Your_Sleep_Score_5_Page
from Your_Sleep_Score_6_Page import Your_Sleep_Score_6_Page
from Your_Sleep_Score_7_Page import Your_Sleep_Score_7_Page
from Your_Sleep_Score_8_Page import Your_Sleep_Score_8_Page
from Your_Sleep_Score_Age_Page import Your_Sleep_Score_Age_Page
from Your_Sleep_Score_Employment_Page import Your_Sleep_Score_Employment_Page
from Your_Sleep_Score_Productivity_Page import Your_Sleep_Score_Productivity_Page
from Your_Sleep_Score_Hours_Missed_Page import Your_Sleep_Score_Hours_Missed_Page
from Your_Sleep_Score_Expert_Guides_Page import Your_Sleep_Score_Expert_Guides_Page
from Your_Sleep_Score_Signup_Page import Your_Sleep_Score_Signup_Page
import random
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
page_6.select_option_by_index(4)
page_6.get_continue_button().click()
page_7 = Your_Sleep_Score_7_Page(driver)
page_7.select_option_by_index(2)
page_7.get_continue_button().click()
page_8 = Your_Sleep_Score_8_Page(driver)
page_8.select_entry(0)
page_8.get_continue_button().click()
page_age = Your_Sleep_Score_Age_Page(driver)
page_age.select_month(3)
page_age.select_day(5)
page_age.select_year(18)
page_age.get_continue_button().click()
page_employment = Your_Sleep_Score_Employment_Page(driver)
page_employment.select_option_by_index(1)
page_employment.get_continue_button().click()
page_productivity = Your_Sleep_Score_Productivity_Page(driver)
page_productivity.select_option_by_index(4)
page_productivity.get_continue_button().click()
hours_page = Your_Sleep_Score_Hours_Missed_Page(driver)
hours_page.get_hours_input().send_keys("10")
hours_page.get_continue_button().click()
guides_page = Your_Sleep_Score_Expert_Guides_Page(driver)
guides_page.select_entry(1)
guides_page.select_entry(2)
guides_page.select_entry(3)
guides_page.select_entry(1)
guides_page.get_continue_button().click()
signup_page = Your_Sleep_Score_Signup_Page(driver)
signup_page.get_first_name().send_keys("Matt")
signup_page.get_last_name().send_keys("Telles")
num = str(random.randint(100,500))
email_address = "fred" + num + "@george.com"
signup_page.get_email().send_keys(email_address)
signup_page.get_password().send_keys("Password1234")
signup_page.get_privacy_checkbox().click()
signup_page.get_acknowledge_checkbox().click()
signup_page.get_signup_button().click()
sleep(25)
txt = "Why this Sleep Score?"
assert txt in driver.get_page_source()
driver.shutdown()
