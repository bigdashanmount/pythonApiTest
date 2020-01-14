import requests
url="http://pyapitest.lexue.com/user/user/listBanner"
parameter= {"cityId":"110100", "gradeName":"五年级"}
headers = {'appKey': '201820011141153', 'os': 'Android', 'version': '3.1.0', 'signature': '6E095987AD3BF14942C2ED50C35ED88CC0B6DEC6', 'did': '869633047841059', 'cityId': '110100'}
r = requests.get(url,headers = headers,params = parameter)

print(r.text)