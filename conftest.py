import pytest
from selenium import webdriver
from datetime import datetime, timedelta
from locators.locators import MainPage, OrderPage


base_url = 'https://qa-scooter.praktikum-services.ru/'


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()
