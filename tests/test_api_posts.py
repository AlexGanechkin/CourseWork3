import pytest
import main


""" Создаем фикстуру для тестирования API вьюшек """


@pytest.fixture()
def test_client():
    app = main.app
    return app.test_client()


""" Определяем, какие ключи ожидаем получать в списке и словаре """
keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'pk', 'views_count', 'likes_count'}


class TestAPIposts:

    def test_get_list(self, test_client):
        """ Проверяем, верный ли статус-код и верная ли структура данных в возвращаемом списке"""
        response = test_client.get('api/posts', follow_redirects=True)
        response_data = response.json
        assert type(response_data) == list, "Возвращаемое значение не список"
        assert set(response_data[0].keys()) == keys_should_be, "Неверный список ключей в первом элементе списка"

    def test_get_post(self, test_client):
        """ Проверяем, верный ли статус-код и верная ли структура данных в возвращаемом элементе списка """
        response = test_client.get('api/posts/1', follow_redirects=True)
        response_data = response.json
        assert type(response_data) == dict, "Возвращаемое значение не словарь"
        assert set(response_data.keys()) == keys_should_be, "Неверный список ключей в элементе списка"
