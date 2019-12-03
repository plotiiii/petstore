"""订单管理DAO"""
import pymysql

from com.jcl.petstore.dao.base_dao import BaseDao

class OrderDao(BaseDao):
    def __init__(self):
        super().__init__()

    def findall(self):
        """查询所有订单"""
        orders = []
        try:
            # 创建游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL操作
                sql = 'select orderid,userid,orderdate from orders'
                cursor.execute(sql)
                # 提取结果集
                result_set = cursor.fetchall()

                for row in result_set:
                    order = {}
                    order['orderid'] = row[0]
                    order['userid'] = row[1]
                    order['orderdate'] = row[2]
                    orders.append(order)

                # with代码块结束 5.关闭游标
        finally:
            # 6.关闭数据库连接
            self.close()
        return orders

    def create(self,order):
        """创建订单，插入到数据库"""
        try:
            # 创建游标对象
            with self.conn.cursor() as cursor:
                # 执行SQL操作
                sql = 'insert into orders(orderid,userid,orderdate,status,amount)'\
                      'values (%s,%s,%s,%s,%s)'
                affectedcount = cursor.execute(sql,order)
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
            self.close()