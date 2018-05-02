import datetime
import json
from SQLOper import *
from ladder.lib.CheckData import CheckData
from ladder.lib.Logger import Logger

logger=Logger().getlog()

class UserDao:
    def __init__(self):
        self.table_name = "tbl_user"
        self.pattern = ""
        self.unique_check = False
        self.check = CheckData()

    def countUserDB(self, settleDt):

        sql = "select count(*) from %s where settle_dt= '%s' " % (self.table_name, settleDt)
        sqlOper = SQLOper()
        count = sqlOper.executeSql(sql)
        return count[0][0]

    def insertUser2DB(self, user):
        print("insert oper")
        # print("AAA"+user.data.get("wechat_no","")+user.data.get("qq_no",""))
        if (user.data.get("wechat_no","")+user.data.get("qq_no","")).strip().__len__() == 0:
            # print("qq号, 微信号 不同时为空")
            logger.error("qq号, 微信号 不同时为空")
            return
        checkRes = self.check.uniqueUserCheck(user.data, "user_id").uniqueUserCheck(user.data, "qq_no").uniqueUserCheck(
            user.data, "wechat_no").unique_check
        if (checkRes == False):
            logger.error("{}含有重复数据，请确认后输入".format(self.check.un_unique_key))
            return
        sqlOper = SQLOper()
        sqlRes = sqlOper.executeInsertSql(self.table_name, user.pattern, user.value_str)

        if (sqlRes):
            logger.info("insert SUCCESS")
        else:
            logger.info("insert FAIL")

    # 一个条件搜索
    def selectUserFromDBCon1(self, which, key, value):
        print("select oper")

        sqlOper = SQLOper()

        res = sqlOper.executeSelectCondition1(which, self.table_name, key, value)

        if (res != ""):
            logger.info("select SUCCESS")
            return res
        else:
            logger.info("select FAIL")

    # 两个条件搜索

    def selectUserFromDBCon2(self, which, key, value, key2, value2):
        logger.info("select oper")

        sqlOper = SQLOper()

        res = sqlOper.executeSelectCondition2(which, self.table_name, key, value, key2, value2)

        if res != "":
            print("select SUCCESS")
            return res
        else:
            print("select FAIL")

    def uniqueCheck(self, key, value):
        sql = "select count(*) from %s where %s=%s" % (self.table_name, key, value)
        # print(sql)
        sqlOper = SQLOper()
        count = sqlOper.executeSql(sql)[0][0]
        if count > 0:
            logger.info("%s=%s is not only" % (key, value))
            self.unique_check = False
        else:
            logger.info("%s=%s is only" % (key, value))
            self.unique_check = True
        return self


class User:
    def __init__(self):
        self.pattern = ""
        self.value_str = ""
        self.data = dict()

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def checkData(self, data):
        # TODO 参数格式检查，防sql注入
        data.get("")
        return True

    def setUser(self, data):
        self.data = data
        res = self.checkData(data)
        if res is False:
            logger.error("参数错误")
            return
        for k, v in data.items():
            self.pattern = "%s,%s" % (self.pattern, k)
            if isinstance(v, int):
                self.value_str = "%s,%d" % (self.value_str, v)
            else:
                self.value_str = "%s,'%s'" % (self.value_str, v)
        self.pattern = self.pattern[1:]
        self.value_str = self.value_str[1:]


def insertUser():
    user = User()
    user_dao = UserDao()

    data = {"wechat_no": "lyk11111", "wechat_name":"weeee","qq_name": "qq_name1"}
    # d=json.loads(data)

    settle_dt = datetime.datetime.now().strftime('%Y%m%d')
    print("settle_dt=" + settle_dt)
    res = user_dao.countUserDB(settle_dt)
    print(res)
    user_id = "%s%04d" % (settle_dt, int(res) + 1)
    print("user_id=%s" % user_id)

    data["settle_dt"] = settle_dt
    data["user_id"] = user_id
    user.setUser(data)

    # print(user.pattern)
    # print(user.value_str)
    user_dao.insertUser2DB(user)


def selectUser():
    user_dao = UserDao()
    which = "user_id,settle_dt,wechat_no,wechat_name,qq_no,qq_name"
    res = user_dao.selectUserFromDBCon1(which, "qq_no", "978611111")

    print(res)


if __name__ == '__main__':
    # selectUser()
    insertUser()
