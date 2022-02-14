# encoding = utf-8
from typing import List
from typing import Dict


class useritem():
    def __init__(self, accountinfo: Dict[str, str], app: List[str], client, platform: List[str], userType: List[str],
                 password="neGH6QnHHuvNP7BlIvVm7Q==", twoFa=False, disable=False, inblacklist=False):
        # 默认密码 sxw@123 neGH6QnHHuvNP7BlIvVm7Q==
        self.__accountinfo = accountinfo
        self.__app = app
        self.__client = client
        self.__platform = platform
        self.__userType = userType
        self.__password = password
        self.__twoFa = twoFa
        self.__disable = disable
        self.__inblacklist = inblacklist
        pass

    @property
    def accountinfo(self):
        return self.__accountinfo

    @accountinfo.setter
    def accountinfo(self, value):
        self.__accountinfo = value

    @property
    def app(self):
        return self.__app

    @app.setter
    def app(self, value):
        self.__app = value

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, value):
        self.__client = value

    @property
    def platform(self):
        return self.__platform

    @platform.setter
    def platform(self, value):
        self.__platform = value

    @property
    def userType(self):
        return self.__userType

    @userType.setter
    def userType(self, value):
        self.__userType = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def twoFa(self):
        return self.__twoFa

    @twoFa.setter
    def twoFa(self, value):
        self.__twoFa = value

    @property
    def disable(self):
        return self.__disable

    @disable.setter
    def disable(self, value):
        self.__disable = value

    @property
    def inblacklist(self):
        return self.__inblacklist

    @inblacklist.setter
    def inblacklist(self, value):
        self.__inblacklist = value

    def show(self):
        print(
            "accountinfo={}, app={}, client={}, platform={}, userType={}, password={}, twoFa={}, inblacklist={}".format(
                self.accountinfo, self.app,
                self.client, self.platform,
                self.userType, self.password,
                self.twoFa, self.inblacklist))
