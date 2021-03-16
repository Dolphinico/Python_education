import unittest
from survey import AnonymousSurvey
# Первый тестовый метод проверяет, что
# сохраненный ответ действительно попадает в список ответов опроса. Этому методу
# присваивается хорошее содержательное имя test_store_single_response():
class TestAnonymousSurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvey"""
# Если тест не проходит, имя метода в выходных данных сбойного теста ясно показывает,
# что проблема связана с сохранением отдельного ответа на опрос: 
    def test_store_single_response(self):
        """Проверяет что один ответ сохранен правильно"""
        question = "What language did you fisrt learn to speak?"
# создается экземпляр с именем my_survey для вопроса "What language
# did you first learn to speak?",
# Один ответ (English) сохраняется с использованием метода store_response().
# Затем программа убеждается в том, что ответ был
# сохранен правильно; для этого она проверяет, что значение English присутствует
# в списке my_survey.responses:        
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn("English", my_survey.responses)
        
    def test_store_three_responses(self):
        """Проверяет, что три ответа были даны правильно"""
# создаем объект опроса по аналогии с тем, как это делалось в test_store_single_response().
# Затем определяется список, содержащий три разных ответа:
        question = "What language did you fisrt learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin']
# После того как ответы будут сохранены, следующий цикл проверяет,
# что каждый ответ теперь присутствует в my_survey.responses:
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response,my_survey.responses)

unittest.main()


# добавим еще один метод, чтобы проверить что правильно сохраняется более одного ответа

