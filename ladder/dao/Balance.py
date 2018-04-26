
import json
from SQLOper import *

class BalanceDao:
    def __init__(self):
        self.tableName="tbl_balance"

        self.pattren=""

    #zidong xiugai
    def autoUpdateBalance(self):


        #TODO

        pass

    # zidong xiugai status 余额加上超期时间为0的用户
    #return 修改用户号
    def autoUpdateStatus(self):

        # TODO

        pass

    def insertTable(self):
        strValue=self.toString()
        sql="INSERT INTO tbl_balance (%s) VALUES() "%(self.pattern,strValue)
        #TODO


    def selectStop(self):
        sql= "select user_id from tbl_balance WHERE user_status=0 and server_id!=null;"



    def toString(self):

        return

class Balance:
    def __init__(self):
        self.userId=""

        pass








