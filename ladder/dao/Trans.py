
import json
import datetime

class TransDao:

    def __init__(self):

        pass



    #插入新交易，同步修改余额表
    def insertTrans(self):
        # TODO


        pass



class Trans:

    def __init__(self,userId,bussNo,transCd,transAt,transDate):
        self.userId=userId
        self.bussNo=bussNo
        self.transCd=transCd
        self.transAt=transAt
        self.transDate=transDate
        self.settleDt=datetime.datetime.now().strftime('%Y%m%d')
        self.currDate=""
        self.currBalance=""




    def setCurrentDetail(self):

