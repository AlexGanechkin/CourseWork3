from flask import Blueprint, jsonify, request
from utils import *
import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)

handler = logging.FileHandler('./logs/api.log', encoding='utf-8')
handler.setLevel(logging.INFO)

log_format = '%(asctime)s [%(levelname)s] %(message)s'
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

path = './data/posts.json'


api_posts_blueprint = Blueprint('api_posts_blueprint', __name__)
api_posts_by_id_blueprint = Blueprint('api_posts_by_id_blueprint', __name__)


@api_posts_blueprint.route('/api/posts')
def api_posts():
    logger.info(f'Запрос {request.path}')
    posts = get_posts_all(path)
    return jsonify(posts)


@api_posts_by_id_blueprint.route('/api/posts/<int:post_id>')
def api_posts_by_id(post_id):
    logger.info(f'Запрос {request.path}')
    post = get_posts_by_pk(path, post_id)
    return jsonify(post)
