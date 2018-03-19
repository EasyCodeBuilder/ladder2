
import json

class User:
    def __init__(self):
        self.userId = 0
        self.qqNo = ""
        self.qqNicheng = ""
        self.wechat = ""
        self.xianyu = ""
        self.zhuanzhuan = ""
        self.realName = ""
        self.phoneNo = ""
        self.crtTime = ""
        self.uptTime = ""

    def insertUser(self,dataStr):
        data=json.loads(dataStr)
        print(type(data))

        print(data['userId'])
        print(data['qqNo'])
        print(data.keys())

    def setUser(self,dataStr):
        data={}
        data=json.loads(dataStr)

        if(data.has_key('userId')):
            self.userId=data['userId']
        if (data.has_key('qqNo')):
            self.qqNo = data['qqNo']
        if (data.has_key('qqNicheng')):
           self.qqNicheng = data['qqNicheng']
        if(data.has_key('wechat')):
            self.wechat=data['wechat']
        if (data.has_key('xianyu')):
            self.xianyu = data['xianyu']
        if (data.has_key('zhuanzhuan')):
           self.zhuanzhuan = data['zhuanzhuan']
        if (data.has_key('realName')):
            self.realName = data['realName']
        if (data.has_key('crtTime')):
            self.crtTime = data['crtTime']
        if (data.has_key('uptTime')):
            self.uptTime = data['uptTime']

if __name__=='__main__':

    data = '{"user_id":"0001","qq_no":"123456"}'
    user=User()
    user.insertUser(data)
    print("hello world")