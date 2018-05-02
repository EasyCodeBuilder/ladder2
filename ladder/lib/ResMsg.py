from .Const import *



class ResMsg:
    def __init__(self,respCode,respMsg):
        self.respCode=respCode
        self.respMsg=respMsg






Const.respSUCCESS=ResMsg("0000","成功")
Const.respFAIL=ResMsg("9999","未知异常")