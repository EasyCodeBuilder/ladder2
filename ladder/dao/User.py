
import json
# import SQLOper
from . import SQLOper
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
        self.tableName="tbl_usr"


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

    def insertUser2DB(self):

        if(self.paramCheck()):
            pattern="user_id,qq_no,qq_nicheng,wechat,xianyu,zhuanzhuan,real_name,phone_no"
            sqlOper = SQLOper()

            res= sqlOper.executeInsertSql(self.tableName,pattern,self.toString())

            if(res==True):
                print("insert SUCCESS")
            else:
                print("insert FAIL")


    def paramCheck(self):
        sql="select count(*) from %s"%self.tableName
        print(sql)
        sqlOper = SQLOper()
        print(sqlOper.executeSql(sql))
        return True

    def toString(self):
        str=self.userId+','+self.qqNo+','+self.qqNicheng+','+self.wechat+','+self.xianyu+','+self.zhuanzhuan+','+self.realName+','+self.phoneNo
        return str
if __name__=='__main__':

    data = '{"user_id":"0001","qq_no":"123456"}'
    d=json.loads(data)
    user=User()
    # user.insertUser(data)
    print("hello %s world %s"%(d['user_id'],d['qq_no']))

    user.paramCheck()
