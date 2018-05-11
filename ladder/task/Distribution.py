from ladder.dao.include import *
from ladder.lib.include import *
from ladder.task.include import *


logger=Logger("distri").getlog()


class Distribution:

    def __init__(self):

        pass
    def destribution(self,data):
        trans_cd = data.get("trans_cd")
        res=RetMsg("9900","没有此类交易")
        if trans_cd is "1001":
            logger.info("start register ")
            res = Register(data).process()
            if res.getCode() is SUCCESS.getCode():
                logger.info("charge success")

        if trans_cd is "2001":
            logger.info("start charge")
            res = Charge(data).process()
            if res.getCode() is SUCCESS.getCode():
                logger.info("charge success")
        # 返回结果
        logger.info("返回参数：{}".format(res.data))
        return res




