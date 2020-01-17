import requests
import  json
url="http://pyapitest.lexue.com/order/order/v2/check"
payload = {
	"studentId": "1175",
	"classId": "101292",
	"classFee": "0",
	"courseNum": "2",
	"schoolId": "0",
	"activityId":"0",
	"gradeId": "1160"
}

print(type(payload))
headers = {"Accept-Language": "zh-CN,zh;q=0.8",'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; V1818A Build/OPM1.171019.026) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 'os': 'Android','channel': 'lexue','version': '3.1.0','appKey': '201820011141153',  'did': '869633047841059','signature': '79E48482F30ED5CA96DCBB4DFA43D1576DBC2B74','cityId': '110100', 'userId': '1410', 'token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNDEwIiwiaWF0IjoxNTc5MDYzNTU2LCJleHAiOjE1ODY4Mzk1NTZ9.P14jISo2wZX5vRIGqU-QsfSjyN18q07a177oBgqBBYI','Content-Type': 'application/json;charset=utf-8','Host': 'pyapitest.lexue.com'}
r = requests.post(url, headers=headers, json=payload)
print(r.text)
