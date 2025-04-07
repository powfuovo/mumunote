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
    # ���� ImageCode ��� get_code ��������ȡ��֤���ı���ͼ�����������
    code,bstring = ImageCode().get_code()

    # ��ͼ����������ݰ�װ�� Flask ��Ӧ����
    response = make_response(bstring)

    # ������Ӧͷ��������������� JPEG ͼƬ
    response.headers['Content-Type'] = 'image/jpeg'

    # ����֤���ı�תΪСд����� session�����ں�����֤��
    session['vcode'] = code.lower()

    # ���ذ�����֤��ͼƬ����Ӧ
    return response
