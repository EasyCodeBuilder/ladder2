
from ladder.lib.Logger import Logger
from ladder.lib.RetMsg import *

logger=Logger('request').getlog()

class RequestDao:

    def __init__(self):
        self.table_name="tbl_request"
        self.select_all_which="req_no,req_cd,settle_dt,req_param,res_msg"
        self.pattern = ""
        self.value_str = ""

    def insertRequset(self,request):

        sqlOper = SQLOper()
        sqlRes = sqlOper.executeInsertSql(self.table_name, request.pattern, request.value_str)

        if (sqlRes):
            logger.info("insert{:^25}SUCCESS".format(request.data['req_no']))
            ret = SUCCESS
        else:
            logger.error(" insert FAIL {}={} ".format("req_no", request.data['req_no']))
            ret = FAILURE.setRet(msg=" insert FAIL {}={} ".format("req_no", request.data['req_no']))


class Request:

    def __init__(self,data={}):
        self.data = {}
        self.keys_list = ["req_no","req_cd","settle_dt","req_param", "res_msg"]
        self.pattern = ""
        self.value_str = ""
        if data.keys().__len__ != 0:
            self.setRequestDict(data)

    def setRequestDict(self, data):
        # data={}
        for key in self.keys_list:
            if data.__contains__(key) is True :
                # logger.error(" don't have key='{}'".format(key))
                # return FAILURE.setRet(msg=" don't have key='{}'".format(key))
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


