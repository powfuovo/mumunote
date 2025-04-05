# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request
import logging
from app.config.config import config
from app.settings import env

from model.article import Article

index = Blueprint("index",__name__)


# 对应前端显示分类的字典
label_types = {
    "recommend": {"name": "推荐", "selected": "selected"},
    "auto_test": {"name": "自动化测试", "selected": "no-selected"},
    "python": {"name": "Python", "selected": "no-selected"},
    "java": {"name": "Java", "selected": "no-selected"},
    "function_test": { "name": "功能测试", "selected": "no-selected"},
    "perf_test": {"name": "性能测试", "selected": "no-selected"},
    "funny": {"name": "幽默段子", "selected": "no-selected"},
}

@index.route("/")
def home():
    # 获取当前到底是第几页
    page = request.args.get("page")
    article_type = request.args.get("article_type")
    logging.debug("page: " + str(page))
    logging.debug("article_type: "+ str(article_type))

    if page is None:
        page = 1
    if article_type is None:
        article_type = "recommend"

    #  到数据库中查询文章数据，然后返回给前端页面
    article = Article()
    db_result = article.find_article(page, article_type)

    for article, nickname in db_result:
      # 分类内容显示的转换
      article.label = label_types.get(article.label_name).get("name")

      # 日期的显示
      article.create_time = str(article.create_time.month) + '.' + str(article.create_time.day)

      # 图片路径的处理  "/images/article/header/"
      article.article_image = config[env].article_header_image_path + str(article.article_image)

      # 文章标签格式的修改
      article.article_tag = article.article_tag.replace(","," · ")

    return render_template("index.html",
                          result=db_result,
                          label_types=label_types)
