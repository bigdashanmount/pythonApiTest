# coding:utf-8
import requests
url="http://pyapitest.lexue.com/search/SearchResource/v4/searchContent"
payload = {"gradeName": "高三", "pageSize": "10","cityId":"110100","pageNum":"1","switchOpen":"0"}
headers = {'appKey': '201820011141153', 'os': 'Android', 'version': '3.1.0', "signature": "signature_value", 'did': '869633047841059', 'cityId': 'cityId_value', 'userId': 'userId_value', 'token': 'token_value'}
r = requests.post(url, headers=headers, data=payload)

print(r.text)
