import json

from flask import Blueprint, render_template, request, redirect, url_for, session
import logging
from app.config.config import config
from app.settings import env
from common import response_message

from model.article import Article
from model.favorite import Favorite
from model.user import User

favorite = Blueprint("favorite",__name__)

@favorite.route("/favorite/update_status", methods=["post"])
def update_status():
    request_data = json.loads(request.data)
    user_id = session.get("user_id")
    print("🚀 ~ user_id:", user_id)
    article_id = request_data.get("article_id")
    canceled = request_data.get("canceled")
    try:
        favorite = Favorite()
        favorite.update_status(article_id=article_id,
                                   user_id=user_id,
                                   canceled=canceled)
        return response_message.FavoriteMessage.success("收藏成功")
    except Exception as e:
        logging.error(e)
        return response_message.FavoriteMessage.error("收藏失败")
