
from ladder.dao.Trans import *
from ladder.dao.Balance import *

def dailyWork():

#1查询余额表，设置天数减一

    balance     =Balance()
    balanceDao  =BalanceDao()

    res=balanceDao.selectBalance("user_id",{})


    if(res==False):
        print("daily work 1 faild")
        return


#2余额天数为<0的，设置用户状态为0

    res = balanceDao.autoUpdateStatus()

    if (res == False):
        print("daily work 1 faild")
        return


#3状态为0的用户，删除 端口与密码

    #（1）查询出待修改服务器ID
    res=balanceDao.select







