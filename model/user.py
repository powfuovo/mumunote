import random

from sqlalchemy import Table

from common.database import db_connect

db_session, Base, engine = db_connect()

class User(Base):
    # 表结构的反射加载
    __table__ = Table('user', Base.metadata, autoload_with=engine)

    def get_one(self):
        return db_session.query(User).first()

    def find_by_username(self, username):
        return db_session.query(User).filter_by(username=username).all()

    def do_register(self, username, password):
        nickname = username.split("@")[0]
        # avatar
        picture = str(random.randint(1, 428))+".jpg"
        job="小学生"
        user = User(nickname=nickname,
                    picture=picture,
                    job=job,
                    username=username,
                    password=password)
        db_session.add(user)
        db_session.commit()
        return user
