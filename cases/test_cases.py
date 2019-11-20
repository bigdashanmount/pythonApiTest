# coding:utf-8

import unittest
import ddt
import requests
import json
import common.global_var as gl
from configs.config_reader import ReadConfig
from common.http_client import Client
from util.case_filter import get_test_cases


# 筛选有效用例
test_data = get_test_cases()
login_data = test_data[0]
test_data.pop(0)


@ddt.ddt
class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("开始执行测试用例......\n")
        url = f'{ReadConfig().get_project("host")}{login_data.get("url")}'
        str_headers = login_data.get("headers").replace("app_version", ReadConfig().get_project("app_version"))
        dic_headers = json.loads(str_headers)
        dic_data = json.loads(login_data.get("body"))
        s = requests.session()
        res = s.post(url=url, json=dic_data, headers=dic_headers)
        if res is not None:
            gl.init()
            gl.set_value("token", res.json().get("lgtk"))
        else:
            print("登录失败")

    @ddt.data(*test_data)
    def test_api(self, data):
        data["url"] = f'{ReadConfig().get_project("host")}{data.get("url")}'
        str_data_version = json.dumps(data).replace("app_version", ReadConfig().get_project("app_version"))
        str_data_token = str_data_version.replace("token", gl.get_value("token"))
        dic_data_token = json.loads(str_data_token)
        c = Client(dic_data_token)
        c.send()
        checks = c.checks.split('&')
        for check in checks:
            exec(check)
        if c.count > 0:
            self.assertTrue(False, msg=c.message)

    @classmethod
    def tearDownClass(cls):
        print("测试用例执行完毕......\n")


if __name__ == "__main__":
    unittest.main()





