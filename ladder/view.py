from django.http import HttpResponse
from ladder.dao.include import *
import json
from ladder.task.task import *

logger=Logger("view").getlog()

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
    dataHeadStr=request.GET['dataHead']
    dataBodyStr=request.GET['dataBody']

    head=eval(dataHeadStr)
    body=eval(dataBodyStr)

    print(type(head))
    print(body)

    trans_cd=head.get("function_id")

    if trans_cd is "1001":
        logger.info("start register ")
        res=register(body)

    if trans_cd is "2001":
        logger.info("start charge")
        res=chargeAccount(body)
    #返回结果
    reshead={}
    reshead.update(function_id=head.get("function_id"))
    reshead.update(buss_no=head.get("buss_no"))
    reshead.update(settle_dt=head.get("settle_dt"))
    reshead.update(resp_no=res.getCode())
    reshead.update(resp_msg=res.msg)

    print("head and body = {}".format(dict(head,**body)))
    insertRequsert(dict(head,**body),dict(res.data,**reshead))
    return HttpResponse(str(dict(res.data,**reshead)))