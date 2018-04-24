
import json

class TransDao:

    def __init__(self):

        pass



    #插入新交易，同步修改余额表
    def insertTrans(self):
        # TODO


        pass



class Trans:

    def __init__(self):
        self.transId=""
        self.userId=""
        self.during=30
        self.serverId=""
        self.acct=0
        self.crtTime=""
        self.uptTime=""

    #dataStr="{'xxx':'123','aaa':'334'}"
    def setTrans(self, dataStr):
        data = {}
        data = json.loads(dataStr)

        if (data.has_key('transId')):
            self.transId = data['transId']
        if (data.has_key('userId')):
            self.userId = data['userId']
        if (data.has_key('during')):
            self.during = data['during']
        if (data.has_key('serverId')):
            self.serverId = data['serverId']
        if (data.has_key('acct')):
            self.acct = data['acct']
        if (data.has_key('crtTime')):
            self.crtTime = data['crtTime']
        if (data.has_key('uptTime')):
            self.uptTime = data['uptTime']