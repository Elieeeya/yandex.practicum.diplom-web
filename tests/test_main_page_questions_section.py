import allure
import pytest
from pages.main_page import SectionQuestions
from pages.base_pages import BasePage
from parametrize.parametrize import TextSectionQuestions


class TestQuestions:
    @allure.title('Проверка выпадающего списка в разделе «Вопросы о важном»')
    @pytest.mark.parametrize('question, answer, text_answer', TextSectionQuestions.data)
    def test_click_section_questions_check_text(self, question, answer, text_answer, driver):
        self.driver = driver
        sc = SectionQuestions(self.driver)
        bp = BasePage(self.driver)
        bp.accept_cookies()
        bp.wait_load_main_page()
        sc.click_question(question)
        text = sc.text_answer(answer)

        assert text == text_answer


