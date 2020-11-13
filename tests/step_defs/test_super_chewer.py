from pytest_bdd import scenario, given, when, then, parsers, scenarios
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


@scenario('../features/super_chewer.feature', 'verify tax is displayed correctly')
def test_add():
    pass


@when("I choose a plan")
def choose_plan(super_chewer_page):
    super_chewer_page.click_choose_plan()


@when("I enter the dogs name")
def enter_name(super_chewer_page):
    time.sleep(3)
    super_chewer_page.select_male()
    super_chewer_page.enter_name()
    super_chewer_page.submit_dog_name()


@when("I select the size of the dog")
def select_size(super_chewer_page):
    time.sleep(2)
    super_chewer_page.select_medium_size()


@when("I enter the breed of the dog")
def enter_breed(super_chewer_page):
    time.sleep(1)
    super_chewer_page.select_breed()
    super_chewer_page.breed_submit_button()


@when("I enter the dog date of birth")
def enter_date_birth(super_chewer_page):
    time.sleep(1)
    super_chewer_page.select_date_of_birth()


@when("I select treats")
def select_treat(super_chewer_page):
    time.sleep(1)
    super_chewer_page.select_everything()


@when("I enter my email address")
def enter_email(super_chewer_page):
    time.sleep(1)
    super_chewer_page.fill_email_textfield()
    super_chewer_page.commit_email()


@when("I select type of subscription")
def select_subscription(super_chewer_page):
    time.sleep(1)
    super_chewer_page.select_one_month_subscription()


@when("I decline extra toy")
def decline_extra_toy(super_chewer_page):
    time.sleep(1)
    super_chewer_page.select_no_extra_toy()


@when("I select the theme")
def select_theme(super_chewer_page):
    time.sleep(1)
    super_chewer_page.select_top_rated_theme()


@then("I should be on the checkout page")
def checkout_page(browser):
    assert browser.current_url == "https://www.barkbox.com/subscribe/super-chewer/checkout"


@then("I should assert the tax is displayed correctly")
def assert_tax(browser):
    cost = browser.find_element(By.CSS_SELECTOR, ".desktop-display > #summary .hide-from-bright > .value > p").text
    tax = browser.find_element(By.CSS_SELECTOR, ".desktop-display > #summary .tax > .value > p").text
    expected_tax = re.sub(r"[^.0-9]+", '', tax)
    final_cost = float(re.sub(r"[^.0-9]+", '', cost))
    actual_tax = final_cost/8.875
    assert actual_tax == expected_tax


@when("I select super chewer")
def select_super_chewer(super_chewer_page):
    time.sleep(2)
    super_chewer_page.click_on_super_chewer_link()


@then("I  select credit card as means of payment")
def select_credit_card(super_chewer_page):
    time.sleep(2)
    super_chewer_page.click_on_credit_card_link()


@then("I fill shipping address form")
def shipping_address(super_chewer_page):
    super_chewer_page.fill_shopping_address()
