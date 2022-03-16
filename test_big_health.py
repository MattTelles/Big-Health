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

# Test 1: Check main page for all elements.
def test_page_one_happy_path():
    txt = "Discover your Sleep Score\nand how to improve it"
    # Get the initial page
    driver = ChromeWebDriver()
    driver.maximize()
    driver.fetch_page('https://onboarding.sleepio.com/sleepio/big-health')
    main_page = MainPage(driver)
    page_source = driver.get_page_source()
    assert txt in page_source
    assert "© 2022 Big Health" in page_source
    assert "Version" in page_source
    assert main_page.login_button()
    assert main_page.get_started_button()
    assert main_page.get_email_button()
    driver.shutdown()

# Test 2: Click to second page, validate
def test_getting_started():
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
    page_source = driver.get_page_source()
    assert "© 2022 Big Health" in page_source
    assert "Version" in page_source
    assert page_1.login_button()
    assert page_1.get_email_button()
    assert page_1.get_logo_button()
    driver.shutdown()

# Test 3: Enable the continue button
def test_getting_started_continue_enabled():
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
    chkboxes[0].click()
    assert page_1.is_continue_button_enabled()
    driver.shutdown()

# Test 4: Disable the continue button by clicking twice.
def test_getting_started_continue_disabled():
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
    chkboxes[0].click()
    chkboxes[0].click()
    assert not page_1.is_continue_button_enabled()
    driver.shutdown()

# Test 5: Clicking none of the above turns off others.
def test_getting_started_none_of_the_above():
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
    for i in range(0,3):
        chkboxes[i].click()
    chkboxes[4].click()
    assert not chkboxes[0].is_selected()
    driver.shutdown()

# Test 6: Clicking anything turns off none of the above
def test_getting_started_none_of_the_above_off():
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
    for i in range(0,3):
        chkboxes[i].click()
    chkboxes[4].click()
    chkboxes[1].click()
    assert not chkboxes[4].is_selected()
    driver.shutdown()

# Test 7: Test second screen
def test_second_screen():
    driver = ChromeWebDriver()
    driver.maximize()
    driver.fetch_page('https://onboarding.sleepio.com/sleepio/big-health')
    main_page = MainPage(driver)
    start_btn = main_page.get_started_button()
    start_btn.click()
    page_1 = Your_Sleep_Score_1_Page(driver)
    page_1.get_checkbox(0).click()
    page_1.get_continue_button().click()
    page_2 = Your_Sleep_Score_2_Page(driver)
    txt = "How long have you had a problem with your sleep?"
    assert txt in driver.get_page_source()
    driver.shutdown()

# Test 8: Test second screen, enable continue
def test_second_screen_enable_continue_button():
    driver = ChromeWebDriver()
    driver.maximize()
    driver.fetch_page('https://onboarding.sleepio.com/sleepio/big-health')
    main_page = MainPage(driver)
    start_btn = main_page.get_started_button()
    start_btn.click()
    page_1 = Your_Sleep_Score_1_Page(driver)
    page_1.get_checkbox(0).click()
    page_1.get_continue_button().click()
    page_2 = Your_Sleep_Score_2_Page(driver)
    page_2.select_option_by_index(1)
    assert page_2.get_continue_button().is_enabled
    driver.shutdown()

# Test 9: Verify full process
def test_full_signon():
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
    num = str(random.randint(100, 500))
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