
import pymysql

class SQLOper:

    def __init__(self):
        self.host="localhost"
        self.user="root"
        self.port=3306
        self.password="password"
        self.dbname="vpndb"
        self.db=""

    def getDB(self):
        self.db = pymysql.connect(host=self.host, user=self.user,
                                  password=self.password, db=self.dbname, port=self.port)
    def closeDB(self):
        self.db.close()

    def executeSql(self,sql):
        self.getDB()
        cur = self.db.cursor()
        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录

        except Exception as e:
            raise e
        finally:
            self.closeDB()
            return results
    def executeInsertSql(self,pattern,value):
        self.getDB()
        cur = self.db.cursor()
        try:
            sql="insert into tbl_user ()values()"
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录

        except Exception as e:
            raise e
        finally:
            self.closeDB()
            return results

    def executeDelectSql(self,sql):
        self.getDB()
        cur = self.db.cursor()

        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录

        except Exception as e:
            raise e
        finally:
            self.closeDB()
            return results

    def executeUpdateSql(self,sql):
        self.getDB()
        cur = self.db.cursor()
        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录

        except Exception as e:
            raise e
        finally:
            db.close()
            return results