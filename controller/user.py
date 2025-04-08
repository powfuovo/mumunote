# -*- coding: utf-8 -*-
import hashlib
import json
import re

from flask import Blueprint, make_response, session, request

from common import response_message
from common.email_utils import gen_email_code, send_email
from common.utils import ImageCode
from model.user import User

# from model.user import User

user = Blueprint('user', __name__)

@user.route('/vcode')
def vcode():
    # 调用 ImageCode 类的 get_code 方法，获取验证码文本和图像二进制数据
    code,bstring = ImageCode().get_code()

    # 将图像二进制数据包装成 Flask 响应对象
    response = make_response(bstring)

    # 设置响应头，告诉浏览器这是 JPEG 图片
    response.headers['Content-Type'] = 'image/jpeg'

    # 将验证码文本转为小写后存入 session（用于后续验证）
    session['vcode'] = code.lower()

    # 返回包含验证码图片的响应
    return response


@user.route('/ecode',methods=['POST'])
def email_code():
    email = request.form.get('email')
    # 简单的邮箱格式验证
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return response_message.UserMessage.other("Invalid email")
    # 生成邮箱验证码的随机字符串
    code = gen_email_code()

    # 发送邮件
    try:
        send_email(email,code)
        session['ecode'] = code.lower()
        return response_message.UserMessage.success("邮件发送成功")
    except Exception as e:
        print(e)
        return response_message.UserMessage.error("邮件发送失败")

@user.route('/reg',methods=['POST'])
def register():
    request_data = json.loads(request.data)
    username = request_data['username']
    password = request_data['password']
    second_password = request_data['second_password']
    ecode = request_data['ecode']
    # 做数据的验证
    if ecode.lower() != session.get("ecode"):
        return response_message.UserMessage.error("邮箱验证码错误")
    # 用户名 和 密码的验证
    if not re.match(".+@.+\..+", username):
        return response_message.UserMessage.other("无效的邮箱")

    if len(password) < 6:
        return response_message.UserMessage.error("密码不合法")

    if password != second_password:
        return response_message.UserMessage.error("两次密码不一致")

    # 用户名是否已经被注册
    user = User()
    if len(user.find_by_username(username)) > 0:
        return response_message.UserMessage.error("用户名已存在")

    # 实现注册功能
    password = hashlib.md5(password.encode()).hexdigest()
    result = user.do_register(username, password)
    return response_message.UserMessage.success("用户注册成功！")

