from utils import *
import pytest

path = './data/posts.json'
keys_should_be = {'poster_name', 'poster_avatar', 'pic', 'content', 'pk', 'views_count', 'likes_count'}


@pytest.fixture
def get_all_data():
    return get_posts_all(path)


class TestLoadData:

    """ Проверяем загружается ли файл с постами пользователей """
    def test_load_data(self):
        with pytest.raises(FileNotFoundError):
            load_data('./data/no_file.json')


class TestPosts:

    """ Проверяем структуру списка с постами пользователей, данные получены через фикстуру """
    def test_get_posts_all(self, get_all_data):
        assert type(get_all_data) == list, "возвращается не список"
        assert len(get_all_data) > 0, "возвращается пустой список"
        assert set(get_all_data[0].keys()) == keys_should_be, "неверный список ключей"


class TestPoster:

    """ Проверяем корректность поиска пользователя и его постов """
    def test_get_poster(self):
        user = get_posts_by_user(path, user_name='leo')
        assert type(user) == list, "возвращается не список"
        assert len(user) > 0, "пользователь не найден"

    def test_no_poster_name(self):
        with pytest.raises(ValueError):
            get_posts_by_user(path, user_name="no such user name")


class TestSearchPosts:

    """ Проверяем корректность поиска по ключевым словам """
    def test_search_for_posts(self):
        found_posts = search_for_posts('./data/posts_for_test.json', query='еда')
        assert len(found_posts) > 0, "посты не найдены"
        assert len(found_posts) > 10, "найдено больше 10 постов"

        with pytest.raises(ValueError):
            search_for_posts('./data/posts_for_test.json', query='нет таких слов')


class TestGetPosts:

    """ Проверяем корректность поиска по id пользователя """
    def test_get_post_by_pk(self):
        posts_by_id = get_posts_by_pk(path, pk='1')
        assert len(posts_by_id) > 0, "посты не найдены"


class TestComments:

    """ Проверяем корректность поиска по id пользователя """
    def test_get_comments_by_post_id(self):
        post = get_posts_by_pk(path, pk='1')
        comments_by_post_id = get_comments_by_post_id('./data/comments.json', post, post_id=1)
        assert len(comments_by_post_id) > 0, "комментарии не найдены"
