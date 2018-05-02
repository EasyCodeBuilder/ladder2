

class TestClass:
    def __init__(self):
        self.userId="123"
        self.qqNo="qww"

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key]=value


test= TestClass()

print(test.__dict__)
print(test.__doc__)
print(test.__getattr__("userId"))

test.__setattr__("name","zhangsan")
print(test.__dict__)