import requests
url="http://pyapitest.lexue.com/foremarketing/messageCenter/getMessagePageList?pageSize=20&pageNum=1"
parameter= {"pageSize":"20", "pageNum":"1"}
headers = {'appKey': '201820011141153', 'os': 'Android', 'version': '3.1.0', 'signature': '1FA5EF6BF3C96508A96FF1FCE1AAC9C21BD1B37F', 'did': '869633047841059', 'cityId': '110100', 'userId': '1410'}
r = requests.get(url,headers = headers,params = parameter)

print(r.text)