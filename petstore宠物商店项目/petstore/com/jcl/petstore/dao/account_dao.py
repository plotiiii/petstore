"""用户管理DAO"""
from com.jcl.petstore.dao.base_dao import BaseDao

class AccountDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findbyid(self,userid):
        account = None
        try:
            #创建游标对象
            with self.conn.cursor() as cursor:
                #执行SQL操作
                sql = 'select userid,password,email,name,addr,city,country,phone ' \
                      'from accounts where userid =%s'
                cursor.execute(sql, userid)
                #提取结果集
                row = cursor.fetchone()

                if row is not None:
                    account = {}
                    account['userid'] = row[0]
                    account['password'] = row[1]
                    account['email'] = row[2]
                    account['name'] = row[3]
                    account['addr'] = row[4]
                    account['city'] = row[5]
                    account['country'] = row[6]
                    account['phone'] = row[7]

                #with代码块结束 5.关闭游标
        finally:
            # 6.关闭数据库连接
            self.close()
        return account