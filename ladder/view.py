from django.http import HttpResponse
from ladder.dao.include import *
import json
from ladder.task.task import *

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
    #返回结果
    resData={}
    resData.update(res="success")

    print("head and body = {}".format(dict(head,**body)))
    insertRequsert(dict(head,**body),resData)
    return HttpResponse(str(resData))