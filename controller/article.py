from flask import Blueprint, render_template, request, redirect, url_for, session
import logging

from werkzeug.debug import console

from app.config.config import config
from app.settings import env

from model.article import Article
from model.favorite import Favorite
from model.user import User

article = Blueprint("article",__name__)


@article.route("/detail")
def article_detail():
    article_id = request.args.get("article_id")
    article = Article()
    # 获取文章的所有信息
    article_content = article.get_article_detail(article_id)
    article_tag_string =article_content.article_tag
    article_tag_list = article_tag_string.split(",")
    # 获取文章作者信息
    user = User()
    user_info = user.find_by_user_id(article_content.user_id)

    # @todo 待办 补充获取文章的评论信息

    # @todo 待办 补充获取文章的点赞信息

    # @todo 待办 "我"是否收藏
    is_favorite = 1

    if session.get("is_login") == "true":
        user_id = session.get("user_id")
        is_favorite = Favorite().user_if_favorite(user_id, article_id)

     # 相关文章功能
    about_article = article.find_about_article(article_content.label_name)


    return render_template("article-info.html",
                           article_content=article_content,
                           user_info=user_info,
                           is_favorite=is_favorite,
                           article_tag_list=article_tag_list,
                           about_article=about_article)
