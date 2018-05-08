class RetMsg:
    def __init__(self, code="", msg="", data={}):
        """

        :rtype: object
        """
        self.code = code
        self.msg = msg
        self.data = {}
        self.copyDict(data)

    def setData(self, data):

        return RetMsg(self.code,self.msg,data)

    def setMsg(self, msg):

        return RetMsg(self.code, msg, self.data)
    def setCode(self, code):

        return RetMsg(code, self.msg, self.data)

    def getCode(self):
        return self.code

    def getMsg(self):
        return self.msg

    def getData(self):
        return self.data

    def copyDict(self,data={}):
        self.data={}
        for k,v in data.items():
            # print("{}={}".format(k,v))
            self.data[k]=v


SUCCESS = RetMsg("0000", "SUCCESS")
FAILURE = RetMsg("9999", "FAILURE")
