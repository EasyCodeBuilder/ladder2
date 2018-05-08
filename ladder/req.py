from datetime import datetime
from urllib import parse, request

import json


def displayRes(list):
    for i in range(len(list)):
        print(list[i])


def reqPOST(url, data):
    # sData=parse.urlencode(data).encode("utf-8")

    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}
    req = request.Request(url=url, data=bytes(json.dumps(data), encoding="utf-8"), headers=header_dict)
    # print(req)
    res = request.urlopen(req)
    res = res.read().decode("utf-8")
    # print(res)
    return res
    # print(res.decode(encoding='utf-8'))


def reqGET(url, data):
    postfix = "?"
    url = url +postfix+ parse.urlencode(data)
    print(url)
    req = request.Request(url);

    res_data = request.urlopen(req);

    res = res_data.read().decode('utf8')
    return eval(res)
    # print(res)


def run():
    data = {"adminAccount": "root", "adminPassword": "OStem@00"}
    # url="http://member.3efang.com/Login.php"
    # data={"uid":"121212","upass":"111111","Submit":"提 交"}
    # reqPOST(url,data)
    # reqGET(url,data)

    # createAdmin={"adminAccount":"root","adminPassword":"OStem@00","adminName":"aras","adminPhone":"13500001111"}
    # createAdminUrl="http://127.0.0.1:3000/admin"
    #
    # reqPOST(createAdminUrl,createAdmin)



    # resJson=json.loads(res)
    #
    #
    #
    # print(type(resJson['result']))
    # # print(resJson['result'])
    # displayRes(resJson['result'])

    checkurl = "https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxb6a454852c62b7e0&redirect_uri=http%3A%2F%2Foauth.youtoupiao.com%2Fauthorize%2Fauthorize.html%3Fjump%3Dhttp%3A%2F%2Fme0cb28c7f4cd194c.wxvote.youtoupiao.com%2Fpage%2Fshow%2Fid%2F7dc9ba75e1b7bbec.html%3Fiiid%3D1524185209036177000&response_type=code&scope=snsapi_userinfo&state=9080be1269ea12d23f53a2016bb4ec3c#wechat_redirect"
    data = {}
    reqGET(checkurl, data)


def run2():
    url = "http://127.0.0.1:8000/"
    res = reqGET(url, {})
    for k, v in res.items():
        print("{}={}".format(k, v))


def register():
    data = {}
    send_data = {}
    trans_cd = "1001"
    settle_dt = datetime.now().strftime('%Y%m%d')
    buss_no = datetime.now().strftime('%Y%m%d%H%M%S%f')

    data.update(trans_cd=trans_cd)
    data.update(buss_no=buss_no)
    data.update(settle_dt=settle_dt)

    data_body = {"qq_name": "qwerft","wechat_no":"123"}

    data.update(data_body)
    send_data.update(data=str(data))
    url = "http://182.150.27.208:8000/trans"
    print(send_data)
    res = reqGET(url, send_data)
    print(res)


def charge():
    data     = {}
    send_data={}
    trans_cd = "2001"
    settle_dt   = datetime.now().strftime('%Y%m%d')
    buss_no     = datetime.now().strftime('%Y%m%d%H%M%S%f')

    data.update(trans_cd=trans_cd)
    data.update(buss_no=buss_no)
    data.update(settle_dt=settle_dt)

    data_body={"user_id":"201805040001","trans_at":10,"trans_day":30}

    data.update(data_body)
    send_data.update(data=str(data))

    url = "http://182.150.27.208:8000/trans"
    # "http://182.150.27.208:8000/"
    print(send_data)
    res = reqGET(url, send_data)
    print(res)

if __name__ == "__main__":
    register()
