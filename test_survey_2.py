import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""
    def setUp(self):
        """Создание опроса и набора ответов для всех тестовых методов"""
        question = 'what language did you first learn to speak?'
# Метод setUp() решает две задачи: он создает экземпляр опроса:
        self.my_survey = AnonymousSurvey(question)
# список ответов:
        self.responses = ['English','Spanish','Mandarin']
 
    def test_store_single_response(self):
        """Проверяет что один ответ сохранен правильно"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        """Проверяет, что три ответа были даны правильно"""

        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()

# Каждый из этих атрибутов снабжается префиксом self,
# поэтому он может использоваться где угодно в классе. 
# Это обстоятельство упрощает два тестовых метода, 
# потому что им уже не нужно создавать экземпляр опроса или ответы.
# Метод test_store_single_response() убеждается в том, что первый ответ в self.responses — self.responses[0] 
# — сохранен правильно, а метод test_store_single_response()
# убеждается в том, что правильно были сохранены все три ответа в self.responses.

# При тестировании классов, написанных вами, метод setUp() упрощает написание
# тестовых методов. Вы создаете один набор экземпляров и атрибутов в setUp(),
# а затем используете эти экземпляры во всех тестовых методах. Это намного проще
# и удобнее, чем создавать новый набор экземпляров и атрибутов в каждом тестовом методе.