import time

from flask import Blueprint, render_template, request, redirect, url_for, session, make_response, jsonify
import logging

from werkzeug.debug import console
from app.config.config import config
from app.config.ue_config import FEEDBACK_UECONFIG
from app.settings import env
from common.utils import compress_image
from model.article import Article
from model.favorite import Favorite
from model.feedback import Feedback
from model.user import User

feedback = Blueprint("feedback",__name__)

@feedback.route("/feedback", methods=["GET", "POST"])
def ueditor():
    param = request.args.get("action")
    if request.method == "GET" and param == "config":
        return make_response(FEEDBACK_UECONFIG)
    # 下边为图片上传的代码
    elif param == "image":
        f = request.files.get("file")
        filename = f.filename
        # 文件的后缀名
        suffix = filename.split(".")[-1]
        newname = time.strftime("%Y%m%d_%H%M%S." + suffix)
        f.save("resource/upload/" + newname)
        # 大图片压缩
        source = dest = "resource/upload" + newname
        compress_image(source, dest, 1200)

        # 构造响应数据
        result = {}
        result["state"] = "SUCCESS"
        result['url'] = "/upload/" + newname
        result["title"] = filename
        result["original"] = filename
        return jsonify(result)

