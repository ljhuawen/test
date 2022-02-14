# encoding = utf-8
from domain.caseitem import caseitem
import requests


def api(case: caseitem):
    retext = ""
    if case.method.lower() == "get":
        retext = requests.get(url=case.url, params=None).text
    elif case.method.lower() == "post":
        headers = {"Content-Type": "application/json"}
        retext = requests.post(url=case.url, data=case.parameter, headers=headers).text
    elif case.method.lower() == "put":
        retext = requests.put(url=case.url).text
    elif case.method.lower() == "delete":
        retext = requests.delete(url=case.url).text
    return retext
