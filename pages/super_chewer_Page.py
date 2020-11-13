import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


class SuperChewerPage:
    # The part is not full implemented. In an idea framework i would define the element and use the variables in the
    # methods.

    CHOOSE_PLAN_BUTTON = (By.CSS_SELECTOR, ".pull-right:nth-child(2) > .button"),
    MALE_RADIO_BUTTON = (By.ID, "male"),
    DOG_NAME_ID = (By.ID, "subscription_dog_name_dog_name"),
    DOG_NAME_SUBMIT_BUTTON = (By.ID, "dog-name-submit"),
    Medium_size_CSS = (By.CSS_SELECTOR, ".medium .emphasize"),
    BREED_DROP_DOWN = (By.ID, "subscription_dog_breed_dog_breed_1_name"),
    BREED_SUBMIT_BUTTON = (By.CSS_SELECTOR, ".full-blue-continue-btn")

    def __init__(self, browser, ):
        self.browser = browser

    def seed_data(self):
        with open('data/super_chewer.json') as json_file:
            return json.load(json_file)

    def click_choose_plan(self):
        self.browser.execute_script("window.scrollTo(0,451)")
        self.browser.find_element(By.CSS_SELECTOR, ".pull-right:nth-child(2) > .button").click()

    def select_male(self):
        self.browser.find_element(By.ID, "male").click()

    def enter_name(self):
        data = self.seed_data()
        self.browser.find_element(By.ID, "subscription_dog_name_dog_name").click()
        self.browser.find_element(By.ID, "subscription_dog_name_dog_name").send_keys(data['dog_name'])

    def submit_dog_name(self):
        self.browser.find_element(By.ID, "dog-name-submit").click()

    def select_medium_size(self):
        self.browser.find_element(By.CSS_SELECTOR, ".medium .emphasize").click()

    def select_breed(self):
        element = self.browser.find_element(By.ID, "subscription_dog_breed_dog_breed_1_name")
        element.click()
        element.send_keys("poodle")
        self.browser.find_element(By.CSS_SELECTOR, ".single-result:nth-child(3)").click()

    def breed_submit_button(self):
        self.browser.find_element(By.CSS_SELECTOR, ".full-blue-continue-btn").click()

    def select_date_of_birth(self):
        month = Select(self.browser.find_element(By.ID, "subscription_dog_birthday_dog_birth_month"))
        month.select_by_visible_text("July")
        date = Select(self.browser.find_element(By.ID, "subscription_dog_birthday_dog_birth_day"))
        date.select_by_visible_text("12")
        year = Select(self.browser.find_element(By.ID, "subscription_dog_birthday_dog_birth_year"))
        year.select_by_visible_text("2020")
        self.browser.find_element(By.CSS_SELECTOR, ".full-blue-continue-btn").click()

    def select_everything(self):
        self.browser.find_element(By.CSS_SELECTOR, ".subscription_allergy_selection_no_exclusions p").click()
        self.browser.find_element(By.CSS_SELECTOR, ".full-blue-continue-btn").click()

    def fill_email_textfield(self):
        data = self.seed_data()
        self.browser.find_element(By.ID, "subscription_email_email").click()
        self.browser.find_element(By.ID, "subscription_email_email").send_keys(data['email'])

    def commit_email(self):
        self.browser.find_element(By.NAME, "commit").click()

    def select_one_month_subscription(self):
        self.browser.find_element(By.CSS_SELECTOR, ".sc2-2020q4 > .col:nth-child(3) .group-content").click()

    def select_no_extra_toy(self):
        self.browser.find_element(By.CSS_SELECTOR, ".dark-grey").click()

    def select_top_rated_theme(self):
        self.browser.find_element(By.CSS_SELECTOR, ".col:nth-child(6) .tile").click()

    def click_on_super_chewer_link(self):
        self.browser.find_element(By.CSS_SELECTOR, ".brand-nav-logo--superchewer").click()

    def fill_shopping_address(self):
        data = self.seed_data()
        print(data['mailingAddress']['first_name'])
        self.browser.find_element(By.ID, "subscription_express_checkout_address_attributes_first_name").click()
        self.browser.find_element(By.ID, "subscription_express_checkout_address_attributes_first_name").send_keys(
            data['mailingAddress']['first_name'])
        self.browser.find_element(By.ID, "subscription_express_checkout_address_attributes_last_name").send_keys(
            data['mailingAddress']['last_name'])
        self.browser.find_element(By.ID, "subscription_express_checkout_address_attributes_street1").send_keys(
            data['mailingAddress']['street'])
        self.browser.find_element(By.ID, "subscription_express_checkout_address_attributes_city").send_keys(
            data['mailingAddress']['city'])
        dropdown = Select(self.browser.find_element(By.ID, "subscription_express_checkout_address_attributes_state"))
        dropdown.select_by_visible_text(data['mailingAddress']['state'])
        self.browser.find_element(By.ID, "subscription_express_checkout_address_attributes_zip").send_keys(
            data['mailingAddress']['zip_code'])

    def click_on_credit_card_link(self):
        self.browser.find_element(By.ID, "credit-card").click()
