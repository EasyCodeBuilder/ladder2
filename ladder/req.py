
from urllib import parse,request

import json

def displayRes(list):

    for i in range(len(list)):
        print(list[i])

def reqPOST(url,data):

    # sData=parse.urlencode(data).encode("utf-8")

    header_dict = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
    req = request.Request(url=url, data=bytes(json.dumps(data),encoding="utf-8"), headers=header_dict)
    # print(req)
    res = request.urlopen(req)
    res=res.read().decode("utf-8")
    print(res)
    # print(res.decode(encoding='utf-8'))

def reqGET(url,data):

    postfix="?"
    url= url+parse.urlencode(data)
    print(url)
    req=request.Request(url);

    res_data=request.urlopen(req);

    res=res_data.read().decode('utf8')

    print(res)

url="http://127.0.0.1:3000/admin/login"
url2="http://127.0.0.1:3000//consumeRecord"



def run():

    data={"adminAccount":"root","adminPassword":"OStem@00"}
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

    checkurl="https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxb6a454852c62b7e0&redirect_uri=http%3A%2F%2Foauth.youtoupiao.com%2Fauthorize%2Fauthorize.html%3Fjump%3Dhttp%3A%2F%2Fme0cb28c7f4cd194c.wxvote.youtoupiao.com%2Fpage%2Fshow%2Fid%2F7dc9ba75e1b7bbec.html%3Fiiid%3D1524185209036177000&response_type=code&scope=snsapi_userinfo&state=9080be1269ea12d23f53a2016bb4ec3c#wechat_redirect"
    data={}
    reqGET(checkurl,data)

def run2():
    print("good")
    pass

if __name__=="__main__":

    run2()