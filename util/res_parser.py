# coding:utf-8

import jsonpath
import json

#res是个对象类型
def find_one(res, key):
    if res:
        obj = jsonpath.jsonpath(res.json(), key)
        if obj:
            return obj[0]
        return None


def find_all(res, key):
    if res:
        obj = jsonpath.jsonpath(res.json(), key)
        if obj:
            return obj
    return None


def json_parser(res, key):
    if isinstance(res, dict):
        for k, v in res.items():
            if k == key:
                return v
            else:
                if isinstance(v, dict):
                    json_parser(v, key)
                elif isinstance(v, list):
                    for i in v:
                        va = json_parser(i, key)
                        return va
    elif isinstance(res, list):
        for i in res:
            va = json_parser(i, key)
            return va
    elif isinstance(res, str):
        dic_data = json.loads(res)
        va = json_parser(dic_data, key)
        return va
    else:
        print("未知数据类型：", type(res))


if __name__ == "__main__":
    s = '{"rpco":200,"ver":0,"tsrp":1561540392581,"rpbd":{"brco":206,"bmsg":"登录成功","bitd":0,"scid":0,"subj":0,"region":0,"grad":0,"leid":31200053,"nick":"小明","sex":0,"utp":0,"upow":["NONE"],"reft":"97418DC70D07FB3B9A4812D8F1F8A9EF","rct":"OQPQjJ/u9MMbZR92WY1+ZFKSP72vqxiHqrqxQvwiN68vRIIfn9lDh77rNUNfbQURB3xGAD4uJtAxLeU1Rh/QSoRuXhsvckMi","tid":0},"lgtk":"3fOIaT4IvmobFsX1arwkwXQ33sYSkn0sEflYGasW9pAi/Dnh38us4YRrcssGZcPnnVK2/58TQ9QqZfPVChrl1kjbdb9GlEgh"}'
    v = find_one(s, "bmsg")
    print(v)
    # s = '{"status": "SUCCESS", "msg": "error", "data":[{"id": 31,"userId": 12, "phone":"18380476370"}], "m":1}'
    # s = [{"status": "SUCCESS", "msg": "error", "data": [{"id": 31, "userId": 12, "phone": "18380476370"}], "m": 1},
    #      {"abc": 3}]
    #
    # v = json_parser(s, "id")
    # print(v)





