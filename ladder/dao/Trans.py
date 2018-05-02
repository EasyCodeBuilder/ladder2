
import json
import datetime

class TransDao:

    def __init__(self):
        self.table_name="tbl_trans"
        self.select_all_which="user_id,buss_no,trans_cd,trans_at,trans_day,settle_dt,curr_day,curr_balance"



    #插入新交易，同步修改余额表
    def insertTrans(self):
        # TODO


        pass



class Trans:

    def __init__(self,data={}):
        self.data = {}
        self.keys_list = ["user_id", "buss_no", "trans_cd", "trans_at", "trans_day", "settle_dt","curr_day","curr_balance"]
        self.pattern = ""
        self.value_str = ""

        self.setTrans(data)
        self.flushInsert()

    def setTrans(self,data):
        data={}
        for i in range(self.keys_list.__len__()):
            key=self.key_list[i]
            if data.__contains__(key):
                self.data[key]=data[key]

    def flushInsert(self):
        self.pattern = ""
        self.value_str = ""
        for k, v in self.data.items():
            self.pattern = "%s,%s" % (self.pattern, k)
            if isinstance(v, int):
                self.value_str = "%s,%d" % (self.value_str, v)
            else:
                self.value_str = "%s,'%s'" % (self.value_str, v)
        self.pattern = self.pattern[1:]
        self.value_str = self.value_str[1:]

def insertTrans():
    data={"user_id":"201805020002","buss_no":"20180502181423111256","trans_cd":"1002","trans_at":10,
          "trans_day":30,"settle_dt":"20180502","curr_day":30,"curr_balance":10 }

    trans=Trans(data)

    trans_dao= TransDao()
    trans_dao.insertTrans(trans)


if __name__=='__main__':

    insertTrans()
