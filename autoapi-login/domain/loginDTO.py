# encoding = utf-8
from domain.useritem import useritem


class logindto():
    def __init__(self, user: useritem, account, accountType, app, platform, userType, client):
        self.__account = account
        self.__accountType = accountType
        self.__app = app
        self.__client = client
        self.__platform = platform
        self.__userType = userType
        self.__password = user.password
        self.__twoFa = user.twoFa
        pass

    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, value):
        self.__account = value

    @property
    def accountType(self):
        return self.__accountType

    @accountType.setter
    def accountType(self, value):
        self.__accountType = value

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

    def ToDict(self):
        dict1 = {
            'account': self.__account,
            'accountType': self.__accountType,
            'app': self.__app,
            'client': self.__client,
            'platform': self.__platform,
            'userType': self.__userType,
            'password': self.__password,
            'twoFa': self.__twoFa,
        }
        return dict1
