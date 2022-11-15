from flask import Blueprint, render_template, request
from utils import *

path = "./data/posts.json"

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
post_blueprint = Blueprint('post_blueprint', __name__, template_folder='templates')
search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')
user_feed_blueprint = Blueprint('user_feed_blueprint', __name__, template_folder='templates')

""" Блюпоринт главной страницы """


@main_blueprint.route('/')
def main_page():
    posts = get_posts_all(path)
    return render_template('index.html', posts=posts)


""" Блюпоринт страницы с подробным постом пользователя """


@post_blueprint.route('/posts/<int:post_id>')
def post_page(post_id):
    post = get_posts_by_pk(path, post_id)
    comments = get_comments_by_post_id("./data/comments.json", post, post_id)
    number_comments = len(comments)
    comment_ending = get_word_ending(number_comments)
    return render_template(
        'post.html', post=post, comments=comments,
        number_comments=number_comments, comment_ending=comment_ending
    )


""" Блюпоринт страницы с результатами поиска по ключевым словам """


@search_blueprint.route('/search')
def search_page():
    query = request.args['s']
    posts = search_for_posts(path, query)
    number_posts = len(posts)
    return render_template('search.html', posts=posts, number_posts=number_posts)


@user_feed_blueprint.route('/users/<username>')
def user_feed_page(username):
    user_posts = get_posts_by_user(path, username)
    return render_template('user-feed.html', user_posts=user_posts)
