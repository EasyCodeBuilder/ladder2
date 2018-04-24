
import json
from SQLOper import *

class UserDao:
    def __init__(self):
        self.tableName="tbl_usr"
        self.pattern = ""
        self.userIdcheck=False

    def countUserDB(self,settleDt):

        sql="select count(*) from %s where settle_dt= '%s' "%(self.tableName,settleDt)
        sqlOper=SQLOper()

        res=sqlOper.executeSql(sql)

        print(res)

    def insertUser2DB(self,user):
        print("insert oper")

        self.userIdCheck(user.userId)

        sqlOper = SQLOper()

        res= sqlOper.executeInsertSql(self.tableName,self.pattern,self.toString(user))

        if(res==True):
            print("insert SUCCESS")
        else:
            print("insert FAIL")

    #一个条件搜索
    def selectUserFromDBCon1(self,key,value):
        print("select oper")

        sqlOper = SQLOper()

        res= sqlOper.executeSelectCondition1(self.tableName,key,value)

        if(res!=""):
            print("select SUCCESS")
            return res
        else:
            print("select SUCCESS")

    # 两个条件搜索

    def selectUserFromDBCon1(self, key, value,key2,value2):
        print("select oper")

        sqlOper = SQLOper()

        res = sqlOper.executeSelectCondition2(self.tableName, key, value,key2,value2)

        if (res != ""):
            print("select SUCCESS")
            return res
        else:
            print("select SUCCESS")

    def userIdCheck(self,userId):
        sql="select count(*) from %s"%self.tableName
        sql2="select user_id from %s"%self.tableName
        # print(sql)
        sqlOper = SQLOper()
        # count=sqlOper.executeSql(sql)[0][0]
        userIdList=[x[0] for x in sqlOper.executeSql(sql2)]

        # print( type(self.user.userId))
        # print(type(userIdList[0]))
        if(int(userId )in userIdList):
            self.userIdValid=False
            self.pattern = "qq_no,qq_nicheng,wechat,xianyu,zhuanzhuan,real_name,phone_no"
            print("user id  no valid")

        else:
            self.pattern = "user_id,qq_no,qq_nicheng,wechat,xianyu,zhuanzhuan,real_name,phone_no"
            self.userIdValid = True
            print("user id   valid")


        # print(count)
        # print(userIdList)


    def toString(self,user):

        if(self.userIdValid):
            str="'"+user.userId+"','"+user.qqNo+"','"+user.qqNicheng+"','"+user.wechat+"','"+user.xianyu+"','"+user.zhuanzhuan+"','"+user.realName+"','"+user.phoneNo+"'"
        else:
            str="'"+user.qqNo+"','"+user.qqNicheng+"','"+user.wechat+"','"+user.xianyu+"','"+user.zhuanzhuan+"','"+user.realName+"','"+user.phoneNo+"'"
        return str

class User:
    def __init__(self):
        self.userId = ""
        self.qqNo = ""
        self.qqNicheng = ""
        self.wechat = ""
        self.xianyu = ""
        self.zhuanzhuan = ""
        self.realName = ""
        self.phoneNo = ""
        self.crtTime = ""
        self.uptTime = ""

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
    d=json.loads(data)
    user=User()
    user.userId="44"
    user.phoneNo="15242532"
    userDao=UserDao()
    # user.insertUser(data)
    print("hello %s world %s"%(d['user_id'],d['qq_no']))
    userDao.insertUser2DB(user)
    print(userDao.selectUserFromDB1("user_id",44))

