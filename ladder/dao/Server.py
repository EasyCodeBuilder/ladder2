import json
from random import Random

from ladder.dao.SQLOper import SQLOper
from ladder.lib.RetMsg import *
from ladder.lib.Logger import Logger

logger = Logger("server").getlog()


class ServerDao:
    def __init__(self):
        self.table_name = "tbl_server"
        self.select_all_which = "server_id,port,password,server_status"

    def countUserDB(self, server_id):

        sql = "select count(*) from %s where server_id = '%s' " % (self.table_name, server_id)
        sqlOper = SQLOper()
        count = sqlOper.executeSql(sql)
        return count[0][0]

    def insertServer2DB(self, server):
        logger.info("enter insertBalance2DB")
        server_id = server.data["server_id"]

        if self.countUserDB(server_id) == 0:

            sqlOper = SQLOper()
            sqlRes = sqlOper.executeInsertSql(self.table_name, server.pattern, server.value_str)

            if (sqlRes):
                logger.info("insert{:^25}SUCCESS".format(server_id))
                ret = SUCCESS
            else:
                logger.error(" insert FAIL {}={} ".format("server_id", server_id))
                ret = FAILURE.setRet(msg=" insert FAIL {}={} ".format("server_id", server_id))
        else:
            logger.error("{}={} 已存在".format("server_id", server_id))
            ret = FAILURE.setRet(msg="{}={} 已存在".format("server_id", server_id))

        return ret

    def getServer(self, server_id):
        data = {}

        if self.countUserDB(server_id) == 1:
            sqlOper = SQLOper()
            keys = self.select_all_which.replace(" ", "").split(",")
            res = sqlOper.executeSelectCondition1(self.select_all_which, self.table_name, "server_id", server_id)
            # balance = Balance(user_id)
            print(res)
            for i in range(keys.__len__()):
                data.setdefault(keys[i], res[0][i])
            print(data)
            return SUCCESS.setData(data)
        else:
            logger.error("user_id 不存在")
            return FAILURE.setRet(msg="user_id 不存在")

    def updateServer(self, server_id, data):

        if self.countUserDB(server_id) == 1:
            sqlOper = SQLOper()
            str_update = self.getUpdateStr(data)
            res = sqlOper.executeSomeUpdateSql(self.table_name, str_update, "server_id", server_id)
            logger.info("update server_id={} success".format(server_id))
            return SUCCESS.setRet(msg="update server_id={} success".format(server_id), data={"res", res})
        else:
            logger.error("user_id 不存在")
            return FAILURE.setRet(msg="user_id 不存在")

    def getUpdateStr(self, data):
        if data.__len__() == 0:
            return ""
        str = ""
        for k, v in data.items():
            if isinstance(v, int):
                str = "%s,%s='%d'" % (str, k, v)
            else:
                str = "%s,%s='%s'" % (str, k, v)

        return str[1:]
    def selectServer(self,which,data):
        cond = ""
        for k, v in data.items():
            cond = " %s and %s='%s' " % (cond, k, v)
        sql = "select %s from %s where 1=1 %s" % (which, self.table_name, cond)
        sqlOper = SQLOper()
        res=sqlOper.executeSql(sql)

        return res


class Server:
    def __init__(self):
        self.data = {}
        self.keys_list = ["server_id", "port", "password", "server_status"]
        self.pattern = ""
        self.value_str = ""
        self.flushInsert()

    def setServerDict(self, data):
        # data={}
        for key in self.keys_list:
            if data.__contains__(key) is False:
                logger.error(" don't have key='{}'".format(key))
                return FAILURE.setRet(msg=" don't have key='{}'".format(key))
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

    def changeServerPassword(self,server_id):
        data={}
        rand=Random()
        password=
        self.updateServer(server_id, data)


def insertServer():
    server_dao = ServerDao()
    server = Server()
    data = {"server_id": "10120120325265545", "port": "66545", "password": "PLOKIJKLKK", "server_status": "1"}
    server.setServerDict(data)
    # data={"user_id":"201805020001"}
    # print(balance.__dict__)
    server_dao.insertServer2DB(server)


def updateServer():
    server_dao = ServerDao()
    server = Server()
    server_id = "201805020002"
    data = {"port": 65225, "total_day": 180, "total_balance": 55}
    server_dao.updateServer(server_id, data)


def selectServer():
    server_dao = ServerDao()
    server = Server()

    # ret=balance_dao.


def getServer():
    ret = RetMsg()
    server_dao = ServerDao()
    server_id = ""
    ret = server_dao.getServer(server_id)

    print(SUCCESS.getCode())
    print(ret.getCode())
    if ret.getCode() is SUCCESS.getCode():
        print(ret.data)
    else:
        print(ret)


if __name__ == '__main__':
    # insertServer()
    # getBalance()
    # balance=Balance()
    # balance.setBalanceDict(getBalance())
    # print(balance.data)
    # updateServer()
    rand=Random()
    print(rand.randint(10,15))