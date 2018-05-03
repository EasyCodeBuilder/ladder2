import datetime

from ladder.dao.include import *
from ladder.lib.Logger import Logger

logger = Logger("task").getlog()


def addUser(data):
    settle_dt = datetime.datetime.now().strftime('%Y%m%d')
    data.update(settle_dt=settle_dt)

    user = User()
    user_dao = UserDao()
    count = user_dao.countUserDB(settle_dt)
    user_id = "%s%04d" % (settle_dt, int(count) + 1)
    data.update(user_id=user_id)

    user.setUser(data)

    user_dao.insertUser2DB(user)

    return user_id


def openAccount(user_id):
    balance_dao = BalanceDao()
    balance = Balance()
    data = {}
    data.update(user_id=user_id)
    balance.setBalanceDict(data)
    balance_dao.insertBalance2DB(balance)


def register():
    data = {"wechat_no": "goodkkk", "wechat_name": "weeee", "qq_name": "qq_name1"}
    user_id = addUser(data)
    openAccount(user_id)
    logger.info(" register success !! ")


def addTrans(user_id, trans_at, trans_day,trans_cd):
    data_trans = {}

    settle_dt = datetime.datetime.now().strftime('%Y%m%d')
    buss_no = datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')

    data_trans.update(user_id=user_id)
    data_trans.update(trans_day=trans_day)
    data_trans.update(trans_at=trans_at)
    data_trans.update(trans_cd=trans_cd)
    data_trans.update(settle_dt=settle_dt)
    data_trans.update(buss_no=buss_no)

    trans = Trans()
    trans_dao = TransDao()
    balance = Balance()
    balance_dao = BalanceDao()

    ret = balance_dao.getBalance(user_id)
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
    trans.setTrans(data_trans)
    ret = trans_dao.insertTrans(trans)
    if ret.getCode() != SUCCESS.getCode():
        logger.error("non exist user_id={}".format(user_id))
        return FAILURE.setRet(data="non exist user_id={}".format(user_id))

    logger.info("change_balance={}".format(change_balance))
    return SUCCESS.setData(change_balance)


def chargeAccount(user_id, trans_at, trans_day,trans_cd):
    # data_trans = {}
    # data_balance = {}
    #
    # trans_cd = "1002"
    # settle_dt = datetime.datetime.now().strftime('%Y%m%d')
    # buss_no=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')
    #
    # data_trans.update(user_id=user_id)
    # data_trans.update(trans_day=trans_day)
    # data_trans.update(trans_at=trans_at)
    # data_trans.update(trans_cd=trans_cd)
    # data_trans.update(settle_dt=settle_dt)
    # data_trans.update(buss_no=buss_no)

    trans = Trans()
    trans_dao = TransDao()
    balance = Balance()
    balance_dao = BalanceDao()

    # ret = balance_dao.getBalance(user_id)
    # if ret.getCode() != SUCCESS.getCode():
    #     logger.error("non exist user_id={}".format(user_id))
    #     return FAILURE.setRet(data="non exist user_id={}".format(user_id))
    # # user_balance.update(ret.data)
    # data_balance.update(ret.data)
    # change_balance={}
    # change_balance["current_day"]=int(data_balance["current_day"])+int(trans_day)
    # change_balance["total_day"]=int(data_balance["total_day"])+int(trans_day)
    # change_balance["total_balance"]=int(data_balance["total_balance"])+int(trans_at)
    #
    # curr_day= change_balance["current_day"]
    # curr_balance=change_balance["total_balance"]
    # data_trans.update(curr_day=curr_day)
    # data_trans.update(curr_balance=curr_balance)
    # print("data_trans{}".format(data_trans))
    # trans.setTrans(data_trans)
    # ret=trans_dao.insertTrans(trans)

    ret = addTrans(user_id, trans_at, trans_day,trans_cd)
    if ret.getCode() != SUCCESS.getCode():
        logger.error("add trans Filed user_id={}".format(user_id))
        return FAILURE.setRet(msg="add trans Filed user_id={}".format(user_id))
    logger.info("user_id={} add trans success".format(user_id))
    # balance.setBalanceDict(change_balance)
    # print("ret.data={}".format(ret.data))
    ret = balance_dao.updateBalance(user_id, ret.data)
    if ret.getCode() != SUCCESS.getCode():
        logger.error("update Balance Failed user_id={},che xiao charu Trans".format(user_id))
        trans_at= 0-int(trans_at)
        trans_day= 0-int(trans_day)
        trans_cd="2003"
        ret = addTrans(user_id, trans_at, trans_day,trans_cd)
        if ret.getCode() != SUCCESS.getCode():
            logger.error(" user_id={} rollback failed".format(user_id))
            return FAILURE.setRet(msg=" user_id={} rollback failed".format(user_id))

        logger.error("user_id={},rollback success".format(user_id))
        return FAILURE.setRet(msg="user_id={},rollback success".format(user_id))

    logger.info("charge user_id={} success".format(user_id))


if __name__ == "__main__":
    # register()

    user_id = "201805020002"
    trans_at = 10
    trans_day = 30
    trans_cd="2001"

    chargeAccount(user_id, trans_at, trans_day,trans_cd)
