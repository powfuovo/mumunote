# 全局通用配置
class Config(object):
    db_url = "mysql+pymysql://admin1:123@127.0.0.1:3306/mumunote"
    # 前端页面显示的条数
    page_count = 10
    # 配置一下文章图片的存储路径
    article_header_image_path = "/images/article/header/"

    # 发送邮箱配置
    email_name = "powfuovoo@163.com"
    email_passwd = "MVnABhHUwffn8TLU"

    # 配置头像存储路径
    user_header_image_path = "/images/headers/"

    label_types = {
        "recommend": {"name": "请选择需要投递的栏目", "selected": "selected"},
        "auto_test": {"name": "自动化测试", "selected": "no-selected"},
        "python": {"name": "Python", "selected": "no-selected"},
        "java": {"name": "Java", "selected": "no-selected"},
        "function_test": {"name": "功能测试", "selected": "no-selected"},
        "perf_test": {"name": "性能测试", "selected": "no-selected"},
        "funny": {"name": "幽默段子", "selected": "no-selected"},
    }

    article_types = {
        "recommend": {"name": "请选择", "selected": "selected"},
        "first": {"name": "首发", "selected": "no-selected"},
        "original": {"name": "原创", "selected": "no-selected"},
        "other": {"name": "其它", "selected": "no-selected"},
    }
    article_tags = [
        "Html5", "Angular", "JS", "CSS3", "Sass/Less",
        "JAVA", "Python", "Go", "C++", "C#", "MySQL",
        "Oracle", "MongoDB", "Android", "Unity 3", "DCocos2d-x"
    ]

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
