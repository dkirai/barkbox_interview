import json

from pytest_bdd import scenario, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from pages.super_chewer_Page import SuperChewerPage

URL = 'https://www.barkbox.com/'

@pytest.fixture
def browser():
    # You can change this fixture to use any browser but best practice is it get browser from a config file.
    b = webdriver.Chrome()
    b.implicitly_wait(20)
    yield b
    b.quit()

@pytest.fixture
def super_chewer_page(browser):
    return SuperChewerPage(browser)


@given("the home page as launch")
def barkbox_home(browser):
    browser.get(URL)
