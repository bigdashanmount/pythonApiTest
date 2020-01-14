# coding:utf-8
import unittest
import ddt
import requests
import json
import common.global_var as gl
from configs.config_reader import ReadConfig
from common.http_client import Client
from util.case_filter import get_test_cases
from util.signatureUtil import Signature
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
        #根据参数算sginature
        dic_data = json.loads(login_data.get("body"))
        login_sginature = Signature().get_signature(dic_data)
        #print(login_sginature)
        str_headers = login_data.get("headers")
        #print(str_headers)
        str_headers = str_headers.replace("signature_value",login_sginature)
        #print(str_headers)
        dic_headers = json.loads(str_headers)
        s = requests.session()
        res = s.post(url, data=dic_data, headers=dic_headers)
        if res is not None:
            print(res.text)
            gl.init()
            #将登陆用户的城市ID，用户ID和Token存储到全局变量池
            gl.set_value("token", res.json().get("value").get("token"))
            gl.set_value("userId", res.json().get("value").get("current").get("userId"))
            gl.set_value("cityId", res.json().get("value").get("current").get("cityId"))
        else:
            print("登录失败")
        # print(res.json().get("value").get("token"))
        # print(res.json().get("value").get("sysUserId"))
    @ddt.data(*test_data)
    def test_api(self, data):
        #加日志
        log_path = ReadConfig().get_log("log_path")
        mylog = MyLogger(log_path, logging.ERROR, logging.DEBUG)
        mylog.info("请求参数如下：")
        mylog.info(data)
        #data是字典类型
        data["url"] = f'{ReadConfig().get_project("host")}{data.get("url")}'
        #获取所以用例并且将字典转字符串
        print(type(data))
        str_data = json.dumps(data)
        #替换token
        pr=str_data.replace("token_value", gl.get_value("token"))
        # 替换城市ID
        pr1 = pr.replace("cityId_value", str(gl.get_value("cityId")))
        #替换uisrId
        pr2 = pr1.replace("userId_value", str(gl.get_value("userId")))#userId类型int转一下str
        # 根据参数算sginature
        if data["method"] == "GET":
            print(data["method"])
            dic_data = json.loads(data.get("params"))
        if data["method"] == "POST":
            print(data["method"])
            dic_data = json.loads(data.get("body"))
        sginature = Signature().get_signature(dic_data)
        str_data = pr2.replace("signature_value", sginature)
        dic_data = json.loads(str_data)
        #print(dic_data)
        c = Client(dic_data)
        res=c.send()
        mylog.info("接口响应信息如下：")
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





