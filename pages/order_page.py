import allure
from selenium.webdriver.common.by import By
from locators.locators import OrderPage
from faker import Faker
import random


class UserData:
    fake = Faker("ru_RU")
    a = random.randint(920, 999)
    b = random.randint(900, 999)
    c = random.randint(00, 99)

    # generation male first name, surname, address, phone
    firstname_male = fake.first_name_male()
    surname_male = fake.last_name_male()
    address_male = 'Москва, Арбатская площадь, 14с1'
    station_male = 'Арбатская'
    phone_male = f'7{a}{b}{c}{c}'
    date_male = '28.02.2023'
    indx_male = 3
    color_male = 'grey'
    comment_male = 'Какой то комент'

    # generation female first name, surname, address, phone
    firstname_female = fake.first_name_female()
    surname_female = fake.last_name_female()
    address_female = 'Москва, Большая Тульская улица, 2'
    station_female = 'Комсомольская'
    phone_female = f'7{a}{b}{c}{c}'
    date_female = '28.02.2023'
    indx_female = 4
    color_female = 'black'
    comment_female = 'Какой то комент'


class WorkflowOrder:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполняем первую страницу формы заказа')
    def fill_first_form(self, name, surname, addres, station, phone):
        self.driver.find_element(*OrderPage.FirstPage.name).send_keys(name)
        self.driver.find_element(*OrderPage.FirstPage.surname).send_keys(surname)
        self.driver.find_element(*OrderPage.FirstPage.addres).send_keys(addres)
        self.driver.find_element(*OrderPage.FirstPage.station).click()
        self.driver.find_element(*OrderPage.FirstPage.station).send_keys(station)
        self.driver.find_element(*OrderPage.FirstPage.click_station).click()
        self.driver.find_element(*OrderPage.FirstPage.phone).send_keys(phone)

    @allure.step('После заполнения формы, нажимаем кнопку "Далее"')
    def fill_first_form_button_next(self):
        self.driver.find_element(*OrderPage.FirstPage.button_next).click()

    @allure.step('Заполняем вторую страницу формы заказа')
    def fill_second_form(self, date, index, color, comment):
        self.driver.find_element(*OrderPage.SecondPage.date).click()
        self.driver.find_element(*OrderPage.SecondPage.date).send_keys(date)
        self.driver.find_element(*OrderPage.SecondPage.dropdown).click()
        self.driver.find_elements(*OrderPage.SecondPage.dropdown_option)[index].click()
        self.driver.find_element(By.ID, color).click()
        self.driver.find_element(*OrderPage.SecondPage.comment).send_keys(comment)

    @allure.step('После заполнения формы, нажимаем кнопку "Далее"')
    def fill_second_form_button_next(self):
        self.driver.find_element(*OrderPage.SecondPage.button_next).click()

    @allure.step('В модальном окне нажимаем кнопку "Да"')
    def button_yes_confirmation_window(self):
        self.driver.find_element(*OrderPage.ModalWindow.button_window).click()

    @allure.step('В модальном окне проверям сообщение об успешном создании заказа')
    def order_window(self):
        text = self.driver.find_element(*OrderPage.ModalWindow.title_window).text
        return text

    @allure.step('В модальном окне нажимаем кнопку "Проверить заказ"')
    def button_check_status_modal_window(self):
        self.driver.find_element(*OrderPage.ModalWindow.button_check_status).click()
