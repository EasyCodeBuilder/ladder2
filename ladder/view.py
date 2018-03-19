from django.http import HttpResponse
from .dao.User import *
from .dao.Server import *
from .dao.Trans import *
import json


def hello(request):
    json={"name":"lyk","no":"12548"}
    return HttpResponse(json)

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