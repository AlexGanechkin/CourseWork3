import json


def load_data(path):
    """ Загружает данные из файла c постами и возвращает список словарей"""
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_posts_all(path):
    """ Возвращает список постов всех пользователей со всеми данными"""
    posts = load_data(path)
    return posts


def get_posts_by_user(path, user_name):
    """ Возвращает список постов одного пользователя по его имени"""
    posts = load_data(path)
    poster_posts = []
    for post in posts:
        if post['poster_name'] == user_name.lower():
            poster_posts.append(post)
    if len(poster_posts) == 0:
        raise ValueError("Нет такого пользователя")
    return poster_posts


def search_for_posts(path, query):
    """ Возвращает список постов, содержащих ключевое слово, полученное от пользователя """
    posts = load_data(path)
    poster_posts = []
    for post in posts:
        if query.lower() in post['content'].lower():
            poster_posts.append(post)
            if len(poster_posts) > 10:
                return poster_posts
    if len(poster_posts) == 0:
        raise ValueError("Нет постов с таким ключевым словом")
    return poster_posts


def get_posts_by_pk(path, pk):
    """ Возвращает пост по его идентификатору """
    posts = load_data(path)
    for post in posts:
        if post['pk'] == int(pk):
            return post


def get_comments_by_post_id(path, post, post_id):
    """ Возвращает список комментов по идентификатору поста либо ошибку если нет запрошенного поста """

    if post is None:
        raise ValueError("Нет такого поста")

    comments = load_data(path)
    post_comments = []
    for comment in comments:
        if int(post_id) == comment['post_id']:
            post_comments.append(comment)
    return post_comments


def get_word_ending(number_comments):
    """ Возвращает окончание слова комментарий в зависимости от их количества """
    number_comments = round(number_comments % 10, 1)
    if number_comments == 1:
        comment_ending = "комментарий"
    elif number_comments in (2, 3, 4):
        comment_ending = "комментария"
    else:
        comment_ending = "комментариев"
    return comment_ending
