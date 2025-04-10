from sqlalchemy import Table, or_
from common.database import db_connect
from app.config.config import config
from app.settings import env
from common.utils import model_to_json
from model.user import User

db_session, Base, engine = db_connect()

class Feedback(Base):
    __table__ = Table("comment", Base.metadata, autoload_with=engine)

    def get_feedback_user_list(self,article_id):
        final_data_list = []
        # 查询一级评论 即新开的
        feedback_list = self.get_feedback_by_article_id(article_id)
        for feedback in feedback_list:
            user = User()
            # 根据一级评论 获取每楼下面的回复
            all_reply = self.find_reply_by_replyid(feedback.id)
            feedback_user = user.find_by_user_id(feedback.user_id)
            reply_list = []
            # 根据每一条评论的回复 查询用户信息
            for reply in all_reply:
                reply_content_with_user = {}
                from_user_data = user.find_by_user_id(reply.user_id)
                # 获取回复的是谁 的用户信息
                to_user_reply_data = self.find_reply_by_id(reply.reply_id)
                to_user_data = user.find_by_user_id(to_user_reply_data[0].user_id)

                reply_content_with_user["from_user"]=model_to_json(from_user_data)
                reply_content_with_user["to_user"]=model_to_json(to_user_data)
                reply_content_with_user["content"]=model_to_json(reply)
                reply_list.append(reply_content_with_user)

            # 储存每一个回复下面的所有数据
            every_feedback_data = model_to_json(feedback)
            every_feedback_data.update(model_to_json(feedback_user))
            every_feedback_data["reply_list"] = reply_list
            final_data_list.append(every_feedback_data)
        return final_data_list

    def get_feedback_by_article_id(self,article_id):
        result = db_session.query(Feedback).filter_by(
            article_id=article_id,
            reply_id=0,
            base_reply_id=0
        ).order_by(
            Feedback.id.desc()
        ).all()
        return result

    def find_reply_by_replyid(self,base_reply_id):
        result = db_session.query(Feedback).filter_by(
            base_reply_id=base_reply_id,
        ).order_by(
            Feedback.id.desc()
        ).all()
        return result

    def find_reply_by_id(self, reply_id):
        result = db_session.query(Feedback).filter_by(
            reply_id=id,
        ).order_by(
            Feedback.id.desc()
        ).all()
        return result

    def get_article_feedback_count(self,article_id):
        result = db_session.query(Feedback).filter_by(
            article_id=article_id,
            reply_id=0,
            base_reply_id=0
        ).count()
        return result
