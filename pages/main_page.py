import allure
from selenium.webdriver.support.wait import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import MainPage


class SectionQuestions:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 3)

    @allure.step('Нажимаем на вопросы')
    def click_question(self, question):
        self.wait.until(EC.visibility_of_element_located(question))
        el = self.driver.find_element(*question)
        self.driver.execute_script('arguments[0].scrollIntoView();', el)
        self.wait.until(EC.visibility_of_element_located(question))
        self.wait.until(EC.element_to_be_clickable(question))
        self.driver.find_element(*question).click()

    @allure.step('Проверяем текст вопросов')
    def text_answer(self, answer):
        return self.driver.find_element(*answer).text


class ButtonsOrder:
    def __init__(self, driver):
        self.driver = driver
        self.wait = wait(self.driver, 3)

    def click_button_order_header(self, button):
        self.driver.find_element(*button).click()
