import datetime

from ladder.dao.include import *
from ladder.lib.Logger import Logger

logger=Logger("task").getlog()

def addUser(data):


    settle_dt = datetime.datetime.now().strftime('%Y%m%d')
    data.update(settle_dt=settle_dt)

    user = User()
    user_dao = UserDao()
    count=user_dao.countUserDB(settle_dt)
    user_id="%s%04d" % (settle_dt, int(count) + 1)
    data.update(user_id=user_id)

    user.setUser(data)

    user_dao.insertUser2DB(user)

    return user_id


def openAccount(user_id):

    balance_dao = BalanceDao()
    balance = Balance()
    data={}
    data.update(user_id=user_id)
    balance.setBalanceDict(data)
    balance_dao.insertBalance2DB(balance)


def register():

    data = {"wechat_no": "goodkkk", "wechat_name": "weeee", "qq_name": "qq_name1"}
    user_id=addUser(data)
    openAccount(user_id)
    logger.info(" register success !! ")

if __name__=="__main__":
    register()