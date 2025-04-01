from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base
from app.config.config import config
from app.settings import env

def db_connect():
    # 创建一个引擎，连接到数据库                                                              调试用
    engine = create_engine(config[env].db_url, echo = config[env].if_echo)
    # 打开数据库的连接会话
    session = sessionmaker(engine)
    # 保证线程安全
    db_session = scoped_session(session)
    # 获取基类
    Base = declarative_base()
    return db_session, Base, engine