import pymysql


class SQLOper:
    def __init__(self):
        self.host = "127.0.0.1"
        # self.host="182.150.27.208"
        self.user = "test"
        self.port = 3306
        self.password = "test"
        self.dbname = "vpndb"
        self.db = ""

    def getDB(self):
        self.db = pymysql.connect(host=self.host, user=self.user,
                                  password=self.password, db=self.dbname, port=self.port)

    def closeDB(self):
        self.db.close()

    def executeDoubleSql(self, sql1, sql2):
        self.getDB()
        cur = self.db.cursor()
        try:
            cur.execute(sql1)  # 执行sql1语句
            cur.execute(sql2)  # 执行sql2语句
            results = cur.fetchall()

        except Exception as e:
            print("\033[1;31m{}\033[0m".format(e))
            raise e
        finally:
            self.closeDB()
            self.db.rollback()
            return results

    def executeSql(self, sql):
        self.getDB()
        cur = self.db.cursor()
        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录

        except Exception as e:
            print("\033[1;31m{}\033[0m".format(e))
            raise e
        finally:
            self.closeDB()
            return results

    def executeSelectAll(self, table):
        self.getDB()
        cur = self.db.cursor()
        try:
            sql = "select * from %s " % (table)
            print(sql)
            cur.execute(sql)  # 执行sql语句
            results = cur.fetchall()  # 获取查询的所有记录

            return results
        except Exception as e:
            print(e)
            self.db.rollback()
            return False
            raise e
        finally:
            self.closeDB()

    def executeSelectCondition1(self, which, table, param, value):
        self.getDB()
        cur = self.db.cursor()
        try:
            sql = "select %s from %s where %s='%s'" % (which, table, param, value)
            print(sql)
            cur.execute(sql)  # 执行sql语句
            results = cur.fetchall()  # 获取查询的所有记录

            return results
        except Exception as e:
            print("\033[1;31m{}\033[0m".format(e))
            self.db.rollback()
            return False
            raise e
        finally:
            self.closeDB()

    def executeSelectCondition2(self, which, table, param1, value1, param2, value2):
        self.getDB()
        cur = self.db.cursor()
        try:
            sql = "select %s from %s where %s='%s' and %s='%s' " % (which, table, param1, value1, param2, value2)
            print(sql)
            cur.execute(sql)  # 执行sql语句
            results = cur.fetchall()  # 获取查询的所有记录

            return results
        except Exception as e:
            self.db.rollback()
            return False
            raise e
        finally:
            self.closeDB()

    def executeUpdateSql(self, table, key, value, condKey, condValue):
        ret = False
        data = {}
        self.getDB()
        cur = self.db.cursor()
        try:
            sql = "UPDATE %s SET %s='%s' WHERE %s=%s" % (table, key, value, condKey, condValue)

            print(sql)
            cur.execute(sql)  # 执行sql语句
            self.db.commit()
            ret = True
        except Exception as e:
            print("\033[1;31m{}\033[0m".format(e))
            self.db.rollback()
            ret = False
            raise e
        finally:
            self.closeDB()
            return ret

    def executeSomeUpdateSql(self, table, str_update_values, condKey, condValue):
        data = {}
        self.getDB()
        cur = self.db.cursor()
        try:
            sql = "UPDATE %s SET %s WHERE %s='%s' " % (table, str_update_values, condKey, condValue)

            print(sql)
            cur.execute(sql)  # 执行sql语句
            self.db.commit()
            return True
        except Exception as e:
            print("\033[1;31m{}\033[0m".format(e))
            self.db.rollback()
            return False
            raise e
        finally:
            self.closeDB()

    def executeInsertSql(self, table, pattern, value):
        self.getDB()
        cur = self.db.cursor()
        try:
            sql = "insert into %s (%s)values(%s)" % (table, pattern, value)
            print(sql)
            cur.execute(sql)  # 执行sql语句
            self.db.commit()
            return True
        except Exception as e:
            print("\033[1;31m{}\033[0m".format(e))
            self.db.rollback()
            return False
            raise e
        finally:
            self.closeDB()

    def executeDelectSql(self, sql):
        self.getDB()
        cur = self.db.cursor()

        try:
            cur.execute(sql)  # 执行sql语句

            results = cur.fetchall()  # 获取查询的所有记录

        except Exception as e:
            print("\033[1;31m{}\033[0m".format(e))
            raise e
        finally:
            self.closeDB()
            return results


if __name__ == '__main__':
    sqloper = SQLOper()
    sql = sqloper.executeSql("select count(*) from tbl_usr")
