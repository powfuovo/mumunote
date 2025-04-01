# 全局通用配置
class Config(object):
    db_url = "mysql+pymysql://admin1:123@192.168.73.45:3306/mumushouji"

#测试环境 继承
class TestConfig(Config):
    if_echo = True
    LOG_LEVEL = "DEBUG"

#生产环境
class ProductionConfig(Config):
    if_echo = False
    LOG_LEVEL = "INFO"

config = {
    'test': TestConfig,
    'prop': ProductionConfig,
}