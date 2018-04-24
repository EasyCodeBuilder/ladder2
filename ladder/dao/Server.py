
import json

class ServerDao:

    def __init__(self):

        pass


    # 同步数据库与服务器上记录密码
    def checkPassword(self):
        # TODO
        pass


    #修改过期的密码
    def updatePassword(self):
        # TODO
        pass

    #插入新主机
    def insertNewServer(self):
        # TODO


        pass


class Server:

    def __init__(self):
        self.serverId=""
        self.ip=""
        self.port=""
        self.key=""
        self.used=False
        self.crtTime=""
        self.uptTime=""

#dataStr="{'xxx':'123','aaa':'334'}"
    def setServer(self, dataStr):
        data = {}
        data = json.loads(dataStr)

        if (data.has_key('serverId')):
            self.serverId = data['serverId']
        if (data.has_key('ip')):
            self.ip = data['ip']
        if (data.has_key('port')):
            self.port = data['port']
        if (data.has_key('key')):
            self.key = data['key']
        if (data.has_key('used')):
            self.used = data['used']
        if (data.has_key('crtTime')):
            self.crtTime = data['crtTime']
        if (data.has_key('uptTime')):
            self.uptTime = data['uptTime']
