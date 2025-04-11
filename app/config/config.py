# 全局通用配置
class Config(object):
    db_url = "mysql+pymysql://admin1:123@192.168.1.102:3306/mumunote"
    # 前端页面显示的条数
    page_count = 10
    # 配置一下文章图片的存储路径
    article_header_image_path = "/images/article/header/"

    # 发送邮箱配置
    email_name = "powfuovoo@163.com"
    email_passwd = "MVnABhHUwffn8TLU"

    # 配置头像存储路径
    user_header_image_path = "/images/headers/"

# 测试环境
class TestConfig(Config):
    # db_url = ""
    if_echo=True
    LOG_LEVEL="DEBUG"

class ProductionConfig(Config):
    if_echo=False
    LOG_LEVEL = "INFO"

config = {
    "test": TestConfig,
    "prod": ProductionConfig
}
