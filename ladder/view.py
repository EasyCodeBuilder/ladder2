from django.http import HttpResponse
from ladder.dao.include import *
from ladder.lib.include import *
from ladder.task.include import *
import json
from ladder.task.task import *
from ladder.task.Distribution import Distribution
from datetime import datetime


logger=Logger("view").getlog()

def home(request):
    f=open("ladder/page/register.html","r")
    str=f.read()
    return HttpResponse(str)

def hello(request):
    json={"name":"lyk","no":"12548","qq_no":"97848484"}
    hello_str="<h1>This is hello page of LADDER</h1>"
    return HttpResponse(hello_str)

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
    logger.info("返回参数：{}".format(res.data))
    # insertRequsert(data,res.data)
    return HttpResponse(str(res.data))

def register(request):
    data_str = request.GET['data']
    logger.info("接收参数：data_str={}".format(data_str))
    data = eval(data_str)

    logger.info("接收参数：{}".format(data))

    trans_cd = "1001"
    settle_dt = datetime.now().strftime('%Y%m%d')
    buss_no = datetime.now().strftime('%Y%m%d%H%M%S%f')

    data.update(trans_cd=trans_cd)
    data.update(buss_no=buss_no)
    data.update(settle_dt=settle_dt)

    logger.info("start register ")
    distr=Distribution()
    res=distr.destribution(data)

    response=HttpResponse(str(res.data))
    response.__setitem__("Access-Control-Allow-Origin", "*")
    return response

def trans2(data):

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
    logger.info("返回参数：{}".format(res.data))
    return res