# coding:utf-8
import requests
url="http://pyapitest.lexue.com/order/order/offlinePayOrder"
headers={'appKey': '201820011141153', 'os': 'Android', 'version': '3.1.0', "signature": "8171D8D9B1BDFC6C08C94F875FF432CA3FE5CAAC", 'did': '869633047841059', 'cityId': '110100', 'userId': '1410', 'token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxNDEwIiwiaWF0IjoxNTc5MjQyOTMyLCJleHAiOjE1ODcwMTg5MzJ9.b5KIxzqCYQrceoc6WOGY-MhnzEZm_Z_-PRnlWd0XkBY',"Content-Type":"application/x-www-form-urlencoded"}
data={"orderSource":"1","orderCode":"170941021230727259"}
response = requests.post(url=url, headers=headers, data=data)
print(response.text)
