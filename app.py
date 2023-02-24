from flask import Flask

""" Импортируем блюпринты """
from views import main_blueprint, post_blueprint, search_blueprint, user_feed_blueprint
from api_views import api_posts_blueprint, api_posts_by_id_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


""" Регистрируем блюпринты вьюшек """
app.register_blueprint(main_blueprint)
app.register_blueprint(post_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(user_feed_blueprint)

""" Регистрируем блюпринты API-вьюшек """
app.register_blueprint(api_posts_blueprint)
app.register_blueprint(api_posts_by_id_blueprint)


@app.errorhandler(404)
def no_page(e):
    return "Запрошенная страница не найдена"


@app.errorhandler(500)
def no_page(e):
    return "Ошибка на странице"


if __name__ == "__main__":
    app.run()
