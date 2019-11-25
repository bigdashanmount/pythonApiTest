# coding:utf-8

import unittest
import ddt
import requests
import json
import common.global_var as gl
from configs.config_reader import ReadConfig
from common.http_client import Client
from util.case_filter import get_test_cases
from util.logger import MyLogger;
import logging
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
        str_headers = login_data.get("headers")
        dic_headers = json.loads(str_headers)
        dic_data = json.loads(login_data.get("body"))
        s = requests.session()
        res = s.post(url, data=dic_data, headers=dic_headers)
        if res is not None:
            gl.init()
            gl.set_value("token", res.json().get("value").get("token"))
            gl.set_value("userId", res.json().get("value").get("sysUserId"))
        else:
            print("登录失败")
        # print(res.json().get("value").get("token"))
        # print(res.json().get("value").get("sysUserId"))
    @ddt.data(*test_data)
    def test_api(self, data):
        #加日志
        log_path = ReadConfig().get_log("log_path")
        mylog = MyLogger(log_path, logging.ERROR, logging.DEBUG)
        mylog.info("CMS_请求参数如下：")
        mylog.info(data)
        # print(data)
        #data是字典类型
        data["url"] = f'{ReadConfig().get_project("host")}{data.get("url")}'
        #字典转字符串
        str_data_version = json.dumps(data)
        #替换token
        pr=str_data_version.replace("token_value", gl.get_value("token"))
        #替换uisrId
        pr2 = pr.replace("userId_value", str(gl.get_value("userId")))#userId类型int转一下str
        str_data = pr2.replace("signature_value", "2549059CB2A1A7D855940251D05003960A4EEB7B")
        dic_data = json.loads(str_data)
        # print(dic_data)
        c = Client(dic_data)
        res=c.send()
        mylog.info("CMS_接口响应信息如下：")
        mylog.info(res.text)
        print(res.text)
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





