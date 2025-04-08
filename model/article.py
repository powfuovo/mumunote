from sqlalchemy import Table, or_
from common.database import db_connect
from app.config.config import config
from app.settings import env
from model.user import User

db_session, Base, engine = db_connect()

class Article(Base):
    __table__ = Table("article", Base.metadata, autoload_with=engine)
    # ��ѯ���������£����ǲ�Ҫ�ݸ�
    def find_article(self, page, article_type="recommend"):
        #  һҳ��ʾ����������, ����Ĭ��Ϊһ��10, pageĬ��Ӧ���Ǵ�1��ʼ
        if int(page) < 1:
            page = 1
        count = int(page) * config[env].page_count
        # ���֤�����������Ƽ��ķ����±�
        if article_type == "recommend":
            result = db_session.query(Article, User.nickname).join(
                User, User.user_id == Article.user_id
            ).filter(
                Article.drafted == 1
            ).order_by(
                Article.browse_num.desc()
            ).limit(count).all()
        else:
            result = db_session.query(Article, User.nickname).join(
                User, User.user_id == Article.user_id
            ).filter(
                Article.label_name == article_type,
                Article.drafted == 1
            ).order_by(
                Article.browse_num.desc()
            ).limit(count).all()
        return result

    def search_article(self, page, keyword):
        if int(page) < 1:
            page = 1
        count = int(page) * config[env].page_count
        result = db_session.query(Article, User.nickname).join(
            User,User.user_id==Article.user_id).filter(
            or_(Article.title.like('%{}%'.format(keyword)),
                Article.article_content.like('%{}%'.format(keyword)),)
        ).order_by(
            Article.browse_num.desc()
        ).limit(count).all()
        return result

    # ��ȡ��������
    def get_article_detail(self, article_id):
        return db_session.query(Article).filter_by(id=article_id).first()
