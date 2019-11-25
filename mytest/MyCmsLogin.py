import unittest
import ddt
import requests
import json
from configs.config_reader import ReadConfig
from util.case_filter import get_test_cases
import common.global_var as gl
test_data = get_test_cases()
login_data = test_data[0]

def login():
    print("开始执行测试用例......\n")
    #配置文件config取host，Excel取接口path拼接url
    url = f'{ReadConfig().get_project("host")}{login_data.get("url")}'
    print(url)
    str_headers = login_data.get("headers")
    print(str_headers)
    dic_headers = json.loads(str_headers)
    print(dic_headers)
    dic_data = json.loads(login_data.get("body"))
    print(dic_data)
    res = requests.post(url, data=dic_data, headers=dic_headers)
    print(res.text)
    token= res.json().get("value").get("token")
    print(token)
    userId = res.json().get("value").get("sysUserId")
    print(userId)
    if res is not None:
        gl.init()
        gl.set_value("token", res.json().get("value").get("token"))
        gl.set_value("userId", res.json().get("value").get("sysUserId"))
    else:
        print("登录失败")
login()

