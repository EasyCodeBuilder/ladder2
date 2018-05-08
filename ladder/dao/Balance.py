import json
from ladder.dao.SQLOper import SQLOper
from ladder.lib.RetMsg import *
from ladder.lib.Logger import Logger

logger = Logger("balance").getlog()


class BalanceDao:
    def __init__(self):
        self.table_name = "tbl_balance"
        self.select_all_which = "user_id,current_day,total_day,total_balance,over_day,server_id"
        self.pattren = ""

    # zidong xiugai
    def autoUpdateBalance(self):

        # TODO

        pass

    # zidong xiugai status 余额加上超期时间为0的用户
    # return 修改用户号
    def autoUpdateStatus(self):

        # TODO

        pass

    def countUserDB(self, user_id):

        sql = "select count(*) from %s where user_id = '%s' " % (self.table_name, user_id)
        sqlOper = SQLOper()
        count = sqlOper.executeSql(sql)
        return count[0][0]

    def insertBalance2DB(self, balance):
        logger.info("enter insertBalance2DB")
        user_id = balance.data["user_id"]

        if self.countUserDB(user_id) == 0:

            sqlOper = SQLOper()
            sqlRes = sqlOper.executeInsertSql(self.table_name, balance.pattern, balance.value_str)

            if (sqlRes):
                logger.info("insert{:^25}SUCCESS".format(user_id))
                ret = SUCCESS
            else:
                logger.error(" insert FAIL {}={} ".format("user_id", user_id))
                ret = FAILURE.setRet(msg=" insert FAIL {}={} ".format("user_id", user_id))
        else:
            logger.error("{}={} 已存在".format("user_id", user_id))
            ret = FAILURE.setRet(msg="{}={} 已存在".format("user_id", user_id))

        return ret
    def getInsertBalance2DBSql(self, balance):
        logger.info("enter insertBalance2DB")
        user_id = balance.data["user_id"]

        if self.countUserDB(user_id) == 0:

            sql = "insert into %s (%s)values(%s)" % (self.table_name, balance.pattern, balance.value_str)
            ret=SUCCESS.setRet(data={"sql":sql})
        else:
            logger.error("{}={} 已存在".format("user_id", user_id))
            ret = FAILURE.setRet(msg="{}={} 已存在".format("user_id", user_id))

        return ret

    def selectStop(self):
        sql = "select user_id from tbl_balance WHERE user_status=0 and server_id!=null;"

    def fromUserIdGetCurr(self, userId):

        sql = "select current_day,total_balance from tbl_balance"
        sqlOper = SQLOper()
        res = sqlOper.executeSql(sql)
        return res

    def toString(self):

        return

    def getBalance(self, user_id):
        data = {}

        if self.countUserDB(user_id) == 1:
            sqlOper = SQLOper()
            keys = self.select_all_which.replace(" ", "").split(",")
            res = sqlOper.executeSelectCondition1(self.select_all_which, self.table_name, "user_id", user_id)
            # balance = Balance(user_id)
            # print(res)
            for i in range(keys.__len__()):
                data.setdefault(keys[i], res[0][i])
            # print(data)
            return SUCCESS.setData(data)
        else:
            logger.error("user_id 不存在")
            return FAILURE.setRet(msg="user_id 不存在")

    def updateBalance(self, user_id, data):

        if self.countUserDB(user_id) != 1:
            logger.error("user_id 不存在")
            return FAILURE.setRet(msg="user_id 不存在")
        sqlOper = SQLOper()
        str_update = self.getUpdateStr(data)
        res = sqlOper.executeSomeUpdateSql(self.table_name, str_update, "user_id", user_id)
        if res is False:
            logger.error("update  balance  failed")
            return FAILURE.setRet(msg="update  balance  failed")
        logger.info("update user_id={} success".format(user_id))
        return SUCCESS.setRet(msg="update user_id={} success".format(user_id), data={"res":res})



    def getUpdateStr(self, data):
        if data.__len__() == 0:
            return ""
        str = ""
        for k, v in data.items():
            if k in self.select_all_which.replace(" ","").split(","):
                if isinstance(v, int):
                    str = "%s,%s='%d'" % (str, k, v)
                else:
                    str = "%s,%s='%s'" % (str, k, v)

        return str[1:]

    def selectBalance(self,which,data):
        cond = ""
        for k, v in data.items():
            cond = " %s and %s='%s' " % (cond, k, v)
        sql = "select %s from %s where 1=1 %s" % (which, self.table_name, cond)
        sqlOper = SQLOper()
        res=sqlOper.executeSql(sql)

        return res

class Balance:
    def __init__(self, user_id=""):
        self.data = {}
        self.keys_list = ["user_id", "current_day", "total_day", "total_balance", "over_day", "server_id"]

        if user_id.__len__() != 0:
            self.data.setdefault("user_id", user_id)
        self.pattern = ""
        self.value_str = ""
        self.flushInsert()

    def setBalUserId(self, user_id):
        self.data["user_id"] = user_id
        self.flushInsert()

    def setBalanceDict(self, data):
        # data={}
        for key in self.keys_list:
            if data.__contains__(key):
                self.data[key] = data[key]
        self.flushInsert()

    def flushInsert(self):
        self.pattern = ""
        self.value_str = ""
        for k, v in self.data.items():
            self.pattern = "%s,%s" % (self.pattern, k)
            if isinstance(v, int):
                self.value_str = "%s,%d" % (self.value_str, v)
            else:
                self.value_str = "%s,'%s'" % (self.value_str, v)
        self.pattern = self.pattern[1:]
        self.value_str = self.value_str[1:]


def insertBalance():
    balance_dao = BalanceDao()
    balance = Balance("201805020001")
    data = {"user_id": "201805020002", "current_day": 30, "total_balance": 10}
    balance.setBalanceDict(data)
    # data={"user_id":"201805020001"}
    # print(balance.__dict__)
    balance_dao.insertBalance2DB(balance)

    data = {}


def updateBalance():
    balance_dao = BalanceDao()
    balance = Balance()
    user_id = "201805020002"
    data = {"current_day": 180, "total_day": 180, "total_balance": 55}
    balance_dao.updateBalance(user_id, data)


def selectBalance():
    balance_dao = BalanceDao()
    data={}
    ret=balance_dao.selectBalance("user_id",data)


def getBalance():
    ret = RetMsg()
    balance_dao = BalanceDao()
    # balance = Balance("12355")
    ret = balance_dao.getBalance("201805020002")

    print(SUCCESS.getCode())
    print(ret.getCode())
    if ret.getCode() is SUCCESS.getCode():
        print(ret.data)
    else:
        print(ret)


if __name__ == '__main__':
    # insertBalance()
    # getBalance()
    # balance=Balance()
    # balance.setBalanceDict(getBalance())
    # print(balance.data)
    updateBalance()
