import pymysql
import logging
import sys
import configparser

# 加入日志
# 获取logger实例
logger = logging.getLogger("dbSql")
# 指定输出格式
formatter = logging.Formatter('%(asctime)s\
              %(levelname)-8s:%(message)s')
# 文件日志
file_handler = logging.FileHandler("dbSql.log")
file_handler.setFormatter(formatter)
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)

# 为logge添加具体的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.setLevel(logging.INFO)


class DbManager:
    # 构造函数
    def __init__(self, host='127.0.0.1', port=3306, user='root',
                 passwd='123456', db='video', charset='utf8'):
        # config = configparser.ConfigParser()
        # config.read("../config/mysql.ini")
        # self.host = config.get("connectString", "host")
        # self.port = int(config.get("connectString", "port"))
        # self.user = config.get("connectString", "user")
        # self.passwd = config.get("connectString", "passwd")
        # self.db = config.get("connectString", "db")
        # self.charset = config.get("connectString", "charset")
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset
        self.conn = None
        self.cur = None

    # 修改查询数据库
    def setDatabase(self, database):
        self.db = database

    # 连接数据库
    def connectDatabase(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
                                        charset=self.charset)
        except:
            logger.error("connectDatabase failed")
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库
    def close(self):
        # 如果数据打开，则关闭；否则没有操作
        if self.conn and self.cur:
            self.cur.close()
            self.conn.close()
        return True

    # 执行数据库的sq语句,主要用来做插入操作
    def execute(self, sql, params=None, commit=False, ):
        # 连接数据库
        res = self.connectDatabase()
        if not res:
            return False
        try:
            if self.conn and self.cur:
                # 正常逻辑，执行sql，提交操作
                rowcount = self.cur.execute(sql, params)
                # print(rowcount)
                if commit:
                    self.conn.commit()
                else:
                    pass
        except:
            logger.error("execute failed: " + sql)
            logger.error("params: " + str(params))
            self.close()
            return False
        return rowcount

    # 查询所有数据
    def fetchall(self, sql, params=None):
        res = self.execute(sql, params)
        if not res:
            logger.info("查询失败")
            return False
        self.close()
        results = self.cur.fetchall()
        logger.info("查询成功" + str(results))
        return results

    # 查询一条数据
    def fetchone(self, sql, params=None):
        res = self.execute(sql, params)
        if not res:
            logger.info("查询失败")
            return False
        self.close()
        result = self.cur.fetchone()
        logger.info("查询成功" + str(result))
        return result

    # 增删改数据
    def queryStr(self, sql, params=None):
        res = self.execute(sql, params, True)
        if not res:
            logger.info("操作失败")
            return False
        self.conn.commit()
        self.close()
        logger.info("操作成功" + str(res))
        return res


if __name__ == '__main__':
    dbManager = DbManager()

    """插入
    sql = "insert into user(username,password) values(%s,%s);"
    values = ["ccc", "123456"]
    result = dbManager.queryStr(sql, values)
    """

    """删除
    sql = "delete from user where id = %s;"
    values = [7]
    result = dbManager.queryStr(sql, values)
    """

    """更新
    sql = "update user set password = %s where id = %s;"
    values = ["123", 5]
    result = dbManager.queryStr(sql, values)
    """

    """查找一条数据
    sql = "select * from user;"
    result = dbManager.fetchone(sql)
    """

    """查找所有数据
    sql = "select username,password from user;"
    result = dbManager.fetchall(sql)
    """

    sql = "select username,password from user;"
    result = dbManager.fetchall(sql)