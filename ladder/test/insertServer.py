from ladder.dao.Server import ServerDao,Server

def inserFileServer():
    f=open("server.txt","r")
    lines=f.readlines()
    for line in lines:
        values=line[:-1].split("\t")
        insertOne(values)
        # print(values)

def insertOne(ser=list()):
    ip = ser[0]
    port = int(ser[1])
    password = ser[2]
    resv1 = ser[3]
    server_id="%s%d"%(manageIP(ip),port)

    data={}
    data.update(ip=ip)
    data.update(port=port)
    data.update(password=password)
    data.update(resv1=resv1)
    data.update(server_id=server_id)
    print(data)


    server_dao=ServerDao()
    server=Server()
    server.setServerDict(data)
    server_dao.insertServer2DB(server)

def manageIP(ip="0.0.0.0"):
    ip_list=ip.replace(" ","").split(".")
    if ip_list.__len__() != 4 :
        print("ip is illegal")
        return ""
    str=''.join(["%03d"%(int(p)) for p in ip_list])
    # print(str)
    return str

if __name__=="__main__":
    print("sss")
    inserFileServer()