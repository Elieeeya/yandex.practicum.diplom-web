import allure
import pytest
from pages.order_page import WorkflowOrder, UserData as us
from pages.base_pages import BasePage


class TestWorkflow:
    @allure.title('Запуск флоу позитивного сценария по кнопке "Заказать" в хидере страницы')
    def test_click_button_in_the_header_for_filling_out_the_order_form_success(self, driver):
        self.driver = driver
        bp = BasePage(self.driver)
        wf = WorkflowOrder(self.driver)
        bp.accept_cookies()
        bp.click_button_order_header()
        wf.fill_first_form(name=us.firstname_male, surname=us.surname_male, addres=us.address_male,
                           station=us.station_male, phone=us.phone_male)
        wf.fill_first_form_button_next()
        wf.fill_second_form(date=us.date_male, index=us.indx_male, color=us.color_male, comment=us.comment_male)
        wf.fill_second_form_button_next()
        wf.button_yes_confirmation_window()
        title = wf.order_window()
        wf.button_check_status_modal_window()

        assert 'Заказ оформлен' in title

        bp.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
        bp.click_logo_yandex()
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'

    @allure.title('Запуск флоу позитивного сценария по кнопке "Заказать" в середине страницы')
    def test_click_button_in_the_middle_for_filling_out_the_order_form_success(self, driver):
        self.driver = driver
        bp = BasePage(self.driver)
        wf = WorkflowOrder(self.driver)
        bp.accept_cookies()
        bp.scroll_button_order_middle()
        bp.click_button_order_middle()
        wf.fill_first_form(name=us.firstname_female, surname=us.surname_female, addres=us.address_female,
                           station=us.station_female, phone=us.phone_female)
        wf.fill_first_form_button_next()
        wf.fill_second_form(date=us.date_female, index=us.indx_female, color=us.color_female, comment=us.comment_female)
        wf.fill_second_form_button_next()
        wf.button_yes_confirmation_window()
        title = wf.order_window()
        wf.button_check_status_modal_window()
        assert 'Заказ оформлен' in title

        bp.click_logo_scooter()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'
        bp.click_logo_yandex()
        assert driver.current_url == 'https://dzen.ru/?yredirect=true'
