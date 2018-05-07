from ladder.lib.Logger import Logger
from ladder.dao.include import *

logger = Logger("register").getlog()


class Register:
    def __init__(self, data):
        self.data = {}
        self.data.update(data)
        self.user_list = ["user_id", "nike_name", "qq_no", "qq_name", "wechat_no",
                          "wechat_name", "phone_no", "user_status", "password", "settle_dt"]
        self.req_list = ["trans_cd", "buss_no", "settle_dt"]
        self.rsp_list = []
        self.rsp_data = {}
        self.user_id = ""
        self.user = User()
        self.user_dao = UserDao()
        self.balance_dao = BalanceDao()
        self.balance = Balance()

    def checkParam(self):

        if (self.data.get("qq_no", "") + self.data.get("wechat_no", "")).__len__() == 0:
            msg = "qq号 与 微信号 都不存在"
            logger.error(msg)
            return FAILURE.setRet(msg=msg)
        for key in self.req_list:
            if self.data.__contains__(key) is False:
                msg=" register 参数检查失败"
                logger.error(msg)
                return FAILURE.setRet(msg=msg)
        return SUCCESS

    def process(self):

        ret = self.checkParam()
        if ret.getCode() !=  SUCCESS.getCode():
            logger.error("param is wrong ")
            self.setReturn(ret)
            return ret.setRet(data=self.rsp_data)

        ret = self.localProcess()
        if ret.getCode() != SUCCESS.getCode():
            logger.error("processing  Done ")
            self.setReturn(ret)
            return ret.setRet(data=self.rsp_data)
        msg="注册成功"
        self.setReturn(SUCCESS.setRet(msg=msg,data=self.rsp_data))

        return SUCCESS.setRet(msg=msg,data=self.rsp_data)

    def localProcess(self):

        ret = self.register()
        if ret.getCode() != SUCCESS.getCode():
            logger.error("register  failed ")
            print("111"+ret.msg)
            return ret
            # return FAILURE.setRet(msg="register  failed")
        return SUCCESS
        # self.rsp_data.update(trans_cd=self.data.get("trans_cd"))
        # self.rsp_data.update(buss_no=self.data.get("buss_no"))
        # self.rsp_data.update(resp_no=ret.getCode())
        # self.rsp_data.update(resp_msg=ret.msg)
        # self.rsp_data.update(ret.data)
        # # print("self.rsp_data2={}".format(self.rsp_data))
        # return True

    def addUser(self):
        # settle_dt = datetime.datetime.now().strftime('%Y%m%d')
        # data.update(settle_dt=settle_dt)
        user_data = {}
        settle_dt = self.data.get("settle_dt")
        count = self.user_dao.countUserDB(settle_dt)
        if isinstance(count, int) is False:
            msg = "db select failed"
            logger.error(msg)
            return FAILURE.setRet(msg=msg)
        user_id = "%s%04d" % (settle_dt, int(count) + 1)
        user_data.update(user_id=user_id)

        for key in self.user_list:
            if self.data.__contains__(key):
                user_data[key] = self.data[key]

        self.user.setUser(user_data)

        res = self.user_dao.insertUser2DB(self.user)
        if res.getCode() != SUCCESS.getCode():
            print("222"+res.msg)
            return res
        self.user_id = user_id
        return SUCCESS.setData({"user_id": user_id})

    def setReturn(self,ret):

        self.rsp_data.update(trans_cd=self.data.get("trans_cd"))
        self.rsp_data.update(buss_no=self.data.get("buss_no"))
        self.rsp_data.update(resp_no=ret.getCode())
        self.rsp_data.update(resp_msg=ret.msg)
        self.rsp_data.update(ret.data)

    def openAccount(self):

        data = {}
        data.update(user_id=self.user_id)
        self.balance.setBalanceDict(data)
        ret = self.balance_dao.insertBalance2DB(self.balance)
        if ret.getCode() is SUCCESS.getCode():
            return SUCCESS
        else:
            msg = " open account failed"
            return ret.setRet(msg=msg)

    def register(self):
        """
        register a member
        :param data: save the user information
        :return:
        """
        ret = self.addUser()
        if ret.getCode() != SUCCESS.getCode():
            return ret
        ret = self.openAccount()
        if ret.getCode() != SUCCESS.getCode():
            return ret

        logger.info(" register success !! ")
        return SUCCESS.setRet(data={"user_id": self.user_id})
