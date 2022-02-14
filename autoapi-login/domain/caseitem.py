# encoding = utf-8

class caseitem():
    def __init__(self, module, id, case_name, method, url, parameter, assertion, isactive):
        self.__module = module
        self.__id = id
        self.__case_name = case_name
        self.__method = method
        self.__url = url
        self.__parameter = parameter
        self.__assertion = assertion
        self.__isactive = isactive
        pass

    @property
    def module(self):
        return self.__module

    @module.setter
    def module(self, value):
        self.__module = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def case_name(self):
        return self.__case_name

    @case_name.setter
    def case_name(self, value):
        self.__case_name = value

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, value):
        self.__url = value

    @property
    def parameter(self):
        return self.__parameter

    @parameter.setter
    def parameter(self, value):
        self.__parameter = value

    @property
    def assertion(self):
        return self.__assertion

    @assertion.setter
    def assertion(self, value):
        self.__assertion = value

    @property
    def isactive(self):
        return self.__isactive

    @isactive.setter
    def isactive(self, value):
        self.__isactive = value

    def ToDict(self):
        dict1 = {
            'module': self.__module,
            'id': self.__id,
            'case_name': self.__case_name,
            'method': self.__method,
            'url': self.__url,
            'parameter': self.__parameter,
            'assertion': self.__assertion,
            'isactive': self.__isactive,
        }
        return dict1

    def show(self):
        message = (
            "module={},id={}，case_name={}，method={}，url={}，parameter={}，assertion={}，isactive={}".format(self.module,
                                                                                                         self.id,
                                                                                                         self.case_name,
                                                                                                         self.method,
                                                                                                         self.url,
                                                                                                         self.parameter,
                                                                                                         self.assertion,
                                                                                                         self.isactive
                                                                                                         ))
        print(message)
        return message
