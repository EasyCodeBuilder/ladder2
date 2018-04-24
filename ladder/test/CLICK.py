import random
import time

class CHARCLICK:

    def __init__(self):
        self.num=50
        self.step=5

    def randomStr(self):

        str=""

        for i in range(1,self.num):

            str=str+chr(random.randint(ord('a'),ord('z')));

            if (i%self.step==0):
                str+=" "

        return str
    def addColor(self,str):
        return "\033[1;31m{}\033[0m".format(str)

    def checkStr(self,str,msg,dur):
        strOut=""
        isSame=True
        num=min(len(str),len(msg))
        # print(dur)
        wrongCount=0
        speed=int(num*60/dur)
        for i in range(num):
            if(str[i]==msg[i]):
                strOut+=msg[i]
            else:
                wrongCount+=1
                strOut+=self.addColor(msg[i])
                isSame=False
        if(isSame):

            strOut="\033[1;34m{}\033[0m ALL RIGHT !! speed={} key/min".format(strOut,speed)
        else:
            strOut+=" WRONG {} times!! speed={} key/min"\
                .format(wrongCount,speed)
        print(strOut+"\n---------------------------")


    def run(self):

        str=self.randomStr();

        print(str)

        t1=time.clock()
        msg=input()
        t2 = time.clock()
        while(True):
            if(str=="bye"):
                break
            # elif(str==msg):
            #     msg+="  OK !!!"
            # else:
            #     msg+="  WRONG !!!"
            # print(msg+"\n-------------------------")
            self.checkStr(str,msg,t2-t1)
            str = self.randomStr()
            print(str)
            t1=time.clock()
            msg = input()
            t2=time.clock()


if __name__=='__main__':

    charClick= CHARCLICK()
    charClick.run()