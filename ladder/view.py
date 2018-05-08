from django.http import HttpResponse
from ladder.dao.include import *
import json
from ladder.task.task import *
from ladder.task.Charge import Charge
from ladder.task.Register import Register

logger=Logger("view").getlog()

def home(request):
    f=open("ladder/page/home.html","r")
    str=f.read()
    return HttpResponse(str)

def hello(request):
    json={"name":"lyk","no":"12548","qq_no":"97848484"}
    return HttpResponse(str(json))

def add(request):
    data=request.GET['data']
    type=request.GET['type']
    print(type)
    dataStr = json.loads(data)

    if(type=="adduser"):
        user=User()
        user.setUser(dataStr)
    elif (type == "addserver"):
        server=Server()
        server.setServer(dataStr)
    elif (type == "addtrans"):
        trans=Trans()
        trans.setTrans(dataStr)
    else :
        return HttpResponse("Wrong")

    return HttpResponse("Done")

def trans(request):
    #接受结果
    data_str=request.GET['data']
    logger.info("接收参数：data_str={}".format(data_str))
    data=eval(data_str)

    logger.info("接收参数：{}".format(data))

    trans_cd=data.get("trans_cd")

    if trans_cd is "1001":
        logger.info("start register ")
        res = Register(data).process()
        if res.getCode() is SUCCESS.getCode():
            logger.info("charge success")

    if trans_cd is "2001":
        logger.info("start charge")
        res= Charge(data).process()
        if res.getCode() is SUCCESS.getCode():
            logger.info("charge success")
    #返回结果
    print("返回参数：{}".format(res.data))
    insertRequsert(data,res.data)
    return HttpResponse(str(res.data))