from flask import Blueprint, make_response, session

from common.utils import ImageCode

# from model.user import User

user = Blueprint('user', __name__)

# @user.route('/user')
# def get_one():
#     user = User()
#     result = user.get_one()
#     print (result.__dict__)
#     return "ok"

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
