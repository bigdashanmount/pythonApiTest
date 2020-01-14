# coding:utf-8
#将字典类型的get请求参数转为字符串路径
#cityId=110100&gradeName=五年级
class dict_to_str_params:
    def dict_params(self,dict):
        str_params = ""
        for key in dict:
            params_key_value = key + "=" + dict[key]
            #print(params_key_value)
            #拼加
            str_params += params_key_value + "&"
            #返回拼结果去除最后的&
        return str_params[0:(len(str_params)-1)]
if __name__ =="__main__":
    test =dict_to_str_params()
    dict_params = {"cityId": "110100", "gardeName": "五年级"}
    #print(type(dict_params))
    a =test.dict_params(dict_params)
    #print(a)