# 主要是对数据库进行增查删改操作，这些操作建立在数据库连接，最后还要关闭数据库连接，把基本功能
# 封装在DAO基类中
import pymysql
#配置文件解析模块
import configparser

class BaseDao(object):
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini',encoding='utf-8')

        host = self.config['db']['host']
        user = self.config['db']['user']
        #读取数据
        port = self.config.getint('db','port')
        password = self.config['db']['password']
        database = self.config['db']['database']
        charset = self.config['db']['charset']

        self.conn = pymysql.connect(host=host,
                                    user=user,
                                    port=port,
                                    password=password,
                                    database=database,
                                    charset=charset)

    def close(self):
        """ 关闭数据库连接 """
        self.conn.close()