"""订单明细管理DAO"""
import pymysql

from com.jcl.petstore.dao.base_dao import BaseDao

class OrderDetailDao(BaseDao):
    def __init__(self):
        super().__init__()

    def create(self,orderdetail):
        try:
            # 创建游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL操作
                sql = 'insert into orderdetails(orderid,productid,quantity,unitcost' \
                      ' values (%s,%s,%s,%s)'
                affectedcount = cursor.execute(sql, orderdetail)
                print('成功插入{0}条数据'.format(affectedcount))
                #提交数据库事务
                self.conn.commit()
                # 代码块结束 关闭游标
        except pymysql.DatabaseError as e:
            #回滚数据库事务
            self.conn.rollback()
            print(e)
        finally:
            # 6.关闭数据库连接
            self.conn.close()