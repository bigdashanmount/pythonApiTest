# coding:utf-8


import urllib3
import requests
import json
import random
import common.global_var as gl
from util.excel_parser import Excel
from configs.config_reader import ReadConfig
from requests_toolbelt.multipart.encoder import MultipartEncoder
from util.res_parser import find_one, find_all
from util.db_operator import db_values
from util.dict_to_str_params import dict_to_str_params
from util.signatureUtil import Signature
urllib3.disable_warnings()


class Client:

    def __init__(self, data):
        self.count = 0
        self.message = []
        self.timeout = float(ReadConfig().get_project("timeout"))
        self.url = data["url"]
        self.method = data["method"]
        self.headers = eval(data["headers"])
        self.type = data["type"]
        if data["params"] != "":
            self.params = data["params"]
        else:
            self.params = ""
        if data["body"] != "":
            self.data = json.loads(data["body"])
        else:
            self.data = ""
        if data["depend"] != "":
            self.depend = eval(data["depend"])
        else:
            self.depend = ""
        self.checks = data["exp_res"]
        self.res = None

    def get(self):
        try:
            print(self.url)
            print(self.headers)
            print(self.params)
            if len(self.params) > 0:
              dict_params=json.loads(self.params)
            else:
              # 参数为空创建空字典，使用固定的signature
              dict_params = {}
            signature = Signature().get_signature(dict_params)
            print(signature)
            #将header转dic,并更新sginature
            self.headers['signature']=signature
            #增加了将get方法的字典转成拼接参数样式
            self.params=dict_to_str_params().dict_params(dict_params)
            response = requests.get(url=self.url, headers=self.headers, params=self.params, timeout=self.timeout, verify=False)
            return response
        except TimeoutError:
            return None

    def post(self):
        try:
            if self.method == "POST" and self.type == "JSON":
               dic_data = {}
            else:
               dic_data = self.data
            sginature = Signature().get_signature(dic_data)
            self.headers['signature']=sginature
            if self.type == "URL_ENCODE":
                response = requests.post(url=self.url, headers=self.headers, data=self.data, timeout=self.timeout, verify=False)
            elif self.type == "JSON":
                response = requests.post(url=self.url, headers=self.headers, json=self.data, timeout=self.timeout, verify=False)
            elif self.type == "multipart/form-data":
                response = requests.post(url=self.url, headers=self.headers, data=self.data, timeout=self.timeout,
                                         verify=False)
                #上传图片
                #response = self.upload_photo(ReadConfig().get_file("picture_path"))
            elif self.type == "XML":
                xml_str = self.data.get('xml')
                if xml_str and isinstance(xml_str, str):
                    response = requests.post(url=self.url, headers=self.headers, data=xml_str, timeout=self.timeout, verify=False)
                else:
                    raise Exception('xml格式不正确')
            else:
                print("暂不支持Content-Type: ", self.type)
            return response
        except TimeoutError:
            return None

    def put(self):
        try:
            if self.method == "POST" and self.type == "JSON":
               dic_data = {}
            else:
               dic_data = self.data
            sginature = Signature().get_signature(dic_data)
            self.headers['signature']=sginature
            if self.type == "URL_ENCODE":
                response = requests.put(url=self.url, headers=self.headers, data=self.data, timeout=self.timeout,
                                         verify=False)
            elif self.type == "JSON":
                response = requests.put(url=self.url, headers=self.headers, json=self.data, timeout=self.timeout,
                                         verify=False)
            elif self.type == "multipart/form-data":
                response = requests.put(url=self.url, headers=self.headers, data=self.data, timeout=self.timeout,
                                         verify=False)
            elif self.type == "XML":
                xml_str = self.data.get('xml')
                if xml_str and isinstance(xml_str, str):
                    response = requests.put(url=self.url, headers=self.headers, data=xml_str, timeout=self.timeout,
                                             verify=False)
                else:
                    raise Exception('xml格式不正确')
            else:
                print("暂不支持Content-Type: ", self.type)
            return response
        except TimeoutError:
            return None
    def execute_pre_case(self):
        excel_cases_path = ReadConfig().get_cases("excel_cases_path")
        sheet_name = ReadConfig().get_cases("sheet_name")
        er = Excel(excel_cases_path, sheet_name)
        d = er.read_excel()
        n = self.depend.get("case_id") - 1
        #依赖的接口数据
        depend_data = d[n]
        #str_data_version = json.dumps(depend_data).replace("app_version", ReadConfig().get_project("app_version"))
        #str_depend_data_token = json.dumps(str_data_version).replace("token", gl.get_value("token"))
        #dic_depend_data_token = eval(json.loads(str_depend_data_token))
        #method = dic_depend_data_token["method"]
        #headers = eval(dic_depend_data_token["headers"])
        #params = dic_depend_data_token["params"]
        #body = dic_depend_data_token["body"]
        #new_type = dic_depend_data_token["type"]
        #调用单独方法depend_request_replace替换token userid cityId 还有算nature
        url = f'{ReadConfig().get_project("host")}{depend_data["url"]}'
        dic_data=self.depend_request_replace(depend_data)
        method = dic_data["method"]
        headers = dic_data["headers"]
        #header和params都是字符串，都转dict
        headers = eval(headers)
        new_type = dic_data["type"]
        if method == "GET":
            dict_params = eval(dic_data["params"])
            # get参数由字典转为拼接的字符串
            params = dict_to_str_params().dict_params(dict_params)
            res = requests.get(url=url, headers=headers, params=params, timeout=self.timeout, verify=False)
            print("前置接口响应值： "+res.text)
        elif method == "POST":
            body = eval(dic_data["body"])
            # print("-----------------------------------")
            # print(type(headers))
            # print(type(body))
            # print("-----------------------------------")
            if new_type == "URL_ENCODE":
                res = requests.post(url=url, headers=headers, data=body, timeout=self.timeout, verify=False)
                print("前置接口响应值： " + res.text)
            elif new_type == "JSON":
                res = requests.post(url=url, headers=headers, json=body, timeout=self.timeout, verify=False)
                print("前置接口响应值： " + res.text)
            elif new_type == "multipart/form-data":
                res = requests.post(url=url, headers=headers, data=body, timeout=self.timeout,
                                         verify=False)
                print("前置接口响应值： " + res.text)
                #res = self.upload_photo(ReadConfig().get_file("picture_path"))
            elif new_type == "XML":
                xml_str = self.data.get('xml')
                if xml_str and isinstance(xml_str, str):
                    res = requests.post(url=url, headers=headers, json=xml_str, timeout=self.timeout, verify=False)
                    print("前置接口响应值： " + res.text)
                else:
                    raise Exception('xml格式不正确')
        elif method == "PUT":
            body = dic_data["body"]
            if new_type == "URL_ENCODE":
                res = requests.post(url=url, headers=headers, data=body, timeout=self.timeout, verify=False)
                print("前置接口响应值： " + res.text)
            elif new_type == "JSON":
                res = requests.post(url=url, headers=headers, json=body, timeout=self.timeout, verify=False)
                print("前置接口响应值： " + res.text)
            elif new_type == "multipart/form-data":
                res = requests.post(url=url, headers=headers, data=body, timeout=self.timeout,
                                         verify=False)
                print("前置接口响应值： " + res.text)
                #res = self.upload_photo(ReadConfig().get_file("picture_path"))
            elif new_type == "XML":
                xml_str = self.data.get('xml')
                if xml_str and isinstance(xml_str, str):
                    res = requests.post(url=url, headers=headers, json=xml_str, timeout=self.timeout, verify=False)
                    print("前置接口响应值： " + res.text)
                else:
                    raise Exception('xml格式不正确')
        else:
            print("暂不支持method: ", method)
            return None
        #将依赖的接口的相应值res对象和想获取的依赖值的路径传入find_one，得到依赖数据
        # print("9999999999999999999")
        # print(res.text)
        # print("9999999999999999999")
        old_arg = find_one(res, self.depend.get("from_arg"))
        return old_arg

    def get_depend(self):
        #  old_arg就是接口需要依赖的数据
        old_arg = self.execute_pre_case()
        print("接口依赖数据：  ")
        print(old_arg)
        #传递依赖数据给要执行的参数
        self.params = self.params.replace(self.depend.get("to_arg"), str(old_arg))
        response = self.get()
        return response

    def post_depend(self):
        old_arg = self.execute_pre_case()
        print("接口依赖数据：  ")
        print(old_arg)
        #字典转字符串做替换，然后再转回字典做post请求
        self.data=str(self.data)
        self.data = self.data.replace(self.depend.get("to_arg"), str(old_arg))
        self.data=eval(self.data)
        response = self.post()
        return response
    def put_depend(self):
        old_arg = self.execute_pre_case()
        # 字典转字符串做替换，然后再转回字典做post请求
        self.data = str(self.data)
        self.data = self.data.replace(self.depend.get("to_arg"), str(old_arg))
        self.data = eval(self.data)
        response = self.put()
        return response
    #上传图片
    def upload_photo(self, file_path):
        try:
            multipart_encoder = MultipartEncoder(
                fields={
                    'file': (file_path, open(file_path, 'rb'), 'image/png')
                },
                # boundary='Boundary+' + str(random.randint(1e15, 1e16 - 1))
            )
            self.headers['Content-Type'] = multipart_encoder.content_type
            response = requests.post(url=self.url, data=multipart_encoder, headers=self.headers, timeout=self.timeout, verify=False)
            return response
        except TimeoutError:
            return None

    def send(self):
        if self.method == "POST":
            if self.depend == "":
                self.res = self.post()
            else:
                self.res = self.post_depend()
            return self.res
        elif self.method == "GET":
            if self.depend == "":
                self.res = self.get()
            else:
                self.res = self.get_depend()
            return self.res
        elif self.method == "PUT":
            if self.depend == "":
                self.res = self.put()
            else:
                self.res = self.put_depend()
            return self.res
        else:
            print("暂不支持method: ", self.method)
            return None

    def assert_status_code(self, exp_status=200):
        if self.res:
            if exp_status == self.res.status_code:
                self.message.append('$..status_code------>预期结果：[{first}]，实际结果：[{second}]'.format(first=exp_status, second=str(self.res.status_code)))
            else:
                self.message.append('$..status_code------>预期结果：[{first}]，实际结果：[{second}]'.format(first=exp_status, second=str(self.res.status_code)))
                self.count += 1
        else:
            self.count += 1
            print("请求出错，请检查请求入参")
            print("响应信息为：", self.res)
            print("URL：", self.url)
            print("Headers：", self.headers)
            print("Params：", self.params)
            print("Body：", self.data)

    def assert_equal(self, key, exp):
        if self.res:
            value = find_one(self.res, key)
            if exp == value:
                self.message.append(key + '------>预期结果：[{first}], 实际结果：[{second}]'.format(first=exp, second=value))
            else:
                self.message.append(key + '------>预期结果：[{first}]，实际结果：[{second}]'.format(first=exp, second=value))
                self.count += 1
        else:
            self.count += 1

    def assert_in(self, key, exp):
        if self.res:
            values = find_all(self.res, key)
            if exp in values:
                self.message.append(key + '------>预期结果：[{first}], 实际结果：[{second}]'.format(first=exp, second=values))
            else:
                self.message.append(key + '------>预期结果：[{first}]，实际结果：[{second}]'.format(first=exp, second=values))
                self.count += 1
        else:
            self.count += 1

    def check_json_value_equal_db(self, key, sql):
        data = db_values(sql)
        exp = find_one(self.res, key)
        if data:
            if exp:
                if exp == str(data[0][0]):
                    print("验证通过，数据库中存在：", exp)
                else:
                    print("验证失败，数据库中不存在：", exp)
            else:
                print("json取值无效：", key)
        else:
            print("sql执行错误：", sql)
    #独立新建处理依赖接口的请求，data是依赖的接口数据
    def depend_request_replace(self,data):
        str_data = json.dumps(data)
        # 替换token
        pr = str_data.replace("token_value", gl.get_value("token"))
        # 替换城市ID
        pr1 = pr.replace("cityId_value", str(gl.get_value("cityId")))
        # 替换uisrId
        pr2 = pr1.replace("userId_value", str(gl.get_value("userId")))  # userId类型int转一下str
        # 根据参数算sginature
        # #028CE8719F62630D3251F0CBAE1D1DF1475E78AD
        if data["method"] == "GET":
            print(data["method"])
            # 参数不为空，参数转字典
            if len(data.get("params")) > 0:
                dic_data = json.loads(data.get("params"))
            else:
                # 参数为空创建空字典，使用固定的signature
                dic_data = {}
        if data["method"] == "POST":
            print(data["method"])
            if data["type"] == "JSON":
                dic_data = {}
            else:
                dic_data = json.loads(data.get("body"))
        if data["method"] == "PUT":
            print(data["method"])
            dic_data = json.loads(data.get("body"))
        # 调用生成signature
        sginature = Signature().get_signature(dic_data)
        str_data = pr2.replace("signature_value", sginature)
        dic_data = json.loads(str_data)
        return dic_data

if __name__ =="__main__":
    Client=Client()
    Client.execute_pre_case()
