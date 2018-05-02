from ladder.dao.SQLOper import *


class CheckData:
    def __init__(self):
        self.user_tbl = "tbl_user"
        self.unique_check = True
        self.input_check = True
        self.un_unique_key = ""

    # 字典中的值 是否在数据库中唯一
    def uniqueUserCheck(self, dict, key):

        if self.unique_check is False:
            return self

        if  dict.get(key,"").strip().__len__() != 0:
            sql = "select count(*) from %s where %s='%s'" % (self.user_tbl, key, dict.get(key))
            # print(sql)
            sqlOper = SQLOper()
            count = sqlOper.executeSql(sql)[0][0]
            # print(count)
            if count > 0:
                # print("Checking %s=%s is not only" % (key, dict.get(key)))
                self.un_unique_key = key
                self.unique_check = False
            else:
                # print("Checking %s=%s is only one" % (key,dict.get(key)))
                self.unique_check = True

        return self

    def inputCheck(self, key, value):

        if self.input_check & (value.strip() != ""):
            pass
            # TODO

        return self


if __name__ == '__main__':
    c = CheckData()
    data = {"user_id": "201804270004", "qq_no": "978611111", "wechat_no": "123"}

    c.uniqueUserCheck(data, "user_id").uniqueUserCheck(data, "qq_no")
    print(c.unique_check)
