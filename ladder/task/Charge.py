from ladder.lib.Logger import Logger
from ladder.dao.include import *
logger=Logger("charge module").getlog()
class Charge:
    """
    charge interface
    """
    def __init__(self,data):
        self.data={}
        self.data.update(data)
        self.req_list=["user_id","trans_cd","buss_no","settle_dt","trans_at","trans_day"]
        self.rsp_list=["trans_cd","buss_no","settle_dt","resp_no","resp_msg","user_id","current_day","total_balance"]
        self.rsp_data={}
        self.trans = Trans()
        self.trans_dao = TransDao()
        self.balance = Balance()
        self.balance_dao = BalanceDao()
        self.user_dao = UserDao()


    def checkParam(self):

        for key in self.req_list:
            if self.data.__contains__(key) is False:
                return False
        return True


    def process(self):

        ret=self.checkParam()
        if ret is False:
            logger.error("param is wrong ")
            return FAILURE.setRet(msg="param is wrong")

        ret=self.localProcess()
        if ret is False:
            logger.error("processing  failed ")
            return FAILURE.setRet(msg="processing  failed")
        # print("self.rsp_data={}".format(self.rsp_data))
        return SUCCESS.setData(self.rsp_data)

    def localProcess(self):

        ret =self.chargeAccount()
        if ret.getCode() != SUCCESS.getCode():
            logger.error("chargeAccount  failed ")
            return FAILURE.setRet(msg="chargeAccount  failed")

        self.rsp_data.update(trans_cd=self.data.get("trans_cd"))
        self.rsp_data.update(buss_no=self.data.get("buss_no"))
        self.rsp_data.update(resp_no=ret.getCode())
        self.rsp_data.update(resp_msg=ret.msg)
        self.rsp_data.update(ret.data)
        # print("self.rsp_data2={}".format(self.rsp_data))
        return True


    def addTrans(self,user_id, trans_at, trans_day, trans_cd,settle_dt,buss_no):
        """
        add a new trans item
        :param user_id: 用户号
        :param trans_at: 交易金额
        :param trans_day: 交易时间
        :param trans_cd: 交易类型
        :return:
        """
        data_trans = {}

        # settle_dt = datetime.datetime.now().strftime('%Y%m%d')
        # buss_no = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

        data_trans.update(user_id=user_id)
        data_trans.update(trans_day=trans_day)
        data_trans.update(trans_at=trans_at)
        data_trans.update(trans_cd=trans_cd)
        data_trans.update(settle_dt=settle_dt)
        data_trans.update(buss_no=buss_no)

        ret = self.balance_dao.getBalance(user_id)
        if ret.getCode() != SUCCESS.getCode():
            logger.error("non exist user_id={}".format(user_id))
            return FAILURE.setRet(msg="non exist user_id={}".format(user_id))

        change_balance = {}
        change_balance["current_day"] = int(ret.data["current_day"]) + int(trans_day)
        change_balance["total_day"] = int(ret.data["total_day"]) + int(trans_day)
        change_balance["total_balance"] = int(ret.data["total_balance"]) + int(trans_at)

        curr_day = change_balance["current_day"]
        curr_balance = change_balance["total_balance"]

        data_trans.update(curr_day=curr_day)
        data_trans.update(curr_balance=curr_balance)
        self.trans.setTrans(data_trans)
        ret = self.trans_dao.insertTrans(self.trans)
        if ret.getCode() != SUCCESS.getCode():
            logger.error("non exist user_id={}".format(user_id))
            return FAILURE.setRet(data="non exist user_id={}".format(user_id))

        ret = self.user_dao.updateUserAttr("user_status", "1", user_id)
        logger.info("change_balance={}".format(change_balance))
        return SUCCESS.setData(change_balance)

    def chargeAccount(self):

        user_id     = self.data.get("user_id")
        trans_at    = self.data.get("trans_at")
        trans_day   = self.data.get("trans_day")
        trans_cd    = self.data.get("trans_cd")
        settle_dt   = self.data.get("settle_dt")
        buss_no     = self.data.get("buss_no")

        ret = self.addTrans(user_id, trans_at, trans_day, trans_cd,settle_dt,buss_no)
        if ret.getCode() != SUCCESS.getCode():
            logger.error("add trans Filed user_id={}".format(user_id))
            return FAILURE.setRet(msg="add trans Filed user_id={}".format(user_id))
        current_day = ret.data.get("current_day")
        total_balance = ret.data.get("total_balance")
        logger.info("user_id={} add trans success".format(user_id))
        # balance.setBalanceDict(change_balance)
        # print("ret.data={}".format(ret.data))
        ret = self.balance_dao.updateBalance(user_id, ret.data)
        if ret.getCode() != SUCCESS.getCode():
            logger.error("update Balance Failed user_id={},che xiao charu Trans".format(user_id))
            trans_at = 0 - int(trans_at)
            trans_day = 0 - int(trans_day)
            trans_cd = "2003"
            ret = self.addTrans(user_id, trans_at, trans_day, trans_cd,settle_dt,buss_no)
            if ret.getCode() != SUCCESS.getCode():
                logger.error(" user_id={} rollback failed".format(user_id))
                return FAILURE.setRet(msg=" user_id={} rollback failed".format(user_id))

            logger.error("user_id={},rollback success".format(user_id))
            return FAILURE.setRet(msg="user_id={},rollback success".format(user_id))
        res_data = {}
        res_data.update(user_id=user_id)
        res_data.update(current_day=current_day)
        res_data.update(total_balance=total_balance)

        logger.info("charge user_id={} success".format(user_id))
        return SUCCESS.setData(res_data)




