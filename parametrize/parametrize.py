from locators.locators import MainPage, OrderPage
from datetime import datetime, timedelta


class TextSectionQuestions:
    data = [
        (MainPage.num_questions_0, MainPage.num_questions_0_text, 'Сутки — 400 рублей. Оплата курьеру — наличными или '
                                                                  'картой.'),

        (MainPage.num_questions_1, MainPage.num_questions_1_text,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
         'можете просто сделать несколько заказов — один за другим.'),

        (MainPage.num_questions_2, MainPage.num_questions_2_text,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. '
         'Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. '
         'Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),

        (MainPage.num_questions_3, MainPage.num_questions_3_text, 'Только начиная с завтрашнего дня. Но скоро станем '
                                                                  'расторопнее.'),

        (MainPage.num_questions_4, MainPage.num_questions_4_text,
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),

        (MainPage.num_questions_5, MainPage.num_questions_5_text,
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — '
         'даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),

        (MainPage.num_questions_6, MainPage.num_questions_6_text,
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),

        (MainPage.num_questions_7, MainPage.num_questions_7_text, 'Да, обязательно. Всем самокатов! И Москве, '
                                                                  'и Московской области.')

    ]

