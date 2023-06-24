from selenium.webdriver.common.by import By


class MainPage:
    button_coockie = (By.ID, 'rcc-confirm-button')
    home_page = [By.CLASS_NAME, 'Home_HomePage__ZXKIX']
    questions = (By.CLASS_NAME, 'accordion')
    num_questions_0 = (By.XPATH, './/*[contains(@id, "accordion__heading-0")]')
    num_questions_1 = (By.XPATH, './/*[contains(@id, "accordion__heading-1")]')
    num_questions_2 = (By.XPATH, './/*[contains(@id, "accordion__heading-2")]')
    num_questions_3 = (By.XPATH, './/*[contains(@id, "accordion__heading-3")]')
    num_questions_4 = (By.XPATH, './/*[contains(@id, "accordion__heading-4")]')
    num_questions_5 = (By.XPATH, './/*[contains(@id, "accordion__heading-5")]')
    num_questions_6 = (By.XPATH, './/*[contains(@id, "accordion__heading-6")]')
    num_questions_7 = (By.XPATH, './/*[contains(@id, "accordion__heading-7")]')
    num_questions_0_text = (By.ID, 'accordion__panel-0')
    num_questions_1_text = (By.ID, 'accordion__panel-1')
    num_questions_2_text = (By.ID, 'accordion__panel-2')
    num_questions_3_text = (By.ID, 'accordion__panel-3')
    num_questions_4_text = (By.ID, 'accordion__panel-4')
    num_questions_5_text = (By.ID, 'accordion__panel-5')
    num_questions_6_text = (By.ID, 'accordion__panel-6')
    num_questions_7_text = (By.ID, 'accordion__panel-7')

    button_order_header = (By.XPATH, "(//button[text()='Заказать'])[1]")
    sroll_button_midle = (By.CLASS_NAME, 'Home_FinishButton__1_cWm')
    button_order_middle = (By.XPATH, "(//button[text()='Заказать'])[2]")
    logo_scooter = (By.XPATH, ".//*[@alt='Scooter']")
    logo_yandex = (By.XPATH, ".//*[@alt='Yandex']")


class YandexPage:
    yadnex_search = (By.NAME, 'text')


class OrderPage:
    class FirstPage:
        name = (By.XPATH, "//input[@placeholder='* Имя']")
        surname = (By.XPATH, "//input[@placeholder='* Фамилия']")
        addres = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        station = (By.XPATH, "//input[@placeholder='* Станция метро']")
        click_station = (By.CLASS_NAME, "select-search__select")
        phone = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
        button_next = (By.XPATH, "//button[text()='Далее']")

    class SecondPage:
        date = [By.XPATH, ".//*[@placeholder='* Когда привезти самокат']"]
        date_selected = [By.CLASS_NAME, 'react-datepicker__day--selected']
        dropdown = (By.XPATH, ".//*[@class='Dropdown-arrow']")
        dropdown_option = (By.XPATH, ".//*[@class='Dropdown-menu']/div")
        comment = (By.XPATH, ".//*[@placeholder='Комментарий для курьера']")
        button_next = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

    class ModalWindow:
        button_window = (By.XPATH, "//button[text()='Да']")
        button_check_status = (By.XPATH, "//button[text()='Посмотреть статус']")
        title_window = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
