import json
import datetime
from ladder.dao.SQLOper import SQLOper
from ladder.lib.Logger import Logger
from ladder.lib.RetMsg import *

logger = Logger("trans").getlog()

class TransDao:
    """
     operation the tbl_trans table
    """

    def __init__(self):
        self.table_name = "tbl_trans"
        self.select_all_which = "user_id,buss_no,trans_cd,trans_at,trans_day,settle_dt,curr_day,curr_balance"

    # 插入新交易，同步修改余额表
    def insertTrans(self, trans):
        logger.info("enter")
        user_id=trans.data["user_id"]
        trans_cd=trans.data["trans_cd"]

        sqlOper = SQLOper()
        sqlRes = sqlOper.executeInsertSql(self.table_name, trans.pattern, trans.value_str)
        if (sqlRes):
            logger.info("insert user_id={},trans_cd={} SUCCESS".format(user_id,trans_cd))
            return SUCCESS.setRet(msg="insert user_id={},trans_cd={} SUCCESS".format(user_id,trans_cd))
        else:
            logger.error(" insert FAILURE {}={} ".format("user_id", user_id))
            return FAILURE.setRet(msg=" insert FAIL {}={} ".format("user_id", user_id))

    def getTrans(self,data):
        logger.info("enter")
        cond=""
        for k,v in data.items():
            cond=" %s and %s='%s' "%(cond,k,v)
        sql="select %s from %s where 1=1 %s"%(self.select_all_which,self.table_name,cond)
        sqlOper = SQLOper()
        res=sqlOper.executeSql(sql)

        return res


class Trans:
    def __init__(self, data={}):
        self.data = {}
        self.keys_list = ["user_id", "buss_no", "trans_cd", "trans_at", "trans_day", "settle_dt", "curr_day",
                          "curr_balance"]
        self.pattern = ""
        self.value_str = ""

        self.setTrans(data)
        self.flushInsert()

    def setTrans(self, data):
        for i in range(self.keys_list.__len__()):
            key = self.keys_list[i]
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


def insertTrans():
    data = {"user_id": "201805020002", "trans_cd": "1002", "trans_at": 10,
            "trans_day": 30, "settle_dt": "20180502", "curr_day": 30, "curr_balance": 10}
    buss_no=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    # print(buss_no.__str__())
    data.update(buss_no=buss_no)
    print(data)
    # print(buss_n)
    trans = Trans(data)

    trans_dao = TransDao()
    trans_dao.insertTrans(trans)


def selectTrans():
    data = {"user_id": "201805020002"}

    trans_dao = TransDao()
    res= trans_dao.getTrans(data)

    for i in range(res.__len__()):
        value=res[i]
        print(value)


if __name__ == '__main__':
    # insertTrans()
    selectTrans()